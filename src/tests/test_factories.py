# src/tests/test_factories.py
"""
Testes de lógica para as factories.
"""

from unittest.mock import MagicMock, patch

import src.infrastructure.factories as factories_module


class TestFactories:
    """Testes para as factories."""

    def test_create_translator_real(self):
        """Deve criar tradutor real quando simulate=False."""
        with patch("src.infrastructure.factories.GoogleTranslator") as mock_gt:
            translator = factories_module.create_translator(api_key="test_key", simulate=False)

            mock_gt.assert_called_once_with(api_key="test_key")
            assert not isinstance(translator, factories_module.MockTranslator)

    def test_create_translator_mock(self):
        """Deve criar tradutor mock quando simulate=True."""
        translator = factories_module.create_translator(simulate=True)

        assert isinstance(translator, factories_module.MockTranslator)
        assert translator.traduzir("teste") == "[EN MOCK] teste"

    def test_create_translator_fallback(self):
        """Deve cair no mock quando a criação real falha."""
        with patch("src.infrastructure.factories.GoogleTranslator", side_effect=Exception("Erro")):
            translator = factories_module.create_translator(api_key="test_key", simulate=False)

            assert isinstance(translator, factories_module.MockTranslator)

    def test_create_spacy_analyzer_real(self):
        """Deve criar analisador real quando simulate=False."""
        with patch("src.infrastructure.factories.SpacyAnalyzer") as mock_sa:
            analyzer = factories_module.create_spacy_analyzer(simulate=False)

            mock_sa.assert_called_once()
            assert not isinstance(analyzer, factories_module.MockSpacyAnalyzer)

    def test_create_spacy_analyzer_mock(self):
        """Deve criar analisador mock quando simulate=True."""
        analyzer = factories_module.create_spacy_analyzer(simulate=True)

        assert isinstance(analyzer, factories_module.MockSpacyAnalyzer)
        assert analyzer.analisar("texto", 1).documento_id == 1

    def test_create_spacy_analyzer_com_preload(self):
        """Deve tentar pré-carregar modelos quando especificado."""
        with patch("src.infrastructure.factories.SpacyAnalyzer") as mock_sa:
            mock_instance = MagicMock()
            mock_sa.return_value = mock_instance

            factories_module.create_spacy_analyzer(preload=["ru", "en"], simulate=False)

            assert mock_instance._get_model.call_count == 2
            mock_instance._get_model.assert_any_call("ru")
            mock_instance._get_model.assert_any_call("en")

    def test_create_wordcloud_generator(self):
        """Deve criar gerador de wordcloud."""
        # Importar diretamente para o patch
        with patch("src.infrastructure.analysis.wordcloud_generator.WordCloudGenerator") as mock_wc:
            generator = factories_module.create_wordcloud_generator(teste="valor")

            mock_wc.assert_called_once_with(teste="valor")

    def test_create_pdf_exporter(self):
        """Deve criar exportador PDF mock."""
        exporter = factories_module.create_pdf_exporter()

        assert exporter.exportar() == "/tmp/mock.pdf"

    def test_service_factories_mapeamento(self):
        """O dicionário SERVICE_FACTORIES deve conter todas as factories."""
        assert "translator" in factories_module.SERVICE_FACTORIES
        assert "spacy" in factories_module.SERVICE_FACTORIES
        assert "wordcloud" in factories_module.SERVICE_FACTORIES
        assert "pdf_exporter" in factories_module.SERVICE_FACTORIES

        assert callable(factories_module.SERVICE_FACTORIES["translator"])
        assert callable(factories_module.SERVICE_FACTORIES["spacy"])
        assert callable(factories_module.SERVICE_FACTORIES["wordcloud"])
        assert callable(factories_module.SERVICE_FACTORIES["pdf_exporter"])
