# src/application/use_cases/obter_documento.py
"""
Caso de uso: Obter documento completo por ID.
"""

from typing import Optional
from src.domain.interfaces.repositories import RepositorioDocumento
from src.application.dtos.documento_dto import DocumentoDTO
from src.domain.value_objects.nome_russo import NomeRusso


class ObterDocumento:
    """
    Caso de uso para obter um documento completo.
    """
    
    def __init__(self, repo: RepositorioDocumento):
        self.repo = repo
        self._tradutor_nomes = True
    
    def com_traducao_nomes(self, ativo: bool = True):
        """Ativa/desativa tradução de nomes."""
        self._tradutor_nomes = ativo
        return self
    
    def executar(self, documento_id: int) -> Optional[DocumentoDTO]:
        """
        Busca documento por ID e converte para DTO.
        """
        documento = self.repo.buscar_por_id(documento_id)
        
        if not documento:
            return None
        
        # Buscar traduções do documento
        from src.application.use_cases.listar_traducoes import ListarTraducoes
        listar_trad = ListarTraducoes(self.repo)
        traducoes = listar_trad.executar(documento_id)
        
        # Função de tradução
        def tradutor(nome):
            if not self._tradutor_nomes or not nome:
                return None
            try:
                return NomeRusso(nome).transliterar()
            except:
                return nome
        
        return DocumentoDTO.from_domain(documento, tradutor, traducoes)