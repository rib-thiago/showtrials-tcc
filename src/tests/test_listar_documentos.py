# src/tests/test_listar_documentos.py
"""
Testes para o caso de uso ListarDocumentos (sem telemetria).
"""

from unittest.mock import MagicMock, Mock, patch

import pytest

from src.application.use_cases.listar_documentos import ListarDocumentos


class TestListarDocumentos:
    """Testes para a lógica de listagem de documentos."""

    @pytest.fixture
    def repo_mock(self):
        """Fixture para mock do repositório."""
        repo = Mock()
        return repo

    @pytest.fixture
    def documentos_mock(self):
        """Cria uma lista de documentos mock."""
        docs = []
        for i in range(5):
            doc = Mock()
            doc.id = i + 1
            doc.centro = "lencenter" if i < 3 else "moscenter"
            doc.titulo = f"Documento {i+1}"
            doc.data_original = f"1934-{i+1:02d}-04"
            doc.tipo = "interrogatorio"
            doc.tipo_descricao = "Protocolo de Interrogatório"
            doc.pessoa_principal = "Л.В. Николаева" if i < 2 else None
            docs.append(doc)
        return docs

    def test_executar_com_paginacao_basica(self, repo_mock, documentos_mock):
        """Deve executar listagem com paginação básica."""
        repo_mock.listar.return_value = documentos_mock
        repo_mock.contar.return_value = 10

        use_case = ListarDocumentos(repo_mock)
        resultado = use_case.executar(pagina=1, limite=5)

        assert len(resultado["items"]) == 5
        assert resultado["total"] == 10
        assert resultado["pagina"] == 1
        assert resultado["total_paginas"] == 2
        repo_mock.listar.assert_called_once_with(offset=0, limite=5, centro=None, tipo=None)

    def test_executar_com_filtros(self, repo_mock, documentos_mock):
        """Deve aplicar filtros corretamente."""
        repo_mock.listar.return_value = documentos_mock[:3]
        repo_mock.contar.return_value = 3

        use_case = ListarDocumentos(repo_mock)
        resultado = use_case.executar(pagina=1, limite=5, centro="lencenter", tipo="interrogatorio")

        assert len(resultado["items"]) == 3
        repo_mock.listar.assert_called_once_with(
            offset=0, limite=5, centro="lencenter", tipo="interrogatorio"
        )
        repo_mock.contar.assert_called_once_with(centro="lencenter", tipo="interrogatorio")

    def test_executar_pagina_2(self, repo_mock, documentos_mock):
        """Deve calcular offset corretamente para página 2."""
        repo_mock.listar.return_value = documentos_mock
        repo_mock.contar.return_value = 10

        use_case = ListarDocumentos(repo_mock)
        resultado = use_case.executar(pagina=2, limite=5)

        assert resultado["pagina"] == 2
        repo_mock.listar.assert_called_once_with(offset=5, limite=5, centro=None, tipo=None)

    def test_executar_sem_resultados(self, repo_mock):
        """Deve lidar com lista vazia."""
        repo_mock.listar.return_value = []
        repo_mock.contar.return_value = 0

        use_case = ListarDocumentos(repo_mock)
        resultado = use_case.executar(pagina=1)

        assert len(resultado["items"]) == 0
        assert resultado["total"] == 0
        assert resultado["total_paginas"] == 0

    def test_com_traducao_nomes_fluent(self, repo_mock):
        """Método com_traducao_nomes deve retornar self para chamadas encadeadas."""
        use_case = ListarDocumentos(repo_mock)
        resultado = use_case.com_traducao_nomes(True)

        assert resultado is use_case
        assert use_case._tradutor_nomes is True

    def test_listar_tipos_basico(self, repo_mock, documentos_mock):
        """Deve listar tipos com contagens."""
        repo_mock.listar.return_value = documentos_mock

        use_case = ListarDocumentos(repo_mock)
        tipos = use_case.listar_tipos()

        assert len(tipos) > 0
        assert len(tipos[0]) == 4  # (tipo, descricao, icone, count)
        repo_mock.listar.assert_called_once_with(limite=1000, centro=None)

    def test_listar_tipos_com_filtro_centro(self, repo_mock, documentos_mock):
        """Deve filtrar por centro ao listar tipos."""
        repo_mock.listar.return_value = documentos_mock

        use_case = ListarDocumentos(repo_mock)
        tipos = use_case.listar_tipos(centro="lencenter")

        repo_mock.listar.assert_called_once_with(limite=1000, centro="lencenter")

    def test_listar_tipos_com_tipos_variados(self, repo_mock):
        """Deve lidar com diferentes tipos de documento."""
        docs = []
        tipos = ["interrogatorio", "carta", "relatorio", "interrogatorio", "carta"]

        for i, tipo in enumerate(tipos):
            doc = Mock()
            doc.id = i + 1
            doc.tipo = tipo
            doc.centro = "lencenter"
            docs.append(doc)

        repo_mock.listar.return_value = docs

        use_case = ListarDocumentos(repo_mock)
        tipos_resultado = use_case.listar_tipos()

        # Deve vir ordenado por frequência
        assert tipos_resultado[0][0] == "interrogatorio"  # 2 ocorrências
        assert tipos_resultado[0][3] == 2
        assert tipos_resultado[1][0] == "carta"  # 2 ocorrências
        assert tipos_resultado[1][3] == 2
        assert tipos_resultado[2][0] == "relatorio"  # 1 ocorrência
        assert tipos_resultado[2][3] == 1

    def test_listar_tipos_sem_tipos(self, repo_mock):
        """Documentos sem tipo devem ser ignorados."""
        docs = []
        for i in range(3):
            doc = Mock()
            doc.id = i + 1
            doc.tipo = None
            docs.append(doc)

        repo_mock.listar.return_value = docs

        use_case = ListarDocumentos(repo_mock)
        tipos = use_case.listar_tipos()

        assert len(tipos) == 0

    @patch("src.infrastructure.persistence.sqlite_repository.SQLiteDocumentoRepository")
    def test_verificar_traducoes_com_sucesso(self, mock_repo_class, repo_mock):
        """Deve verificar traduções corretamente."""
        # Configurar mock da conexão
        mock_repo = Mock()
        mock_repo_class.return_value = mock_repo

        # Configurar o context manager _conexao usando MagicMock
        mock_context_manager = MagicMock()
        mock_repo._conexao.return_value = mock_context_manager

        # Configurar o __enter__ para retornar a conexão mockada
        mock_conn = MagicMock()
        mock_context_manager.__enter__.return_value = mock_conn

        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = [3]  # 3 traduções

        use_case = ListarDocumentos(repo_mock)
        resultado = use_case._verificar_traducoes(1)

        assert resultado is True
        mock_cursor.execute.assert_called_once_with(
            "SELECT COUNT(*) FROM traducoes WHERE documento_id = ?", (1,)
        )

    @patch("src.infrastructure.persistence.sqlite_repository.SQLiteDocumentoRepository")
    def test_verificar_traducoes_sem_traducao(self, mock_repo_class, repo_mock):
        """Deve retornar False quando não há traduções."""
        mock_repo = Mock()
        mock_repo_class.return_value = mock_repo

        mock_context_manager = MagicMock()
        mock_repo._conexao.return_value = mock_context_manager

        mock_conn = MagicMock()
        mock_context_manager.__enter__.return_value = mock_conn

        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = [0]  # 0 traduções

        use_case = ListarDocumentos(repo_mock)
        resultado = use_case._verificar_traducoes(1)

        assert resultado is False

    @patch("src.infrastructure.persistence.sqlite_repository.SQLiteDocumentoRepository")
    def test_verificar_traducoes_com_erro(self, mock_repo_class, repo_mock):
        """Erro na consulta deve retornar False e não quebrar."""
        mock_repo = Mock()
        mock_repo_class.return_value = mock_repo

        # Configurar para lançar exceção ao acessar _conexao
        mock_repo._conexao.side_effect = Exception("Erro simulado")

        use_case = ListarDocumentos(repo_mock)
        resultado = use_case._verificar_traducoes(1)

        assert resultado is False  # Fallback seguro
