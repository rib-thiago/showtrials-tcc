# src/infrastructure/analysis/wordcloud_generator.py
"""
Gerador de nuvem de palavras.
"""

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from pathlib import Path
import spacy
from collections import Counter
from typing import Optional


class WordCloudGenerator:
    """
    Gera nuvens de palavras a partir de textos.
    """
    
    def __init__(self):
        # Carregar stopwords para múltiplos idiomas
        self.stopwords = self._carregar_stopwords()
    
    def _carregar_stopwords(self) -> set:
        """Carrega stopwords de vários idiomas."""
        stopwords = set()
        
        # Stopwords em russo (básicas)
        stopwords_ru = {'и', 'в', 'на', 'с', 'по', 'для', 'что', 'как', 'это', 
                        'весь', 'мой', 'твой', 'его', 'ее', 'их', 'к', 'у', 'о',
                        'из', 'за', 'над', 'под', 'а', 'но', 'да', 'или', 'если'}
        
        # Stopwords em inglês
        try:
            from wordcloud import STOPWORDS
            stopwords.update(STOPWORDS)
        except:
            pass
        
        stopwords.update(stopwords_ru)
        return stopwords
    
    def gerar(self, 
              texto: str,
              titulo: str = "Nuvem de Palavras",
              idioma: str = 'ru',
              max_palavras: int = 100,
              largura: int = 800,
              altura: int = 400,
              salvar_em: Optional[str] = None) -> Optional[Path]:
        """
        Gera nuvem de palavras a partir do texto.
        """
        # Processar texto com SpaCy para melhor tokenização
        try:
            if idioma == 'ru':
                nlp = spacy.load('ru_core_news_sm')
            else:
                nlp = spacy.load('en_core_web_sm')
            
            doc = nlp(texto[:50000])  # Limitar tamanho
            
            # Extrair palavras significativas
            palavras = [
                token.text.lower() for token in doc
                if not token.is_stop 
                and not token.is_punct 
                and not token.is_space
                and len(token.text) > 2
                and token.text.lower() not in self.stopwords
            ]
            
            # Contar frequências
            frequencias = Counter(palavras)
            
        except:
            # Fallback: split simples
            palavras = texto.lower().split()
            palavras = [p for p in palavras if len(p) > 2 and p not in self.stopwords]
            frequencias = Counter(palavras)
        
        # Gerar nuvem
        wordcloud = WordCloud(
            width=largura,
            height=altura,
            background_color='white',
            max_words=max_palavras,
            stopwords=self.stopwords,
            collocations=False
        ).generate_from_frequencies(frequencias)
        
        # Plotar
        plt.figure(figsize=(largura/100, altura/100))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title(titulo)
        
        if salvar_em:
            caminho = Path(salvar_em)
            caminho.parent.mkdir(exist_ok=True)
            plt.savefig(caminho, bbox_inches='tight', dpi=300)
            plt.close()
            return caminho
        else:
            plt.show()
            return None