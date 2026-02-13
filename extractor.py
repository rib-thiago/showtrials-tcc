# extractor.py
# VERSÃO 2.0 - COM CLASSIFICADOR DE DOCUMENTOS
# Autor: Thiago Ribeiro
# Data: 2024
#
# MODIFICAÇÕES:
# - Classificação automática do tipo de documento
# - Extração de pessoas (réus, remetentes, destinatários)
# - Detecção de anexos
# - Normalização de texto (HTML entities)
# - Suporte a 7 tipos de documentos históricos

import requests
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import urljoin
import re

BASE_URL = "http://showtrials.ru"

# ==============================================
# CLASSIFICADOR DE DOCUMENTOS (BASEADO EM DADOS REAIS)
# ==============================================

TIPOS_DOCUMENTO = {
    'interrogatorio': {
        'padroes': ['Протокол допроса'],
        'prioridade': 1,
        'descricao': 'Protocolo de Interrogatório'
    },
    'acareacao': {
        'padroes': ['Протокол очной ставки'],
        'prioridade': 2,
        'descricao': 'Protocolo de Acareação'
    },
    'acusacao': {
        'padroes': [
            'Проект обвинительного заключения',
            'Обвинительное заключение'
        ],
        'prioridade': 3,
        'descricao': 'Auto de Acusação'
    },
    'declaracao': {
        'padroes': ['Заявление'],
        'prioridade': 4,
        'descricao': 'Declaração/Requerimento'
    },
    'carta': {
        'padroes': ['Письмо'],
        'prioridade': 5,
        'descricao': 'Correspondência'
    },
    'relatorio': {
        'padroes': ['Спецсообщение'],
        'prioridade': 6,
        'descricao': 'Relatório Especial (NKVD)'
    },
    'depoimento': {
        'padroes': [
            'Показания',    # plural (já existe)
            'Показание'     # singular (FALTANDO!)
        ],
        'prioridade': 7,
        'descricao': 'Depoimento Espontâneo'
    },
    'laudo': {
        'padroes': ['Акт судебно-медицинского'],
        'prioridade': 8,
        'descricao': 'Laudo Pericial'
    }
}

def classificar_documento(titulo: str) -> dict:
    """
    Classifica documento e extrai metadados estruturados.
    
    Args:
        titulo: Título original em russo
        
    Returns:
        dict: {
            'tipo': 'interrogatorio',
            'tipo_descricao': 'Protocolo de Interrogatório',
            'pessoa_principal': 'Л.В. Николаева',
            'remetente': 'Г.Г. Ягода',
            'destinatario': 'И.В. Сталин',
            'envolvidos': ['Н.С. Антонов', 'И.И. Котолынов'],
            'tem_anexos': False
        }
    """
    resultado = {
        'tipo': 'desconhecido',
        'tipo_descricao': 'Não classificado',
        'pessoa_principal': None,
        'remetente': None,
        'destinatario': None,
        'envolvidos': [],
        'tem_anexos': False,
        'destinatario_orgao': None
    }
    
    if not titulo:
        return resultado
    
    # 1. QUAL O TIPO DE DOCUMENTO?
    for tipo, config in TIPOS_DOCUMENTO.items():
        for padrao in config['padroes']:
            if padrao in titulo:
                resultado['tipo'] = tipo
                resultado['tipo_descricao'] = config['descricao']
                break
        if resultado['tipo'] != 'desconhecido':
            break
    
    # 2. EXTRAIR PESSOAS (padrão: Л.В. Николаева)
    # Pega TODAS as pessoas mencionadas no título
    pessoas = re.findall(r'([А-Я]\. ?[А-Я]\. [А-Я][а-я]+)', titulo)
    
    if pessoas:
        # Primeira pessoa é a principal (réu/interrogado)
        resultado['pessoa_principal'] = pessoas[0]
        
        # Se for acareação, pega os dois envolvidos
        if resultado['tipo'] == 'acareacao' and len(pessoas) >= 2:
            resultado['envolvidos'] = pessoas
        
        # Se for carta/relatório, identifica remetente/destinatário
        elif resultado['tipo'] in ['carta', 'relatorio', 'declaracao']:
            if len(pessoas) >= 2:
                resultado['remetente'] = pessoas[0]
                resultado['destinatario'] = pessoas[1]
            elif len(pessoas) == 1:
                resultado['remetente'] = pessoas[0]
    
    # 3. DETECTAR DESTINATÁRIO INSTITUCIONAL
    orgaos = [
        'СПО Ленинградского управления НКВД',
        'ЦК ВКП\(б\)',
        'Политбюро ЦК ВКП\(б\)',
        'Следственную комиссию',
        'Административной комиссии НКВД'
    ]
    
    for orgao in orgaos:
        if re.search(orgao, titulo):
            resultado['destinatario_orgao'] = orgao.replace('\(', '(').replace('\)', ')')
            break
    
    # 4. TEM ANEXOS?
    resultado['tem_anexos'] = 'приложением' in titulo.lower()
    
    return resultado


