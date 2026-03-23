# src/tests/test_exportar_documento_telemetry.py
"""
Testes de telemetria para o caso de uso ExportarDocumento.
"""

import tempfile
from datetime import datetime
from unittest.mock import MagicMock, Mock

import pytest

import src.application.use_cases.exportar_documento as uc_module
from src.application.use_cases.exportar_documento import ExportarDocumento


class TestExportarDocumentoTelemetry:
    """Testes para telemetria do ExportarDocumento."""

    def setup_method(self):
        """Reconfigura o módulo antes de cada teste."""
        uc_module._telemetry = None

    def _criar_mock_documento(self):
        """Cria um mock de documento com todos os atributos necessários."""
        doc = Mock()
        doc.id = 1
        doc.texto = "Conteúdo do documento para teste"
        doc.data_coleta = datetime.now()
        doc.titulo = "Título Teste"
        doc.centro = "lencenter"
        doc.data_original = "1934"
        doc.url = "http://test.com"
        doc.pessoa_principal = None
        doc.remetente = None
        doc.destinatario = None
        doc.envolvidos = []
        doc.tem_anexos = False
        doc.tamanho_caracteres = len(doc.texto)
        doc.tipo = None
        doc.tipo_descricao = None
        return doc

    def test_telemetria_execucao_sucesso(self):
        """Telemetria deve registrar execução bem-sucedida."""
        mock_telemetry = MagicMock()
        uc_module.configure_telemetry(telemetry_instance=mock_telemetry)

        mock_doc = self._criar_mock_documento()
        mock_repo_doc = Mock()
        mock_repo_doc.buscar_por_id.return_value = mock_doc

        use_case = ExportarDocumento(mock_repo_doc)

        with tempfile.TemporaryDirectory() as tmpdir:
            resultado = use_case.executar(documento_id=1, diretorio=tmpdir)

        assert resultado["sucesso"] is True

        # Verificar chamadas principais
        mock_telemetry.increment.assert_any_call("exportar_documento.executar.iniciado")
        mock_telemetry.increment.assert_any_call("exportar_documento.executar.concluido")

    def test_telemetria_formato_invalido(self):
        """Telemetria deve registrar formato inválido."""
        mock_telemetry = MagicMock()
        uc_module.configure_telemetry(telemetry_instance=mock_telemetry)

        use_case = ExportarDocumento(Mock())

        resultado = use_case.executar(documento_id=1, formato="docx")

        assert resultado["sucesso"] is False
        mock_telemetry.increment.assert_any_call("exportar_documento.erro.formato_invalido")

    def test_telemetria_documento_nao_encontrado(self):
        """Telemetria deve registrar documento não encontrado."""
        mock_telemetry = MagicMock()
        uc_module.configure_telemetry(telemetry_instance=mock_telemetry)

        mock_repo_doc = Mock()
        mock_repo_doc.buscar_por_id.return_value = None

        use_case = ExportarDocumento(mock_repo_doc)

        resultado = use_case.executar(documento_id=999)

        assert resultado["sucesso"] is False
        mock_telemetry.increment.assert_any_call("exportar_documento.erro.documento_indisponivel")

    def test_telemetria_traducao_nao_encontrada(self):
        """Telemetria deve registrar tradução não encontrada."""
        mock_telemetry = MagicMock()
        uc_module.configure_telemetry(telemetry_instance=mock_telemetry)

        mock_doc = self._criar_mock_documento()
        mock_repo_doc = Mock()
        mock_repo_doc.buscar_por_id.return_value = mock_doc

        mock_repo_trad = Mock()
        mock_repo_trad.buscar_por_documento.return_value = None

        use_case = ExportarDocumento(mock_repo_doc, mock_repo_trad)

        resultado = use_case.executar(documento_id=1, idioma="fr")

        assert resultado["sucesso"] is False
        mock_telemetry.increment.assert_any_call("exportar_documento.erro.traducao_nao_encontrada")

    def test_telemetria_pdf_nao_implementado(self):
        """Telemetria deve registrar tentativa de PDF."""
        mock_telemetry = MagicMock()
        uc_module.configure_telemetry(telemetry_instance=mock_telemetry)

        mock_doc = self._criar_mock_documento()
        mock_repo_doc = Mock()
        mock_repo_doc.buscar_por_id.return_value = mock_doc

        use_case = ExportarDocumento(mock_repo_doc)

        resultado = use_case.executar(documento_id=1, formato="pdf")

        assert resultado["sucesso"] is False
        mock_telemetry.increment.assert_any_call("exportar_documento.executar.pdf_nao_implementado")

    def test_telemetria_erro_execucao(self):
        """Telemetria NÃO deve registrar erro para exceções não capturadas."""
        mock_telemetry = MagicMock()
        uc_module.configure_telemetry(telemetry_instance=mock_telemetry)

        mock_repo_doc = Mock()
        mock_repo_doc.buscar_por_id.side_effect = Exception("Erro simulado")

        use_case = ExportarDocumento(mock_repo_doc)

        with pytest.raises(Exception):
            use_case.executar(documento_id=1)

        # Verificar chamadas que ocorreram ANTES da exceção
        mock_telemetry.increment.assert_any_call("exportar_documento.executar.iniciado")

        # Verificar que erro.execucao NÃO foi chamado
        calls = [call[0][0] for call in mock_telemetry.increment.call_args_list]
        assert "exportar_documento.erro.execucao" not in calls

    def test_telemetria_listar_idiomas(self):
        """Telemetria deve registrar listagem de idiomas."""
        mock_telemetry = MagicMock()
        uc_module.configure_telemetry(telemetry_instance=mock_telemetry)

        mock_repo_trad = Mock()
        mock_repo_trad.listar_por_documento.return_value = [Mock(), Mock()]

        use_case = ExportarDocumento(Mock(), mock_repo_trad)

        idiomas = use_case.listar_idiomas_disponiveis(1)

        assert len(idiomas) == 3
        mock_telemetry.increment.assert_any_call("exportar_documento.listar_idiomas.iniciado")
        mock_telemetry.increment.assert_any_call("exportar_documento.listar_idiomas.encontrados.2")

    def test_sem_telemetria_nao_quebra(self):
        """Sem telemetria configurada, o código deve funcionar normalmente."""
        uc_module.configure_telemetry(telemetry_instance=None)

        mock_doc = self._criar_mock_documento()
        mock_repo_doc = Mock()
        mock_repo_doc.buscar_por_id.return_value = mock_doc

        use_case = ExportarDocumento(mock_repo_doc)

        with tempfile.TemporaryDirectory() as tmpdir:
            resultado = use_case.executar(documento_id=1, diretorio=tmpdir)

        assert resultado["sucesso"] is True
