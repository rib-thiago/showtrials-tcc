# src/tests/test_traduzir_documento.py
"""
Testes de lógica para o caso de uso TraduzirDocumento.
"""

from datetime import datetime
from unittest.mock import Mock

import pytest

from src.application.use_cases.traduzir_documento import TraduzirDocumento
from src.domain.entities.documento import Documento
from src.domain.entities.traducao import Traducao
from src.infrastructure.registry import ServiceRegistry


class MockTranslator:
    """Mock do tradutor para testes."""

    def traduzir_documento_completo(self, texto: str, destino: str = "en") -> str:
        return f"Tradução de: {texto[:20]}..."


class TestTraduzirDocumento:
    """Testes para o caso de uso TraduzirDocumento."""

    @pytest.fixture
    def setup_mocks(self):
        """Fixture com mocks configurados."""
        mock_repo_doc = Mock()
        mock_repo_trad = Mock()
        mock_registry = Mock(spec=ServiceRegistry)
        mock_translator = MockTranslator()

        mock_registry.get.return_value = mock_translator

        return {
            "repo_doc": mock_repo_doc,
            "repo_trad": mock_repo_trad,
            "registry": mock_registry,
            "translator": mock_translator,
        }

    def test_executar_com_sucesso(self, setup_mocks):
        """Deve traduzir documento com sucesso."""
        # Configurar mocks
        doc = Documento(
            id=1,
            centro="lencenter",
            titulo="Documento Teste",
            url="http://teste.com",
            texto="Texto original para tradução",
            data_coleta=datetime.now(),
        )
        setup_mocks["repo_doc"].buscar_por_id.return_value = doc
        setup_mocks["repo_trad"].buscar_por_documento.return_value = None
        setup_mocks["repo_trad"].salvar.return_value = 42

        # Executar caso de uso
        caso_uso = TraduzirDocumento(
            repo_doc=setup_mocks["repo_doc"],
            repo_trad=setup_mocks["repo_trad"],
            registry=setup_mocks["registry"],
        )

        resultado = caso_uso.executar(documento_id=1, idioma_destino="en")

        # Verificações
        assert resultado is not None
        assert resultado.id == 42
        assert resultado.documento_id == 1
        assert resultado.idioma == "en"

        setup_mocks["repo_doc"].buscar_por_id.assert_called_once_with(1)
        setup_mocks["repo_trad"].buscar_por_documento.assert_called_once_with(1, "en")
        setup_mocks["repo_trad"].salvar.assert_called_once()
        setup_mocks["registry"].get.assert_called_once_with("translator")

    def test_documento_nao_encontrado(self, setup_mocks):
        """Deve levantar erro se documento não existir."""
        setup_mocks["repo_doc"].buscar_por_id.return_value = None

        caso_uso = TraduzirDocumento(
            repo_doc=setup_mocks["repo_doc"],
            repo_trad=setup_mocks["repo_trad"],
            registry=setup_mocks["registry"],
        )

        with pytest.raises(ValueError, match="Documento 999 não encontrado"):
            caso_uso.executar(documento_id=999)

    def test_traducao_existente(self, setup_mocks):
        """Deve retornar tradução existente sem criar nova."""
        # Configurar mocks
        doc = Documento(
            id=1,
            centro="lencenter",
            titulo="Documento Teste",
            url="http://teste.com",
            texto="Texto",
            data_coleta=datetime.now(),
        )
        setup_mocks["repo_doc"].buscar_por_id.return_value = doc

        traducao_existente = Traducao(
            id=42,
            documento_id=1,
            idioma="en",
            texto_traduzido="Existing translation",
            data_traducao=datetime.now(),
        )
        setup_mocks["repo_trad"].buscar_por_documento.return_value = traducao_existente

        caso_uso = TraduzirDocumento(
            repo_doc=setup_mocks["repo_doc"],
            repo_trad=setup_mocks["repo_trad"],
            registry=setup_mocks["registry"],
        )

        resultado = caso_uso.executar(documento_id=1, idioma_destino="en")

        # Verificações
        assert resultado.id == 42
        setup_mocks["registry"].get.assert_not_called()  # Não deve chamar tradutor
        setup_mocks["repo_trad"].salvar.assert_not_called()  # Não deve salvar

    def test_forcar_novo_ignora_existente(self, setup_mocks):
        """Com forcar_novo=True, deve criar nova tradução mesmo se existir."""
        # Configurar mocks
        doc = Documento(
            id=1,
            centro="lencenter",
            titulo="Documento Teste",
            url="http://teste.com",
            texto="Texto original",
            data_coleta=datetime.now(),
        )
        setup_mocks["repo_doc"].buscar_por_id.return_value = doc

        # Existe tradução, mas vamos ignorar
        traducao_existente = Traducao(
            id=42,
            documento_id=1,
            idioma="en",
            texto_traduzido="Existing",
            data_traducao=datetime.now(),
        )
        setup_mocks["repo_trad"].buscar_por_documento.return_value = traducao_existente
        setup_mocks["repo_trad"].salvar.return_value = 43

        caso_uso = TraduzirDocumento(
            repo_doc=setup_mocks["repo_doc"],
            repo_trad=setup_mocks["repo_trad"],
            registry=setup_mocks["registry"],
        )

        resultado = caso_uso.executar(documento_id=1, idioma_destino="en", forcar_novo=True)

        # Verificações
        assert resultado.id == 43  # Novo ID
        setup_mocks["registry"].get.assert_called_once()  # Chamou tradutor
        setup_mocks["repo_trad"].salvar.assert_called_once()  # Salvou novo

    def test_erro_na_traducao(self, setup_mocks):
        """Erro no tradutor deve ser propagado."""
        # Configurar mocks
        doc = Documento(
            id=1,
            centro="lencenter",
            titulo="Documento Teste",
            url="http://teste.com",
            texto="Texto",
            data_coleta=datetime.now(),
        )
        setup_mocks["repo_doc"].buscar_por_id.return_value = doc

        # IMPORTANTE: Garantir que buscar_por_documento retorne None (não uma tradução existente)
        setup_mocks["repo_trad"].buscar_por_documento.return_value = None

        # Tradutor que falha
        class TradutorQueFalha:
            def traduzir_documento_completo(self, texto, destino):
                raise Exception("Falha na tradução")

        setup_mocks["registry"].get.return_value = TradutorQueFalha()

        caso_uso = TraduzirDocumento(
            repo_doc=setup_mocks["repo_doc"],
            repo_trad=setup_mocks["repo_trad"],
            registry=setup_mocks["registry"],
        )

        with pytest.raises(RuntimeError, match="Erro na tradução"):
            caso_uso.executar(documento_id=1)
