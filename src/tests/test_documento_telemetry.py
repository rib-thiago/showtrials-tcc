# src/tests/test_documento_telemetry.py
"""
Testes de telemetria para a entidade Documento.
"""

from datetime import datetime
from typing import Any, Callable
from unittest.mock import MagicMock

import pytest

import src.domain.entities.documento as doc_module


def _noop_monitor(_: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Monitor no-op: retorna um decorator que não altera a função."""

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        return func

    return decorator


class TestDocumentoTelemetry:
    """Testes específicos para telemetria do Documento."""

    def setup_method(self):
        """Reconfigura o módulo antes de cada teste."""
        doc_module._telemetry = None
        doc_module._monitor = _noop_monitor

    def test_telemetria_criacao(self):
        """Verifica se a criação registra telemetria."""
        mock_telemetry = MagicMock()
        doc_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.domain.entities.documento import Documento

        doc = Documento(
            centro="lencenter",
            titulo="Título",
            url="url",
            texto="texto",
            data_coleta=datetime.now(),
        )
        mock_telemetry.increment.assert_any_call("documento.criado")

    def test_telemetria_centro_invalido(self):
        """Centro inválido deve registrar erro."""
        mock_telemetry = MagicMock()
        doc_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.domain.entities.documento import Documento

        with pytest.raises(ValueError):
            Documento(
                centro="invalido",
                titulo="Título",
                url="url",
                texto="texto",
                data_coleta=datetime.now(),
            )
        mock_telemetry.increment.assert_any_call("documento.centro_invalido")

    def test_telemetria_titulo_vazio(self):
        """Título vazio deve registrar erro."""
        mock_telemetry = MagicMock()
        doc_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.domain.entities.documento import Documento

        with pytest.raises(ValueError):
            Documento(
                centro="lencenter",
                titulo="",
                url="url",
                texto="texto",
                data_coleta=datetime.now(),
            )
        mock_telemetry.increment.assert_any_call("documento.titulo_vazio")

    def test_telemetria_url_vazia(self):
        """URL vazia deve registrar erro."""
        mock_telemetry = MagicMock()
        doc_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.domain.entities.documento import Documento

        with pytest.raises(ValueError):
            Documento(
                centro="lencenter",
                titulo="Título",
                url="",
                texto="texto",
                data_coleta=datetime.now(),
            )
        mock_telemetry.increment.assert_any_call("documento.url_vazia")

    def test_telemetria_extrair_pessoas(self):
        """Extrair pessoas deve registrar contador."""
        mock_telemetry = MagicMock()
        doc_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.domain.entities.documento import Documento

        doc = Documento(
            centro="lencenter",
            titulo="Протокол допроса Л.В. Николаева и И.И. Иванова",
            url="url",
            texto="texto",
            data_coleta=datetime.now(),
        )
        pessoas = doc.extrair_pessoas_do_titulo()
        assert len(pessoas) == 2
        mock_telemetry.increment.assert_any_call("documento.pessoas_extraidas", value=2)

    def test_telemetria_from_dict(self):
        """from_dict deve registrar contador."""
        mock_telemetry = MagicMock()
        doc_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.domain.entities.documento import Documento

        data = {
            "centro": "lencenter",
            "titulo": "Título",
            "url": "url",
            "texto": "texto",
            "data_coleta": datetime.now().isoformat(),
        }
        doc = Documento.from_dict(data)
        mock_telemetry.increment.assert_any_call("documento.from_dict")

    def test_sem_telemetria_nao_quebra(self):
        """Sem telemetria, o código deve funcionar normalmente."""
        from src.domain.entities.documento import Documento

        doc = Documento(
            centro="lencenter",
            titulo="Título",
            url="url",
            texto="texto",
            data_coleta=datetime.now(),
        )
        assert doc.centro == "lencenter"
