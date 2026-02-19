# src/domain/value_objects/analise_texto.py
"""
Value Objects para resultados de análise de texto com telemetria.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Tuple

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
class Entidade:
    """Entidade extraída do texto."""

    texto: str
    tipo: str  # PERSON, ORG, LOC, DATE, etc
    confianca: float
    posicao_inicio: int
    posicao_fim: int

    def __post_init__(self):
        """Validações após inicialização."""
        if self.confianca < 0 or self.confianca > 1:
            if _telemetry:
                _telemetry.increment("entidade.confianca_invalida")
            raise ValueError(f"Confiança deve estar entre 0 e 1: {self.confianca}")

        if self.posicao_inicio < 0 or self.posicao_fim < self.posicao_inicio:
            if _telemetry:
                _telemetry.increment("entidade.posicao_invalida")
            raise ValueError(f"Posições inválidas: {self.posicao_inicio}-{self.posicao_fim}")

        if _telemetry:
            _telemetry.increment("entidade.criada")


@dataclass
class Sentimento:
    """Análise de sentimento do texto."""

    polaridade: float  # -1 (negativo) a 1 (positivo)
    subjetividade: float  # 0 (objetivo) a 1 (subjetivo)
    classificacao: str  # positivo, negativo, neutro

    def __post_init__(self):
        """Validações após inicialização."""
        if self.polaridade < -1 or self.polaridade > 1:
            if _telemetry:
                _telemetry.increment("sentimento.polaridade_invalida")
            raise ValueError(f"Polaridade deve estar entre -1 e 1: {self.polaridade}")

        if self.subjetividade < 0 or self.subjetividade > 1:
            if _telemetry:
                _telemetry.increment("sentimento.subjetividade_invalida")
            raise ValueError(f"Subjetividade deve estar entre 0 e 1: {self.subjetividade}")

        if self.classificacao not in ["positivo", "negativo", "neutro"]:
            if _telemetry:
                _telemetry.increment("sentimento.classificacao_invalida")
            raise ValueError(f"Classificação inválida: {self.classificacao}")

        if _telemetry:
            _telemetry.increment("sentimento.criado")


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

    def __post_init__(self):
        """Validações após inicialização."""
        if self.total_palavras < 0:
            if _telemetry:
                _telemetry.increment("estatisticas.palavras_negativas")
            raise ValueError(f"Total de palavras não pode ser negativo: {self.total_palavras}")

        if self.palavras_unicas > self.total_palavras:
            if _telemetry:
                _telemetry.increment("estatisticas.unicas_maior_que_total")
            raise ValueError("Palavras únicas não pode ser maior que total de palavras")

        if _telemetry:
            _telemetry.increment("estatisticas.criado")


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
    palavras_frequentes: List[Tuple[str, int]]

    # Metadados da análise
    modelo_utilizado: str
    tempo_processamento: float  # segundos

    def __post_init__(self):
        """Validações após inicialização."""
        if self.tempo_processamento < 0:
            if _telemetry:
                _telemetry.increment("analise.tempo_negativo")
            raise ValueError(
                f"Tempo de processamento não pode ser negativo: {self.tempo_processamento}"
            )

        # Verificar se idioma é suportado
        idiomas_suportados = ["ru", "en", "pt"]
        if self.idioma not in idiomas_suportados:
            if _telemetry:
                _telemetry.increment("analise.idioma_nao_suportado")
            raise ValueError(f"Idioma não suportado: {self.idioma}")

        if _telemetry:
            _telemetry.increment("analise.criada")
            _telemetry.increment(f"analise.idioma.{self.idioma}")
            _telemetry.increment("analise.entidades", value=len(self.entidades))

    @property
    def resumo(self) -> str:
        """Resumo da análise."""
        if _telemetry:
            _telemetry.increment("analise.resumo_acessado")
        return (
            f"Doc {self.documento_id} ({self.idioma}): "
            f"{self.estatisticas.total_palavras} palavras, "
            f"{len(self.entidades)} entidades, "
            f"sentimento {self.sentimento.classificacao}"
        )
