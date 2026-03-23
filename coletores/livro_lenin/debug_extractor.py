# debug_extractor.py
import requests
from bs4 import BeautifulSoup

URL_LIVRO = "https://leninism.su/books/4135-politicheskoe-zaveshhanie-lenina-realnost-istorii-i-mify-politiki.html"

print(f"Acessando: {URL_LIVRO}")
response = requests.get(URL_LIVRO)
response.encoding = "utf-8"
print(f"Status code: {response.status_code}")
print(f"Tamanho da página: {len(response.text)} bytes")

soup = BeautifulSoup(response.text, "lxml")

# 1. Verificar se encontrou alguma coisa
print("\n--- Título da página ---")
print(soup.title.string if soup.title else "Sem título")

# 2. Procurar por elementos que possam ser o menu
print("\n--- Procurando por 'article-index' ---")
menu = soup.find("div", class_="card float-end article-index")
if menu:
    print("✅ ENCONTOU!")
