# src/tests/test_analisar_texto.py
"""
Testes de lógica para o caso de uso AnalisarDocumento.
"""

from datetime import datetime
from pathlib import Path
from unittest.mock import Mock, patch

import pytest

from src.application.use_cases.analisar_texto import AnalisarDocumento
from src.domain.entities.documento import Documento
from src.domain.entities.traducao import Traducao
from src.domain.value_objects.analise_texto import AnaliseTexto, EstatisticasTexto, Sentimento
from src.infrastructure.registry import ServiceRegistry


class MockSpacyAnalyzer:
    """Mock do analisador spaCy."""

    def analisar(self, texto, documento_id, idioma):
        estatisticas = Mock(spec=EstatisticasTexto)
        estatisticas.total_palavras = len(texto.split())

        sentimento = Mock(spec=Sentimento)
        sentimento.classificacao = "neutro"

        analise = Mock(spec=AnaliseTexto)
        analise.documento_id = documento_id
        analise.idioma = idioma
        analise.estatisticas = estatisticas
        analise.sentimento = sentimento
        return analise


class MockWordCloudGenerator:
    """Mock do gerador de wordcloud."""

    def gerar(self, texto, titulo, idioma, salvar_em):
        return Path(salvar_em)


class TestAnalisarDocumento:
    """Testes para o caso de uso AnalisarDocumento."""

    @pytest.fixture
    def setup_mocks(self):
        """Fixture com mocks configurados."""
        mock_repo_doc = Mock()
        mock_repo_trad = Mock()
        mock_registry = Mock(spec=ServiceRegistry)

        mock_registry.get.side_effect = lambda name: {
            "spacy": MockSpacyAnalyzer(),
            "wordcloud": MockWordCloudGenerator(),
        }.get(name)

        return {"repo_doc": mock_repo_doc, "repo_trad": mock_repo_trad, "registry": mock_registry}

    def test_executar_com_documento_original(self, setup_mocks):
        """Deve analisar documento original com sucesso."""
        doc = Documento(
            id=1,
            centro="lencenter",
            titulo="Documento Teste",
            url="http://teste.com",
            texto="Texto para análise com várias palavras para teste",
            data_coleta=datetime.now(),
        )
        setup_mocks["repo_doc"].buscar_por_id.return_value = doc

        caso_uso = AnalisarDocumento(
            repo_doc=setup_mocks["repo_doc"],
            repo_trad=setup_mocks["repo_trad"],
            registry=setup_mocks["registry"],
        )

        resultado = caso_uso.executar(documento_id=1, idioma="ru")

        assert resultado is not None
        assert resultado.documento_id == 1
        assert resultado.idioma == "ru"
        setup_mocks["repo_doc"].buscar_por_id.assert_called_once_with(1)

    def test_executar_com_traducao(self, setup_mocks):
        """Deve analisar tradução com sucesso."""
        doc = Documento(
            id=1,
            centro="lencenter",
            titulo="Documento Teste",
            url="http://teste.com",
            texto="Texto original",
            data_coleta=datetime.now(),
        )
        setup_mocks["repo_doc"].buscar_por_id.return_value = doc

        traducao = Traducao(
            id=42,
            documento_id=1,
            idioma="en",
            texto_traduzido="Translated text",
            data_traducao=datetime.now(),
        )
        setup_mocks["repo_trad"].buscar_por_documento.return_value = traducao

        caso_uso = AnalisarDocumento(
            repo_doc=setup_mocks["repo_doc"],
            repo_trad=setup_mocks["repo_trad"],
            registry=setup_mocks["registry"],
        )

        resultado = caso_uso.executar(documento_id=1, idioma="en")

        assert resultado is not None
        assert resultado.idioma == "en"
        setup_mocks["repo_trad"].buscar_por_documento.assert_called_once_with(1, "en")

    def test_documento_nao_encontrado(self, setup_mocks):
        """Deve retornar None se documento não existir."""
        setup_mocks["repo_doc"].buscar_por_id.return_value = None

        caso_uso = AnalisarDocumento(
            repo_doc=setup_mocks["repo_doc"],
            repo_trad=setup_mocks["repo_trad"],
            registry=setup_mocks["registry"],
        )

        resultado = caso_uso.executar(documento_id=999)
        assert resultado is None

    def test_traducao_nao_encontrada(self, setup_mocks):
        """Deve retornar None se tradução não existir."""
        doc = Documento(
            id=1,
            centro="lencenter",
            titulo="Documento Teste",
            url="http://teste.com",
            texto="Texto original",
            data_coleta=datetime.now(),
        )
        setup_mocks["repo_doc"].buscar_por_id.return_value = doc
        setup_mocks["repo_trad"].buscar_por_documento.return_value = None

        caso_uso = AnalisarDocumento(
            repo_doc=setup_mocks["repo_doc"],
            repo_trad=setup_mocks["repo_trad"],
            registry=setup_mocks["registry"],
        )

        resultado = caso_uso.executar(documento_id=1, idioma="en")
        assert resultado is None

    def test_sem_repo_trad_para_traducao(self, setup_mocks):
        """Sem repositório de tradução, não deve permitir análise de tradução."""
        caso_uso = AnalisarDocumento(
            repo_doc=setup_mocks["repo_doc"],
            repo_trad=None,  # Sem repositório de tradução
            registry=setup_mocks["registry"],
        )

        resultado = caso_uso.executar(documento_id=1, idioma="en")
        assert resultado is None

    def test_com_wordcloud(self, setup_mocks, tmp_path):
        """Deve gerar wordcloud quando solicitado."""
        doc = Documento(
            id=1,
            centro="lencenter",
            titulo="Documento Teste",
            url="http://teste.com",
            texto="Texto para análise com wordcloud",
            data_coleta=datetime.now(),
        )
        setup_mocks["repo_doc"].buscar_por_id.return_value = doc

        caso_uso = AnalisarDocumento(
            repo_doc=setup_mocks["repo_doc"],
            repo_trad=setup_mocks["repo_trad"],
            registry=setup_mocks["registry"],
        )

        with patch("pathlib.Path.mkdir"):
            resultado = caso_uso.executar(documento_id=1, gerar_wordcloud=True)

        assert resultado is not None
        # Verificar se o wordcloud foi chamado (indiretamente)
        setup_mocks["registry"].get.assert_called_with("wordcloud")
