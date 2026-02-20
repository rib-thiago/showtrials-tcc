# src/application/use_cases/listar_documentos.py
"""
Caso de uso: Listar documentos com paginação e filtros.
"""

from collections import Counter
from typing import Counter as CounterType
from typing import Dict, List, Optional

from src.application.dtos.documento_dto import DocumentoListaDTO
from src.domain.interfaces.repositories import RepositorioDocumento
from src.domain.value_objects.tipo_documento import TipoDocumento

# Telemetria opcional
_telemetry = None


def configure_telemetry(telemetry_instance=None):
    """Configura telemetria para este módulo (usado apenas em testes)."""
    global _telemetry
    _telemetry = telemetry_instance


class ListarDocumentos:
    """
    Caso de uso para listar documentos.

    Responsabilidades:
    - Aplicar filtros (centro, tipo)
    - Paginar resultados
    - Converter para DTO de listagem
    """

    def __init__(self, repo: RepositorioDocumento):
        self.repo = repo
        self._tradutor_nomes: Optional[bool] = None  # ← MyPy: type hint corrigido

    def com_traducao_nomes(self, ativo: bool = True):
        """Ativa/desativa tradução de nomes."""
        if _telemetry:
            _telemetry.increment("listar_documentos.com_traducao_nomes")
        self._tradutor_nomes = ativo
        return self

    def executar(
        self,
        pagina: int = 1,
        limite: int = 20,
        centro: Optional[str] = None,
        tipo: Optional[str] = None,
    ) -> Dict:
        """
        Executa a listagem com filtros e paginação.
        """
        if _telemetry:
            _telemetry.increment("listar_documentos.executar.iniciado")
            _telemetry.increment(f"listar_documentos.pagina.{pagina}")

        offset = (pagina - 1) * limite

        # Buscar documentos
        documentos = self.repo.listar(offset=offset, limite=limite, centro=centro, tipo=tipo)

        # Contar total
        total = self.repo.contar(centro=centro, tipo=tipo)

        # Converter para DTO
        items = []
        for doc in documentos:
            # Verificar se tem tradução (com proteção contra None)
            tem_traducao = False
            if doc.id is not None:  # ← MyPy: verificação adicionada
                tem_traducao = self._verificar_traducoes(doc.id)

            dto = DocumentoListaDTO.from_domain(
                doc, tem_traducao=tem_traducao, tradutor_nomes=self._tradutor_nomes
            )
            items.append(dto)

        if _telemetry:
            _telemetry.increment("listar_documentos.executar.concluido")
            _telemetry.increment("listar_documentos.resultados", value=len(items))

        return {
            "items": items,
            "total": total,
            "pagina": pagina,
            "total_paginas": (total + limite - 1) // limite,
            "filtros": {"centro": centro, "tipo": tipo, "limite": limite},
        }

    def listar_tipos(self, centro: Optional[str] = None) -> List[tuple]:
        """
        Lista tipos disponíveis com contagens.

        Returns:
            Lista de (tipo, descricao, icone, count)
        """
        if _telemetry:
            _telemetry.increment("listar_documentos.listar_tipos.iniciado")

        # Buscar todos (limitado para performance)
        docs = self.repo.listar(limite=1000, centro=centro)

        # Contar por tipo
        counter: CounterType[str] = Counter()  # ← MyPy: type hint adicionado
        for doc in docs:
            if doc.tipo:
                counter[doc.tipo] += 1

        # Converter para lista ordenada
        resultado = []
        for tipo, count in counter.most_common():
            try:
                tipo_enum = TipoDocumento(tipo)
                descricao = tipo_enum.descricao_pt
                icone = tipo_enum.icone
            except Exception:
                descricao = tipo
                icone = "📄"

            resultado.append((tipo, descricao, icone, count))

        if _telemetry:
            _telemetry.increment("listar_documentos.listar_tipos.concluido")
            _telemetry.increment("listar_documentos.tipos_encontrados", value=len(resultado))

        return resultado

    def _verificar_traducoes(self, documento_id: int) -> bool:
        """
        Verifica se documento tem alguma tradução consultando o banco.
        """
        if _telemetry:
            _telemetry.increment("listar_documentos.verificar_traducoes.iniciado")

        try:
            # Usar o repositório para buscar traduções
            from src.infrastructure.persistence.sqlite_repository import SQLiteDocumentoRepository

            repo = SQLiteDocumentoRepository()

            with repo._conexao() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT COUNT(*) FROM traducoes WHERE documento_id = ?", (documento_id,)
                )
                count = cursor.fetchone()[0]
                tem_traducao = count > 0

                if _telemetry:
                    _telemetry.increment("listar_documentos.verificar_traducoes.sucesso")

                return tem_traducao

        except Exception as e:
            # Se algo der errado, assume que não tem tradução
            if _telemetry:
                _telemetry.increment("listar_documentos.verificar_traducoes.erro")
            print(f"Erro ao verificar traduções: {e}")
            return False
