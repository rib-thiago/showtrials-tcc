# ui/__init__.py
from ui.console import (
    console,
    limpar_tela,
    cabecalho,
    mostrar_tabela_documentos,
    mostrar_documento,
    menu_principal,
    menu_navegacao,
    spinner_processo,
    exibir_estatisticas,
    mensagem_sucesso,
    mensagem_erro,
    mensagem_aviso,
    criar_tabela_documentos,
    mostrar_status_traducao,
    badge_tipo_documento,      # <-- ADICIONAR
    badge_idioma,             # <-- ADICIONAR
    mostrar_metadados_completos  # <-- ADICIONAR
)

__all__ = [
    'console',
    'limpar_tela',
    'cabecalho',
    'mostrar_tabela_documentos',
    'mostrar_documento',
    'menu_principal',
    'menu_navegacao',
    'spinner_processo',
    'exibir_estatisticas',
    'mensagem_sucesso',
    'mensagem_erro',
    'mensagem_aviso',
    'criar_tabela_documentos',
    'mostrar_status_traducao',
    'badge_tipo_documento',      # <-- ADICIONAR
    'badge_idioma',             # <-- ADICIONAR
    'mostrar_metadados_completos'  # <-- ADICIONAR
]