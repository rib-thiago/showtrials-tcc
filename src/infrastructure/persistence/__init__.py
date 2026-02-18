# src/infrastructure/persistence/__init__.py
from src.infrastructure.persistence.migrations import criar_tabelas, migrar_banco_existente
from src.infrastructure.persistence.sqlite_repository import SQLiteDocumentoRepository

__all__ = ["SQLiteDocumentoRepository", "criar_tabelas", "migrar_banco_existente"]
