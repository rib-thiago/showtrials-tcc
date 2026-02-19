# src/tests/test_traducao_dto_telemetry.py
"""
Testes de telemetria para o DTO de tradução.
"""

from datetime import datetime
from unittest.mock import MagicMock

import pytest

import src.application.dtos.traducao_dto as dto_module


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


class TestTraducaoDTOTelemetry:
    """Testes específicos para telemetria do TraducaoDTO."""

    def setup_method(self):
        """Reconfigura o módulo antes de cada teste."""
        dto_module._telemetry = None

    def test_telemetria_criacao(self):
        """Verifica se a criação do DTO registra telemetria."""
        mock_telemetry = MagicMock()
        dto_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.application.dtos.traducao_dto import TraducaoDTO

        dto = TraducaoDTO(
            id=1,
            documento_id=42,
            idioma="en",
            idioma_nome="Inglês",
            idioma_icone="🇺🇸",
            texto_traduzido="Hello",
            data_traducao="2024-01-01",
            modelo="nmt",
            custo=0.15,
        )

        mock_telemetry.increment.assert_any_call("traducao_dto.criado")

    def test_telemetria_custo_negativo(self):
        """Custo negativo deve registrar erro."""
        mock_telemetry = MagicMock()
        dto_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.application.dtos.traducao_dto import TraducaoDTO

        with pytest.raises(ValueError):
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

        mock_telemetry.increment.assert_any_call("traducao_dto.custo_negativo")

    def test_telemetria_texto_vazio(self):
        """Texto vazio deve registrar erro."""
        mock_telemetry = MagicMock()
        dto_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.application.dtos.traducao_dto import TraducaoDTO

        with pytest.raises(ValueError):
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

        mock_telemetry.increment.assert_any_call("traducao_dto.texto_vazio")

    def test_telemetria_from_domain(self):
        """from_domain deve registrar contador."""
        mock_telemetry = MagicMock()
        dto_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.application.dtos.traducao_dto import TraducaoDTO

        mock = MockTraducao()

        dto = TraducaoDTO.from_domain(mock)

        mock_telemetry.increment.assert_any_call("traducao_dto.from_domain")

    def test_telemetria_to_dict(self):
        """to_dict deve registrar contador."""
        mock_telemetry = MagicMock()
        dto_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.application.dtos.traducao_dto import TraducaoDTO

        dto = TraducaoDTO(
            id=1,
            documento_id=42,
            idioma="en",
            idioma_nome="Inglês",
            idioma_icone="🇺🇸",
            texto_traduzido="Hello",
            data_traducao="2024-01-01",
            modelo="nmt",
            custo=0.15,
        )

        d = dto.to_dict()

        mock_telemetry.increment.assert_any_call("traducao_dto.to_dict")

    def test_sem_telemetria_nao_quebra(self):
        """Sem telemetria, o código deve funcionar normalmente."""
        from src.application.dtos.traducao_dto import TraducaoDTO

        dto = TraducaoDTO(
            id=1,
            documento_id=42,
            idioma="en",
            idioma_nome="Inglês",
            idioma_icone="🇺🇸",
            texto_traduzido="Hello",
            data_traducao="2024-01-01",
            modelo="nmt",
            custo=0.15,
        )
        assert dto.idioma == "en"
