# src/tests/test_sqlite_traducao_repository.py
"""
Testes de lógica para o repositório SQLite de traduções.
"""

import tempfile
from datetime import datetime

import pytest

from src.domain.entities.traducao import Traducao
from src.infrastructure.persistence.sqlite_traducao_repository import SQLiteTraducaoRepository


@pytest.fixture
def repo_memoria():
    """Fixture que cria um repositório com banco em memória."""
    with tempfile.NamedTemporaryFile(suffix=".db") as tmp:
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


class TestSQLiteTraducaoRepository:
    """Testes de lógica para o repositório SQLite de traduções."""

    def test_salvar_nova_traducao(self, repo_memoria):
        """Deve inserir uma nova tradução."""
        data = datetime.now()
        traducao = Traducao(
            documento_id=42,
            idioma="en",
            texto_traduzido="Hello world",
            data_traducao=data,
            modelo="nmt",
            custo=0.15,
        )

        traducao_id = repo_memoria.salvar(traducao)

        assert traducao_id > 0

        # Verificar se salvou
        salva = repo_memoria.buscar_por_id(traducao_id)
        assert salva is not None
        assert salva.documento_id == 42
        assert salva.idioma == "en"
        assert salva.texto_traduzido == "Hello world"
        assert salva.modelo == "nmt"
        assert salva.custo == 0.15

    def test_salvar_traducao_existente(self, repo_memoria):
        """Deve atualizar uma tradução existente."""
        data = datetime.now()
        traducao = Traducao(
            documento_id=42,
            idioma="en",
            texto_traduzido="Original",
            data_traducao=data,
            modelo="nmt",
            custo=0.15,
        )

        traducao_id = repo_memoria.salvar(traducao)

        # Modificar e salvar
        traducao.id = traducao_id
        traducao.texto_traduzido = "Modificado"
        traducao.custo = 0.20

        repo_memoria.salvar(traducao)

        # Verificar atualização
        atualizada = repo_memoria.buscar_por_id(traducao_id)
        assert atualizada.texto_traduzido == "Modificado"
        assert atualizada.custo == 0.20

    def test_buscar_por_id_inexistente(self, repo_memoria):
        """Deve retornar None para ID inexistente."""
        traducao = repo_memoria.buscar_por_id(99999)
        assert traducao is None

    def test_buscar_por_documento(self, repo_memoria):
        """Deve buscar tradução por documento e idioma."""
        data = datetime.now()

        # Inserir tradução
        traducao = Traducao(
            documento_id=42,
            idioma="en",
            texto_traduzido="Hello",
            data_traducao=data,
        )
        repo_memoria.salvar(traducao)

        # Buscar
        encontrada = repo_memoria.buscar_por_documento(42, "en")
        assert encontrada is not None
        assert encontrada.idioma == "en"

        # Idioma diferente
        nao_encontrada = repo_memoria.buscar_por_documento(42, "pt")
        assert nao_encontrada is None

    def test_listar_por_documento(self, repo_memoria):
        """Deve listar todas as traduções de um documento."""
        data = datetime.now()

        # Inserir 3 traduções
        for idioma in ["en", "pt", "es"]:
            traducao = Traducao(
                documento_id=42,
                idioma=idioma,
                texto_traduzido=f"Texto em {idioma}",
                data_traducao=data,
            )
            repo_memoria.salvar(traducao)

        # Inserir tradução de outro documento (não deve aparecer)
        outra = Traducao(
            documento_id=99,
            idioma="en",
            texto_traduzido="Outro",
            data_traducao=data,
        )
        repo_memoria.salvar(outra)

        # Listar
        traducoes = repo_memoria.listar_por_documento(42)

        assert len(traducoes) == 3
        idiomas = [t.idioma for t in traducoes]
        assert "en" in idiomas
        assert "pt" in idiomas
        assert "es" in idiomas

    def test_contar_por_documento(self, repo_memoria):
        """Deve contar traduções de um documento."""
        data = datetime.now()

        # Inserir 2 traduções
        for idioma in ["en", "pt"]:
            traducao = Traducao(
                documento_id=42,
                idioma=idioma,
                texto_traduzido=f"Texto em {idioma}",
                data_traducao=data,
            )
            repo_memoria.salvar(traducao)

        count = repo_memoria.contar_por_documento(42)
        assert count == 2

        count_outro = repo_memoria.contar_por_documento(99)
        assert count_outro == 0
