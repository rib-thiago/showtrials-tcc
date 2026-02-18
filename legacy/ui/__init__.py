# ui/__init__.py
from ui.console import badge_idioma  # <-- ADICIONAR
from ui.console import badge_tipo_documento  # <-- ADICIONAR
from ui.console import mostrar_metadados_completos  # <-- ADICIONAR
from ui.console import (
    cabecalho,
    console,
    criar_tabela_documentos,
    exibir_estatisticas,
    limpar_tela,
    mensagem_aviso,
    mensagem_erro,
    mensagem_sucesso,
    menu_navegacao,
    menu_principal,
    mostrar_documento,
    mostrar_status_traducao,
    mostrar_tabela_documentos,
    spinner_processo,
)

__all__ = [
    "console",
    "limpar_tela",
    "cabecalho",
    "mostrar_tabela_documentos",
    "mostrar_documento",
    "menu_principal",
    "menu_navegacao",
    "spinner_processo",
    "exibir_estatisticas",
    "mensagem_sucesso",
    "mensagem_erro",
    "mensagem_aviso",
    "criar_tabela_documentos",
    "mostrar_status_traducao",
    "badge_tipo_documento",  # <-- ADICIONAR
    "badge_idioma",  # <-- ADICIONAR
    "mostrar_metadados_completos",  # <-- ADICIONAR
]
