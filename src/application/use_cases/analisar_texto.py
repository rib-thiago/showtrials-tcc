# src/application/use_cases/analisar_texto.py
"""
Caso de uso: Analisar um documento individual.
"""

from datetime import datetime
from pathlib import Path
from typing import Optional

from src.domain.interfaces.repositories import RepositorioDocumento
from src.domain.interfaces.repositorio_traducao import RepositorioTraducao
from src.domain.value_objects.analise_texto import AnaliseTexto
from src.infrastructure.analysis.spacy_analyzer import SpacyAnalyzer
from src.infrastructure.analysis.wordcloud_generator import WordCloudGenerator
from src.infrastructure.registry import ServiceRegistry


class AnalisarDocumento:
    """
    Caso de uso para analisar um documento.
    Agora usa Service Registry para obter serviços sob demanda.
    """

    def __init__(
        self,
        repo_doc: RepositorioDocumento,
        repo_trad: Optional[RepositorioTraducao] = None,
        registry: Optional[ServiceRegistry] = None,
    ):
        """
        Args:
            repo_doc: Repositório de documentos
            repo_trad: Repositório de traduções (opcional)
            registry: Registry de serviços (para lazy loading)
        """
        self.repo_doc = repo_doc
        self.repo_trad = repo_trad
        self.registry = registry or ServiceRegistry()

    def _get_analyzer(self) -> SpacyAnalyzer:
        """Obtém analisador spaCy do registry (lazy)."""
        return self.registry.get("spacy")

    def _get_wordcloud(self) -> WordCloudGenerator:
        """Obtém gerador de wordcloud do registry (lazy)."""
        return self.registry.get("wordcloud")

    def executar(
        self, documento_id: int, idioma: str = "ru", gerar_wordcloud: bool = False
    ) -> Optional[AnaliseTexto]:
        """
        Analisa um documento específico.

        Args:
            documento_id: ID do documento
            idioma: 'ru' (original) ou código de tradução
            gerar_wordcloud: Se True, gera imagem da nuvem

        Returns:
            AnaliseTexto com resultados
        """
        # 1. Buscar texto
        if idioma == "ru":
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

        # 2. Analisar (usa registry para obter analyzer)
        analyzer = self._get_analyzer()
        analise = analyzer.analisar(texto=texto, documento_id=documento_id, idioma=idioma)

        # 3. Gerar wordcloud se solicitado
        if gerar_wordcloud:
            wordcloud = self._get_wordcloud()
            nome_arquivo = (
                f"wordcloud_{documento_id}_{idioma}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            )
            caminho = Path("analises") / nome_arquivo
            wordcloud.gerar(
                texto=texto,
                titulo=f"Documento {documento_id} - {idioma}",
                idioma=idioma,
                salvar_em=str(caminho),
            )
            # Opcional: adicionar caminho à análise
            # analise.wordcloud_path = str(caminho)

        return analise
