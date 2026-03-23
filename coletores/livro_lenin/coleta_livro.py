"""
COLETA - Orquestra a coleta e salva no banco de dados
Pergunta, coordena, salva e dá feedback pro usuário.
"""

import sqlite3
import sys
from pathlib import Path
from typing import Dict  # ← ADICIONE ESTA LINHA

# Adicionar projeto ao path para importar configurações
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

# Importar o extractor (nosso funcionário)
from coletores.livro_lenin import extractor_livro
from src.infrastructure.config.settings import settings


def testar_conexao_com_site():
    """TESTE 1: Verificar se consegue acessar o site e extrair links."""
    print("\n🔍 TESTE 1: Coletando links do site...")
    links = extractor_livro.extrair_links_capitulos()

    if not links:
        print("❌ FALHA: Nenhum link encontrado")
        return False

    print(f"✅ SUCESSO: {len(links)} links encontrados")
    print("\nPrimeiros 3 links:")
    for i, link in enumerate(links[:3], 1):
        print(f"  {i}. {link['titulo'][:50]}...")

    return links


def testar_primeiro_capitulo(links):
    """TESTE 2: Verificar se consegue extrair texto do primeiro capítulo."""
    if not links:
        return False

    print("\n🔍 TESTE 2: Testando extração do primeiro capítulo...")
    primeiro = links[0]
    texto_info = extractor_livro.extrair_texto_capitulo(primeiro["url"])

    if not texto_info or not texto_info["texto"]:
        print("❌ FALHA: Não conseguiu extrair texto")
        return False

    print("✅ SUCESSO!")
    print(f"  Título: {texto_info['titulo'][:50]}...")
    print(f"  Autor: {texto_info['autor']}")
    print(f"  Tamanho do texto: {len(texto_info['texto'])} caracteres")
    print(f"  Primeiros 100 caracteres: {texto_info['texto'][:100]}...")

    return True


def inserir_documento_no_banco(doc):
    """Salva um documento no banco de dados."""
    conn = sqlite3.connect(str(settings.DB_PATH))
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT OR IGNORE INTO documentos (
                centro, titulo, data_original, url, texto, data_coleta,
                tipo_documento, tipo_descricao, pessoa_principal, remetente,
                destinatario, envolvidos, tem_anexos, tipo_en
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                doc["centro"],
                doc["titulo"],
                doc["data_original"],
                doc["url"],
                doc["texto"],
                doc["data_coleta"],
                doc["tipo_documento"],
                doc["tipo_descricao"],
                doc["pessoa_principal"],
                doc["remetente"],
                doc["destinatario"],
                doc["envolvidos"],
                doc["tem_anexos"],
                doc["tipo_en"],
            ),
        )

        conn.commit()
        return cursor.lastrowid if cursor.rowcount > 0 else None
    except Exception as e:
        print(f"    ERRO no banco: {e}")
        conn.rollback()
        return None
    finally:
        conn.close()


def montar_documento(centro: str, capitulo: Dict, texto_info: Dict) -> Dict:
    """
    Monta o dicionário no formato que o banco espera.
    """
    titulo = texto_info["titulo"]
    tipo, desc_pt, desc_en = extractor_livro.classificar_tipo_por_titulo(titulo)
    pessoas = extractor_livro.extrair_pessoas_do_titulo(titulo)

    from datetime import datetime

    return {
        "centro": centro,
        "titulo": f"{titulo} - {texto_info['autor']}" if texto_info["autor"] else titulo,
        "data_original": None,
        "url": texto_info["url"],
        "texto": texto_info["texto"],
        "data_coleta": datetime.now().isoformat(),
        "tipo_documento": tipo,
        "tipo_descricao": desc_pt,
        "tipo_en": desc_en,
        "pessoa_principal": pessoas[0] if pessoas else None,
        "remetente": texto_info["autor"],
        "destinatario": None,
        "envolvidos": ", ".join(pessoas) if pessoas else None,
        "tem_anexos": 1 if "приложени" in titulo.lower() else 0,
    }


def main():
    """Fluxo principal da coleta."""
    print("=" * 60)
    print("📚 COLETOR DE LIVRO - Leninism.su")
    print("=" * 60)

    # PASSO 1: Testes rápidos para garantir que tudo funciona
    links = testar_conexao_com_site()
    if not links:
        print("\n❌ Abortando: não foi possível conectar ao site")
        return

    if not testar_primeiro_capitulo(links):
        print("\n❌ Abortando: não foi possível extrair texto")
        return

    # PASSO 2: Perguntar configurações
    print("\n" + "=" * 60)
    print("⚙️  CONFIGURAÇÃO")
    print("Em qual centro estes documentos devem ser classificados?")
    print("  1 - Leningrad Center (lencenter)")
    print("  2 - Moscow Center (moscenter)")
    print("  3 - Outro (usar lencenter como padrão)")

    escolha = input("\nEscolha (1/2/3): ").strip()
    if escolha == "1":
        centro = "lencenter"
    elif escolha == "2":
        centro = "moscenter"
    else:
        centro = "lencenter"
        print("Usando 'lencenter' como padrão")

    # PASSO 3: Confirmar início da coleta
    print(f"\n📊 Serão coletados {len(links)} capítulos")
    print(f"📁 Centro: {centro}")
    confirmar = input("\nIniciar coleta? (s/N): ").strip().lower()

    if confirmar != "s":
        print("Coleta cancelada.")
        return

    # PASSO 4: COLETA REAL
    print("\n" + "=" * 60)
    print("🚀 INICIANDO COLETA...")
    print("=" * 60)

    sucessos = 0
    falhas = 0

    for i, cap in enumerate(links, 1):
        print(f"\n[{i}/{len(links)}] {cap['titulo'][:70]}...")

        # Extrair texto
        texto_info = extractor_livro.extrair_texto_capitulo(cap["url"])

        if texto_info and texto_info["texto"]:
            # Montar documento
            doc = montar_documento(centro, cap, texto_info)

            # Salvar no banco
            doc_id = inserir_documento_no_banco(doc)

            if doc_id:
                print(f"  ✅ Salvo no banco (ID: {doc_id})")
                sucessos += 1
            else:
                print("  ⚠ URL já existente no banco (ignorado)")
                falhas += 1
        else:
            print("  ❌ Falha ao extrair texto")
            falhas += 1

    # PASSO 5: RESUMO FINAL
    print("\n" + "=" * 60)
    print("📊 RESUMO DA COLETA")
    print("=" * 60)
    print(f"Total de capítulos: {len(links)}")
    print(f"✅ Inseridos com sucesso: {sucessos}")
    print(f"⚠ Já existiam (ignorados): {falhas}")
    print("=" * 60)


if __name__ == "__main__":
    main()
