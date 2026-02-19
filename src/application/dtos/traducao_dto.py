# src/application/dtos/traducao_dto.py
"""
DTO para Tradução com telemetria.
"""

from dataclasses import dataclass
from typing import Any, Dict, Optional

# Telemetria opcional
_telemetry = None


def configure_telemetry(telemetry_instance=None):
    """Configura telemetria para este módulo (usado apenas em testes)."""
    global _telemetry
    _telemetry = telemetry_instance


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

    def __post_init__(self):
        """Validações após inicialização."""
        if self.custo < 0:
            if _telemetry:
                _telemetry.increment("traducao_dto.custo_negativo")
            raise ValueError(f"Custo não pode ser negativo: {self.custo}")

        if not self.texto_traduzido:
            if _telemetry:
                _telemetry.increment("traducao_dto.texto_vazio")
            raise ValueError("Texto traduzido não pode ser vazio")

        if _telemetry:
            _telemetry.increment("traducao_dto.criado")

    @classmethod
    def from_domain(cls, traducao: Any) -> "TraducaoDTO":
        """
        Converte entidade para DTO.

        Args:
            traducao: Entidade Traducao do domínio

        Returns:
            TraducaoDTO
        """
        if _telemetry:
            _telemetry.increment("traducao_dto.from_domain")

        # Extrair data no formato ISO (apenas a parte da data)
        data_iso = traducao.data_traducao.isoformat()[:10]

        return cls(
            id=traducao.id,
            documento_id=traducao.documento_id,
            idioma=traducao.idioma,
            idioma_nome=traducao.idioma_nome,
            idioma_icone=traducao.idioma_icone,
            texto_traduzido=traducao.texto_traduzido,
            data_traducao=data_iso,
            modelo=traducao.modelo,
            custo=traducao.custo,
        )

    def to_dict(self) -> Dict[str, Any]:
        """Converte DTO para dicionário (útil para serialização JSON)."""
        if _telemetry:
            _telemetry.increment("traducao_dto.to_dict")

        return {
            "id": self.id,
            "documento_id": self.documento_id,
            "idioma": self.idioma,
            "idioma_nome": self.idioma_nome,
            "idioma_icone": self.idioma_icone,
            "texto_traduzido": self.texto_traduzido,
            "data_traducao": self.data_traducao,
            "modelo": self.modelo,
            "custo": self.custo,
        }
