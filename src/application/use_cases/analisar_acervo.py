# src/application/use_cases/analisar_acervo.py
"""
Caso de uso: Analisar todo o acervo (estatísticas globais) com telemetria.
"""

from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional

from src.domain.interfaces.repositories import RepositorioDocumento
from src.infrastructure.analysis.spacy_analyzer import SpacyAnalyzer
from src.infrastructure.analysis.wordcloud_generator import WordCloudGenerator
from src.infrastructure.registry import ServiceRegistry

# Telemetria opcional
_telemetry = None


def configure_telemetry(telemetry_instance=None):
    """Configura telemetria para este módulo (usado apenas em testes)."""
    global _telemetry
    _telemetry = telemetry_instance


class AnalisarAcervo:
    """
    Caso de uso para análise global do acervo.
    """

    def __init__(self, repo_doc: RepositorioDocumento, registry: Optional[ServiceRegistry] = None):
        self.repo_doc = repo_doc
        self.registry = registry or ServiceRegistry()

    def _get_analyzer(self) -> SpacyAnalyzer:
        """Obtém analisador spaCy do registry."""
        return self.registry.get("spacy")

    def _get_wordcloud(self) -> WordCloudGenerator:
        """Obtém gerador de wordcloud do registry."""
        return self.registry.get("wordcloud")

    def estatisticas_globais(self) -> Dict[str, Any]:
        """
        Estatísticas agregadas de todo o acervo.
        """
        if _telemetry:
            _telemetry.increment("analisar_acervo.estatisticas.iniciado")

        documentos = self.repo_doc.listar(limite=5000)

        stats: Dict[str, Any] = {
            "total_docs": len(documentos),
            "total_palavras": 0,
            "total_caracteres": 0,
            "media_palavras_por_doc": 0,
            "documentos_por_tamanho": {
                "pequeno (<1000 palavras)": 0,
                "médio (1000-5000 palavras)": 0,
                "grande (>5000 palavras)": 0,
            },
            "pessoas_mais_citadas": [],
            "top_locais": [],
            "top_organizacoes": [],
        }

        if _telemetry:
            _telemetry.increment("analisar_acervo.estatisticas.documentos", value=len(documentos))

        # Amostra para análise de entidades (limitado por performance)
        amostra = documentos[:100]

        # Usa analyzer se disponível
        try:
            analyzer = self._get_analyzer()
            analyzer_disponivel = True
            if _telemetry:
                _telemetry.increment("analisar_acervo.analyzer.disponivel")
        except Exception:
            analyzer = None
            analyzer_disponivel = False
            if _telemetry:
                _telemetry.increment("analisar_acervo.analyzer.indisponivel")

        for doc in amostra:
            # Estatísticas básicas
            palavras = doc.texto.split()
            num_palavras = len(palavras)
            stats["total_palavras"] += num_palavras
            stats["total_caracteres"] += len(doc.texto)

            # Classificar por tamanho
            if num_palavras < 1000:
                stats["documentos_por_tamanho"]["pequeno (<1000 palavras)"] += 1
            elif num_palavras < 5000:
                stats["documentos_por_tamanho"]["médio (1000-5000 palavras)"] += 1
            else:
                stats["documentos_por_tamanho"]["grande (>5000 palavras)"] += 1

            # Análise de entidades (apenas se analyzer disponível)
            if analyzer and len(amostra) < 50:  # Performance
                try:
                    if doc.id is not None:
                        analise = analyzer.analisar(doc.texto[:20000], doc.id, "ru")
                    if _telemetry:
                        _telemetry.increment("analisar_acervo.analise_entidades.sucesso")
                except Exception:
                    if _telemetry:
                        _telemetry.increment("analisar_acervo.analise_entidades.erro")
                    pass

        # Calcular médias
        if stats["total_docs"] > 0:
            stats["media_palavras_por_doc"] = stats["total_palavras"] / stats["total_docs"]

        if _telemetry:
            _telemetry.increment("analisar_acervo.estatisticas.concluido")

        return stats

    def gerar_wordcloud_geral(self, idioma: str = "ru") -> Path:
        """
        Gera nuvem de palavras com todo o acervo.
        """
        if _telemetry:
            _telemetry.increment("analisar_acervo.wordcloud.iniciado")
            _telemetry.increment(f"analisar_acervo.wordcloud.idioma.{idioma}")

        documentos = self.repo_doc.listar(limite=500)

        # Concatenar textos (limitado)
        texto_completo = ""
        for doc in documentos[:100]:  # Limitar para performance
            texto_completo += doc.texto[:5000] + "\n"

        nome_arquivo = f"wordcloud_acervo_{idioma}_{datetime.now().strftime('%Y%m%d')}.png"
        caminho = Path("analises") / nome_arquivo

        try:
            wordcloud = self._get_wordcloud()
            wordcloud.gerar(
                texto=texto_completo,
                titulo=f"Acervo Completo - {idioma}",
                idioma=idioma,
                max_palavras=200,
                salvar_em=str(caminho),
            )
            if _telemetry:
                _telemetry.increment("analisar_acervo.wordcloud.sucesso")
        except Exception as e:
            if _telemetry:
                _telemetry.increment("analisar_acervo.wordcloud.erro")
            raise e

        return caminho
