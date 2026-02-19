# src/tests/test_factories_telemetry.py
"""
Testes de telemetria para as factories.
"""

from unittest.mock import MagicMock, patch

import src.infrastructure.factories as factories_module


class TestFactoriesTelemetry:
    """Testes de telemetria para as factories."""

    def setup_method(self):
        """Reconfigura o módulo antes de cada teste."""
        factories_module._telemetry = None

    def test_telemetria_translator_mock(self):
        """Tradutor mock deve registrar contador."""
        mock_telemetry = MagicMock()
        factories_module.configure_telemetry(telemetry_instance=mock_telemetry)

        factories_module.create_translator(simulate=True)

        mock_telemetry.increment.assert_any_call("factory.translator.mock")

    def test_telemetria_translator_real(self):
        """Tradutor real deve registrar contador."""
        mock_telemetry = MagicMock()
        factories_module.configure_telemetry(telemetry_instance=mock_telemetry)

        with patch("src.infrastructure.factories.GoogleTranslator"):
            factories_module.create_translator(api_key="test", simulate=False)

        mock_telemetry.increment.assert_any_call("factory.translator.real")

    def test_telemetria_translator_fallback(self):
        """Fallback do tradutor deve registrar contador."""
        mock_telemetry = MagicMock()
        factories_module.configure_telemetry(telemetry_instance=mock_telemetry)

        with patch("src.infrastructure.factories.GoogleTranslator", side_effect=Exception("Erro")):
            factories_module.create_translator(api_key="test", simulate=False)

        mock_telemetry.increment.assert_any_call("factory.translator.fallback")

    def test_telemetria_spacy_mock(self):
        """Spacy mock deve registrar contador."""
        mock_telemetry = MagicMock()
        factories_module.configure_telemetry(telemetry_instance=mock_telemetry)

        factories_module.create_spacy_analyzer(simulate=True)

        mock_telemetry.increment.assert_any_call("factory.spacy.mock")

    def test_telemetria_spacy_real(self):
        """Spacy real deve registrar contador."""
        mock_telemetry = MagicMock()
        factories_module.configure_telemetry(telemetry_instance=mock_telemetry)

        with patch("src.infrastructure.factories.SpacyAnalyzer"):
            factories_module.create_spacy_analyzer(simulate=False)

        mock_telemetry.increment.assert_any_call("factory.spacy.real")

    def test_telemetria_spacy_preload(self):
        """Pré-carregamento de modelos deve registrar contadores."""
        mock_telemetry = MagicMock()
        factories_module.configure_telemetry(telemetry_instance=mock_telemetry)

        with patch("src.infrastructure.factories.SpacyAnalyzer") as mock_sa:
            mock_instance = MagicMock()
            mock_sa.return_value = mock_instance

            factories_module.create_spacy_analyzer(preload=["ru", "en"], simulate=False)

        mock_telemetry.increment.assert_any_call("factory.spacy.preload.ru")
        mock_telemetry.increment.assert_any_call("factory.spacy.preload.en")

    def test_telemetria_wordcloud(self):
        """Wordcloud deve registrar contador."""
        mock_telemetry = MagicMock()
        factories_module.configure_telemetry(telemetry_instance=mock_telemetry)

        with patch("src.infrastructure.analysis.wordcloud_generator.WordCloudGenerator"):
            factories_module.create_wordcloud_generator()

        mock_telemetry.increment.assert_any_call("factory.wordcloud")

    def test_telemetria_pdf_exporter(self):
        """PDF exporter deve registrar contador."""
        mock_telemetry = MagicMock()
        factories_module.configure_telemetry(telemetry_instance=mock_telemetry)

        factories_module.create_pdf_exporter()

        mock_telemetry.increment.assert_any_call("factory.pdf_exporter")

    def test_sem_telemetria_nao_quebra(self):
        """Sem telemetria, o código deve funcionar normalmente."""
        translator = factories_module.create_translator(simulate=True)
        assert isinstance(translator, factories_module.MockTranslator)
