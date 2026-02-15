# src/infrastructure/__init__.py
"""
Infrastructure Layer - Implementações concretas.
"""

from src.infrastructure.persistence.sqlite_repository import SQLiteDocumentoRepository

__all__ = ['SQLiteDocumentoRepository']