# src/application/dtos/traducao_dto.py
"""
DTO para Tradução.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class TraducaoDTO:
    """
    DTO para exibição de tradução.
    """

    id: Optional[int]
    documento_id: int
    idioma: str
    idioma_nome: str
    idioma_icone: str
    texto_traduzido: str
    data_traducao: str
    modelo: Optional[str]
    custo: float

    @classmethod
    def from_domain(cls, traducao):
        """Converte entidade para DTO."""
        return cls(
            id=traducao.id,
            documento_id=traducao.documento_id,
            idioma=traducao.idioma,
            idioma_nome=traducao.idioma_nome,
            idioma_icone=traducao.idioma_icone,
            texto_traduzido=traducao.texto_traduzido,
            data_traducao=traducao.data_traducao.isoformat()[:10],
            modelo=traducao.modelo,
            custo=traducao.custo,
        )
