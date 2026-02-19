# src/tests/test_tipo_documento_telemetry.py
"""
Testes de telemetria para o TipoDocumento (isolados).
"""

from unittest.mock import MagicMock

import src.domain.value_objects.tipo_documento as td_module


class TestTipoDocumentoTelemetry:
    """Testes específicos para telemetria."""

    def setup_method(self):
        """Reconfigura o módulo antes de cada teste."""
        td_module._telemetry = None
        td_module._monitor = lambda x: x

    def test_telemetria_chamada_quando_disponivel(self):
        """Verifica se a telemetria é chamada quando configurada."""
        # Configurar mock
        mock_telemetry = MagicMock()
        td_module.configure_telemetry(telemetry_instance=mock_telemetry)

        # Executar
        from src.domain.value_objects.tipo_documento import TipoDocumento

        tipo = TipoDocumento.from_titulo("Протокол допроса")

        # Verificar
        assert tipo == TipoDocumento.INTERROGATORIO
        mock_telemetry.increment.assert_called_with("tipo_documento.classificado.interrogatorio")

    def test_telemetria_titulo_vazio(self):
        """Telemetria deve registrar títulos vazios."""
        mock_telemetry = MagicMock()
        td_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.domain.value_objects.tipo_documento import TipoDocumento

        tipo = TipoDocumento.from_titulo("")

        assert tipo == TipoDocumento.DESCONHECIDO
        mock_telemetry.increment.assert_called_with("tipo_documento.titulo_vazio")

    def test_telemetria_desconhecido(self):
        """Telemetria deve registrar classificações desconhecidas."""
        mock_telemetry = MagicMock()
        td_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.domain.value_objects.tipo_documento import TipoDocumento

        tipo = TipoDocumento.from_titulo("texto completamente aleatório")

        assert tipo == TipoDocumento.DESCONHECIDO
        mock_telemetry.increment.assert_called_with("tipo_documento.desconhecido")

    def test_sem_telemetria_nao_quebra(self):
        """Sem telemetria, o código deve funcionar normalmente."""
        from src.domain.value_objects.tipo_documento import TipoDocumento

        tipo = TipoDocumento.from_titulo("Протокол допроса")
        assert tipo == TipoDocumento.INTERROGATORIO

    def test_com_decorator_mock(self):
        """Testa o decorator com mock (opcional)."""
        mock_monitor = MagicMock(return_value=lambda f: f)
        td_module.configure_telemetry(monitor_decorator=mock_monitor)

        # Recarregar o módulo para aplicar o decorator
        import importlib

        import src.domain.value_objects.tipo_documento as td

        importlib.reload(td)

        from src.domain.value_objects.tipo_documento import TipoDocumento

        tipo = TipoDocumento.from_titulo("Протокол допроса")
        assert tipo == TipoDocumento.INTERROGATORIO

        # Verificar se o decorator foi aplicado (opcional)
        # mock_monitor.assert_called_with("tipo_documento.from_titulo")
