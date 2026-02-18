# src/application/use_cases/obter_documento.py
"""
Caso de uso: Obter documento completo por ID.
"""

from typing import List, Optional

from src.application.dtos.documento_dto import DocumentoDTO
from src.domain.interfaces.repositories import RepositorioDocumento
from src.domain.interfaces.repositorio_traducao import RepositorioTraducao
from src.domain.value_objects.nome_russo import NomeRusso


class ObterDocumento:
    """
    Caso de uso para obter um documento completo.
    """

    def __init__(
        self, repo_doc: RepositorioDocumento, repo_trad: Optional[RepositorioTraducao] = None
    ):
        self.repo_doc = repo_doc
        self.repo_trad = repo_trad
        self._tradutor_nomes = True

    def com_traducao_nomes(self, ativo: bool = True):
        """Ativa/desativa tradução de nomes."""
        self._tradutor_nomes = ativo
        return self

    def _buscar_traducoes(self, documento_id: int) -> List[dict]:
        """Busca traduções do documento se o repositório estiver disponível."""
        if not self.repo_trad:
            return []

        try:
            traducoes = self.repo_trad.listar_por_documento(documento_id)
            return [
                {
                    "idioma": t.idioma,
                    "data_traducao": t.data_traducao.isoformat()[:10],
                    "modelo": t.modelo,
                    "custo": t.custo,
                }
                for t in traducoes
            ]
        except Exception as e:
            print(f"⚠️ Erro ao buscar traduções: {e}")
            return []

    def executar(self, documento_id: int) -> Optional[DocumentoDTO]:
        """
        Busca documento por ID e converte para DTO.
        """
        documento = self.repo_doc.buscar_por_id(documento_id)

        if not documento:
            return None

        # Buscar traduções do documento
        traducoes = self._buscar_traducoes(documento_id)

        # Função de tradução de nomes
        def tradutor(nome):
            if not self._tradutor_nomes or not nome:
                return None
            try:
                return NomeRusso(nome).transliterar()
            except Exception:
                return nome

        return DocumentoDTO.from_domain(documento, tradutor, traducoes)
