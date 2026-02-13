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
    mostrar_status_traducao  # <--- FALTAVA ESTA LINHA!
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
    'mostrar_status_traducao'  # <--- E AQUI TAMBÉM!
]