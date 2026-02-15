# src/tests/test_infrastructure/test_migrations.py
"""
Testes para migrações do banco de dados.
"""

import pytest
import sqlite3
import tempfile
from pathlib import Path

from src.infrastructure.persistence.migrations import (
    criar_tabelas,
    migrar_banco_existente,
    verificar_integridade,
    estatisticas_banco
)
from src.infrastructure.config.settings import settings


@pytest.fixture
def db_temporario():
    """Fixture que cria um banco temporário para testes."""
    with tempfile.NamedTemporaryFile(suffix='.db') as tmp:
        # Salvar caminho original e substituir
        original_path = settings.DB_PATH
        settings.DB_PATH = Path(tmp.name)
        
        yield tmp.name
        
        # Restaurar
        settings.DB_PATH = original_path


class TestMigrations:
    """Testes para scripts de migração."""
    
    def test_criar_tabelas(self, db_temporario):
        """Deve criar tabelas sem erros."""
        criar_tabelas()
        
        # Verificar
        conn = sqlite3.connect(db_temporario)
        cursor = conn.cursor()
        
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tabelas = [row[0] for row in cursor.fetchall()]
        
        assert 'documentos' in tabelas
        assert 'traducoes' in tabelas
        
        conn.close()
    
    def test_migrar_banco_existente(self, db_temporario):
        """Deve adicionar colunas de metadados."""
        # Criar tabela sem metadados
        conn = sqlite3.connect(db_temporario)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE documentos (
                id INTEGER PRIMARY KEY,
                centro TEXT,
                titulo TEXT,
                url TEXT,
                texto TEXT,
                data_coleta TEXT
            )
        """)
        conn.commit()
        conn.close()
        
        # Executar migração
        migrar_banco_existente()
        
        # Verificar colunas adicionadas
        conn = sqlite3.connect(db_temporario)
        cursor = conn.cursor()
        cursor.execute("PRAGMA table_info(documentos)")
        colunas = [row[1] for row in cursor.fetchall()]
        
        assert 'tipo_documento' in colunas
        assert 'pessoa_principal' in colunas
        assert 'tem_anexos' in colunas
        
        conn.close()
    
    def test_verificar_integridade_banco_ok(self, db_temporario):
        """Banco íntegro deve retornar lista vazia."""
        criar_tabelas()
        migrar_banco_existente()
        
        problemas = verificar_integridade()
        
        assert problemas == []
    
    def test_verificar_integridade_banco_incompleto(self, db_temporario):
        """Banco incompleto deve apontar problemas."""
        conn = sqlite3.connect(db_temporario)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE documentos (id INTEGER PRIMARY KEY)")
        conn.commit()
        conn.close()
        
        problemas = verificar_integridade()
        
        assert len(problemas) > 0
        assert any('traducoes' in p for p in problemas)
    
    def test_estatisticas_banco(self, db_temporario):
        """Deve retornar estatísticas básicas."""
        criar_tabelas()
        
        # Inserir alguns dados
        conn = sqlite3.connect(db_temporario)
        cursor = conn.cursor()
        
        for i in range(5):
            cursor.execute("""
                INSERT INTO documentos 
                (centro, titulo, url, texto, data_coleta)
                VALUES (?, ?, ?, ?, ?)
            """, (
                'lencenter' if i % 2 == 0 else 'moscenter',
                f'Doc {i}',
                f'url{i}',
                'texto',
                '2024-01-01'
            ))
        
        conn.commit()
        conn.close()
        
        stats = estatisticas_banco()
        
        assert stats['total_docs'] == 5
        assert 'lencenter' in stats['docs_por_centro']
        assert 'moscenter' in stats['docs_por_centro']