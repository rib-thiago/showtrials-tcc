# src/tests/test_nome_russo_telemetry.py
"""
Testes de telemetria para o NomeRusso.
"""

from typing import Any, Callable
from unittest.mock import MagicMock

import pytest

import src.domain.value_objects.nome_russo as nr_module


def _noop_monitor(_: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Monitor no-op: retorna um decorator que não altera a função."""

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        return func

    return decorator


class TestNomeRussoTelemetry:
    """Testes específicos para telemetria do NomeRusso."""

    def setup_method(self):
        """Reconfigura o módulo antes de cada teste."""
        nr_module._telemetry = None
        nr_module._monitor = _noop_monitor

    def test_telemetria_criacao(self):
        """Verifica se a criação de nome registra telemetria."""
        mock_telemetry = MagicMock()
        nr_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.domain.value_objects.nome_russo import NomeRusso

        nome = NomeRusso("Л.В. Николаева")

        assert nome.original == "Л.В. Николаева"
        mock_telemetry.increment.assert_any_call("nome_russo.criado")

    def test_telemetria_formato_invalido(self):
        """Formato inválido deve registrar erro."""
        mock_telemetry = MagicMock()
        nr_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.domain.value_objects.nome_russo import NomeRusso

        with pytest.raises(ValueError):
            NomeRusso("invalido")

        mock_telemetry.increment.assert_called_with("nome_russo.formato_invalido")

    def test_telemetria_transliteracao_excecao(self):
        """Transliteração com exceção deve registrar contador."""
        mock_telemetry = MagicMock()
        nr_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.domain.value_objects.nome_russo import NomeRusso

        nome = NomeRusso("И.В. Сталину")
        resultado = nome.transliterar()

        assert resultado == "Joseph V. Stalin"
        mock_telemetry.increment.assert_any_call("nome_russo.transliterado.excecao")

    def test_telemetria_transliteracao_regra(self):
        """Transliteração por regra deve registrar contador."""
        mock_telemetry = MagicMock()
        nr_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.domain.value_objects.nome_russo import NomeRusso

        # Usar um nome que NÃO é exceção
        nome = NomeRusso("В.Г. Петров")
        resultado = nome.transliterar()

        assert resultado == "В.Г. Petrov"
        mock_telemetry.increment.assert_any_call("nome_russo.transliterado.regra")

    def test_sem_telemetria_nao_quebra(self):
        """Sem telemetria, o código deve funcionar normalmente."""
        from src.domain.value_objects.nome_russo import NomeRusso

        nome = NomeRusso("Л.В. Николаева")
        # "Л.В. Николаева" é exceção
        assert nome.transliterar() == "Leonid V. Nikolaev"
