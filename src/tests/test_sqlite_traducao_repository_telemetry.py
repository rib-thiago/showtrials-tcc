# src/tests/test_sqlite_traducao_repository_telemetry.py
"""
Testes de telemetria para o repositório SQLite de traduções.
"""

import tempfile
from datetime import datetime
from unittest.mock import MagicMock

import pytest

import src.infrastructure.persistence.sqlite_traducao_repository as repo_module


@pytest.fixture
def repo_memoria():
    """Fixture que cria um repositório com banco em memória."""
    with tempfile.NamedTemporaryFile(suffix=".db") as tmp:
        from src.infrastructure.persistence.sqlite_traducao_repository import (
            SQLiteTraducaoRepository,
        )

        repo = SQLiteTraducaoRepository(db_path=tmp.name)

        # Criar tabela
        with repo._conexao() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE traducoes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    documento_id INTEGER NOT NULL,
                    idioma TEXT NOT NULL,
                    texto_traduzido TEXT NOT NULL,
                    modelo TEXT,
                    custo REAL,
                    data_traducao TEXT NOT NULL
                )
            """
            )

        yield repo


class TestSQLiteTraducaoRepositoryTelemetry:
    """Testes de telemetria para o repositório."""

    def setup_method(self):
        """Reconfigura o módulo antes de cada teste."""
        repo_module._telemetry = None

    def test_telemetria_insercao(self, repo_memoria):
        """Inserção deve registrar contador."""
        mock_telemetry = MagicMock()
        repo_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.domain.entities.traducao import Traducao
        from src.infrastructure.persistence.sqlite_traducao_repository import (
            SQLiteTraducaoRepository,
        )

        repo = SQLiteTraducaoRepository(db_path=repo_memoria.db_path)

        traducao = Traducao(
            documento_id=42,
            idioma="en",
            texto_traduzido="Hello",
            data_traducao=datetime.now(),
        )

        repo.salvar(traducao)

        mock_telemetry.increment.assert_any_call("sqlite_traducao.insercao")

    def test_telemetria_atualizacao(self, repo_memoria):
        """Atualização deve registrar contador."""
        mock_telemetry = MagicMock()
        repo_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.domain.entities.traducao import Traducao
        from src.infrastructure.persistence.sqlite_traducao_repository import (
            SQLiteTraducaoRepository,
        )

        repo = SQLiteTraducaoRepository(db_path=repo_memoria.db_path)

        # Inserir
        traducao = Traducao(
            documento_id=42,
            idioma="en",
            texto_traduzido="Original",
            data_traducao=datetime.now(),
        )
        traducao.id = repo.salvar(traducao)

        # Atualizar
        traducao.texto_traduzido = "Modificado"
        repo.salvar(traducao)

        mock_telemetry.increment.assert_any_call("sqlite_traducao.atualizacao")

    def test_telemetria_busca_por_id(self, repo_memoria):
        """Busca por ID deve registrar contador."""
        mock_telemetry = MagicMock()
        repo_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.infrastructure.persistence.sqlite_traducao_repository import (
            SQLiteTraducaoRepository,
        )

        repo = SQLiteTraducaoRepository(db_path=repo_memoria.db_path)
        repo.buscar_por_id(1)

        mock_telemetry.increment.assert_any_call("sqlite_traducao.busca_por_id")

    def test_telemetria_busca_por_documento(self, repo_memoria):
        """Busca por documento deve registrar contador."""
        mock_telemetry = MagicMock()
        repo_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.infrastructure.persistence.sqlite_traducao_repository import (
            SQLiteTraducaoRepository,
        )

        repo = SQLiteTraducaoRepository(db_path=repo_memoria.db_path)
        repo.buscar_por_documento(42, "en")

        mock_telemetry.increment.assert_any_call("sqlite_traducao.busca_por_documento")

    def test_telemetria_listagem(self, repo_memoria):
        """Listagem deve registrar contador com valor correto."""
        mock_telemetry = MagicMock()
        repo_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.domain.entities.traducao import Traducao
        from src.infrastructure.persistence.sqlite_traducao_repository import (
            SQLiteTraducaoRepository,
        )

        repo = SQLiteTraducaoRepository(db_path=repo_memoria.db_path)

        # Inserir 2 traduções
        for i in range(2):
            traducao = Traducao(
                documento_id=42,
                idioma="en",
                texto_traduzido=f"Texto {i}",
                data_traducao=datetime.now(),
            )
            repo.salvar(traducao)

        repo.listar_por_documento(42)

        mock_telemetry.increment.assert_any_call("sqlite_traducao.listagem", value=2)

    def test_telemetria_contagem(self, repo_memoria):
        """Contagem deve registrar contador."""
        mock_telemetry = MagicMock()
        repo_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.infrastructure.persistence.sqlite_traducao_repository import (
            SQLiteTraducaoRepository,
        )

        repo = SQLiteTraducaoRepository(db_path=repo_memoria.db_path)
        repo.contar_por_documento(42)

        mock_telemetry.increment.assert_any_call("sqlite_traducao.contagem")

    def test_sem_telemetria_nao_quebra(self, repo_memoria):
        """Sem telemetria, o código deve funcionar normalmente."""
        from src.domain.entities.traducao import Traducao
        from src.infrastructure.persistence.sqlite_traducao_repository import (
            SQLiteTraducaoRepository,
        )

        repo = SQLiteTraducaoRepository(db_path=repo_memoria.db_path)

        traducao = Traducao(
            documento_id=42,
            idioma="en",
            texto_traduzido="Hello",
            data_traducao=datetime.now(),
        )

        traducao_id = repo.salvar(traducao)
        assert traducao_id > 0
