"""
EXTRACTOR - Apenas extrai dados do site
Não salva nada, não pergunta nada, só retorna dados.
"""

import re
from typing import Dict, List, Optional
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://leninism.su"
URL_LIVRO = "https://leninism.su/books/4135-politicheskoe-zaveshhanie-lenina-realnost-istorii-i-mify-politiki.html"


def extrair_links_capitulos() -> List[Dict]:
    """
    Extrai todos os links dos capítulos do menu lateral.
    Baseado no HTML real: os links estão em uma estrutura de "Содержание материала"
    """
    print("[EXTRACTOR] Buscando links dos capítulos...")

    response = requests.get(URL_LIVRO)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "lxml")

    # Procurar pelo título "Содержание материала"
    conteudo_titulo = soup.find(string=re.compile("Содержание материала"))
    if not conteudo_titulo:
        print("[EXTRACTOR] ERRO: Título 'Содержание материала' não encontrado")
        return []

    # Encontrar o container do menu (geralmente vem depois do título)
    menu_container = conteudo_titulo.find_next("ul", class_="nav flex-column")
    if not menu_container:
        print("[EXTRACTOR] ERRO: Menu não encontrado")
        return []

    links = []
    items = menu_container.find_all("li", class_="py-1")

    for item in items:
        link_tag = item.find("a")
        if not link_tag:
            continue

        titulo = link_tag.get_text(strip=True)
        href = link_tag.get("href")

        # Completar URL se necessário
        if href.startswith("/"):
            href = urljoin(BASE_URL, href)
        elif not href.startswith("http"):
            href = urljoin(URL_LIVRO, href)

        # Ignorar link "Все страницы" (mostrar todas)
        if "Все страницы" not in titulo:
            links.append({"titulo": titulo, "url": href})

    print(f"[EXTRACTOR] Encontrados {len(links)} capítulos")
    return links


def extrair_texto_capitulo(url: str) -> Optional[Dict]:
    """
    Extrai texto e metadados de UM capítulo específico.
    """
    print(f"[EXTRACTOR] Acessando capítulo: {url}")

    response = requests.get(url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "lxml")

    # 1. Título do capítulo (está em h2 dentro de page-header)
    titulo_tag = soup.find("div", class_="page-header")
    titulo = "Sem título"
    if titulo_tag:
        h2 = titulo_tag.find("h2")
        if h2:
            titulo = h2.get_text(strip=True)

    # 2. Autor
    autor_tag = soup.find("dd", class_="createdby")
    autor = None
    if autor_tag:
        span = autor_tag.find("span")
        if span:
            autor = span.get_text(strip=True)

    # 3. Texto principal
    corpo = soup.find("div", class_="com-content-article__body")
    if not corpo:
        print("[EXTRACTOR] ERRO: Corpo do texto não encontrado")
        return None

    # Remover navegação de páginas se existir
    pager = corpo.find("div", class_="pager")
    if pager:
        pager.decompose()

    # Extrair todos os parágrafos
    paragrafos = corpo.find_all("p")
    textos_paragrafos = []
    for p in paragrafos:
        texto = p.get_text(strip=True)
        if texto and len(texto) > 10:  # Ignorar parágrafos muito curtos
            textos_paragrafos.append(texto)

    texto = "\n\n".join(textos_paragrafos)

    # 4. Notas de rodapé (geralmente em spans com estilo específico)
    notas = corpo.find_all("span", style="font-size: x-small;")
    for nota in notas:
        nota_texto = nota.get_text(strip=True)
        if nota_texto:
            texto += f"\n\n[NOTA: {nota_texto}]"

    print(f"[EXTRACTOR] Texto extraído: {len(texto)} caracteres")

    return {"titulo": titulo, "autor": autor, "texto": texto, "url": url}


def classificar_tipo_por_titulo(titulo: str) -> tuple:
    """
    Classifica o tipo do documento baseado no título.
    Retorna (tipo, descricao_pt, descricao_en)
    """
    titulo_lower = titulo.lower()

    if "введение" in titulo_lower:
        return ("introducao", "Introdução", "Introduction")
    elif "глава" in titulo_lower:
        return ("capitulo", "Capítulo", "Chapter")
    elif "§" in titulo_lower:
        return ("paragrafo", "Parágrafo", "Paragraph")
    elif "заключени" in titulo_lower:
        return ("conclusao", "Conclusão", "Conclusion")
    elif "приложени" in titulo_lower:
        return ("anexo", "Anexo", "Appendix")
    else:
        return ("desconhecido", "Seção", "Section")


def extrair_pessoas_do_titulo(titulo: str) -> List[str]:
    """
    Extrai nomes no formato russo (Л.В. Николаева) do título.
    """
    padrao = r"([А-Я]\. ?[А-Я]\. [А-Я][а-я]+)"
    return re.findall(padrao, titulo)


# Teste rápido se executado diretamente
if __name__ == "__main__":
    print("🔍 Testando extractor...")
    links = extrair_links_capitulos()
    if links:
        print("\nPrimeiros 5 capítulos:")
        for i, link in enumerate(links[:5], 1):
            print(f"{i}. {link['titulo']}")
            print(f"   {link['url']}\n")
