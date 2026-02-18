# src/infrastructure/persistence/sqlite_traducao_repository.py
"""
Implementação SQLite do repositório de traduções.
"""

import sqlite3
from contextlib import contextmanager
from datetime import datetime
from typing import List, Optional

from src.domain.entities.traducao import Traducao
from src.domain.interfaces.repositorio_traducao import RepositorioTraducao
from src.infrastructure.config.settings import settings


class SQLiteTraducaoRepository(RepositorioTraducao):
    """Repositório SQLite para traduções."""

    def __init__(self, db_path: Optional[str] = None):
        self.db_path = db_path or str(settings.DB_PATH)

    @contextmanager
    def _conexao(self):
        """Gerenciador de contexto para conexões."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

    def _row_para_entidade(self, row: sqlite3.Row) -> Traducao:
        """Converte linha do banco para entidade."""
        return Traducao(
            id=row["id"],
            documento_id=row["documento_id"],
            idioma=row["idioma"],
            texto_traduzido=row["texto_traduzido"],
            modelo=row["modelo"],
            custo=row["custo"],
            data_traducao=datetime.fromisoformat(row["data_traducao"]),
        )

    def salvar(self, traducao: Traducao) -> int:
        """Salva uma tradução."""
        with self._conexao() as conn:
            cursor = conn.cursor()

            if traducao.id:
                # Update
                cursor.execute(
                    """
                    UPDATE traducoes SET
                        idioma = ?,
                        texto_traduzido = ?,
                        modelo = ?,
                        custo = ?,
                        data_traducao = ?
                    WHERE id = ?
                """,
                    (
                        traducao.idioma,
                        traducao.texto_traduzido,
                        traducao.modelo,
                        traducao.custo,
                        traducao.data_traducao.isoformat(),
                        traducao.id,
                    ),
                )
                return traducao.id
            else:
                # Insert
                cursor.execute(
                    """
                    INSERT INTO traducoes
                    (documento_id, idioma, texto_traduzido, modelo, custo, data_traducao)
                    VALUES (?, ?, ?, ?, ?, ?)
                """,
                    (
                        traducao.documento_id,
                        traducao.idioma,
                        traducao.texto_traduzido,
                        traducao.modelo,
                        traducao.custo,
                        traducao.data_traducao.isoformat(),
                    ),
                )
                return cursor.lastrowid

    def buscar_por_id(self, id: int) -> Optional[Traducao]:
        """Busca tradução por ID."""
        with self._conexao() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM traducoes WHERE id = ?", (id,))
            row = cursor.fetchone()
            return self._row_para_entidade(row) if row else None

    def buscar_por_documento(self, documento_id: int, idioma: str) -> Optional[Traducao]:
        """Busca tradução específica de um documento."""
        with self._conexao() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT * FROM traducoes
                WHERE documento_id = ? AND idioma = ?
            """,
                (documento_id, idioma),
            )
            row = cursor.fetchone()
            return self._row_para_entidade(row) if row else None

    def listar_por_documento(self, documento_id: int) -> List[Traducao]:
        """Lista todas as traduções de um documento."""
        with self._conexao() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT * FROM traducoes
                WHERE documento_id = ?
                ORDER BY idioma
            """,
                (documento_id,),
            )
            return [self._row_para_entidade(row) for row in cursor.fetchall()]

    def contar_por_documento(self, documento_id: int) -> int:
        """Conta traduções de um documento."""
        with self._conexao() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT COUNT(*) FROM traducoes
                WHERE documento_id = ?
            """,
                (documento_id,),
            )
            return cursor.fetchone()[0]
