# src/domain/entities/traducao.py
"""
Entidade Traducao - Representa uma tradução de documento.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Optional

# Telemetria opcional
_telemetry = None


def _monitor(name=None):
    """Decorator dummy que não faz nada."""

    def decorator(func):
        return func

    return decorator


def configure_telemetry(telemetry_instance=None, monitor_decorator=None):
    """Configura telemetria para este módulo (usado apenas em testes)."""
    global _telemetry, _monitor
    _telemetry = telemetry_instance
    if monitor_decorator:
        _monitor = monitor_decorator


@dataclass
class Traducao:
    """
    Representa uma tradução de um documento.

    Attributes:
        id: Identificador único
        documento_id: ID do documento original
        idioma: Código do idioma (en, pt, es, fr)
        texto_traduzido: Conteúdo traduzido
        modelo: Modelo usado (nmt, base)
        custo: Custo estimado em USD
        data_traducao: Data da tradução
    """

    documento_id: int
    idioma: str
    texto_traduzido: str
    data_traducao: datetime

    id: Optional[int] = None
    modelo: Optional[str] = None
    custo: float = 0.0

    def __post_init__(self):
        """Validações após inicialização."""
        # Valida idioma
        idiomas_validos = ["en", "pt", "es", "fr"]
        if self.idioma not in idiomas_validos:
            if _telemetry:
                _telemetry.increment("traducao.idioma_invalido")
            raise ValueError(f"Idioma inválido: {self.idioma}")

        # Valida texto
        if not self.texto_traduzido:
            if _telemetry:
                _telemetry.increment("traducao.texto_vazio")
            raise ValueError("Texto traduzido não pode ser vazio")

        if _telemetry:
            _telemetry.increment("traducao.criada")

    @property
    def idioma_nome(self) -> str:
        """Nome do idioma em português."""
        nomes: Dict[str, str] = {
            "en": "Inglês",
            "pt": "Português",
            "es": "Espanhol",
            "fr": "Francês",
        }
        resultado = nomes.get(self.idioma, self.idioma.upper())

        if _telemetry and self.idioma not in nomes:
            _telemetry.increment("traducao.idioma_desconhecido")

        return resultado

    @property
    def idioma_icone(self) -> str:
        """Ícone do idioma."""
        icons: Dict[str, str] = {"en": "🇺🇸", "pt": "🇧🇷", "es": "🇪🇸", "fr": "🇫🇷"}
        return icons.get(self.idioma, "🌐")
