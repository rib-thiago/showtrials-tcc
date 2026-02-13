import sqlite3
from pathlib import Path

DB_PATH = Path("data/showtrials.db")

def conectar():
    DB_PATH.parent.mkdir(exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    return conn

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS documentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            centro TEXT,
            titulo TEXT,
            data_original TEXT,
            url TEXT UNIQUE,
            texto TEXT,
            data_coleta TEXT
        )
    """)

    conn.commit()
    conn.close()


def inserir_documento(doc):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO documentos
        (centro, titulo, data_original, url, texto, data_coleta)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        doc["centro"],
        doc["titulo"],
        doc["data_original"],
        doc["url"],
        doc["texto"],
        doc["data_coleta"]
    ))

    conn.commit()
    conn.close()

def listar_resumo(limite=20):
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, centro, titulo, data_original, url, LENGTH(texto)
        FROM documentos
        ORDER BY id
        LIMIT ?
    """, (limite,))

    dados = cur.fetchall()
    conn.close()
    return dados

def listar_paginado(offset=0, limite=20, centro=None):
    conn = conectar()
    cur = conn.cursor()

    if centro:
        cur.execute("""
            SELECT id, centro, titulo, data_original, url, LENGTH(texto)
            FROM documentos
            WHERE centro = ?
            ORDER BY id
            LIMIT ? OFFSET ?
        """, (centro, limite, offset))
    else:
        cur.execute("""
            SELECT id, centro, titulo, data_original, url, LENGTH(texto)
            FROM documentos
            ORDER BY id
            LIMIT ? OFFSET ?
        """, (limite, offset))

    dados = cur.fetchall()
    conn.close()
    return dados


def contar(centro=None):
    conn = conectar()
    cur = conn.cursor()

    if centro:
        cur.execute("SELECT COUNT(*) FROM documentos WHERE centro = ?", (centro,))
    else:
        cur.execute("SELECT COUNT(*) FROM documentos")

    total = cur.fetchone()[0]
    conn.close()
    return total


def obter_documento(doc_id):
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, centro, titulo, data_original, url, texto
        FROM documentos
        WHERE id = ?
    """, (doc_id,))

    doc = cur.fetchone()
    conn.close()
    return doc



def atualizar_texto(doc_id, novo_texto):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE documentos
        SET texto = ?
        WHERE id = ?
    """, (novo_texto, doc_id))

    conn.commit()
    conn.close()
