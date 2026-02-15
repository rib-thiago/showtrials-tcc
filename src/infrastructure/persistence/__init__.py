# src/infrastructure/persistence/__init__.py
from src.infrastructure.persistence.sqlite_repository import SQLiteDocumentoRepository
from src.infrastructure.persistence.migrations import criar_tabelas, migrar_banco_existente

__all__ = ['SQLiteDocumentoRepository', 'criar_tabelas', 'migrar_banco_existente']