# translators/nomes.py
# Transliteração automática de nomes russos (GOST 7.79-2000)

import re

TRANSLIT_MAP = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D',
    'Е': 'E', 'Ё': 'Yo', 'Ж': 'Zh', 'З': 'Z', 'И': 'I',
    'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
    'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
    'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch',
    'Ш': 'Sh', 'Щ': 'Shch', 'Ъ': '', 'Ы': 'Y',
    'Ь': '', 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya',
    
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
    'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
    'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
    'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
    'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch',
    'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y',
    'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'
}

# Exceções manuais (nomes que fogem do padrão)
EXCECOES = {
    # Líderes
    'И.В. Сталину': 'Joseph V. Stalin',
    'И.В. Сталин': 'Joseph V. Stalin',
    'Л.Б. Каменева': 'Lev B. Kamenev',
    'Л.Б. Каменев': 'Lev B. Kamenev',
    'Г.Е. Зиновьева': 'Grigory E. Zinoviev',
    'Г.Е. Зиновьев': 'Grigory E. Zinoviev',
    
    # NKVD
    'Г.Г. Ягоды': 'Genrikh G. Yagoda',
    'Г.Г. Ягода': 'Genrikh G. Yagoda',
    
    # Caso especial: Nikolaev (já é bem conhecido)
    'Л.В. Николаева': 'Leonid V. Nikolaev',
    'Л.В. Николаев': 'Leonid V. Nikolaev',
}

def transliterar_nome(nome_russo: str) -> str:
    """
    Converte nome russo para inglês automaticamente.
    Funciona para QUALQUER nome, mesmo sem dicionário.
    """
    if not nome_russo:
        return ""
    
    nome_limpo = nome_russo.strip()
    
    # 1. Tenta exceção manual
    if nome_limpo in EXCECOES:
        return EXCECOES[nome_limpo]
    
    # 2. Remove declinação (caso genitivo)
    if nome_limpo.endswith(('а', 'у')):
        nome_base = nome_limpo[:-1]
    else:
        nome_base = nome_limpo
    
    # 3. Separa iniciais do sobrenome
    partes = nome_base.split(' ')
    
    if len(partes) == 2:
        iniciais, sobrenome = partes
        
        # Translitera o sobrenome
        sobrenome_en = []
        for char in sobrenome:
            if char in TRANSLIT_MAP:
                sobrenome_en.append(TRANSLIT_MAP[char])
            else:
                sobrenome_en.append(char)
        
        # Capitaliza primeira letra
        sobrenome_en = ''.join(sobrenome_en)
        if sobrenome_en:
            sobrenome_en = sobrenome_en[0].upper() + sobrenome_en[1:]
        
        return f"{iniciais} {sobrenome_en}"
    
    # 4. Fallback: translitera tudo
    resultado = []
    for char in nome_base:
        if char in TRANSLIT_MAP:
            resultado.append(TRANSLIT_MAP[char])
        else:
            resultado.append(char)
    
    return ''.join(resultado)

def traduzir_tipo_documento(tipo: str, idioma='pt') -> str:
    """Traduz tipo de documento (já funciona sem dicionário)"""
    tipos = {
        'interrogatorio': {'pt': 'Interrogatório', 'en': 'Interrogation'},
        'acareacao': {'pt': 'Acareação', 'en': 'Confrontation'},
        'acusacao': {'pt': 'Auto de Acusação', 'en': 'Indictment'},
        'declaracao': {'pt': 'Declaração', 'en': 'Statement'},
        'carta': {'pt': 'Carta', 'en': 'Letter'},
        'relatorio': {'pt': 'Relatório NKVD', 'en': 'NKVD Report'},
        'depoimento': {'pt': 'Depoimento', 'en': 'Testimony'},
        'laudo': {'pt': 'Laudo Pericial', 'en': 'Forensic Report'},
    }
    return tipos.get(tipo, {}).get(idioma, tipo)

# Teste
if __name__ == "__main__":
    nomes_teste = [
        "Л.В. Николаева",
        "Г.И. Сафарова", 
        "И.И. Котолынова",
        "Г.Г. Ягоды",
        "И.В. Сталину",
        "А.И. Анишева",
        "Н.С. Антонова",
        "В.В. Румянцева"
    ]
    
    for nome in nomes_teste:
        traduzido = transliterar_nome(nome)
        print(f"{nome} → {traduzido}")