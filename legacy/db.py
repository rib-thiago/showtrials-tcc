import sqlite3
from datetime import datetime
from pathlib import Path

DB_PATH = Path("data/showtrials.db")


def conectar():
    DB_PATH.parent.mkdir(exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    return conn


def criar_tabela():
    """Versão atualizada com tabela de traduções"""
    conn = conectar()
    cursor = conn.cursor()

    # Tabela de documentos (existente)
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS documentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            centro TEXT,
            titulo TEXT,
            data_original TEXT,
            url TEXT UNIQUE,
            texto TEXT,
            data_coleta TEXT
        )
    """
    )

    # NOVA: Tabela de traduções
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS traducoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            documento_id INTEGER NOT NULL,
            idioma TEXT NOT NULL,        -- 'en', 'pt', 'es', etc
            texto_traduzido TEXT NOT NULL,
            modelo TEXT,                 -- 'nmt', 'base'
            custo REAL,                 -- custo estimado em USD
            data_traducao TEXT NOT NULL,
            FOREIGN KEY (documento_id) REFERENCES documentos (id) ON DELETE CASCADE
        )
    """
    )

    # Índice para buscas rápidas
    cursor.execute(
        """
        CREATE INDEX IF NOT EXISTS idx_traducoes_documento
        ON traducoes (documento_id, idioma)
    """
    )

    conn.commit()
    conn.close()


def inserir_documento(doc):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT OR IGNORE INTO documentos
        (centro, titulo, data_original, url, texto, data_coleta)
        VALUES (?, ?, ?, ?, ?, ?)
    """,
        (
            doc["centro"],
            doc["titulo"],
            doc["data_original"],
            doc["url"],
            doc["texto"],
            doc["data_coleta"],
        ),
    )

    conn.commit()
    conn.close()


def listar_resumo(limite=20):
    conn = conectar()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT id, centro, titulo, data_original, url, LENGTH(texto)
        FROM documentos
        ORDER BY id
        LIMIT ?
    """,
        (limite,),
    )

    dados = cur.fetchall()
    conn.close()
    return dados


def listar_paginado(offset=0, limite=20, centro=None):
    conn = conectar()
    cur = conn.cursor()

    if centro:
        cur.execute(
            """
            SELECT id, centro, titulo, data_original, url, LENGTH(texto)
            FROM documentos
            WHERE centro = ?
            ORDER BY id
            LIMIT ? OFFSET ?
        """,
            (centro, limite, offset),
        )
    else:
        cur.execute(
            """
            SELECT id, centro, titulo, data_original, url, LENGTH(texto)
            FROM documentos
            ORDER BY id
            LIMIT ? OFFSET ?
        """,
            (limite, offset),
        )

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

    cur.execute(
        """
        SELECT id, centro, titulo, data_original, url, texto
        FROM documentos
        WHERE id = ?
    """,
        (doc_id,),
    )

    doc = cur.fetchone()
    conn.close()
    return doc


