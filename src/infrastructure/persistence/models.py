# src/infrastructure/persistence/models.py
"""
Modelos SQLite para mapeamento objeto-relacional.
Usamos SQLite puro (sem ORM) por simplicidade.
"""

import sqlite3
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class DocumentoModel:
    """
    Modelo de documento para o banco SQLite.
    Reflete exatamente a estrutura da tabela.
    """

    id: Optional[int]
    centro: str
    titulo: str
    data_original: Optional[str]
    url: str
    texto: str
    data_coleta: str

    # Colunas adicionadas nas migrações
    tipo_documento: Optional[str] = None
    tipo_descricao: Optional[str] = None
    pessoa_principal: Optional[str] = None
    remetente: Optional[str] = None
    destinatario: Optional[str] = None
    destinatario_orgao: Optional[str] = None
    envolvidos: Optional[str] = None
    tem_anexos: int = 0  # SQLite não tem boolean, usar 0/1
    tipo_en: Optional[str] = None

    @classmethod
    def criar_tabela(cls, cursor: sqlite3.Cursor):
        """Cria a tabela documentos se não existir."""
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS documentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                centro TEXT NOT NULL,
                titulo TEXT NOT NULL,
                data_original TEXT,
                url TEXT UNIQUE NOT NULL,
                texto TEXT NOT NULL,
                data_coleta TEXT NOT NULL
            )
        """)

    @classmethod
    def adicionar_colunas_metadados(cls, cursor: sqlite3.Cursor):
        """Adiciona colunas de metadados (migração)."""
        colunas = [
            ("tipo_documento", "TEXT"),
            ("tipo_descricao", "TEXT"),
            ("pessoa_principal", "TEXT"),
            ("remetente", "TEXT"),
            ("destinatario", "TEXT"),
            ("destinatario_orgao", "TEXT"),
            ("envolvidos", "TEXT"),
            ("tem_anexos", "INTEGER DEFAULT 0"),
            ("tipo_en", "TEXT"),
        ]

        for coluna, tipo in colunas:
            try:
                cursor.execute(f"ALTER TABLE documentos ADD COLUMN {coluna} {tipo}")
            except sqlite3.OperationalError:
                pass  # Coluna já existe

    def para_entidade(self):
        """
        Converte modelo para entidade do domínio.
        Usado ao carregar dados do banco.
        """
        from src.domain.entities.documento import Documento

        # Converter envolvidos de string para lista
        envolvidos_list = []
        if self.envolvidos:
            envolvidos_list = [e.strip() for e in self.envolvidos.split(",")]

        return Documento(
            id=self.id,
            centro=self.centro,
            titulo=self.titulo,
            data_original=self.data_original,
            url=self.url,
            texto=self.texto,
            data_coleta=datetime.fromisoformat(self.data_coleta),
            tipo=self.tipo_documento,
            tipo_descricao=self.tipo_descricao,
            pessoa_principal=self.pessoa_principal,
            remetente=self.remetente,
            destinatario=self.destinatario,
            envolvidos=envolvidos_list,
            tem_anexos=bool(self.tem_anexos),
        )

    @classmethod
    def de_entidade(cls, documento):
        """
        Converte entidade do domínio para modelo.
        Usado ao salvar dados no banco.
        """
        return cls(
            id=documento.id,
            centro=documento.centro,
            titulo=documento.titulo,
            data_original=documento.data_original,
            url=documento.url,
            texto=documento.texto,
            data_coleta=documento.data_coleta.isoformat(),
            tipo_documento=documento.tipo,
            tipo_descricao=documento.tipo_descricao,
            pessoa_principal=documento.pessoa_principal,
            remetente=documento.remetente,
            destinatario=documento.destinatario,
            envolvidos=", ".join(documento.envolvidos) if documento.envolvidos else None,
            tem_anexos=1 if documento.tem_anexos else 0,
        )


@dataclass
class TraducaoModel:
    """Modelo para tabela de traduções."""

    id: Optional[int]
    documento_id: int
    idioma: str
    texto_traduzido: str
    modelo: Optional[str]
    custo: float
    data_traducao: str

    @classmethod
    def criar_tabela(cls, cursor: sqlite3.Cursor):
        """Cria a tabela traducoes se não existir."""
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS traducoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                documento_id INTEGER NOT NULL,
                idioma TEXT NOT NULL,
                texto_traduzido TEXT NOT NULL,
                modelo TEXT,
                custo REAL,
                data_traducao TEXT NOT NULL,
                FOREIGN KEY (documento_id) REFERENCES documentos (id) ON DELETE CASCADE
            )
        """)

        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_traducoes_documento
            ON traducoes (documento_id, idioma)
        """)
