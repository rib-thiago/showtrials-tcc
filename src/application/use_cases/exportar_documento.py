# src/application/use_cases/exportar_documento.py
"""
Caso de uso: Exportar documento com telemetria.
"""

from datetime import datetime
from pathlib import Path
from typing import Dict, Optional

from src.application.dtos.documento_dto import DocumentoDTO
from src.domain.interfaces.repositories import RepositorioDocumento
from src.domain.interfaces.repositorio_traducao import RepositorioTraducao
from src.domain.value_objects.nome_russo import NomeRusso

# Telemetria opcional
_telemetry = None


def configure_telemetry(telemetry_instance=None):
    """Configura telemetria para este módulo (usado apenas em testes)."""
    global _telemetry
    _telemetry = telemetry_instance


class ExportarDocumento:
    """
    Caso de uso para exportar documento.
    """

    # Formatos suportados
    FORMATOS = ["txt", "pdf"]

    def __init__(
        self, repo_doc: RepositorioDocumento, repo_trad: Optional[RepositorioTraducao] = None
    ):
        self.repo_doc = repo_doc
        self.repo_trad = repo_trad

    def _buscar_documento(
        self, documento_id: int, idioma: str = "original"
    ) -> Optional[DocumentoDTO]:
        """
        Busca documento ou tradução.
        """
        if _telemetry:
            _telemetry.increment("exportar_documento.buscar_documento.iniciado")
            _telemetry.increment(f"exportar_documento.idioma.{idioma}")

        if idioma == "original":
            doc = self.repo_doc.buscar_por_id(documento_id)
            if not doc:
                if _telemetry:
                    _telemetry.increment("exportar_documento.erro.documento_nao_encontrado")
                return None

            def tradutor(nome):
                try:
                    return NomeRusso(nome).transliterar()
                except Exception:
                    return nome

            if _telemetry:
                _telemetry.increment("exportar_documento.buscar_documento.sucesso_original")
            return DocumentoDTO.from_domain(doc, tradutor, [])

        elif self.repo_trad:
            traducao = self.repo_trad.buscar_por_documento(documento_id, idioma)
            if not traducao:
                if _telemetry:
                    _telemetry.increment("exportar_documento.erro.traducao_nao_encontrada")
                return None

            doc = self.repo_doc.buscar_por_id(documento_id)
            if not doc:
                if _telemetry:
                    _telemetry.increment(
                        "exportar_documento.erro.documento_original_nao_encontrado"
                    )
                return None

            dto = DocumentoDTO.from_domain(doc, None, [])
            dto.texto = traducao.texto_traduzido
            dto.titulo = f"{dto.titulo} [{traducao.idioma_nome}]"

            if _telemetry:
                _telemetry.increment("exportar_documento.buscar_documento.sucesso_traducao")
            return dto

        return None

    def _gerar_conteudo_txt(self, dto: DocumentoDTO, incluir_metadados: bool = True) -> str:
        """
        Gera conteúdo formatado para TXT.
        """
        if _telemetry:
            _telemetry.increment("exportar_documento.gerar_conteudo_txt.iniciado")

        linhas = []

        if incluir_metadados:
            linhas.append("=" * 80)
            linhas.append(f"TÍTULO: {dto.titulo}")
            linhas.append(f"CENTRO: {dto.centro}")
            linhas.append(f"DATA ORIGINAL: {dto.data_original or 'Não informada'}")
            linhas.append(f"URL: {dto.url}")
            linhas.append(f"EXPORTADO EM: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

            if dto.pessoa_principal:
                linhas.append(f"PESSOA PRINCIPAL: {dto.pessoa_principal}")
            if dto.remetente:
                linhas.append(f"REMETENTE: {dto.remetente}")
            if dto.destinatario:
                linhas.append(f"DESTINATÁRIO: {dto.destinatario}")
            if dto.envolvidos:
                linhas.append(f"ENVOLVIDOS: {', '.join(dto.envolvidos)}")

            linhas.append("=" * 80)
            linhas.append("")

        linhas.append(dto.texto)

        if _telemetry:
            _telemetry.increment("exportar_documento.gerar_conteudo_txt.concluido")

        return "\n".join(linhas)

    def _gerar_nome_arquivo(self, dto: DocumentoDTO, formato: str, idioma: str) -> str:
        """
        Gera nome do arquivo no formato:
        ID_TITULO_IDIOMA.formato
        """
        if _telemetry:
            _telemetry.increment("exportar_documento.gerar_nome_arquivo.iniciado")

        # Sanitizar título (remover caracteres especiais)
        titulo = "".join(c for c in dto.titulo if c.isalnum() or c in (" ", "-", "_")).rstrip()
        titulo = titulo[:50]  # Limitar tamanho

        if idioma == "original":
            sufixo = "original"
        else:
            sufixo = idioma

        return f"{dto.id}_{titulo}_{sufixo}.{formato}"

    def executar(
        self,
        documento_id: int,
        formato: str = "txt",
        idioma: str = "original",
        diretorio: str = "exportados",
        incluir_metadados: bool = True,
    ) -> Dict:
        """
        Exporta documento.
        """
        if _telemetry:
            _telemetry.increment("exportar_documento.executar.iniciado")
            _telemetry.increment(f"exportar_documento.executar.formato.{formato}")

        # Validar formato
        if formato not in self.FORMATOS:
            if _telemetry:
                _telemetry.increment("exportar_documento.erro.formato_invalido")
            return {
                "sucesso": False,
                "erro": f"Formato não suportado: {formato}. Use: {', '.join(self.FORMATOS)}",
            }

        # Buscar documento
        dto = self._buscar_documento(documento_id, idioma)
        if not dto:
            if _telemetry:
                _telemetry.increment("exportar_documento.erro.documento_indisponivel")
            return {
                "sucesso": False,
                "erro": f"Documento/idioma não encontrado: {documento_id}/{idioma}",
            }

        # Criar diretório
        Path(diretorio).mkdir(exist_ok=True)

        # Gerar nome do arquivo
        nome_arquivo = self._gerar_nome_arquivo(dto, formato, idioma)
        caminho = Path(diretorio) / nome_arquivo

        try:
            if formato == "txt":
                conteudo = self._gerar_conteudo_txt(dto, incluir_metadados)
                with open(caminho, "w", encoding="utf-8") as f:
                    f.write(conteudo)

                if _telemetry:
                    _telemetry.increment("exportar_documento.executar.sucesso_txt")
                    _telemetry.increment("exportar_documento.caracteres", value=len(conteudo))

            elif formato == "pdf":
                if _telemetry:
                    _telemetry.increment("exportar_documento.executar.pdf_nao_implementado")
                return {"sucesso": False, "erro": "Exportação PDF será implementada na FASE 7"}

            if _telemetry:
                _telemetry.increment("exportar_documento.executar.concluido")

            return {
                "sucesso": True,
                "caminho": str(caminho),
                "tamanho": len(conteudo) if formato == "txt" else 0,
            }

        except Exception as e:
            if _telemetry:
                _telemetry.increment("exportar_documento.erro.execucao")
            return {"sucesso": False, "erro": f"Erro ao exportar: {e}"}

    def listar_idiomas_disponiveis(self, documento_id: int) -> list:
        """
        Lista idiomas disponíveis para exportação.
        """
        if _telemetry:
            _telemetry.increment("exportar_documento.listar_idiomas.iniciado")

        idiomas = [{"codigo": "original", "nome": "Original (Russo)"}]

        if self.repo_trad:
            traducoes = self.repo_trad.listar_por_documento(documento_id)
            for t in traducoes:
                idiomas.append({"codigo": t.idioma, "nome": t.idioma_nome, "icone": t.idioma_icone})

            if _telemetry:
                _telemetry.increment(
                    f"exportar_documento.listar_idiomas.encontrados.{len(traducoes)}"
                )

        return idiomas
