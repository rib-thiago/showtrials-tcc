import time

from db import criar_tabela, inserir_documento
from extractor import coletar_links, extrair_texto, montar_documento

LENCENTER = "http://showtrials.ru/glavnaya/lencenter/lencenter-materials/"
MOSCENTER = "http://showtrials.ru/glavnaya/moscow-center-trial/materialy-sledstviya-1935/"


def main():
    criar_tabela()

    print("1 - Leningrad Center")
    print("2 - Moscow Center")

    escolha = input("Escolha: ")

    if escolha == "1":
        url = LENCENTER
        centro = "lencenter"
    elif escolha == "2":
        url = MOSCENTER
        centro = "moscenter"
    else:
        print("Opção inválida.")
        return

    links = coletar_links(url)

    for i, meta in enumerate(links, 1):
        print(f"[{i}/{len(links)}] Coletando {meta['titulo']}")

        texto = extrair_texto(meta["url"])

        if texto:
            doc = montar_documento(centro, meta, texto)
            inserir_documento(doc)

        time.sleep(1)

    print("[✓] Coleta finalizada.")


if __name__ == "__main__":
    main()
