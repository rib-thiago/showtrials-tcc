from db import listar_resumo, obter_documento


def listar():
    docs = listar_resumo()

    for doc in docs:
        print("-" * 80)
        print(f"ID: {doc[0]}")
        print(f"Centro: {doc[1]}")
        print(f"Título: {doc[2]}")
        print(f"URL: {doc[3]}")
        print(f"Tamanho texto: {doc[4]} chars")

    print("-" * 80)


def visualizar(doc_id):
    doc = obter_documento(doc_id)

    if not doc:
        print("Documento não encontrado.")
        return

    print("=" * 80)
    print(f"ID: {doc[0]}")
    print(f"Centro: {doc[1]}")
    print(f"Título: {doc[2]}")
    print(f"URL: {doc[3]}")
    print("-" * 80)
    print(doc[4])
    print("=" * 80)


if __name__ == "__main__":
    print("1 - Listar documentos")
    print("2 - Visualizar documento por ID")

    escolha = input("Escolha: ")

    if escolha == "1":
        listar()
    elif escolha == "2":
        doc_id = int(input("ID: "))
        visualizar(doc_id)
