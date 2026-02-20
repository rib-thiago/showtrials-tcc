# src/tests/test_listar_documentos_telemetry.py
"""
Testes de telemetria para o caso de uso ListarDocumentos.
"""

from unittest.mock import MagicMock, Mock, patch

import src.application.use_cases.listar_documentos as uc_module
from src.application.use_cases.listar_documentos import ListarDocumentos


class TestListarDocumentosTelemetry:
    """Testes para telemetria do ListarDocumentos."""

    def setup_method(self):
        """Reconfigura o módulo antes de cada teste."""
        uc_module._telemetry = None

    def test_telemetria_executar(self):
        """Telemetria deve registrar execução de listagem."""
        mock_telemetry = MagicMock()
        uc_module.configure_telemetry(telemetry_instance=mock_telemetry)

        mock_repo = Mock()
        mock_repo.listar.return_value = []
        mock_repo.contar.return_value = 0

        use_case = ListarDocumentos(mock_repo)
        use_case.executar(pagina=2)

        mock_telemetry.increment.assert_any_call("listar_documentos.executar.iniciado")
        mock_telemetry.increment.assert_any_call("listar_documentos.pagina.2")
        mock_telemetry.increment.assert_any_call("listar_documentos.executar.concluido")
        mock_telemetry.increment.assert_any_call("listar_documentos.resultados", value=0)

    def test_telemetria_com_traducao_nomes(self):
        """Telemetria deve registrar chamada de com_traducao_nomes."""
        mock_telemetry = MagicMock()
        uc_module.configure_telemetry(telemetry_instance=mock_telemetry)

        use_case = ListarDocumentos(Mock())
        use_case.com_traducao_nomes(True)

        mock_telemetry.increment.assert_called_once_with("listar_documentos.com_traducao_nomes")

    def test_telemetria_listar_tipos(self):
        """Telemetria deve registrar listagem de tipos."""
        mock_telemetry = MagicMock()
        uc_module.configure_telemetry(telemetry_instance=mock_telemetry)

        mock_repo = Mock()
        mock_repo.listar.return_value = []

        use_case = ListarDocumentos(mock_repo)
        use_case.listar_tipos()

        mock_telemetry.increment.assert_any_call("listar_documentos.listar_tipos.iniciado")
        mock_telemetry.increment.assert_any_call("listar_documentos.listar_tipos.concluido")
        mock_telemetry.increment.assert_any_call("listar_documentos.tipos_encontrados", value=0)

    @patch("src.infrastructure.persistence.sqlite_repository.SQLiteDocumentoRepository")
    def test_telemetria_verificar_traducoes_sucesso(self, mock_repo_class):
        """Telemetria deve registrar verificação de traduções bem-sucedida."""
        mock_telemetry = MagicMock()
        uc_module.configure_telemetry(telemetry_instance=mock_telemetry)

        # Configurar mocks
        mock_repo = Mock()
        mock_repo_class.return_value = mock_repo

        # Configurar context manager com MagicMock
        mock_context_manager = MagicMock()
        mock_repo._conexao.return_value = mock_context_manager

        mock_conn = MagicMock()
        mock_context_manager.__enter__.return_value = mock_conn

        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = [1]

        use_case = ListarDocumentos(Mock())
        use_case._verificar_traducoes(1)

        mock_telemetry.increment.assert_any_call("listar_documentos.verificar_traducoes.iniciado")
        mock_telemetry.increment.assert_any_call("listar_documentos.verificar_traducoes.sucesso")

    @patch("src.infrastructure.persistence.sqlite_repository.SQLiteDocumentoRepository")
    def test_telemetria_verificar_traducoes_erro(self, mock_repo_class):
        """Telemetria deve registrar erro na verificação de traduções."""
        mock_telemetry = MagicMock()
        uc_module.configure_telemetry(telemetry_instance=mock_telemetry)

        # Configurar mock para lançar exceção
        mock_repo = Mock()
        mock_repo_class.return_value = mock_repo
        mock_repo._conexao.side_effect = Exception("Erro simulado")

        use_case = ListarDocumentos(Mock())
        use_case._verificar_traducoes(1)

        mock_telemetry.increment.assert_any_call("listar_documentos.verificar_traducoes.iniciado")
        mock_telemetry.increment.assert_any_call("listar_documentos.verificar_traducoes.erro")

    def test_sem_telemetria_nao_quebra(self):
        """Sem telemetria configurada, o código deve funcionar normalmente."""
        uc_module.configure_telemetry(telemetry_instance=None)

        mock_repo = Mock()
        mock_repo.listar.return_value = []
        mock_repo.contar.return_value = 0

        use_case = ListarDocumentos(mock_repo)

        # Nenhuma dessas chamadas deve lançar exceção
        use_case.com_traducao_nomes(True)
        use_case.executar(pagina=1)
        use_case.listar_tipos()

        # Agora com o patch correto, este teste vai funcionar
        with patch(
            "src.infrastructure.persistence.sqlite_repository.SQLiteDocumentoRepository"
        ) as mock_repo_class:
            mock_repo_db = Mock()
            mock_repo_class.return_value = mock_repo_db
            mock_repo_db._conexao.side_effect = Exception("Erro simulado")

            resultado = use_case._verificar_traducoes(1)
            assert resultado is False
