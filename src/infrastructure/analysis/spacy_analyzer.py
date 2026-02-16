# src/infrastructure/analysis/spacy_analyzer.py
"""
Integração com SpaCy para análise de texto multilíngue.
"""

import spacy
from typing import List, Dict, Optional
import time
from collections import Counter
import re
from datetime import datetime  # <-- DEVE EXISTIR

from src.domain.value_objects.analise_texto import (
    AnaliseTexto, Entidade, Sentimento, EstatisticasTexto
)


class SpacyAnalyzer:
    """
    Analisador de texto usando SpaCy.
    Suporta múltiplos idiomas.
    """
    
    # Mapeamento de idiomas para modelos SpaCy
    MODELOS = {
        'ru': 'ru_core_news_sm',
        'en': 'en_core_web_sm',
        'pt': 'pt_core_news_sm',  # Opcional
    }
    
    # Mapeamento de tipos de entidade para português
    TIPOS_ENTIDADE = {
        'PERSON': 'Pessoa',
        'ORG': 'Organização',
        'LOC': 'Local',
        'GPE': 'Local (país/cidade)',
        'DATE': 'Data',
        'TIME': 'Hora',
        'MONEY': 'Valor',
        'PERCENT': 'Percentual',
        'FAC': 'Instalação',
        'PRODUCT': 'Produto',
        'EVENT': 'Evento',
        'LAW': 'Lei',
    }
    
    def __init__(self):
        self._modelos = {}
        self._carregar_modelos()
    
    def _carregar_modelos(self):
        """Carrega modelos sob demanda."""
        for idioma, modelo in self.MODELOS.items():
            try:
                self._modelos[idioma] = spacy.load(modelo)
                print(f"✅ Modelo SpaCy carregado: {modelo}")
            except OSError:
                print(f"⚠️ Modelo {modelo} não encontrado. Instale com:")
                print(f"   python -m spacy download {modelo}")
                self._modelos[idioma] = None
    
    def _get_nlp(self, idioma: str):
        """Retorna modelo para o idioma."""
        if idioma not in self._modelos:
            raise ValueError(f"Idioma não suportado: {idioma}")
        
        if self._modelos[idioma] is None:
            raise RuntimeError(f"Modelo para {idioma} não carregado")
        
        return self._modelos[idioma]
    
    def _calcular_estatisticas(self, texto: str, doc) -> EstatisticasTexto:
        """Calcula estatísticas do texto."""
        # Limpeza básica
        texto_limpo = re.sub(r'\s+', ' ', texto)
        palavras = [token.text for token in doc if not token.is_punct and not token.is_space]
        frases = list(doc.sents)
        
        return EstatisticasTexto(
            total_caracteres=len(texto),
            total_palavras=len(palavras),
            total_paragrafos=texto.count('\n') + 1,
            total_frases=len(frases),
            palavras_unicas=len(set(p.lower() for p in palavras)),
            densidade_lexica=len(set(palavras)) / len(palavras) if palavras else 0,
            tamanho_medio_palavra=sum(len(p) for p in palavras) / len(palavras) if palavras else 0,
            tamanho_medio_frase=len(palavras) / len(frases) if frases else 0
        )
    
    def _extrair_entidades(self, doc) -> List[Entidade]:
        """Extrai entidades do documento."""
        entidades = []
        for ent in doc.ents:
            entidades.append(Entidade(
                texto=ent.text,
                tipo=ent.label_,
                confianca=1.0,  # SpaCy não dá confidence score
                posicao_inicio=ent.start_char,
                posicao_fim=ent.end_char
            ))
        return entidades
    
    def _agrupar_entidades(self, entidades: List[Entidade]) -> Dict[str, List[str]]:
        """Agrupa entidades por tipo."""
        grupos = {}
        for ent in entidades:
            tipo_pt = self.TIPOS_ENTIDADE.get(ent.tipo, ent.tipo)
            if tipo_pt not in grupos:
                grupos[tipo_pt] = []
            if ent.texto not in grupos[tipo_pt]:  # <-- ent.texto, não ent.text
                grupos[tipo_pt].append(ent.texto)
        return grupos
    
    def _analisar_sentimento(self, texto: str, idioma: str) -> Sentimento:
        """
        Análise de sentimento básica.
        Para análise avançada, usaríamos transformers.
        """
        from textblob import TextBlob
        
        if idioma == 'en':
            blob = TextBlob(texto)
            polaridade = blob.sentiment.polarity
            subjetividade = blob.sentiment.subjectivity
        else:
            # Para russo/português, usaríamos modelo específico
            # Placeholder
            polaridade = 0.0
            subjetividade = 0.5
        
        if polaridade > 0.1:
            classificacao = 'positivo'
        elif polaridade < -0.1:
            classificacao = 'negativo'
        else:
            classificacao = 'neutro'
        
        return Sentimento(
            polaridade=polaridade,
            subjetividade=subjetividade,
            classificacao=classificacao
        )
    
    def _palavras_frequentes(self, doc, limite: int = 20) -> List[tuple]:
        """Extrai palavras mais frequentes (ignorando stopwords)."""
        palavras = [
            token.text.lower() for token in doc 
            if not token.is_stop 
            and not token.is_punct 
            and not token.is_space
            and len(token.text) > 2
        ]
        
        contador = Counter(palavras)
        return contador.most_common(limite)
    
    def analisar(self, 
                 texto: str, 
                 documento_id: int,
                 idioma: str = 'ru') -> AnaliseTexto:
        """
        Analisa texto completo.
        """
        inicio = time.time()
        
        # Carregar modelo
        nlp = self._get_nlp(idioma)
        
        # Processar texto
        doc = nlp(texto[:100000])  # Limitar tamanho por performance
        
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
            tempo_processamento=tempo
        )