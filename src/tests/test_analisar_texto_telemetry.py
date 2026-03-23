# src/tests/test_analisar_texto_telemetry.py
"""
Testes de telemetria para o caso de uso AnalisarDocumento.
"""

from datetime import datetime
from unittest.mock import MagicMock, Mock, patch

import pytest

import src.application.use_cases.analisar_texto as uc_module


class TestAnalisarDocumentoTelemetry:
    """Testes de telemetria para o caso de uso."""

    def setup_method(self):
        """Reconfigura o módulo antes de cada teste."""
        uc_module._telemetry = None

    def test_telemetria_execucao_sucesso(self):
        """Execução bem-sucedida deve registrar telemetria."""
        mock_telemetry = MagicMock()
        uc_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.application.use_cases.analisar_texto import AnalisarDocumento
        from src.domain.entities.documento import Documento

        mock_repo_doc = Mock()
        mock_registry = Mock()

        doc = Documento(
            id=1,
            centro="lencenter",
            titulo="Teste",
            url="url",
            texto="Texto de teste para análise",
            data_coleta=datetime.now(),
        )
        mock_repo_doc.buscar_por_id.return_value = doc

        class MockAnalyzer:
            def analisar(self, texto, documento_id, idioma):
                return Mock()

        mock_registry.get.return_value = MockAnalyzer()

        caso_uso = AnalisarDocumento(
            repo_doc=mock_repo_doc,
            registry=mock_registry,
        )

        resultado = caso_uso.executar(documento_id=1)

        mock_telemetry.increment.assert_any_call("analisar_documento.executar.iniciado")
        mock_telemetry.increment.assert_any_call("analisar_documento.idioma.ru")
        mock_telemetry.increment.assert_any_call("analisar_documento.analise.sucesso")
        mock_telemetry.increment.assert_any_call(
            "analisar_documento.caracteres", value=len(doc.texto)
        )
        mock_telemetry.increment.assert_any_call("analisar_documento.executar.concluido")

    def test_telemetria_documento_nao_encontrado(self):
        """Documento não encontrado deve registrar erro."""
        mock_telemetry = MagicMock()
        uc_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.application.use_cases.analisar_texto import AnalisarDocumento

        mock_repo_doc = Mock()
        mock_repo_doc.buscar_por_id.return_value = None

        caso_uso = AnalisarDocumento(
            repo_doc=mock_repo_doc,
            registry=Mock(),
        )

        resultado = caso_uso.executar(documento_id=999)

        mock_telemetry.increment.assert_any_call("analisar_documento.erro.documento_nao_encontrado")

    def test_telemetria_traducao_nao_encontrada(self):
        """Tradução não encontrada deve registrar erro."""
        mock_telemetry = MagicMock()
        uc_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.application.use_cases.analisar_texto import AnalisarDocumento
        from src.domain.entities.documento import Documento

        mock_repo_doc = Mock()
        mock_repo_trad = Mock()

        doc = Documento(
            id=1,
            centro="lencenter",
            titulo="Teste",
            url="url",
            texto="Texto",
            data_coleta=datetime.now(),
        )
        mock_repo_doc.buscar_por_id.return_value = doc
        mock_repo_trad.buscar_por_documento.return_value = None

        caso_uso = AnalisarDocumento(
            repo_doc=mock_repo_doc,
            repo_trad=mock_repo_trad,
            registry=Mock(),
        )

        resultado = caso_uso.executar(documento_id=1, idioma="en")

        mock_telemetry.increment.assert_any_call("analisar_documento.erro.traducao_nao_encontrada")

    def test_telemetria_wordcloud(self):
        """Geração de wordcloud deve registrar telemetria."""
        mock_telemetry = MagicMock()
        uc_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.application.use_cases.analisar_texto import AnalisarDocumento
        from src.domain.entities.documento import Documento

        mock_repo_doc = Mock()
        mock_registry = Mock()

        doc = Documento(
            id=1,
            centro="lencenter",
            titulo="Teste",
            url="url",
            texto="Texto para wordcloud",
            data_coleta=datetime.now(),
        )
        mock_repo_doc.buscar_por_id.return_value = doc

        class MockAnalyzer:
            def analisar(self, texto, documento_id, idioma):
                return Mock()

        class MockWordCloud:
            def gerar(self, texto, titulo, idioma, salvar_em):
                pass

        def registry_get(name):
            if name == "spacy":
                return MockAnalyzer()
            return MockWordCloud()

        mock_registry.get.side_effect = registry_get

        caso_uso = AnalisarDocumento(
            repo_doc=mock_repo_doc,
            registry=mock_registry,
        )

        with patch("pathlib.Path.mkdir"):
            resultado = caso_uso.executar(documento_id=1, gerar_wordcloud=True)

        mock_telemetry.increment.assert_any_call("analisar_documento.wordcloud.sucesso")

    def test_telemetria_erro_analise(self):
        """Erro na análise deve registrar erro."""
        mock_telemetry = MagicMock()
        uc_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.application.use_cases.analisar_texto import AnalisarDocumento
        from src.domain.entities.documento import Documento

        mock_repo_doc = Mock()
        mock_registry = Mock()

        doc = Documento(
            id=1,
            centro="lencenter",
            titulo="Teste",
            url="url",
            texto="Texto",
            data_coleta=datetime.now(),
        )
        mock_repo_doc.buscar_por_id.return_value = doc

        class AnalyzerQueFalha:
            def analisar(self, texto, documento_id, idioma):
                raise Exception("Falha na análise")

        mock_registry.get.return_value = AnalyzerQueFalha()

        caso_uso = AnalisarDocumento(
            repo_doc=mock_repo_doc,
            registry=mock_registry,
        )

        with pytest.raises(Exception):
            caso_uso.executar(documento_id=1)

        mock_telemetry.increment.assert_any_call("analisar_documento.analise.erro")

    def test_sem_telemetria_nao_quebra(self):
        """Sem telemetria, o código deve funcionar normalmente."""
        from src.application.use_cases.analisar_texto import AnalisarDocumento
        from src.domain.entities.documento import Documento

        mock_repo_doc = Mock()

        doc = Documento(
            id=1,
            centro="lencenter",
            titulo="Teste",
            url="url",
            texto="Texto",
            data_coleta=datetime.now(),
        )
        mock_repo_doc.buscar_por_id.return_value = doc

        class MockAnalyzer:
            def analisar(self, texto, documento_id, idioma):
                return Mock()

        mock_registry = Mock()
        mock_registry.get.return_value = MockAnalyzer()

        caso_uso = AnalisarDocumento(
            repo_doc=mock_repo_doc,
            registry=mock_registry,
        )

        resultado = caso_uso.executar(documento_id=1)
        assert resultado is not None