def atualizar_texto(doc_id, novo_texto):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE documentos
        SET texto = ?
        WHERE id = ?
    """,
        (novo_texto, doc_id),
    )

    conn.commit()
    conn.close()


# ==============================================
# NOVAS FUNÇÕES PARA TRADUÇÃO
# ==============================================

# db.py - Verifique se salvar_traducao está assim:


def salvar_traducao(
    documento_id: int, idioma: str, texto_traduzido: str, modelo: str = "nmt", custo: float = 0.0
) -> int:
    """
    Salva uma tradução no banco de dados.
    Retorna o ID da tradução inserida.
    """
    conn = conectar()
    cursor = conn.cursor()

    # Verificar se já existe tradução para este documento/idioma
    cursor.execute(
        """
        SELECT id FROM traducoes
        WHERE documento_id = ? AND idioma = ?
    """,
        (documento_id, idioma),
    )

    existente = cursor.fetchone()

    if existente:
        # Atualizar tradução existente
        cursor.execute(
            """
            UPDATE traducoes
            SET texto_traduzido = ?, modelo = ?, custo = ?, data_traducao = ?
            WHERE documento_id = ? AND idioma = ?
        """,
            (texto_traduzido, modelo, custo, datetime.utcnow().isoformat(), documento_id, idioma),
        )
        traducao_id = existente[0]
        print(f"🔄 Tradução atualizada (ID: {traducao_id}, idioma: {idioma}, custo: ${custo:.4f})")
    else:
        # Inserir nova tradução
        cursor.execute(
            """
            INSERT INTO traducoes
            (documento_id, idioma, texto_traduzido, modelo, custo, data_traducao)
            VALUES (?, ?, ?, ?, ?, ?)
        """,
            (documento_id, idioma, texto_traduzido, modelo, custo, datetime.utcnow().isoformat()),
        )
        traducao_id = cursor.lastrowid
        print(f"✅ Tradução salva (ID: {traducao_id}, idioma: {idioma}, custo: ${custo:.4f})")

    conn.commit()
    conn.close()
    return traducao_id


def obter_traducao(documento_id: int, idioma: str = "en"):
    """
    Recupera uma tradução específica para um documento.
    """
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, documento_id, idioma, texto_traduzido, modelo, custo, data_traducao
        FROM traducoes
        WHERE documento_id = ? AND idioma = ?
    """,
        (documento_id, idioma),
    )

    traducao = cursor.fetchone()
    conn.close()

    if traducao:
        return {
            "id": traducao[0],
            "documento_id": traducao[1],
            "idioma": traducao[2],
            "texto": traducao[3],
            "modelo": traducao[4],
            "custo": traducao[5],
            "data_traducao": traducao[6],
        }
    return None


