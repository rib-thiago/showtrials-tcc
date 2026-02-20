# src/tests/test_gerar_relatorio_telemetry.py
"""
Testes de telemetria para o caso de uso GerarRelatorio.
"""

import tempfile
from unittest.mock import MagicMock, Mock

import src.application.use_cases.gerar_relatorio as uc_module
from src.application.use_cases.gerar_relatorio import GerarRelatorio


class TestGerarRelatorioTelemetry:
    """Testes para telemetria do GerarRelatorio."""

    def setup_method(self):
        """Reconfigura o módulo antes de cada teste."""
        uc_module._telemetry = None

    def _criar_repo_doc_mock(self, num_docs=5):
        """Cria mock do repositório com documentos."""
        repo = Mock()
        docs = []
        for i in range(num_docs):
            doc = Mock()
            doc.id = i + 1
            doc.centro = "lencenter"
            doc.tipo = "interrogatorio"
            doc.pessoa_principal = "Pessoa Teste"
            doc.tem_anexos = False
            doc.data_original = "1934"
            docs.append(doc)
        repo.listar.return_value = docs
        return repo

    def test_telemetria_coletar_dados(self):
        """Telemetria deve registrar coleta de dados."""
        mock_telemetry = MagicMock()
        uc_module.configure_telemetry(telemetry_instance=mock_telemetry)

        repo_doc = self._criar_repo_doc_mock()
        use_case = GerarRelatorio(repo_doc)

        use_case._coletar_dados()

        mock_telemetry.increment.assert_any_call("gerar_relatorio.coletar_dados.iniciado")
        mock_telemetry.increment.assert_any_call("gerar_relatorio.coletar_dados.concluido")
        mock_telemetry.increment.assert_any_call("gerar_relatorio.documentos_processados", value=5)

    def test_telemetria_gerar_txt(self):
        """Telemetria deve registrar geração de TXT."""
        mock_telemetry = MagicMock()
        uc_module.configure_telemetry(telemetry_instance=mock_telemetry)

        repo_doc = self._criar_repo_doc_mock()
        use_case = GerarRelatorio(repo_doc)

        use_case.gerar_relatorio_txt()

        mock_telemetry.increment.assert_any_call("gerar_relatorio.gerar_txt.iniciado")
        mock_telemetry.increment.assert_any_call("gerar_relatorio.gerar_txt.concluido")

    def test_telemetria_salvar_txt(self):
        """Telemetria deve registrar salvamento de TXT."""
        mock_telemetry = MagicMock()
        uc_module.configure_telemetry(telemetry_instance=mock_telemetry)

        repo_doc = self._criar_repo_doc_mock()
        use_case = GerarRelatorio(repo_doc)

        with tempfile.TemporaryDirectory() as tmpdir:
            use_case.salvar_relatorio(formato="txt", diretorio=tmpdir)

        mock_telemetry.increment.assert_any_call("gerar_relatorio.salvar.iniciado")
        mock_telemetry.increment.assert_any_call("gerar_relatorio.formato.txt")
        mock_telemetry.increment.assert_any_call("gerar_relatorio.salvar.sucesso_txt")

    def test_telemetria_salvar_html(self):
        """Telemetria deve registrar placeholder HTML."""
        mock_telemetry = MagicMock()
        uc_module.configure_telemetry(telemetry_instance=mock_telemetry)

        repo_doc = self._criar_repo_doc_mock()
        use_case = GerarRelatorio(repo_doc)

        use_case.salvar_relatorio(formato="html")

        mock_telemetry.increment.assert_any_call("gerar_relatorio.salvar.iniciado")
        mock_telemetry.increment.assert_any_call("gerar_relatorio.formato.html")
        mock_telemetry.increment.assert_any_call("gerar_relatorio.salvar.html_placeholder")

    def test_telemetria_salvar_formato_invalido(self):
        """Telemetria deve registrar formato inválido."""
        mock_telemetry = MagicMock()
        uc_module.configure_telemetry(telemetry_instance=mock_telemetry)

        repo_doc = self._criar_repo_doc_mock()
        use_case = GerarRelatorio(repo_doc)

        use_case.salvar_relatorio(formato="pdf")

        mock_telemetry.increment.assert_any_call("gerar_relatorio.salvar.iniciado")
        mock_telemetry.increment.assert_any_call("gerar_relatorio.formato.pdf")
        mock_telemetry.increment.assert_any_call("gerar_relatorio.salvar.formato_invalido")

    def test_sem_telemetria_nao_quebra(self):
        """Sem telemetria configurada, o código deve funcionar normalmente."""
        uc_module.configure_telemetry(telemetry_instance=None)

        repo_doc = self._criar_repo_doc_mock()
        use_case = GerarRelatorio(repo_doc)

        # Nenhuma dessas chamadas deve lançar exceção
        dados = use_case._coletar_dados()
        relatorio = use_case.gerar_relatorio_txt()
        with tempfile.TemporaryDirectory() as tmpdir:
            caminho = use_case.salvar_relatorio(diretorio=tmpdir)

        assert dados["total_documentos"] == 5
        assert len(relatorio) > 0
        assert caminho.endswith(".txt")
