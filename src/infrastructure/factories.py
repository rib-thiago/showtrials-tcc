# src/infrastructure/factories.py
"""
Factories para criação de serviços com configuração e telemetria.
Isola a lógica de criação e permite mocks em testes.
"""

import logging
import os
from typing import Optional, Union

from src.infrastructure.analysis.spacy_analyzer import SpacyAnalyzer
from src.infrastructure.translation.google_translator import GoogleTranslator

# Telemetria opcional
_telemetry = None


def configure_telemetry(telemetry_instance=None):
    """Configura telemetria para este módulo (usado apenas em testes)."""
    global _telemetry
    _telemetry = telemetry_instance


logger = logging.getLogger(__name__)


class MockTranslator:
    """Tradutor mock para testes/simulação."""

    def __init__(self, **kwargs):
        logger.info("🔄 Inicializando tradutor MOCK")
        self._kwargs = kwargs

    def traduzir(self, texto: str, destino: str = "en") -> str:
        """Simula tradução adicionando prefixo."""
        logger.info(f"🔧 MOCK traduzindo para {destino}")
        return f"[{destino.upper()} MOCK] {texto}"

    def traduzir_documento_completo(self, texto: str, destino: str = "en") -> str:
        """Mock de tradução de documento."""
        return self.traduzir(texto, destino)

    def testar_conexao(self) -> bool:
        """Mock sempre funciona."""
        return True


class MockSpacyAnalyzer:
    """Analisador spaCy mock para testes."""

    def __init__(self, **kwargs):
        logger.info("🔄 Inicializando analisador MOCK")
        self._kwargs = kwargs

    def analisar(self, texto: str, documento_id: int, idioma: str = "ru"):
        """Mock de análise com estatísticas consistentes."""
        from datetime import datetime

        from src.domain.value_objects.analise_texto import (
            AnaliseTexto,
            Entidade,
            EstatisticasTexto,
            Sentimento,
        )

        palavras = len(texto.split())

        return AnaliseTexto(
            documento_id=documento_id,
            idioma=idioma,
            data_analise=datetime.now(),
            estatisticas=EstatisticasTexto(
                total_caracteres=len(texto),
                total_palavras=palavras,
                total_paragrafos=texto.count("\n") + 1,
                total_frases=max(1, palavras // 5),
                palavras_unicas=palavras,
                densidade_lexica=1.0,
                tamanho_medio_palavra=5.0,
                tamanho_medio_frase=10.0,
            ),
            entidades=[
                Entidade(
                    texto="Л.В. Николаева",
                    tipo="PER",
                    confianca=1.0,
                    posicao_inicio=0,
                    posicao_fim=15,
                )
            ],
            entidades_por_tipo={"Pessoa": ["Л.В. Николаева"]},
            sentimento=Sentimento(polaridade=0.0, subjetividade=0.5, classificacao="neutro"),
            palavras_frequentes=[("palavra", palavras) for _ in range(min(10, palavras))],
            modelo_utilizado="mock",
            tempo_processamento=0.1,
        )


def create_translator(
    api_key: Optional[str] = None, simulate: bool = False, **kwargs
) -> Union[GoogleTranslator, MockTranslator]:
    """
    Factory para tradutor.

    Args:
        api_key: Chave da API Google
        simulate: Se True, usa mock
        **kwargs: Configurações adicionais

    Returns:
        Instância do tradutor (real ou mock)
    """
    logger.info("🔧 Factory: criando tradutor")

    if simulate:
        logger.info("🎭 Usando tradutor MOCK (simulação)")
        if _telemetry:
            _telemetry.increment("factory.translator.mock")
        return MockTranslator(**kwargs)

    # Tenta pegar API key de kwargs ou variável de ambiente
    api_key = api_key or kwargs.get("api_key") or os.getenv("GOOGLE_TRANSLATE_API_KEY")

    try:
        translator = GoogleTranslator(api_key=api_key)
        if _telemetry:
            _telemetry.increment("factory.translator.real")
        return translator
    except Exception as e:
        logger.error(f"❌ Falha ao criar tradutor real: {e}")
        logger.info("🎭 Fallback para tradutor MOCK")
        if _telemetry:
            _telemetry.increment("factory.translator.fallback")
        return MockTranslator(**kwargs)


def create_spacy_analyzer(preload: Optional[list] = None, simulate: bool = False, **kwargs):
    """
    Factory para analisador spaCy.

    Args:
        preload: Lista de idiomas para pré-carregar
        simulate: Se True, usa mock
        **kwargs: Configurações adicionais

    Returns:
        Instância do analisador (real ou mock)
    """
    logger.info("🔧 Factory: criando analisador spaCy")

    if simulate:
        logger.info("🎭 Usando analisador MOCK (simulação)")
        if _telemetry:
            _telemetry.increment("factory.spacy.mock")
        return MockSpacyAnalyzer(**kwargs)

    analyzer = SpacyAnalyzer()

    if _telemetry:
        _telemetry.increment("factory.spacy.real")

    # Pré-carrega modelos se especificado
    if preload:
        for lang in preload:
            try:
                logger.info(f"🔄 Pré-carregando modelo: {lang}")
                analyzer._get_model(lang)
                if _telemetry:
                    _telemetry.increment(f"factory.spacy.preload.{lang}")
            except Exception as e:
                logger.warning(f"⚠️ Falha ao pré-carregar {lang}: {e}")
                if _telemetry:
                    _telemetry.increment("factory.spacy.preload.error")

    return analyzer


def create_wordcloud_generator(**kwargs):
    """
    Factory para gerador de wordcloud.

    Args:
        **kwargs: Configurações (default_size, max_words, etc)

    Returns:
        Instância do gerador
    """
    logger.info("🔧 Factory: criando gerador de wordcloud")
    from src.infrastructure.analysis.wordcloud_generator import WordCloudGenerator

    if _telemetry:
        _telemetry.increment("factory.wordcloud")

    return WordCloudGenerator(**kwargs)


def create_pdf_exporter(simulate: bool = False, **kwargs):
    """
    Factory para exportador PDF (placeholder).

    Args:
        simulate: Se True, usa mock
        **kwargs: Configurações adicionais

    Returns:
        Instância do exportador PDF
    """
    logger.info("🔧 Factory: criando exportador PDF (mock)")

    class MockPdfExporter:
        def exportar(self, *args, **kwargs):
            logger.info("📑 PDF export (mock)")
            return "/tmp/mock.pdf"

    if _telemetry:
        _telemetry.increment("factory.pdf_exporter")

    return MockPdfExporter()


# Mapeamento de factories por nome de serviço
SERVICE_FACTORIES = {
    "translator": create_translator,
    "spacy": create_spacy_analyzer,
    "wordcloud": create_wordcloud_generator,
    "pdf_exporter": create_pdf_exporter,
}
