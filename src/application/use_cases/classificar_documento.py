# src/application/use_cases/classificar_documento.py
"""
Caso de uso: Classificar documento.
Orquestra a classificação de um documento baseado em seu título.
"""

import re
from typing import Optional

from src.domain.entities.documento import Documento
from src.domain.interfaces.repositories import RepositorioDocumento
from src.domain.value_objects.tipo_documento import TipoDocumento


class ClassificarDocumento:
    """
    Caso de uso para classificar um documento.

    Responsabilidades:
    - Identificar tipo do documento pelo título
    - Extrair pessoas mencionadas
    - Detectar anexos
    - Atualizar metadados do documento
    """

    def __init__(self, repo: RepositorioDocumento):
        """
        Args:
            repo: Repositório para buscar/salvar documentos
        """
        self.repo = repo

    def executar(self, documento_id: int) -> Optional[Documento]:
        """
        Classifica um documento pelo ID.
        """
        documento = self.repo.buscar_por_id(documento_id)
        if not documento:
            return None

        documento = self._classificar(documento)
        self.repo.salvar(documento)
        return documento

    def executar_em_lote(self, limite: Optional[int] = None) -> int:
        """
        Classifica múltiplos documentos não classificados.
        """
        todos = self.repo.listar(limite=1000)
        nao_classificados = [d for d in todos if not d.tipo]

        if limite is not None:
            nao_classificados = nao_classificados[:limite]

        count = 0
        for doc in nao_classificados:
            doc_classificado = self._classificar(doc)
            self.repo.salvar(doc_classificado)
            count += 1

        return count

    def _classificar(self, documento: Documento) -> Documento:
        """
        Aplica as regras de classificação ao documento.
        """
        if not documento.titulo:
            return documento

        titulo = documento.titulo

        tipo = TipoDocumento.from_titulo(titulo)
        documento.tipo = tipo.value
        documento.tipo_descricao = tipo.descricao_pt

        pessoas = self._extrair_pessoas(titulo)

        if pessoas:
            documento.pessoa_principal = pessoas[0]

            if tipo == TipoDocumento.ACAREACAO and len(pessoas) >= 2:
                documento.envolvidos = pessoas
            elif tipo in [TipoDocumento.CARTA, TipoDocumento.RELATORIO, TipoDocumento.DECLARACAO]:
                if len(pessoas) >= 2:
                    documento.remetente = pessoas[0]
                    documento.destinatario = pessoas[1]
                elif len(pessoas) == 1:
                    documento.remetente = pessoas[0]

        documento.tem_anexos = "приложением" in titulo.lower()
        return documento

    def _extrair_pessoas(self, titulo: str) -> list[str]:
        """
        Extrai nomes russos do título.
        """
        if not titulo:
            return []

        padrao = r"([А-Я]\. ?[А-Я]\. [А-Я][а-я]+)"
        return re.findall(padrao, titulo)
