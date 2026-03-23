#!/usr/bin/env python3
# reprocessar_metadados.py - VERSÃO CORRIGIDA
#
# ⚡ REPROCESSAMENTO COMPLETO DE METADADOS ⚡

import sqlite3
import sys
from datetime import datetime
from pathlib import Path

# Importar o classificador do seu extractor
try:
    from extractor import classificar_documento
except ImportError:
    print("❌ Erro: Não foi possível importar classificar_documento do extractor.py")
    print("   Certifique-se de que você já atualizou o extractor.py")
    sys.exit(1)

DB_PATH = Path("data/showtrials.db")


def conectar():
    """Conecta ao banco de dados"""
    return sqlite3.connect(DB_PATH)


def criar_colunas_metadados():
    """Cria as colunas de metadados se não existirem"""
    conn = conectar()
    cursor = conn.cursor()

    print("📦 Criando colunas de metadados...")

    colunas = [
        ("tipo_documento", "TEXT"),
        ("tipo_descricao", "TEXT"),
        ("pessoa_principal", "TEXT"),
        ("remetente", "TEXT"),
        ("destinatario", "TEXT"),
        ("destinatario_orgao", "TEXT"),
        ("envolvidos", "TEXT"),
        ("tem_anexos", "BOOLEAN"),
        ("tipo_en", "TEXT"),
    ]

    colunas_criadas = 0

    for coluna, tipo in colunas:
        try:
            cursor.execute(f"ALTER TABLE documentos ADD COLUMN {coluna} {tipo}")
            print(f"  ✅ {coluna}")
            colunas_criadas += 1
        except sqlite3.OperationalError as e:
            if "duplicate column name" in str(e):
                print(f"  ⏩ {coluna} (já existe)")
            else:
                print(f"  ⚠️  Erro ao criar {coluna}: {e}")

    conn.commit()
    conn.close()

    if colunas_criadas > 0:
        print(f"\n✅ {colunas_criadas} colunas criadas com sucesso!")
    else:
        print("\n✅ Todas as colunas já existem.")

    return colunas_criadas


def contar_documentos():
    """Conta total de documentos no banco"""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM documentos")
    total = cursor.fetchone()[0]
    conn.close()
    return total


def buscar_todos_documentos():
    """Busca TODOS os documentos do banco"""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, titulo FROM documentos ORDER BY id")
    resultados = cursor.fetchall()
    conn.close()
    return resultados


