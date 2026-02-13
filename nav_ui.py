# nav_ui.py
from pathlib import Path
from db import listar_paginado, contar, obter_documento, atualizar_texto
from ui import (
    console, limpar_tela, cabecalho, mostrar_tabela_documentos,
    mostrar_documento, menu_navegacao, mensagem_sucesso, mensagem_erro,
    spinner_processo
)
from rich.prompt import IntPrompt, Prompt
import time

def navegar_lista(centro=None):
    """Navegação paginada com UI melhorada"""
    limite = 20
    pagina = 0
    total = contar(centro)
    
    if total == 0:
        console.print("[yellow]⚠ Nenhum documento encontrado.[/yellow]")
        time.sleep(1.5)
        return
    
    while True:
        limpar_tela()
        titulo = f"📋 Documentos - {centro.upper() if centro else 'Todos os centros'}"
        cabecalho(titulo)
        
        offset = pagina * limite
        docs = listar_paginado(offset=offset, limite=limite, centro=centro)
        
        mostrar_tabela_documentos(docs, total, pagina + 1, limite)
        
        escolha = menu_navegacao()
        
        if escolha == 'n':
            if (pagina + 1) * limite < total:
                pagina += 1
            else:
                mensagem_erro("Você já está na última página!")
                time.sleep(1)
        
        elif escolha == 'p':
            if pagina > 0:
                pagina -= 1
            else:
                mensagem_erro("Você já está na primeira página!")
                time.sleep(1)
        
        elif escolha == 'm':
            break
        
        elif escolha.isdigit():
            visualizar_documento_ui(int(escolha))
        
        else:
            mensagem_erro("Comando inválido!")
            time.sleep(1)

def visualizar_documento_ui(doc_id):
    """Visualização de documento com UI"""
    doc = spinner_processo(
        "Carregando documento...",
        obter_documento,
        doc_id
    )
    
    if not doc:
        mensagem_erro("Documento não encontrado!")
        time.sleep(1.5)
        return
    
    mostrar_documento(doc)
    
    # Aguardar comando
    cmd = input().strip().lower()
    
    if cmd == 'e':
        exportar_documento_ui(doc_id)
    elif cmd == 't':
        mensagem_aviso("Funcionalidade de tradução em desenvolvimento")
        time.sleep(1.5)

def exportar_documento_ui(doc_id):
    """Exporta documento com feedback visual"""
    doc = obter_documento(doc_id)
    
    if not doc:
        mensagem_erro("Documento não encontrado!")
        return
    
    pasta = Path("exportados")
    pasta.mkdir(exist_ok=True)
    
    # Sanitizar nome do arquivo
    titulo = "".join(c for c in doc[2] if c.isalnum() or c in (' ', '-', '_')).rstrip()
    nome_arquivo = f"{doc[0]}_{titulo[:50]}.txt"
    caminho = pasta / nome_arquivo
    
    try:
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(f"Título: {doc[2]}\n")
            f.write(f"Centro: {doc[1]}\n")
            f.write(f"Data original: {doc[3]}\n")
            f.write(f"URL: {doc[4]}\n")
            f.write(f"Exportado em: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 80 + "\n\n")
            f.write(doc[5])
        
        mensagem_sucesso(f"Documento exportado para: {caminho}")
    except Exception as e:
        mensagem_erro(f"Erro ao exportar: {e}")
    
    time.sleep(1.5)

def reimportar_documento_ui():
    """Reimporta texto editado com UI"""
    try:
        doc_id = IntPrompt.ask("[cyan]ID do documento[/cyan]")
        caminho = Prompt.ask("[cyan]Caminho do arquivo .txt[/cyan]")
        
        caminho_path = Path(caminho)
        
        if not caminho_path.exists():
            mensagem_erro("Arquivo não encontrado!")
            return
        
        with open(caminho_path, "r", encoding="utf-8") as f:
            conteudo = f.read()
        
        # Remove cabeçalho
        if "========" in conteudo:
            conteudo = conteudo.split("========", 1)[1].strip()
        
        atualizar_texto(doc_id, conteudo)
        mensagem_sucesso("Texto atualizado no banco de dados!")
    except Exception as e:
        mensagem_erro(f"Erro ao reimportar: {e}")
    
    time.sleep(1.5)