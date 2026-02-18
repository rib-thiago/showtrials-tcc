# src/infrastructure/factories.py
"""
Factories para criação de serviços com configuração.
Isola a lógica de criação e permite mocks em testes.
"""

import os  # <-- IMPORT ADICIONADO!
import logging
from typing import Optional, Dict, Any

from src.infrastructure.config import config as app_config
from src.infrastructure.analysis.spacy_analyzer import SpacyAnalyzer
from src.infrastructure.analysis.wordcloud_generator import WordCloudGenerator
from src.infrastructure.translation.google_translator import GoogleTranslator

logger = logging.getLogger(__name__)


class MockTranslator:
    """Tradutor mock para testes/simulação."""
    
    def __init__(self, **kwargs):
        logger.info("🔄 Inicializando tradutor MOCK")
        self._kwargs = kwargs
    
    def traduzir(self, texto: str, destino: str = 'en') -> str:
        """Simula tradução adicionando prefixo."""
        logger.info(f"🔧 MOCK traduzindo para {destino}")
        return f"[{destino.upper()} MOCK] {texto}"
    
    def traduzir_documento_completo(self, texto: str, destino: str = 'en') -> str:
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
    
    def analisar(self, texto: str, documento_id: int, idioma: str = 'ru'):
        """Mock de análise."""
        from src.domain.value_objects.analise_texto import (
            AnaliseTexto, EstatisticasTexto, Sentimento, Entidade
        )
        from datetime import datetime
        
        return AnaliseTexto(
            documento_id=documento_id,
            idioma=idioma,
            data_analise=datetime.now(),
            estatisticas=EstatisticasTexto(
                total_caracteres=len(texto),
                total_palavras=len(texto.split()),
                total_paragrafos=texto.count('\n') + 1,
                total_frases=10,
                palavras_unicas=50,
                densidade_lexica=0.5,
                tamanho_medio_palavra=5.0,
                tamanho_medio_frase=20.0
            ),
            entidades=[
                Entidade(texto="Л.В. Николаева", tipo="PER", confianca=1.0, posicao_inicio=0, posicao_fim=15)
            ],
            entidades_por_tipo={"Pessoa": ["Л.В. Николаева"]},
            sentimento=Sentimento(polaridade=0.0, subjetividade=0.5, classificacao="neutro"),
            palavras_frequentes=[("palavra", 10) for _ in range(10)],
            modelo_utilizado="mock",
            tempo_processamento=0.1
        )


def create_translator(api_key: Optional[str] = None, 
                     simulate: bool = False,
                     **kwargs) -> GoogleTranslator:
    """
    Factory para tradutor.
    
    Args:
        api_key: Chave da API Google
        simulate: Se True, usa mock
        **kwargs: Configurações adicionais
    
    Returns:
        Instância do tradutor
    """
    logger.info("🔧 Factory: criando tradutor")
    
    if simulate:
        logger.info("🎭 Usando tradutor MOCK (simulação)")
        return MockTranslator(**kwargs)
    
    # Tenta pegar API key de kwargs ou variável de ambiente
    api_key = api_key or kwargs.get('api_key') or os.getenv('GOOGLE_TRANSLATE_API_KEY')
    
    try:
        return GoogleTranslator(api_key=api_key)
    except Exception as e:
        logger.error(f"❌ Falha ao criar tradutor real: {e}")
        logger.info("🎭 Fallback para tradutor MOCK")
        return MockTranslator(**kwargs)


def create_spacy_analyzer(preload: list = None, 
                         simulate: bool = False,
                         **kwargs):
    """
    Factory para analisador spaCy.
    
    Args:
        preload: Lista de idiomas para pré-carregar
        simulate: Se True, usa mock
        **kwargs: Configurações adicionais
    
    Returns:
        Instância do analisador
    """
    logger.info("🔧 Factory: criando analisador spaCy")
    
    if simulate:
        logger.info("🎭 Usando analisador MOCK (simulação)")
        return MockSpacyAnalyzer(**kwargs)
    
    analyzer = SpacyAnalyzer()
    
    # Pré-carrega modelos se especificado
    if preload:
        for lang in preload:
            try:
                logger.info(f"🔄 Pré-carregando modelo: {lang}")
                analyzer._get_model(lang)
            except Exception as e:
                logger.warning(f"⚠️ Falha ao pré-carregar {lang}: {e}")
    
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
    return WordCloudGenerator(**kwargs)


def create_pdf_exporter(simulate: bool = False, **kwargs):
    """
    Factory para exportador PDF (placeholder).
    """
    logger.info("🔧 Factory: criando exportador PDF (mock)")
    
    class MockPdfExporter:
        def exportar(self, *args, **kwargs):
            logger.info("📑 PDF export (mock)")
            return "/tmp/mock.pdf"
    
    return MockPdfExporter()


# Mapeamento de factories por nome de serviço
SERVICE_FACTORIES = {
    'translator': create_translator,
    'spacy': create_spacy_analyzer,
    'wordcloud': create_wordcloud_generator,
    'pdf_exporter': create_pdf_exporter,
}