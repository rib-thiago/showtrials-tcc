# src/tests/test_infrastructure/test_sqlite_repository.py
"""
Testes para o repositório SQLite.
Usa um banco em memória para isolamento.
"""

import tempfile
from datetime import datetime

import pytest

from src.domain.entities.documento import Documento
from src.infrastructure.persistence.models import DocumentoModel, TraducaoModel
from src.infrastructure.persistence.sqlite_repository import SQLiteDocumentoRepository


@pytest.fixture
def repo_memoria():
    """Fixture que cria um repositório com banco em memória."""
    # Criar banco temporário
    with tempfile.NamedTemporaryFile(suffix=".db") as tmp:
        repo = SQLiteDocumentoRepository(db_path=tmp.name)

        # Criar tabelas
        with repo._conexao() as conn:
            cursor = conn.cursor()
            DocumentoModel.criar_tabela(cursor)
            TraducaoModel.criar_tabela(cursor)
            DocumentoModel.adicionar_colunas_metadados(cursor)

        yield repo


class TestSQLiteDocumentoRepository:
    """Testes para o repositório SQLite."""

    def test_salvar_novo_documento(self, repo_memoria):
        """Deve inserir novo documento."""
        doc = Documento(
            centro="lencenter",
            titulo="Teste Documento",
            url="http://teste.com/1",
            texto="Conteúdo do teste",
            data_coleta=datetime.now(),
            tipo="interrogatorio",
            tipo_descricao="Interrogatório",
        )

        doc_id = repo_memoria.salvar(doc)

        assert doc_id > 0

        # Verificar se salvou
        salvo = repo_memoria.buscar_por_id(doc_id)
        assert salvo is not None
        assert salvo.titulo == "Teste Documento"
        assert salvo.tipo == "interrogatorio"

    def test_salvar_documento_existente(self, repo_memoria):
        """Deve atualizar documento existente."""
        doc = Documento(
            centro="lencenter",
            titulo="Original",
            url="http://teste.com/2",
            texto="Original",
            data_coleta=datetime.now(),
        )

        doc_id = repo_memoria.salvar(doc)

        # Modificar e salvar
        doc.id = doc_id
        doc.titulo = "Modificado"
        doc.tipo = "carta"

        repo_memoria.salvar(doc)

        # Verificar atualização
        salvo = repo_memoria.buscar_por_id(doc_id)
        assert salvo.titulo == "Modificado"
        assert salvo.tipo == "carta"

    def test_buscar_por_id_inexistente(self, repo_memoria):
        """Deve retornar None para ID inexistente."""
        doc = repo_memoria.buscar_por_id(99999)
        assert doc is None

    def test_listar_sem_filtros(self, repo_memoria):
        """Deve listar documentos com paginação."""
        # Inserir 5 documentos
        for i in range(1, 6):
            doc = Documento(
                centro="lencenter",
                titulo=f"Doc {i}",
                url=f"http://teste.com/{i}",
                texto=f"Texto {i}",
                data_coleta=datetime.now(),
            )
            repo_memoria.salvar(doc)

        # Listar
        docs = repo_memoria.listar(offset=0, limite=3)

        assert len(docs) == 3
        assert docs[0].titulo == "Doc 1"
        assert docs[1].titulo == "Doc 2"
        assert docs[2].titulo == "Doc 3"

    def test_listar_com_filtro_centro(self, repo_memoria):
        """Deve filtrar por centro."""
        # Lencenter
        for i in range(1, 4):
            doc = Documento(
                centro="lencenter",
                titulo=f"Len {i}",
                url=f"http://len.com/{i}",
                texto="...",
                data_coleta=datetime.now(),
            )
            repo_memoria.salvar(doc)

        # Moscenter
        for i in range(1, 3):
            doc = Documento(
                centro="moscenter",
                titulo=f"Mos {i}",
                url=f"http://mos.com/{i}",
                texto="...",
                data_coleta=datetime.now(),
            )
            repo_memoria.salvar(doc)

        docs_len = repo_memoria.listar(centro="lencenter")
        docs_mos = repo_memoria.listar(centro="moscenter")

        assert len(docs_len) == 3
        assert len(docs_mos) == 2

    def test_contar_documentos(self, repo_memoria):
        """Deve contar documentos corretamente."""
        # Inserir alguns
        for i in range(1, 8):
            doc = Documento(
                centro="lencenter" if i % 2 == 0 else "moscenter",
                titulo=f"Doc {i}",
                url=f"http://teste.com/{i}",
                texto="...",
                data_coleta=datetime.now(),
            )
            repo_memoria.salvar(doc)

        total = repo_memoria.contar()
        total_len = repo_memoria.contar(centro="lencenter")
        total_mos = repo_memoria.contar(centro="moscenter")

        assert total == 7
        assert total_len == 3  # pares
        assert total_mos == 4  # ímpares

    def test_remover_documento(self, repo_memoria):
        """Deve remover documento por ID."""
        doc = Documento(
            centro="lencenter",
            titulo="Para remover",
            url="http://teste.com/remover",
            texto="...",
            data_coleta=datetime.now(),
        )

        doc_id = repo_memoria.salvar(doc)

        # Remover
        resultado = repo_memoria.remover(doc_id)
        assert resultado is True

        # Verificar
        removido = repo_memoria.buscar_por_id(doc_id)
        assert removido is None

    def test_remover_inexistente(self, repo_memoria):
        """Remover documento inexistente deve retornar False."""
        resultado = repo_memoria.remover(99999)
        assert resultado is False
