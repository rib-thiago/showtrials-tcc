# src/tests/test_traduzir_documento_telemetry.py
"""
Testes de telemetria para o caso de uso TraduzirDocumento.
"""

from datetime import datetime
from unittest.mock import MagicMock, Mock

import pytest

import src.application.use_cases.traduzir_documento as uc_module


class MockTranslator:
    """Mock do tradutor para testes."""

    def traduzir_documento_completo(self, texto: str, destino: str = "en") -> str:
        return f"Tradução de: {texto[:20]}..."


class TestTraduzirDocumentoTelemetry:
    """Testes de telemetria para o caso de uso."""

    def setup_method(self):
        """Reconfigura o módulo antes de cada teste."""
        uc_module._telemetry = None

    def test_telemetria_execucao_sucesso(self):
        """Execução bem-sucedida deve registrar contadores."""
        mock_telemetry = MagicMock()
        uc_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.application.use_cases.traduzir_documento import TraduzirDocumento
        from src.domain.entities.documento import Documento
        from src.infrastructure.registry import ServiceRegistry

        # Mocks
        mock_repo_doc = Mock()
        mock_repo_trad = Mock()
        mock_registry = Mock(spec=ServiceRegistry)

        doc = Documento(
            id=1,
            centro="lencenter",
            titulo="Teste",
            url="url",
            texto="Texto de teste para tradução",
            data_coleta=datetime.now(),
        )
        mock_repo_doc.buscar_por_id.return_value = doc
        mock_repo_trad.buscar_por_documento.return_value = None
        mock_repo_trad.salvar.return_value = 42
        mock_registry.get.return_value = MockTranslator()

        caso_uso = TraduzirDocumento(
            repo_doc=mock_repo_doc,
            repo_trad=mock_repo_trad,
            registry=mock_registry,
        )

        resultado = caso_uso.executar(documento_id=1, idioma_destino="pt")

        # Verificações
        mock_telemetry.increment.assert_any_call("traduzir_documento.executar.iniciado")
        mock_telemetry.increment.assert_any_call("traduzir_documento.idioma.pt")
        mock_telemetry.increment.assert_any_call("traduzir_documento.traducao_sucesso")
        mock_telemetry.increment.assert_any_call(
            "traduzir_documento.caracteres", value=len(doc.texto)
        )
        mock_telemetry.increment.assert_any_call("traduzir_documento.traducao_salva")

    def test_telemetria_documento_nao_encontrado(self):
        """Documento não encontrado deve registrar erro."""
        mock_telemetry = MagicMock()
        uc_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.application.use_cases.traduzir_documento import TraduzirDocumento
        from src.infrastructure.registry import ServiceRegistry

        mock_repo_doc = Mock()
        mock_repo_doc.buscar_por_id.return_value = None

        caso_uso = TraduzirDocumento(
            repo_doc=mock_repo_doc,
            repo_trad=Mock(),
            registry=Mock(spec=ServiceRegistry),
        )

        with pytest.raises(ValueError):
            caso_uso.executar(documento_id=999)

        mock_telemetry.increment.assert_any_call("traduzir_documento.erro.documento_nao_encontrado")

    def test_telemetria_traducao_existente(self):
        """Tradução existente deve registrar contador específico."""
        mock_telemetry = MagicMock()
        uc_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.application.use_cases.traduzir_documento import TraduzirDocumento
        from src.domain.entities.documento import Documento
        from src.domain.entities.traducao import Traducao
        from src.infrastructure.registry import ServiceRegistry

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

        traducao_existente = Traducao(
            id=42,
            documento_id=1,
            idioma="en",
            texto_traduzido="Existing",
            data_traducao=datetime.now(),
        )
        mock_repo_trad.buscar_por_documento.return_value = traducao_existente

        caso_uso = TraduzirDocumento(
            repo_doc=mock_repo_doc,
            repo_trad=mock_repo_trad,
            registry=Mock(spec=ServiceRegistry),
        )

        resultado = caso_uso.executar(documento_id=1, idioma_destino="en")

        mock_telemetry.increment.assert_any_call("traduzir_documento.traducao_existente")

    def test_telemetria_erro_traducao(self):
        """Erro na tradução deve registrar contador de erro."""
        mock_telemetry = MagicMock()
        uc_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.application.use_cases.traduzir_documento import TraduzirDocumento
        from src.domain.entities.documento import Documento
        from src.infrastructure.registry import ServiceRegistry

        mock_repo_doc = Mock()
        mock_repo_trad = Mock()
        mock_registry = Mock(spec=ServiceRegistry)

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

        # Tradutor que falha
        class TradutorQueFalha:
            def traduzir_documento_completo(self, texto, destino):
                raise Exception("Falha simulada")

        mock_registry.get.return_value = TradutorQueFalha()

        caso_uso = TraduzirDocumento(
            repo_doc=mock_repo_doc,
            repo_trad=mock_repo_trad,
            registry=mock_registry,
        )

        with pytest.raises(RuntimeError):
            caso_uso.executar(documento_id=1)

        mock_telemetry.increment.assert_any_call("traduzir_documento.erro.traducao")

    def test_sem_telemetria_nao_quebra(self):
        """Sem telemetria, o código deve funcionar normalmente."""
        from src.application.use_cases.traduzir_documento import TraduzirDocumento
        from src.domain.entities.documento import Documento
        from src.infrastructure.registry import ServiceRegistry

        mock_repo_doc = Mock()
        mock_repo_trad = Mock()
        mock_registry = Mock(spec=ServiceRegistry)

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
        mock_repo_trad.salvar.return_value = 42
        mock_registry.get.return_value = MockTranslator()

        caso_uso = TraduzirDocumento(
            repo_doc=mock_repo_doc,
            repo_trad=mock_repo_trad,
            registry=mock_registry,
        )

        resultado = caso_uso.executar(documento_id=1)
        assert resultado is not None
