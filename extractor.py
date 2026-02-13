import requests
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import urljoin

BASE_URL = "http://showtrials.ru"

def coletar_links(url_indice):
    print("[+] Acessando página índice...")
    r = requests.get(url_indice)
    r.encoding = "utf-8"

    soup = BeautifulSoup(r.text, "lxml")

    tabela = soup.find("table")
    if not tabela:
        print("Nenhuma tabela encontrada.")
        return []

    links = []

    for row in tabela.find_all("tr"):
        colunas = row.find_all("td")
        if len(colunas) >= 2:
            data_raw = colunas[0].get_text(strip=True)
            link_tag = colunas[1].find("a")

            if link_tag:
                titulo = link_tag.get_text(strip=True)
                href = link_tag.get("href")
                href = urljoin(BASE_URL, href)

                links.append({
                    "titulo": titulo,
                    "url": href,
                    "data_original": data_raw
                })

    print(f"[+] {len(links)} links extraídos.")
    return links


def extrair_texto(url):
    r = requests.get(url)
    r.encoding = "utf-8"

    soup = BeautifulSoup(r.text, "lxml")

    paragrafos = soup.find_all("p")
    texto = "\n".join(p.get_text(strip=True) for p in paragrafos)

    return texto.strip()


def montar_documento(centro, meta, texto):
    return {
        "centro": centro,
        "titulo": meta["titulo"],
        "data_original": meta["data_original"],
        "url": meta["url"],
        "texto": texto,
        "data_coleta": datetime.utcnow().isoformat()
    }
