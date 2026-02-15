# src/application/dtos/estatisticas_dto.py
"""
DTO para estatísticas do acervo.
"""

from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass
class EstatisticasDTO:
    """
    Objeto para transferência de estatísticas.
    """
    
    # Visão geral
    total_documentos: int
    total_traducoes: int
    
    # Distribuições
    documentos_por_centro: Dict[str, int]
    documentos_por_tipo: Dict[str, int]
    traducoes_por_idioma: Dict[str, int]
    
    # Pessoas
    pessoas_frequentes: List[Tuple[str, int, str]]  # (nome_russo, count, nome_en)
    
    # Métricas especiais
    cartas: int
    declaracoes: int
    relatorios: int
    acareacoes: int
    acusacoes: int
    laudos: int
    documentos_com_anexos: int
    
    # Custos
    custo_total_traducoes: float
    
    @property
    def percentual_traduzido(self) -> float:
        """Percentual de documentos com tradução."""
        if self.total_documentos == 0:
            return 0.0
        return (self.total_traducoes / self.total_documentos) * 100
    
    @property
    def resumo(self) -> str:
        """Resumo das estatísticas para exibição rápida."""
        return (f"{self.total_documentos} docs, "
                f"{self.total_traducoes} traduções, "
                f"${self.custo_total_traducoes:.4f}")