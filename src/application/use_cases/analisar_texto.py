# src/application/use_cases/analisar_texto.py
"""
Caso de uso: Analisar um documento individual.
"""

from typing import Optional
from datetime import datetime  # <-- IMPORT ADICIONADO!
from pathlib import Path

from src.domain.interfaces.repositories import RepositorioDocumento
from src.domain.interfaces.repositorio_traducao import RepositorioTraducao
from src.infrastructure.analysis.spacy_analyzer import SpacyAnalyzer
from src.infrastructure.analysis.wordcloud_generator import WordCloudGenerator
from src.domain.value_objects.analise_texto import AnaliseTexto


class AnalisarDocumento:
    """
    Caso de uso para analisar um documento.
    """
    
    def __init__(self,
                 repo_doc: RepositorioDocumento,
                 repo_trad: Optional[RepositorioTraducao] = None):
        self.repo_doc = repo_doc
        self.repo_trad = repo_trad
        self.analyzer = SpacyAnalyzer()
        self.wordcloud = WordCloudGenerator()
    
    def executar(self, 
                 documento_id: int,
                 idioma: str = 'ru',
                 gerar_wordcloud: bool = False) -> Optional[AnaliseTexto]:
        """
        Analisa um documento específico.
        """
        # 1. Buscar texto
        if idioma == 'ru':
            doc = self.repo_doc.buscar_por_id(documento_id)
            if not doc:
                return None
            texto = doc.texto
        else:
            if not self.repo_trad:
                return None
            traducao = self.repo_trad.buscar_por_documento(documento_id, idioma)
            if not traducao:
                return None
            texto = traducao.texto_traduzido
        
        # 2. Analisar
        analise = self.analyzer.analisar(
            texto=texto,
            documento_id=documento_id,
            idioma=idioma
        )
        
        # 3. Gerar wordcloud se solicitado
        if gerar_wordcloud:
            nome_arquivo = f"wordcloud_{documento_id}_{idioma}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            caminho = Path("analises") / nome_arquivo
            self.wordcloud.gerar(
                texto=texto,
                titulo=f"Documento {documento_id} - {idioma}",
                idioma=idioma,
                salvar_em=str(caminho)
            )
            # Adicionar caminho ao objeto de análise (precisa estender a classe)
            # Por enquanto, apenas retornamos a análise
        
        return analise