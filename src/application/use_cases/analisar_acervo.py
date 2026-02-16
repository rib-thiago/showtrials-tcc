# src/application/use_cases/analisar_acervo.py
"""
Caso de uso: Analisar todo o acervo (estatísticas globais).
"""

from typing import List, Dict
from collections import Counter
from datetime import datetime
from pathlib import Path

from src.domain.interfaces.repositories import RepositorioDocumento
from src.infrastructure.analysis.spacy_analyzer import SpacyAnalyzer
from src.infrastructure.analysis.wordcloud_generator import WordCloudGenerator


class AnalisarAcervo:
    """
    Caso de uso para análise global do acervo.
    """
    
    def __init__(self, repo_doc: RepositorioDocumento):
        self.repo_doc = repo_doc
        self.analyzer = SpacyAnalyzer()
        self.wordcloud = WordCloudGenerator()
    
    def estatisticas_globais(self) -> Dict:
        """
        Estatísticas agregadas de todo o acervo.
        """
        documentos = self.repo_doc.listar(limite=5000)
        
        stats = {
            'total_docs': len(documentos),
            'total_palavras': 0,
            'total_caracteres': 0,
            'media_palavras_por_doc': 0,
            'documentos_por_tamanho': {
                'pequeno (<1000 palavras)': 0,
                'médio (1000-5000 palavras)': 0,
                'grande (>5000 palavras)': 0
            },
            'pessoas_mais_citadas': Counter(),
            'locais_mais_citados': Counter(),
            'organizacoes_mais_citadas': Counter(),
        }
        
        # Amostra para análise de entidades (limitado por performance)
        amostra = documentos[:100]
        
        for doc in amostra:
            # Estatísticas básicas
            palavras = doc.texto.split()
            num_palavras = len(palavras)
            stats['total_palavras'] += num_palavras
            stats['total_caracteres'] += len(doc.texto)
            
            # Classificar por tamanho
            if num_palavras < 1000:
                stats['documentos_por_tamanho']['pequeno (<1000 palavras)'] += 1
            elif num_palavras < 5000:
                stats['documentos_por_tamanho']['médio (1000-5000 palavras)'] += 1
            else:
                stats['documentos_por_tamanho']['grande (>5000 palavras)'] += 1
            
            # Análise de entidades (apenas para alguns)
            if len(amostra) < 50:  # Performance
                try:
                    analise = self.analyzer.analisar(doc.texto[:20000], doc.id, 'ru')
                    
                    # Contar pessoas
                    for ent in analise.entidades:
                        if ent.tipo == 'PERSON':
                            stats['pessoas_mais_citadas'][ent.text] += 1
                        elif ent.tipo in ['LOC', 'GPE']:
                            stats['locais_mais_citados'][ent.text] += 1
                        elif ent.tipo == 'ORG':
                            stats['organizacoes_mais_citadas'][ent.text] += 1
                except:
                    pass
        
        # Calcular médias
        if stats['total_docs'] > 0:
            stats['media_palavras_por_doc'] = stats['total_palavras'] / stats['total_docs']
        
        # Top lists
        stats['top_pessoas'] = stats['pessoas_mais_citadas'].most_common(20)
        stats['top_locais'] = stats['locais_mais_citados'].most_common(10)
        stats['top_organizacoes'] = stats['organizacoes_mais_citadas'].most_common(10)
        
        return stats
    
    def gerar_wordcloud_geral(self, idioma: str = 'ru') -> Path:
        """
        Gera nuvem de palavras com todo o acervo.
        """
        documentos = self.repo_doc.listar(limite=500)
        
        # Concatenar textos (limitado)
        texto_completo = ""
        for doc in documentos[:100]:  # Limitar para performance
            texto_completo += doc.texto[:5000] + "\n"
        
        nome_arquivo = f"wordcloud_acervo_{idioma}_{datetime.now().strftime('%Y%m%d')}.png"
        caminho = Path("analises") / nome_arquivo
        
        self.wordcloud.gerar(
            texto=texto_completo,
            titulo=f"Acervo Completo - {idioma}",
            idioma=idioma,
            max_palavras=200,
            salvar_em=str(caminho)
        )
        
        return caminho