def atualizar_metadados_documento(doc_id, titulo, metadados):
    """Atualiza os metadados de um documento específico"""
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE documentos SET
            tipo_documento = ?,
            tipo_descricao = ?,
            pessoa_principal = ?,
            remetente = ?,
            destinatario = ?,
            destinatario_orgao = ?,
            envolvidos = ?,
            tem_anexos = ?,
            tipo_en = ?
        WHERE id = ?
    """,
        (
            metadados["tipo"],
            metadados["tipo_descricao"],
            metadados["pessoa_principal"],
            metadados["remetente"],
            metadados["destinatario"],
            metadados["destinatario_orgao"],
            ", ".join(metadados["envolvidos"]) if metadados["envolvidos"] else None,
            metadados["tem_anexos"],
            {
                "interrogatorio": "Interrogation",
                "acareacao": "Confrontation",
                "acusacao": "Indictment",
                "declaracao": "Statement",
                "carta": "Letter",
                "relatorio": "Special Report",
                "depoimento": "Testimony",
                "laudo": "Forensic Report",
                "desconhecido": "Unknown",
            }.get(metadados["tipo"], "Unknown"),
            doc_id,
        ),
    )

    conn.commit()
    conn.close()


def gerar_estatisticas():
    """Gera estatísticas completas dos documentos"""
    conn = conectar()
    cursor = conn.cursor()

    print("\n" + "=" * 60)
    print("📊 ESTATÍSTICAS DO ACERVO")
    print("=" * 60)

    # Verifica se as colunas existem
    cursor.execute("PRAGMA table_info(documentos)")
    colunas = [c[1] for c in cursor.fetchall()]

    # 1. Total de documentos
    cursor.execute("SELECT COUNT(*) FROM documentos")
    total_docs = cursor.fetchone()[0]
    print(f"\n📚 Total de documentos: {total_docs}")

    # 2. Documentos por centro
    if "centro" in colunas:
        cursor.execute("SELECT centro, COUNT(*) FROM documentos GROUP BY centro")
        centros = cursor.fetchall()
        if centros:
            print("\n🏛️  DOCUMENTOS POR CENTRO:")
            for centro, total in centros:
                nome = (
                    "Leningrad"
                    if centro == "lencenter"
                    else "Moscow" if centro == "moscenter" else centro
                )
                print(f"  • {nome}: {total}")

    # 3. Distribuição por tipo de documento
    if "tipo_descricao" in colunas:
        cursor.execute(
            """
            SELECT
                COALESCE(tipo_descricao, 'Não classificado') as tipo,
                COUNT(*) as total
            FROM documentos
            GROUP BY tipo_descricao
            ORDER BY total DESC
        """
        )
        tipos = cursor.fetchall()
        if tipos and tipos[0][0]:
            print("\n📋 DISTRIBUIÇÃO POR TIPO:")
            for tipo, total in tipos:
                if tipo:
                    print(f"  • {tipo}: {total}")

    # 4. Pessoas mais frequentes
    if "pessoa_principal" in colunas:
        cursor.execute(
            """
            SELECT pessoa_principal, COUNT(*) as total
            FROM documentos
            WHERE pessoa_principal IS NOT NULL AND pessoa_principal != ''
            GROUP BY pessoa_principal
            ORDER BY total DESC
            LIMIT 10
        """
        )
        pessoas = cursor.fetchall()
        if pessoas:
            print("\n👤 PESSOAS MAIS FREQUENTES:")
            for pessoa, total in pessoas:
                print(f"  • {pessoa}: {total}")

    # 5. Correspondências
    if "tipo_documento" in colunas:
        cursor.execute(
            """
            SELECT
                SUM(CASE WHEN tipo_documento = 'carta' THEN 1 ELSE 0 END) as cartas,
                SUM(CASE WHEN tipo_documento = 'declaracao' THEN 1 ELSE 0 END) as declaracoes,
                SUM(CASE WHEN tipo_documento = 'relatorio' THEN 1 ELSE 0 END) as relatorios,
                SUM(CASE WHEN tipo_documento = 'acareacao' THEN 1 ELSE 0 END) as acareacoes
            FROM documentos
        """
        )
        carta_stats = cursor.fetchone()
        if carta_stats and any(carta_stats):
            print("\n✉️  CORRESPONDÊNCIAS E ATOS:")
            if carta_stats[0]:
                print(f"  • Cartas: {carta_stats[0]}")
            if carta_stats[1]:
                print(f"  • Declarações: {carta_stats[1]}")
            if carta_stats[2]:
                print(f"  • Relatórios: {carta_stats[2]}")
            if carta_stats[3]:
                print(f"  • Acareações: {carta_stats[3]}")

    # 6. Documentos com anexos
    if "tem_anexos" in colunas:
        cursor.execute("SELECT COUNT(*) FROM documentos WHERE tem_anexos = 1")
        total_anexos = cursor.fetchone()[0]
        if total_anexos > 0:
            print(f"\n📎 Documentos com anexos: {total_anexos}")

    conn.close()
    print("\n" + "=" * 60)


def reprocessar_todos(limite=None):
    """Função principal de reprocessamento"""

    print("=" * 60)
    print("⚡ REPROCESSAMENTO DE METADADOS ⚡")
    print("=" * 60)

    # 1. CRIAR AS COLUNAS (FORÇAR CRIAÇÃO)
    print("\n📦 VERIFICANDO COLUNAS...")
    criar_colunas_metadados()

    # 2. Total de documentos
    total_docs = contar_documentos()
    print(f"\n📚 Total de documentos no banco: {total_docs}")

    # 3. Buscar TODOS os documentos
    todos_docs = buscar_todos_documentos()
    if limite:
        todos_docs = todos_docs[:limite]

    print(f"\n🔄 Processando {len(todos_docs)} documentos...")
    print("-" * 60)

    # 4. Processar cada documento
    processados = 0
    erros = 0

    for i, (doc_id, titulo) in enumerate(todos_docs, 1):
        try:
            # Classificar o documento
            metadados = classificar_documento(titulo)

            # Atualizar no banco
            atualizar_metadados_documento(doc_id, titulo, metadados)

            # Feedback visual
            tipo_icone = {
                "interrogatorio": "🔍",
                "acareacao": "⚖️",
                "acusacao": "📜",
                "declaracao": "📝",
                "carta": "✉️",
                "relatorio": "📋",
                "depoimento": "🗣️",
                "laudo": "🏥",
                "desconhecido": "📄",
            }.get(metadados["tipo"], "📄")

            pessoa = metadados.get("pessoa_principal", "")
            if not pessoa and metadados.get("remetente"):
                pessoa = f"{metadados['remetente']} → {metadados['destinatario'] or '?'}"

            print(
                f"  [{i:3d}] {tipo_icone} ID {doc_id:3d}: {metadados['tipo_descricao']:25} - {pessoa[:30]}"
            )
            processados += 1

        except Exception as e:
            print(f"  [{'ERRO':>3}] ID {doc_id}: {str(e)[:50]}")
            erros += 1

    # 5. Resumo final
    print("-" * 60)
    print("\n✅ Processamento concluído!")
    print(f"  📊 Documentos processados: {processados}")
    if erros:
        print(f"  ⚠️  Erros: {erros}")
    print(f"  ⏱️  {datetime.now().strftime('%H:%M:%S')}")

    # 6. Estatísticas
    gerar_estatisticas()


def main():
    """Interface interativa"""

    print(
        """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║     🔄 REPROCESSADOR DE METADADOS - SHOW TRIALS             ║
║                                                              ║
║     Este script vai classificar TODOS os seus documentos    ║
║     e enriquecer o banco com metadados extraídos dos        ║
║     títulos (tipo, pessoas, destinatários, etc).           ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """
    )

    total = contar_documentos()

    print(f"📊 Documentos no banco: {total}")
    print()
    print("Opções:")
    print("  1 - Processar TODOS os documentos (recomendado)")
    print("  2 - Processar apenas 10 (teste rápido)")
    print("  3 - Processar apenas 50")
    print("  4 - Sair")
    print()

    opcao = input("Escolha (1-4): ").strip()

    if opcao == "1":
        reprocessar_todos()
    elif opcao == "2":
        reprocessar_todos(limite=10)
    elif opcao == "3":
        reprocessar_todos(limite=50)
    else:
        print("👋 Operação cancelada.")


if __name__ == "__main__":
    main()
