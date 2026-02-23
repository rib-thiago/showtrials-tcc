# src/tests/test_analisar_acervo_telemetry.py
"""
Testes de telemetria para o caso de uso AnalisarAcervo.
"""

from unittest.mock import MagicMock, Mock, patch

import pytest

import src.application.use_cases.analisar_acervo as uc_module


class TestAnalisarAcervoTelemetry:
    """Testes de telemetria para o caso de uso."""

    def setup_method(self):
        """Reconfigura o módulo antes de cada teste."""
        uc_module._telemetry = None

    @pytest.fixture
    def documentos_mock(self):
        """Fixture com documentos mock."""
        docs = []
        for i in range(5):
            doc = Mock()
            doc.texto = "palavra " * 100
            doc.id = i
            docs.append(doc)
        return docs

    def test_telemetria_estatisticas(self, documentos_mock):
        """Execução de estatísticas deve registrar telemetria."""
        mock_telemetry = MagicMock()
        uc_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.application.use_cases.analisar_acervo import AnalisarAcervo

        mock_repo = Mock()
        mock_repo.listar.return_value = documentos_mock

        caso_uso = AnalisarAcervo(repo_doc=mock_repo)
        stats = caso_uso.estatisticas_globais()

        mock_telemetry.increment.assert_any_call("analisar_acervo.estatisticas.iniciado")
        mock_telemetry.increment.assert_any_call("analisar_acervo.estatisticas.documentos", value=5)
        mock_telemetry.increment.assert_any_call("analisar_acervo.estatisticas.concluido")

    def test_telemetria_analyzer_disponivel(self, documentos_mock):
        """Analyzer disponível deve registrar contador."""
        mock_telemetry = MagicMock()
        uc_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.application.use_cases.analisar_acervo import AnalisarAcervo
        from src.infrastructure.registry import ServiceRegistry

        mock_repo = Mock()
        mock_repo.listar.return_value = documentos_mock

        mock_registry = Mock(spec=ServiceRegistry)
        mock_registry.get.return_value = Mock()

        caso_uso = AnalisarAcervo(
            repo_doc=mock_repo,
            registry=mock_registry,
        )

        stats = caso_uso.estatisticas_globais()

        mock_telemetry.increment.assert_any_call("analisar_acervo.analyzer.disponivel")

    def test_telemetria_analyzer_indisponivel(self, documentos_mock):
        """Analyzer indisponível deve registrar contador."""
        mock_telemetry = MagicMock()
        uc_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.application.use_cases.analisar_acervo import AnalisarAcervo
        from src.infrastructure.registry import ServiceRegistry

        mock_repo = Mock()
        mock_repo.listar.return_value = documentos_mock

        mock_registry = Mock(spec=ServiceRegistry)
        mock_registry.get.side_effect = Exception("Indisponível")

        caso_uso = AnalisarAcervo(
            repo_doc=mock_repo,
            registry=mock_registry,
        )

        stats = caso_uso.estatisticas_globais()

        mock_telemetry.increment.assert_any_call("analisar_acervo.analyzer.indisponivel")

    def test_telemetria_wordcloud(self, documentos_mock):
        """Geração de wordcloud deve registrar telemetria."""
        mock_telemetry = MagicMock()
        uc_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.application.use_cases.analisar_acervo import AnalisarAcervo
        from src.infrastructure.registry import ServiceRegistry

        mock_repo = Mock()
        mock_repo.listar.return_value = documentos_mock

        mock_registry = Mock(spec=ServiceRegistry)

        class MockWordCloud:
            def gerar(self, *args, **kwargs):
                pass

        mock_registry.get.return_value = MockWordCloud()

        caso_uso = AnalisarAcervo(
            repo_doc=mock_repo,
            registry=mock_registry,
        )

        with patch("pathlib.Path.mkdir"):
            caminho = caso_uso.gerar_wordcloud_geral()

        mock_telemetry.increment.assert_any_call("analisar_acervo.wordcloud.iniciado")
        mock_telemetry.increment.assert_any_call("analisar_acervo.wordcloud.idioma.ru")
        mock_telemetry.increment.assert_any_call("analisar_acervo.wordcloud.sucesso")

    def test_telemetria_wordcloud_erro(self, documentos_mock):
        """Erro na wordcloud deve registrar contador de erro."""
        mock_telemetry = MagicMock()
        uc_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.application.use_cases.analisar_acervo import AnalisarAcervo
        from src.infrastructure.registry import ServiceRegistry

        mock_repo = Mock()
        mock_repo.listar.return_value = documentos_mock

        mock_registry = Mock(spec=ServiceRegistry)

        class WordCloudFalhaError(Exception):
            """Erro simulado do gerador de wordcloud no teste."""

        class WordCloudQueFalha:
            def gerar(self, *args, **kwargs):
                raise WordCloudFalhaError("Falha")

        mock_registry.get.return_value = WordCloudQueFalha()

        caso_uso = AnalisarAcervo(
            repo_doc=mock_repo,
            registry=mock_registry,
        )

        with patch("pathlib.Path.mkdir"):
            with pytest.raises(WordCloudFalhaError):
                caso_uso.gerar_wordcloud_geral()

        mock_telemetry.increment.assert_any_call("analisar_acervo.wordcloud.erro")

    def test_sem_telemetria_nao_quebra(self, documentos_mock):
        """Sem telemetria, o código deve funcionar normalmente."""
        from src.application.use_cases.analisar_acervo import AnalisarAcervo

        mock_repo = Mock()
        mock_repo.listar.return_value = documentos_mock

        caso_uso = AnalisarAcervo(repo_doc=mock_repo)
        stats = caso_uso.estatisticas_globais()

        assert stats["total_docs"] == 5
