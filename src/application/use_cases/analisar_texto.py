# src/application/use_cases/analisar_texto.py
"""
Caso de uso: Analisar um documento individual com telemetria.
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

# Telemetria opcional
_telemetry = None


def configure_telemetry(telemetry_instance=None):
    """Configura telemetria para este módulo (usado apenas em testes)."""
    global _telemetry
    _telemetry = telemetry_instance


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
        if _telemetry:
            _telemetry.increment("analisar_documento.executar.iniciado")
            _telemetry.increment(f"analisar_documento.idioma.{idioma}")

        # 1. Buscar texto
        if idioma == "ru":
            doc = self.repo_doc.buscar_por_id(documento_id)
            if not doc:
                if _telemetry:
                    _telemetry.increment("analisar_documento.erro.documento_nao_encontrado")
                return None
            texto = doc.texto
        else:
            if not self.repo_trad:
                if _telemetry:
                    _telemetry.increment("analisar_documento.erro.repo_trad_indisponivel")
                return None
            traducao = self.repo_trad.buscar_por_documento(documento_id, idioma)
            if not traducao:
                if _telemetry:
                    _telemetry.increment("analisar_documento.erro.traducao_nao_encontrada")
                return None
            texto = traducao.texto_traduzido

        # 2. Analisar (usa registry para obter analyzer)
        try:
            analyzer = self._get_analyzer()
            analise = analyzer.analisar(texto=texto, documento_id=documento_id, idioma=idioma)
            if _telemetry:
                _telemetry.increment("analisar_documento.analise.sucesso")
                _telemetry.increment("analisar_documento.caracteres", value=len(texto))
        except Exception as e:
            if _telemetry:
                _telemetry.increment("analisar_documento.analise.erro")
            raise e

        # 3. Gerar wordcloud se solicitado
        if gerar_wordcloud:
            try:
                wordcloud = self._get_wordcloud()
                nome_arquivo = f"wordcloud_{documento_id}_{idioma}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                caminho = Path("analises") / nome_arquivo
                wordcloud.gerar(
                    texto=texto,
                    titulo=f"Documento {documento_id} - {idioma}",
                    idioma=idioma,
                    salvar_em=str(caminho),
                )
                if _telemetry:
                    _telemetry.increment("analisar_documento.wordcloud.sucesso")
                # Opcional: adicionar caminho à análise
                # analise.wordcloud_path = str(caminho)
            except Exception as e:
                if _telemetry:
                    _telemetry.increment("analisar_documento.wordcloud.erro")
                raise e

        if _telemetry:
            _telemetry.increment("analisar_documento.executar.concluido")

        return analise
