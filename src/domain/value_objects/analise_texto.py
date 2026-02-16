# src/domain/value_objects/analise_texto.py
"""
Value Objects para resultados de análise de texto.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
from datetime import datetime


@dataclass
class Entidade:
    """Entidade extraída do texto."""
    texto: str
    tipo: str  # PERSON, ORG, LOC, DATE, etc
    confianca: float
    posicao_inicio: int
    posicao_fim: int


@dataclass
class Sentimento:
    """Análise de sentimento do texto."""
    polaridade: float  # -1 (negativo) a 1 (positivo)
    subjetividade: float  # 0 (objetivo) a 1 (subjetivo)
    classificacao: str  # positivo, negativo, neutro


@dataclass
class EstatisticasTexto:
    """Estatísticas básicas do texto."""
    total_caracteres: int
    total_palavras: int
    total_paragrafos: int
    total_frases: int
    palavras_unicas: int
    densidade_lexica: float  # palavras_unicas / total_palavras
    tamanho_medio_palavra: float
    tamanho_medio_frase: float


@dataclass
class AnaliseTexto:
    """
    Resultado completo da análise de um texto.
    """
    documento_id: int
    idioma: str  # 'ru' ou 'pt' ou 'en'
    data_analise: datetime
    
    # Estatísticas
    estatisticas: EstatisticasTexto
    
    # Entidades
    entidades: List[Entidade]
    entidades_por_tipo: Dict[str, List[str]]
    
    # Sentimento
    sentimento: Sentimento
    
    # Palavras importantes
    palavras_frequentes: List[tuple]  # (palavra, frequencia)
    
    # Metadados da análise
    modelo_utilizado: str
    tempo_processamento: float  # segundos
    
    @property
    def resumo(self) -> str:
        """Resumo da análise."""
        return (f"Doc {self.documento_id} ({self.idioma}): "
                f"{self.estatisticas.total_palavras} palavras, "
                f"{len(self.entidades)} entidades, "
                f"sentimento {self.sentimento.classificacao}")