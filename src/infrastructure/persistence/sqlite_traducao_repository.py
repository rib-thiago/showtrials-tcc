# src/infrastructure/persistence/sqlite_traducao_repository.py
"""
Implementação SQLite do repositório de traduções com telemetria.
"""

import sqlite3
from contextlib import contextmanager
from datetime import datetime
from typing import List, Optional

from src.domain.entities.traducao import Traducao
from src.domain.interfaces.repositorio_traducao import RepositorioTraducao
from src.infrastructure.config.settings import settings

# Telemetria opcional
_telemetry = None


def configure_telemetry(telemetry_instance=None):
    """Configura telemetria para este módulo (usado apenas em testes)."""
    global _telemetry
    _telemetry = telemetry_instance


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
        except Exception as e:
            if _telemetry:
                _telemetry.increment("sqlite_traducao.erro_conexao")
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
                if _telemetry:
                    _telemetry.increment("sqlite_traducao.atualizacao")
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
                if _telemetry:
                    _telemetry.increment("sqlite_traducao.insercao")
                return cursor.lastrowid

    def buscar_por_id(self, id: int) -> Optional[Traducao]:
        """Busca tradução por ID."""
        with self._conexao() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM traducoes WHERE id = ?", (id,))
            row = cursor.fetchone()
            if _telemetry:
                _telemetry.increment("sqlite_traducao.busca_por_id")
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
            if _telemetry:
                _telemetry.increment("sqlite_traducao.busca_por_documento")
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
            resultados = cursor.fetchall()
            if _telemetry:
                _telemetry.increment("sqlite_traducao.listagem", value=len(resultados))
            return [self._row_para_entidade(row) for row in resultados]

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
            count = cursor.fetchone()[0]
            if _telemetry:
                _telemetry.increment("sqlite_traducao.contagem")
            return count