def normalizar_texto(texto: str) -> str:
    """
    Normaliza o texto extraído do HTML.
    
    Correções:
    - HTML entities (&#39; → ')
    - Espaçamento excessivo
    - Typos conhecidos (Румянцнева → Румянцева)
    """
    if not texto:
        return texto
    
    # 1. HTML entities
    replacements = {
        '&#39;': "'",
        '&quot;': '"',
        '&amp;': '&',
        '&lt;': '<',
        '&gt;': '>',
        '&#32;': ' ',
        '&#151;': '—',
        '&#8212;': '—',
        '&#8211;': '–',
    }
    
    for entity, char in replacements.items():
        texto = texto.replace(entity, char)
    
    # 2. Typos conhecidos (baseado nos seus dados)
    typos = {
        'Румянцнева': 'Румянцева',
        # Adicione mais conforme encontrar
    }
    
    for errado, certo in typos.items():
        texto = texto.replace(errado, certo)
    
    # 3. Limpeza geral
    # Remove múltiplas quebras de linha
    texto = re.sub(r'\n\s*\n\s*\n', '\n\n', texto)
    # Remove espaços no início/fim das linhas
    texto = '\n'.join(line.strip() for line in texto.split('\n'))
    
    return texto.strip()


# ==============================================
# FUNÇÕES ORIGINAIS (MANTIDAS E MELHORADAS)
# ==============================================

def coletar_links(url_indice):
    """
    Extrai lista de links da página índice.
    Mantido original, com melhorias de robustez.
    """
    print("[+] Acessando página índice...")
    
    try:
        r = requests.get(url_indice, timeout=30)
        r.encoding = "utf-8"
        r.raise_for_status()
    except Exception as e:
        print(f"[-] Erro ao acessar {url_indice}: {e}")
        return []
    
    soup = BeautifulSoup(r.text, "lxml")
    tabela = soup.find("table")
    
    if not tabela:
        print("[-] Nenhuma tabela encontrada.")
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
    """
    Extrai e normaliza o texto do documento.
    Agora com normalização automática!
    """
    try:
        r = requests.get(url, timeout=30)
        r.encoding = "utf-8"
        r.raise_for_status()
    except Exception as e:
        print(f"[-] Erro ao acessar {url}: {e}")
        return ""
    
    soup = BeautifulSoup(r.text, "lxml")
    paragrafos = soup.find_all("p")
    
    if not paragrafos:
        # Fallback: pegar todo o texto da div principal
        content = soup.find("div", class_="content") or soup.find("main") or soup
        texto_bruto = content.get_text(separator="\n", strip=True)
    else:
        texto_bruto = "\n".join(p.get_text(strip=True) for p in paragrafos)
    
    # NORMALIZAÇÃO AUTOMÁTICA!
    texto_normalizado = normalizar_texto(texto_bruto)
    
    return texto_normalizado


def montar_documento(centro, meta, texto):
    """
    Monta o documento completo com METADADOS ENRIQUECIDOS!
    Agora inclui classificação e pessoas extraídas.
    """
    # Classificar o documento pelo título
    classificacao = classificar_documento(meta["titulo"])
    
    # Montar documento com metadados expandidos
    documento = {
        # Metadados originais (mantidos)
        "centro": centro,
        "titulo": meta["titulo"],
        "data_original": meta["data_original"],
        "url": meta["url"],
        "texto": texto,
        "data_coleta": datetime.utcnow().isoformat(),
        
        # NOVOS METADADOS ENRIQUECIDOS!
        "tipo_documento": classificacao['tipo'],
        "tipo_descricao": classificacao['tipo_descricao'],
        "pessoa_principal": classificacao['pessoa_principal'],
        "remetente": classificacao['remetente'],
        "destinatario": classificacao['destinatario'],
        "destinatario_orgao": classificacao['destinatario_orgao'],
        "envolvidos": ', '.join(classificacao['envolvidos']) if classificacao['envolvidos'] else None,
        "tem_anexos": classificacao['tem_anexos'],
        
        # Versão em inglês para compatibilidade
        "tipo_en": {
            'interrogatorio': 'Interrogation',
            'acareacao': 'Confrontation',
            'acusacao': 'Indictment',
            'declaracao': 'Statement',
            'carta': 'Letter',
            'relatorio': 'Special Report',
            'depoimento': 'Testimony',
            'laudo': 'Forensic Report',
            'desconhecido': 'Unknown'
        }.get(classificacao['tipo'], 'Unknown')
    }
    
    return documento


# ==============================================
# FUNÇÃO DE TESTE (OPCIONAL)
# ==============================================

def testar_classificador():
    """Testa o classificador com títulos reais."""
    testes = [
        "Протокол допроса Л.В. Николаева",
        "Протокол очной ставки между Н.С. Антоновым и И.И. Котолыновым",
        "Письмо В.В. Румянцева секретарю ЦК ВКП(б) И.В. Сталину",
        "Спецсообщение Г.Г. Ягоды И.В. Сталину",
        "Заявление В.И. Звездова в СПО Ленинградского управления НКВД",
        "Акт судебно-медицинского вскрытия трупа М.В. Борисова",
    ]
    
    print("\n🧪 TESTE DO CLASSIFICADOR\n")
    for titulo in testes:
        resultado = classificar_documento(titulo)
        print(f"📄 {titulo}")
        print(f"   → Tipo: {resultado['tipo_descricao']} ({resultado['tipo']})")
        if resultado['pessoa_principal']:
            print(f"   → Pessoa: {resultado['pessoa_principal']}")
        if resultado['remetente']:
            print(f"   → De: {resultado['remetente']}")
        if resultado['destinatario']:
            print(f"   → Para: {resultado['destinatario']}")
        if resultado['envolvidos']:
            print(f"   → Envolvidos: {resultado['envolvidos']}")
        print()

if __name__ == "__main__":
    testar_classificador()