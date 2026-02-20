# src/tests/test_analisar_acervo.py
"""
Testes de lógica para o caso de uso AnalisarAcervo.
"""

from pathlib import Path
from unittest.mock import Mock, patch

import pytest

from src.application.use_cases.analisar_acervo import AnalisarAcervo
from src.domain.entities.documento import Documento
from src.infrastructure.registry import ServiceRegistry


class MockSpacyAnalyzer:
    """Mock do analisador spaCy."""

    def analisar(self, texto, doc_id, idioma):
        return Mock()


class MockWordCloudGenerator:
    """Mock do gerador de wordcloud."""

    def gerar(self, texto, titulo, idioma, max_palavras, salvar_em):
        return Path(salvar_em)


class TestAnalisarAcervo:
    """Testes para o caso de uso AnalisarAcervo."""

    @pytest.fixture
    def documentos_mock(self):
        """Fixture com documentos mock."""
        docs = []
        for i in range(10):
            doc = Mock(spec=Documento)
            doc.texto = "palavra " * 200  # ~400 palavras
            doc.id = i
            docs.append(doc)
        return docs

    @pytest.fixture
    def setup_mocks(self, documentos_mock):
        """Fixture com mocks configurados."""
        mock_repo_doc = Mock()
        mock_repo_doc.listar.return_value = documentos_mock

        mock_registry = Mock(spec=ServiceRegistry)
        mock_registry.get.side_effect = lambda name: {
            "spacy": MockSpacyAnalyzer(),
            "wordcloud": MockWordCloudGenerator(),
        }.get(name)

        return {"repo_doc": mock_repo_doc, "registry": mock_registry}

    def test_estatisticas_globais(self, setup_mocks):
        """Deve calcular estatísticas básicas corretamente."""
        caso_uso = AnalisarAcervo(
            repo_doc=setup_mocks["repo_doc"],
            registry=setup_mocks["registry"],
        )

        stats = caso_uso.estatisticas_globais()

        assert stats["total_docs"] == 10
        assert stats["total_palavras"] > 0
        assert stats["total_caracteres"] > 0
        assert stats["media_palavras_por_doc"] > 0
        assert "documentos_por_tamanho" in stats

    def test_estatisticas_com_documentos_variados(self):
        """Deve classificar documentos por tamanho corretamente."""
        mock_repo = Mock()

        # Criar documentos de diferentes tamanhos (em PALAVRAS, não caracteres)
        docs = []

        # Documento pequeno: 500 palavras
        doc_pequeno = Mock(spec=Documento)
        doc_pequeno.texto = "palavra " * 500
        docs.append(doc_pequeno)

        # Documento médio: 2000 palavras
        doc_medio = Mock(spec=Documento)
        doc_medio.texto = "palavra " * 2000
        docs.append(doc_medio)

        # Documento grande: 6000 palavras
        doc_grande = Mock(spec=Documento)
        doc_grande.texto = "palavra " * 6000
        docs.append(doc_grande)

        mock_repo.listar.return_value = docs

        caso_uso = AnalisarAcervo(repo_doc=mock_repo)
        stats = caso_uso.estatisticas_globais()

        assert stats["documentos_por_tamanho"]["pequeno (<1000 palavras)"] == 1
        assert stats["documentos_por_tamanho"]["médio (1000-5000 palavras)"] == 1
        assert stats["documentos_por_tamanho"]["grande (>5000 palavras)"] == 1

    def test_estatisticas_sem_analyzer(self, documentos_mock):
        """Deve funcionar mesmo sem analyzer disponível."""
        mock_repo = Mock()
        mock_repo.listar.return_value = documentos_mock

        # Registry que falha ao obter analyzer
        mock_registry = Mock(spec=ServiceRegistry)
        mock_registry.get.side_effect = Exception("Falha")

        caso_uso = AnalisarAcervo(
            repo_doc=mock_repo,
            registry=mock_registry,
        )

        stats = caso_uso.estatisticas_globais()
        assert stats["total_docs"] == 10

    def test_gerar_wordcloud_geral(self, setup_mocks, tmp_path):
        """Deve gerar wordcloud e retornar caminho."""
        caso_uso = AnalisarAcervo(
            repo_doc=setup_mocks["repo_doc"],
            registry=setup_mocks["registry"],
        )

        with patch("pathlib.Path.mkdir"):
            caminho = caso_uso.gerar_wordcloud_geral(idioma="ru")

        assert caminho is not None
        assert "wordcloud_acervo_ru_" in str(caminho)

    def test_gerar_wordcloud_com_erro(self, setup_mocks):
        """Erro na geração de wordcloud deve ser propagado."""
        mock_registry = Mock(spec=ServiceRegistry)

        class WordCloudQueFalha:
            def gerar(self, *args, **kwargs):
                raise Exception("Falha na geração")

        mock_registry.get.return_value = WordCloudQueFalha()

        caso_uso = AnalisarAcervo(
            repo_doc=setup_mocks["repo_doc"],
            registry=mock_registry,
        )

        with pytest.raises(Exception, match="Falha na geração"):
            caso_uso.gerar_wordcloud_geral()
