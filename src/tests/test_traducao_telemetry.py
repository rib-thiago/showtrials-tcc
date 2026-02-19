# src/tests/test_traducao_telemetry.py
"""
Testes de telemetria para a entidade Traducao.
"""

from datetime import datetime
from unittest.mock import MagicMock

import pytest

import src.domain.entities.traducao as trad_module


class TestTraducaoTelemetry:
    """Testes específicos para telemetria do Traducao."""

    def setup_method(self):
        """Reconfigura o módulo antes de cada teste."""
        trad_module._telemetry = None
        trad_module._monitor = lambda x: (lambda f: f)

    def test_telemetria_criacao(self):
        """Verifica se a criação registra telemetria."""
        mock_telemetry = MagicMock()
        trad_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.domain.entities.traducao import Traducao

        traducao = Traducao(
            documento_id=1,
            idioma="en",
            texto_traduzido="Hello",
            data_traducao=datetime.now(),
        )

        mock_telemetry.increment.assert_any_call("traducao.criada")

    def test_telemetria_idioma_invalido(self):
        """Idioma inválido deve registrar erro."""
        mock_telemetry = MagicMock()
        trad_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.domain.entities.traducao import Traducao

        with pytest.raises(ValueError):
            Traducao(
                documento_id=1,
                idioma="de",
                texto_traduzido="Hallo",
                data_traducao=datetime.now(),
            )

        mock_telemetry.increment.assert_any_call("traducao.idioma_invalido")

    def test_telemetria_texto_vazio(self):
        """Texto vazio deve registrar erro."""
        mock_telemetry = MagicMock()
        trad_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.domain.entities.traducao import Traducao

        with pytest.raises(ValueError):
            Traducao(
                documento_id=1,
                idioma="en",
                texto_traduzido="",
                data_traducao=datetime.now(),
            )

        mock_telemetry.increment.assert_any_call("traducao.texto_vazio")

    def test_telemetria_idioma_desconhecido(self):
        """Idioma desconhecido no nome deve registrar."""
        mock_telemetry = MagicMock()
        trad_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.domain.entities.traducao import Traducao

        traducao = Traducao(
            documento_id=1,
            idioma="en",
            texto_traduzido="Hello",
            data_traducao=datetime.now(),
        )
        # Forçar idioma inválido
        traducao.idioma = "xx"
        nome = traducao.idioma_nome
        assert nome == "XX"
        mock_telemetry.increment.assert_any_call("traducao.idioma_desconhecido")

    def test_sem_telemetria_nao_quebra(self):
        """Sem telemetria, o código deve funcionar normalmente."""
        from src.domain.entities.traducao import Traducao

        traducao = Traducao(
            documento_id=1,
            idioma="en",
            texto_traduzido="Hello",
            data_traducao=datetime.now(),
        )
        assert traducao.idioma_nome == "Inglês"
