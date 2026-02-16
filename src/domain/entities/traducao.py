# src/domain/entities/traducao.py
"""
Entidade Traducao - Representa uma tradução de documento.
"""

from dataclasses import dataclass
from typing import Optional
from datetime import datetime


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
        idiomas_validos = ['en', 'pt', 'es', 'fr']
        if self.idioma not in idiomas_validos:
            raise ValueError(f"Idioma inválido: {self.idioma}")
        
        if not self.texto_traduzido:
            raise ValueError("Texto traduzido não pode ser vazio")
    
    @property
    def idioma_nome(self) -> str:
        """Nome do idioma em português."""
        nomes = {
            'en': 'Inglês',
            'pt': 'Português',
            'es': 'Espanhol',
            'fr': 'Francês'
        }
        return nomes.get(self.idioma, self.idioma.upper())
    
    @property
    def idioma_icone(self) -> str:
        """Ícone do idioma."""
        icons = {
            'en': '🇺🇸',
            'pt': '🇧🇷',
            'es': '🇪🇸',
            'fr': '🇫🇷'
        }
        return icons.get(self.idioma, '🌐')