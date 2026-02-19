# src/tests/test_traducao_dto.py
"""
Testes para o DTO de tradução (sem telemetria).
"""

from datetime import datetime

import pytest

from src.application.dtos.traducao_dto import TraducaoDTO


class MockTraducao:
    """Mock da entidade Traducao para testes."""

    def __init__(self, **kwargs):
        self.id = kwargs.get("id", 1)
        self.documento_id = kwargs.get("documento_id", 42)
        self.idioma = kwargs.get("idioma", "en")
        self.idioma_nome = kwargs.get("idioma_nome", "Inglês")
        self.idioma_icone = kwargs.get("idioma_icone", "🇺🇸")
        self.texto_traduzido = kwargs.get("texto_traduzido", "Hello world")
        self.data_traducao = kwargs.get("data_traducao", datetime(2024, 1, 1, 12, 0))
        self.modelo = kwargs.get("modelo", "nmt")
        self.custo = kwargs.get("custo", 0.15)


class TestTraducaoDTO:
    """Testes para a classe TraducaoDTO."""

    def test_criar_dto_valido(self):
        """Deve criar um DTO válido."""
        dto = TraducaoDTO(
            id=1,
            documento_id=42,
            idioma="en",
            idioma_nome="Inglês",
            idioma_icone="🇺🇸",
            texto_traduzido="Hello world",
            data_traducao="2024-01-01",
            modelo="nmt",
            custo=0.15,
        )

        assert dto.id == 1
        assert dto.documento_id == 42
        assert dto.idioma == "en"
        assert dto.idioma_nome == "Inglês"
        assert dto.idioma_icone == "🇺🇸"
        assert dto.texto_traduzido == "Hello world"
        assert dto.data_traducao == "2024-01-01"
        assert dto.modelo == "nmt"
        assert dto.custo == 0.15

    def test_custo_negativo(self):
        """Custo negativo deve levantar erro."""
        with pytest.raises(ValueError, match="Custo não pode ser negativo"):
            TraducaoDTO(
                id=1,
                documento_id=42,
                idioma="en",
                idioma_nome="Inglês",
                idioma_icone="🇺🇸",
                texto_traduzido="Hello",
                data_traducao="2024-01-01",
                modelo="nmt",
                custo=-0.1,
            )

    def test_texto_vazio(self):
        """Texto vazio deve levantar erro."""
        with pytest.raises(ValueError, match="Texto traduzido não pode ser vazio"):
            TraducaoDTO(
                id=1,
                documento_id=42,
                idioma="en",
                idioma_nome="Inglês",
                idioma_icone="🇺🇸",
                texto_traduzido="",
                data_traducao="2024-01-01",
                modelo="nmt",
                custo=0.15,
            )

    def test_from_domain(self):
        """Deve criar DTO a partir de entidade do domínio."""
        mock = MockTraducao()

        dto = TraducaoDTO.from_domain(mock)

        assert dto.id == 1
        assert dto.documento_id == 42
        assert dto.idioma == "en"
        assert dto.idioma_nome == "Inglês"
        assert dto.idioma_icone == "🇺🇸"
        assert dto.texto_traduzido == "Hello world"
        assert dto.data_traducao == "2024-01-01"
        assert dto.modelo == "nmt"
        assert dto.custo == 0.15

    def test_from_domain_sem_modelo(self):
        """Deve criar DTO mesmo sem modelo."""
        mock = MockTraducao(modelo=None)

        dto = TraducaoDTO.from_domain(mock)

        assert dto.id == 1
        assert dto.modelo is None

    def test_from_domain_sem_id(self):
        """Deve criar DTO mesmo sem ID."""
        mock = MockTraducao(id=None)

        dto = TraducaoDTO.from_domain(mock)

        assert dto.id is None

    def test_to_dict(self):
        """Deve converter para dicionário corretamente."""
        dto = TraducaoDTO(
            id=1,
            documento_id=42,
            idioma="en",
            idioma_nome="Inglês",
            idioma_icone="🇺🇸",
            texto_traduzido="Hello world",
            data_traducao="2024-01-01",
            modelo="nmt",
            custo=0.15,
        )

        d = dto.to_dict()

        assert d["id"] == 1
        assert d["documento_id"] == 42
        assert d["idioma"] == "en"
        assert d["idioma_nome"] == "Inglês"
        assert d["idioma_icone"] == "🇺🇸"
        assert d["texto_traduzido"] == "Hello world"
        assert d["data_traducao"] == "2024-01-01"
        assert d["modelo"] == "nmt"
        assert d["custo"] == 0.15
