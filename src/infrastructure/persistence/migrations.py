# src/infrastructure/persistence/migrations.py
"""
Scripts de migração para o banco de dados.
Gerencia a evolução do schema sem perder dados.
"""

import sqlite3
from pathlib import Path
from typing import List, Tuple
from src.infrastructure.config.settings import settings
from src.infrastructure.persistence.models import DocumentoModel, TraducaoModel


def conectar() -> sqlite3.Connection:
    """Conecta ao banco de dados."""
    return sqlite3.connect(settings.DB_PATH)


def criar_tabelas():
    """Cria todas as tabelas se não existirem."""
    with conectar() as conn:
        cursor = conn.cursor()
        
        # Criar tabela documentos
        DocumentoModel.criar_tabela(cursor)
        
        # Criar tabela traducoes
        TraducaoModel.criar_tabela(cursor)
        
        conn.commit()
    print("✅ Tabelas criadas/verificadas com sucesso.")


def migrar_banco_existente():
    """
    Adiciona colunas de metadados ao banco existente.
    Usado após a FASE 1 para enriquecer dados antigos.
    """
    with conectar() as conn:
        cursor = conn.cursor()
        
        # Adicionar colunas de metadados
        DocumentoModel.adicionar_colunas_metadados(cursor)
        
        conn.commit()
    print("✅ Migração de metadados concluída.")


def verificar_integridade() -> List[str]:
    """
    Verifica integridade do banco.
    Retorna lista de problemas encontrados.
    """
    problemas = []
    
    with conectar() as conn:
        cursor = conn.cursor()
        
        # Verificar tabelas
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tabelas = [row[0] for row in cursor.fetchall()]
        
        if 'documentos' not in tabelas:
            problemas.append("Tabela 'documentos' não existe")
        
        if 'traducoes' not in tabelas:
            problemas.append("Tabela 'traducoes' não existe")
        
        # Verificar colunas da documentos
        if 'documentos' in tabelas:
            cursor.execute("PRAGMA table_info(documentos)")
            colunas = [row[1] for row in cursor.fetchall()]
            
            colunas_esperadas = [
                'tipo_documento', 'tipo_descricao', 'pessoa_principal',
                'remetente', 'destinatario', 'envolvidos', 'tem_anexos'
            ]
            
            for col in colunas_esperadas:
                if col not in colunas:
                    problemas.append(f"Coluna '{col}' não encontrada em 'documentos'")
    
    return problemas


# CORREÇÃO: verificar se colunas existem antes de usar

def estatisticas_banco() -> dict:
    """Retorna estatísticas do banco de dados."""
    with conectar() as conn:
        cursor = conn.cursor()
        
        stats = {}
        
        # 1. Total de documentos
        cursor.execute("SELECT COUNT(*) FROM documentos")
        stats['total_docs'] = cursor.fetchone()[0]
        
        # 2. Total de traduções
        try:
            cursor.execute("SELECT COUNT(*) FROM traducoes")
            stats['total_traducoes'] = cursor.fetchone()[0]
        except sqlite3.OperationalError:
            stats['total_traducoes'] = 0  # Tabela não existe
        
        # 3. Documentos por centro
        try:
            cursor.execute("SELECT centro, COUNT(*) FROM documentos GROUP BY centro")
            stats['docs_por_centro'] = dict(cursor.fetchall())
        except sqlite3.OperationalError:
            stats['docs_por_centro'] = {}
        
        # 4. Verificar quais colunas existem
        cursor.execute("PRAGMA table_info(documentos)")
        colunas = [row[1] for row in cursor.fetchall()]
        
        # 5. Documentos com metadados (só se a coluna existir)
        if 'tipo_documento' in colunas:
            cursor.execute("SELECT COUNT(*) FROM documentos WHERE tipo_documento IS NOT NULL")
            stats['docs_classificados'] = cursor.fetchone()[0]
        else:
            stats['docs_classificados'] = 0
        
        return stats
