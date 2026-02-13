from pathlib import Path
from db import listar_paginado, contar, obter_documento, atualizar_texto


def menu_principal():
    while True:
        print("\n1 - Listar documentos")
        print("2 - Listar por centro")
        print("3 - Visualizar documento por ID")
        print("4 - Exportar documento")
        print("5 - Reimportar texto editado")
        print("0 - Sair")

        escolha = input("Escolha: ").strip()

        if escolha == "1":
            navegar_lista()
        elif escolha == "2":
            centro = input("Centro (ex: lencenter/moscenter): ").strip()
            navegar_lista(centro)
        elif escolha == "3":
            doc_id = int(input("ID: "))
            visualizar(doc_id)
        elif escolha == "4":
            doc_id = int(input("ID: "))
            exportar(doc_id)
        elif escolha == "5":
            doc_id = int(input("ID: "))
            caminho = input("Caminho do .txt: ")
            reimportar(doc_id, caminho)
        elif escolha == "0":
            break


def navegar_lista(centro=None):
    limite = 20
    pagina = 0
    total = contar(centro)

    if total == 0:
        print("Nenhum documento encontrado.")
        return

    while True:
        offset = pagina * limite
        docs = listar_paginado(offset=offset, limite=limite, centro=centro)

        print("\n" + "=" * 80)
        print(f"Total: {total} | Página: {pagina + 1}")
        print("-" * 80)

        for doc in docs:
            print(
                f"ID: {doc[0]} | "
                f"Data: {doc[3]} | "
                f"Centro: {doc[1]} | "
                f"Título: {doc[2][:50]} | "
                f"Tamanho: {doc[5]} chars"
            )

        print("-" * 80)
        print("[n] Próxima | [p] Anterior | [m] Menu | ID para visualizar")

        escolha = input(">>> ").strip().lower()

        if escolha == "n":
            if (pagina + 1) * limite < total:
                pagina += 1
        elif escolha == "p":
            if pagina > 0:
                pagina -= 1
        elif escolha == "m":
            break
        elif escolha.isdigit():
            visualizar(int(escolha))



def visualizar(doc_id):
    doc = obter_documento(doc_id)

    if not doc:
        print("Documento não encontrado.")
        return

    print(f"ID: {doc[0]}")
    print(f"Centro: {doc[1]}")
    print(f"Data original: {doc[3]}")
    print(f"Título: {doc[2]}")
    print(f"URL: {doc[4]}")
    print("-" * 80)
    print(doc[5])



def exportar(doc_id):
    doc = obter_documento(doc_id)

    if not doc:
        print("Documento não encontrado.")
        return

    pasta = Path("exportados")
    pasta.mkdir(exist_ok=True)

    nome_arquivo = f"{doc[0]}_{doc[2].replace(' ', '_')[:50]}.txt"
    caminho = pasta / nome_arquivo

    with open(caminho, "w", encoding="utf-8") as f:
        f.write(f"Título: {doc[2]}\n")
        f.write(f"Centro: {doc[1]}\n")
        f.write(f"URL: {doc[3]}\n")
        f.write("-" * 80 + "\n\n")
        f.write(doc[4])

    print(f"Exportado para: {caminho}")

def reimportar(doc_id, caminho_txt):
    caminho = Path(caminho_txt)

    if not caminho.exists():
        print("Arquivo não encontrado.")
        return

    with open(caminho, "r", encoding="utf-8") as f:
        conteudo = f.read()

    # remove cabeçalho (até linha separadora)
    if "--------" in conteudo:
        conteudo = conteudo.split("--------", 1)[1].strip()

    atualizar_texto(doc_id, conteudo)
    print("Texto atualizado no banco.")




if __name__ == "__main__":
    menu_principal()
