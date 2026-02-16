# src/application/use_cases/listar_traducoes.py
"""
Caso de uso: Listar traduções de um documento.
"""

from typing import List
from src.domain.interfaces.repositorio_traducao import RepositorioTraducao
from src.application.dtos.traducao_dto import TraducaoDTO


class ListarTraducoes:
    """
    Caso de uso para listar traduções de um documento.
    """
    
    def __init__(self, repo: RepositorioTraducao):
        self.repo = repo
    
    def executar(self, documento_id: int) -> List[TraducaoDTO]:
        """
        Retorna lista de traduções do documento.
        """
        traducoes = self.repo.listar_por_documento(documento_id)
        return [TraducaoDTO.from_domain(t) for t in traducoes]
    
    def contar(self, documento_id: int) -> int:
        """Retorna número de traduções do documento."""
        return self.repo.contar_por_documento(documento_id)