def listar_traducoes_documento(documento_id: int):
    """
    Lista TODAS as traduções disponíveis para um documento.
    """
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT idioma, data_traducao, modelo, custo
        FROM traducoes
        WHERE documento_id = ?
        ORDER BY idioma
    """,
        (documento_id,),
    )

    traducoes = cursor.fetchall()
    conn.close()

    return [
        {"idioma": t[0], "data_traducao": t[1], "modelo": t[2], "custo": t[3]} for t in traducoes
    ]


def contar_traducoes(idioma: str = None):
    """
    Conta total de traduções (opcional: filtradas por idioma)
    """
    conn = conectar()
    cursor = conn.cursor()

    if idioma:
        cursor.execute("SELECT COUNT(*) FROM traducoes WHERE idioma = ?", (idioma,))
    else:
        cursor.execute("SELECT COUNT(*) FROM traducoes")

    total = cursor.fetchone()[0]
    conn.close()
    return total


def obter_documento_com_traducoes(doc_id: int):
    """
    Retorna documento com TODAS as suas traduções.
    """
    conn = conectar()
    cursor = conn.cursor()

    # Buscar documento
    cursor.execute(
        """
        SELECT id, centro, titulo, data_original, url, texto
        FROM documentos
        WHERE id = ?
    """,
        (doc_id,),
    )

    doc = cursor.fetchone()

    if not doc:
        conn.close()
        return None

    # Buscar todas as traduções deste documento
    cursor.execute(
        """
        SELECT idioma, texto_traduzido, data_traducao
        FROM traducoes
        WHERE documento_id = ?
        ORDER BY idioma
    """,
        (doc_id,),
    )

    traducoes = cursor.fetchall()
    conn.close()

    # Montar dicionário completo
    resultado = {
        "id": doc[0],
        "centro": doc[1],
        "titulo": doc[2],
        "data_original": doc[3],
        "url": doc[4],
        "texto_original": doc[5],
        "traducoes": {},
    }

    for t in traducoes:
        resultado["traducoes"][t[0]] = {"texto": t[1], "data": t[2]}

    return resultado


# db.py - Verifique se esta função está assim:


def estatisticas_completas():
    """
    Estatísticas avançadas incluindo dados de tradução.
    """
    conn = conectar()
    cursor = conn.cursor()

    stats = {
        "total_docs": 0,
        "total_traducoes": 0,
        "docs_por_centro": {},
        "traducoes_por_idioma": {},
        "docs_com_traducao": 0,
        "custo_total": 0.0,
        "tags_mais_usadas": [],  # Placeholder
    }

    # Total de documentos
    cursor.execute("SELECT COUNT(*) FROM documentos")
    stats["total_docs"] = cursor.fetchone()[0]

    # Total de traduções
    cursor.execute("SELECT COUNT(*) FROM traducoes")
    stats["total_traducoes"] = cursor.fetchone()[0]

    # Documentos por centro
    cursor.execute("SELECT centro, COUNT(*) FROM documentos GROUP BY centro")
    stats["docs_por_centro"] = dict(cursor.fetchall())

    # Traduções por idioma
    cursor.execute("SELECT idioma, COUNT(*) FROM traducoes GROUP BY idioma")
    stats["traducoes_por_idioma"] = dict(cursor.fetchall())

    # Documentos com pelo menos uma tradução
    cursor.execute(
        """
        SELECT COUNT(DISTINCT documento_id)
        FROM traducoes
    """
    )
    stats["docs_com_traducao"] = cursor.fetchone()[0] or 0

    # Custo total estimado
    cursor.execute("SELECT SUM(custo) FROM traducoes")
    stats["custo_total"] = cursor.fetchone()[0] or 0.0

    conn.close()
    return stats

    # db.py - ADICIONE ESTAS FUNÇÕES


# db.py - ADICIONE ESTA FUNÇÃO


def listar_paginado_com_filtros(offset=0, limite=20, centro=None, tipo=None):
    """
    Lista documentos com filtros opcionais de centro E tipo.
    Usada pela UI com filtros avançados.
    """
    conn = conectar()
    cursor = conn.cursor()

    query = """
        SELECT
            id, centro, titulo, data_original, url,
            LENGTH(texto) as tamanho,
            tipo_documento, pessoa_principal, remetente,
            destinatario, destinatario_orgao, envolvidos, tem_anexos
        FROM documentos
        WHERE 1=1
    """
    params = []

    if centro:
        query += " AND centro = ?"
        params.append(centro)

    if tipo:
        query += " AND tipo_documento = ?"
        params.append(tipo)

    query += " ORDER BY id LIMIT ? OFFSET ?"
    params.extend([limite, offset])

    cursor.execute(query, params)
    dados = cursor.fetchall()
    conn.close()
    return dados


# 1. Já mostrada acima: listar_paginado_com_filtros()


# 2. Contar por tipo
def contar_por_tipo(tipo_documento):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM documentos WHERE tipo_documento = ?", (tipo_documento,))
    total = cursor.fetchone()[0]
    conn.close()
    return total


# 3. Contar por centro + tipo
def contar_por_filtro(centro, tipo_documento):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT COUNT(*) FROM documentos WHERE centro = ? AND tipo_documento = ?",
        (centro, tipo_documento),
    )
    total = cursor.fetchone()[0]
    conn.close()
    return total


# 4. Listar tipos disponíveis (opcional, mas útil)
def listar_tipos_documento(centro=None):
    conn = conectar()
    cursor = conn.cursor()

    if centro:
        cursor.execute(
            """
            SELECT tipo_documento, COUNT(*)
            FROM documentos
            WHERE centro = ? AND tipo_documento IS NOT NULL
            GROUP BY tipo_documento
            ORDER BY COUNT(*) DESC
        """,
            (centro,),
        )
    else:
        cursor.execute(
            """
            SELECT tipo_documento, COUNT(*)
            FROM documentos
            WHERE tipo_documento IS NOT NULL
            GROUP BY tipo_documento
            ORDER BY COUNT(*) DESC
        """
        )

    resultados = cursor.fetchall()
    conn.close()
    return resultados
