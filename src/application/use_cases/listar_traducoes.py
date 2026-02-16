# src/application/use_cases/listar_traducoes.py
"""
Caso de uso: Listar traduções de um documento.
"""

from typing import List, Dict
from src.domain.interfaces.repositories import RepositorioDocumento


class ListarTraducoes:
    """
    Caso de uso para listar traduções de um documento.
    """
    
    def __init__(self, repo: RepositorioDocumento):
        self.repo = repo
    
    def executar(self, documento_id: int) -> List[Dict]:
        """
        Retorna lista de traduções do documento.
        """
        # Por enquanto, retorna lista vazia
        # Será implementado quando tivermos repositório de traduções
        return []