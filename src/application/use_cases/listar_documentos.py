# src/application/use_cases/listar_documentos.py
"""
Caso de uso: Listar documentos com paginação e filtros.
"""

from typing import Optional, List, Dict
from src.domain.interfaces.repositories import RepositorioDocumento
from src.application.dtos.documento_dto import DocumentoListaDTO
from src.domain.value_objects.nome_russo import NomeRusso


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
        self._tradutor_nomes = None
    
    def com_traducao_nomes(self, ativo: bool = True):
        """Ativa/desativa tradução de nomes."""
        self._tradutor_nomes = ativo
        return self
    
    def executar(self, 
                 pagina: int = 1,
                 limite: int = 20,
                 centro: Optional[str] = None,
                 tipo: Optional[str] = None) -> Dict:
        """
        Executa a listagem com filtros e paginação.
        
        Args:
            pagina: Número da página (começa em 1)
            limite: Itens por página
            centro: Filtrar por centro
            tipo: Filtrar por tipo
            
        Returns:
            Dict com:
                - items: List[DocumentoListaDTO]
                - total: int
                - pagina: int
                - total_paginas: int
                - filtros: dict
        """
        offset = (pagina - 1) * limite
        
        # Buscar documentos
        documentos = self.repo.listar(
            offset=offset,
            limite=limite,
            centro=centro,
            tipo=tipo
        )
        
        # Contar total
        total = self.repo.contar(centro=centro, tipo=tipo)
        
        # Converter para DTO
        items = []
        for doc in documentos:
            # Verificar se tem tradução (simplificado)
            tem_traducao = False  # Será implementado depois
            
            dto = DocumentoListaDTO.from_domain(
                doc,
                tem_traducao=tem_traducao,
                tradutor_nomes=self._tradutor_nomes
            )
            items.append(dto)
        
        return {
            'items': items,
            'total': total,
            'pagina': pagina,
            'total_paginas': (total + limite - 1) // limite,
            'filtros': {
                'centro': centro,
                'tipo': tipo,
                'limite': limite
            }
        }
    
    def listar_tipos(self, centro: Optional[str] = None) -> List[tuple]:
        """
        Lista tipos disponíveis com contagens.
        
        Returns:
            Lista de (tipo, descricao, count)
        """
        from collections import Counter
        
        # Buscar todos (limitado para performance)
        docs = self.repo.listar(limite=1000, centro=centro)
        
        # Contar por tipo
        counter = Counter()
        for doc in docs:
            if doc.tipo:
                counter[doc.tipo] += 1
        
        # Converter para lista ordenada
        resultado = []
        for tipo, count in counter.most_common():
            from src.domain.value_objects.tipo_documento import TipoDocumento
            try:
                tipo_enum = TipoDocumento(tipo)
                descricao = tipo_enum.descricao_pt
                icone = tipo_enum.icone
            except:
                descricao = tipo
                icone = "📄"
            
            resultado.append((tipo, descricao, icone, count))
        
        return resultado