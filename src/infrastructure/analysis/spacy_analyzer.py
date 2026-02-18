# src/infrastructure/analysis/spacy_analyzer.py
"""
Integração com SpaCy para análise de texto multilíngue.
Versão com lazy loading - modelos carregados sob demanda.
"""

import logging
import re
import time
from collections import Counter
from datetime import datetime  # <-- IMPORT ADICIONADO!
from typing import Dict, List

import spacy

from src.domain.value_objects.analise_texto import (
    AnaliseTexto,
    Entidade,
    EstatisticasTexto,
    Sentimento,
)

logger = logging.getLogger(__name__)


class SpacyAnalyzer:
    """
    Analisador de texto usando SpaCy com lazy loading.
    Modelos são carregados apenas quando necessários.
    """

    # Mapeamento de idiomas para modelos SpaCy
    MODELOS = {
        "ru": "ru_core_news_sm",
        "en": "en_core_web_sm",
        "pt": "pt_core_news_sm",  # Opcional
    }

    # Mapeamento de tipos de entidade para português
    TIPOS_ENTIDADE = {
        "PERSON": "Pessoa",
        "ORG": "Organização",
        "LOC": "Local",
        "GPE": "Local (país/cidade)",
        "DATE": "Data",
        "TIME": "Hora",
        "MONEY": "Valor",
        "PERCENT": "Percentual",
        "FAC": "Instalação",
        "PRODUCT": "Produto",
        "EVENT": "Evento",
        "LAW": "Lei",
    }

    def __init__(self):
        """Inicializa sem carregar modelos."""
        self._models = {}  # Cache de modelos carregados
        self._stats = {lang: {"loaded": False, "time": None} for lang in self.MODELOS}
        logger.info("🔧 SpacyAnalyzer inicializado (modelos serão carregados sob demanda)")

    def _get_model(self, idioma: str):
        """
        Carrega modelo sob demanda e mantém em cache.

        Args:
            idioma: Código do idioma (ru, en, pt)

        Returns:
            Modelo spaCy carregado
        """
        if idioma not in self.MODELOS:
            raise ValueError(f"Idioma não suportado: {idioma}")

        # Retorna do cache se já carregado
        if idioma in self._models:
            return self._models[idioma]

        modelo_nome = self.MODELOS[idioma]
        logger.info(f"🔄 Carregando modelo spaCy: {modelo_nome}")

        try:
            start = time.time()
            modelo = spacy.load(modelo_nome)
            elapsed = time.time() - start

            self._models[idioma] = modelo
            self._stats[idioma] = {"loaded": True, "time": elapsed}
            logger.info(f"✅ Modelo {modelo_nome} carregado em {elapsed:.2f}s")

            return modelo

        except OSError as e:
            logger.error(f"❌ Modelo {modelo_nome} não encontrado: {e}")
            logger.info(f"   Instale com: python -m spacy download {modelo_nome}")
            raise

    def _get_nlp(self, idioma: str):
        """Retorna modelo para o idioma (com lazy loading)."""
        return self._get_model(idioma)

    def get_loaded_models(self) -> Dict[str, bool]:
        """Retorna quais modelos estão carregados."""
        return {lang: lang in self._models for lang in self.MODELOS}

    def preload_model(self, idioma: str) -> bool:
        """
        Pré-carrega um modelo especificado.

        Returns:
            True se carregado com sucesso
        """
        try:
            self._get_model(idioma)
            return True
        except Exception:
            return False

    def _calcular_estatisticas(self, texto: str, doc) -> EstatisticasTexto:
        """Calcula estatísticas do texto."""
        # Limpeza básica
        texto_limpo = re.sub(r"\s+", " ", texto)
        palavras = [token.text for token in doc if not token.is_punct and not token.is_space]
        frases = list(doc.sents)

        return EstatisticasTexto(
            total_caracteres=len(texto),
            total_palavras=len(palavras),
            total_paragrafos=texto.count("\n") + 1,
            total_frases=len(frases),
            palavras_unicas=len(set(p.lower() for p in palavras)),
            densidade_lexica=len(set(palavras)) / len(palavras) if palavras else 0,
            tamanho_medio_palavra=sum(len(p) for p in palavras) / len(palavras) if palavras else 0,
            tamanho_medio_frase=len(palavras) / len(frases) if frases else 0,
        )

    def _extrair_entidades(self, doc) -> List[Entidade]:
        """Extrai entidades do documento."""
        entidades = []
        for ent in doc.ents:
            entidades.append(
                Entidade(
                    texto=ent.text,
                    tipo=ent.label_,
                    confianca=1.0,  # SpaCy não dá confidence score
                    posicao_inicio=ent.start_char,
                    posicao_fim=ent.end_char,
                )
            )
        return entidades

    def _agrupar_entidades(self, entidades: List[Entidade]) -> Dict[str, List[str]]:
        """Agrupa entidades por tipo."""
        grupos = {}
        for ent in entidades:
            tipo_pt = self.TIPOS_ENTIDADE.get(ent.tipo, ent.tipo)
            if tipo_pt not in grupos:
                grupos[tipo_pt] = []
            if ent.texto not in grupos[tipo_pt]:
                grupos[tipo_pt].append(ent.texto)
        return grupos

    def _analisar_sentimento(self, texto: str, idioma: str) -> Sentimento:
        """
        Análise de sentimento básica.
        Para análise avançada, usaríamos transformers.
        """
        try:
            from textblob import TextBlob

            if idioma == "en":
                blob = TextBlob(texto)
                polaridade = blob.sentiment.polarity
                subjetividade = blob.sentiment.subjectivity
            else:
                # Para russo/português, usaríamos modelo específico
                # Placeholder
                polaridade = 0.0
                subjetividade = 0.5
        except ImportError:
            # TextBlob não instalado
            polaridade = 0.0
            subjetividade = 0.5

        if polaridade > 0.1:
            classificacao = "positivo"
        elif polaridade < -0.1:
            classificacao = "negativo"
        else:
            classificacao = "neutro"

        return Sentimento(
            polaridade=polaridade, subjetividade=subjetividade, classificacao=classificacao
        )

    def _palavras_frequentes(self, doc, limite: int = 20) -> List[tuple]:
        """Extrai palavras mais frequentes (ignorando stopwords)."""
        palavras = [
            token.text.lower()
            for token in doc
            if not token.is_stop
            and not token.is_punct
            and not token.is_space
            and len(token.text) > 2
        ]

        contador = Counter(palavras)
        return contador.most_common(limite)

    def analisar(self, texto: str, documento_id: int, idioma: str = "ru") -> AnaliseTexto:
        """
        Analisa texto completo.
        O modelo é carregado sob demanda na primeira chamada.
        """
        logger.info(f"🔍 Analisando documento {documento_id} em {idioma}")
        inicio = time.time()

        # Carregar modelo (lazy)
        nlp = self._get_model(idioma)

        # Processar texto (limitado por performance)
        doc = nlp(texto[:100000])

        # Estatísticas
        estatisticas = self._calcular_estatisticas(texto, doc)

        # Entidades
        entidades = self._extrair_entidades(doc)
        entidades_agrupadas = self._agrupar_entidades(entidades)

        # Sentimento
        sentimento = self._analisar_sentimento(texto, idioma)

        # Palavras frequentes
        palavras_freq = self._palavras_frequentes(doc)

        tempo = time.time() - inicio
        logger.info(
            f"✅ Análise concluída em {tempo:.2f}s - {len(entidades)} entidades encontradas"
        )

        return AnaliseTexto(
            documento_id=documento_id,
            idioma=idioma,
            data_analise=datetime.now(),
            estatisticas=estatisticas,
            entidades=entidades,
            entidades_por_tipo=entidades_agrupadas,
            sentimento=sentimento,
            palavras_frequentes=palavras_freq,
            modelo_utilizado=f"spacy-{idioma}",
            tempo_processamento=tempo,
        )
