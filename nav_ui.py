# nav_ui.py
from pathlib import Path
from db import listar_paginado, contar, obter_documento, atualizar_texto
from db import obter_traducao, listar_traducoes_documento
from ui import (
    console, limpar_tela, cabecalho, mostrar_tabela_documentos,
    mostrar_documento, menu_navegacao, mensagem_sucesso, mensagem_erro,
    mensagem_aviso, spinner_processo, mostrar_status_traducao
)
from rich.prompt import IntPrompt, Prompt
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
import time

# nav_ui.py - Substitua a função navegar_lista INTEIRA por esta:

def navegar_lista(centro=None):
    """Navegação paginada com status de tradução"""
    limite = 10  # Reduzido de 20 para 10
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
        
        # Verificar se há traduções para mostrar status
        tem_traducao = False
        for doc in docs[:5]:
            if listar_traducoes_documento(doc[0]):
                tem_traducao = True
                break
        
        # CRIAR TABELA MANUALMENTE (em vez de usar a função existente)
        from rich.table import Table
        from rich import box
        
        table = Table(
            title=f"[bold]📚 ACERVO DE DOCUMENTOS[/bold]\n[dim]Total: {total} documentos | Página {pagina + 1}[/dim]",
            box=box.ROUNDED,
            header_style="bold cyan",
            border_style="bright_blue",
            padding=(0, 1)
        )
        
        # Colunas fixas
        table.add_column("ID", style="dim white", width=6, justify="right")
        table.add_column("🏛️ Centro", style="yellow", width=12)
        table.add_column("📅 Data", style="green", width=12)
        table.add_column("📄 Título", style="white", width=50)
        table.add_column("📊 Tamanho", style="blue", width=10, justify="right")
        
        # Coluna de status APENAS se houver traduções
        if tem_traducao:
            table.add_column("🌐 Traduções", style="bold green", width=15)
        
        # Adicionar linhas
        for doc in docs:
            # Formatar título
            titulo_doc = doc[2][:47] + "…" if len(doc[2]) > 48 else doc[2]
            
            # Formatar tamanho
            tamanho = int(doc[5])
            if tamanho < 1000:
                tamanho_str = f"{tamanho}c"
            elif tamanho < 1000000:
                tamanho_str = f"{tamanho/1000:.1f}K"
            else:
                tamanho_str = f"{tamanho/1000000:.1f}M"
            
            # Centro em maiúsculo
            centro_doc = doc[1].upper() if doc[1] else "N/A"
            
            # Montar linha
            linha = [
                str(doc[0]),
                centro_doc,
                doc[3] or "N/D",
                titulo_doc,
                tamanho_str
            ]
            
            # Adicionar status de tradução se houver coluna
            if tem_traducao:
                status = mostrar_status_traducao(doc[0])
                linha.append(status)
            
            table.add_row(*linha)
        
        console.print(table)
        
        # Barra de navegação
        total_paginas = (total + limite - 1) // limite
        nav_bar = Panel(
            f"[bold cyan]📌 Página {pagina + 1} de {total_paginas} • Total: {total} documentos[/bold cyan]\n"
            f"[dim]Comandos: [n] Próxima | [p] Anterior | [número] Ver documento | [m] Menu[/dim]",
            border_style="bright_blue",
            padding=(1, 2)
        )
        console.print(nav_bar)
        
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

# nav_ui.py - Substitua a função visualizar_documento_ui INTEIRA por esta:

def visualizar_documento_ui(doc_id):
    """Visualização de documento com ABAS de tradução"""
    doc = spinner_processo(
        "Carregando documento...",
        obter_documento,
        doc_id
    )
    
    if not doc:
        mensagem_erro("Documento não encontrado!")
        time.sleep(1.5)
        return
    
    # Buscar traduções disponíveis
    traducoes = listar_traducoes_documento(doc_id)
    
    # Inicializar idioma atual se não existir
    if not hasattr(visualizar_documento_ui, 'idioma_atual'):
        visualizar_documento_ui.idioma_atual = 'original'
    
    while True:  # Loop para alternar entre original/traduções
        limpar_tela()
        
        # Cabeçalho
        titulo_texto = Text()
        titulo_texto.append("📄 ", style="bold white")
        titulo_texto.append(doc[2], style="bold yellow")
        
        # Badge de idioma atual
        idioma_atual = visualizar_documento_ui.idioma_atual
        if idioma_atual == 'original':
            badge = "[bold blue]📄 ORIGINAL (Russo)[/bold blue]"
            texto_exibir = doc[5]
        else:
            traducao = obter_traducao(doc_id, idioma_atual)
            if traducao:
                badge = f"[bold green]🌐 TRADUÇÃO ({idioma_atual.upper()})[/bold green]"
                texto_exibir = traducao['texto']
            else:
                # Se a tradução não existir mais, volta para original
                visualizar_documento_ui.idioma_atual = 'original'
                badge = "[bold blue]📄 ORIGINAL (Russo)[/bold blue]"
                texto_exibir = doc[5]
        
        header_panel = Panel(
            f"{titulo_texto}\n\n{badge}",
            border_style="bright_green",
            padding=(1, 2),
            subtitle=f"ID: {doc[0]}",
            subtitle_align="right"
        )
        console.print(header_panel)
        console.print()
        
        # Metadados
        console.print("[bold cyan]📋 METADADOS[/bold cyan]")
        console.print(f"  🏛️  Centro: [yellow]{doc[1].upper()}[/yellow]")
        console.print(f"  📅 Data original: [green]{doc[3] or 'Não informada'}[/green]")
        console.print(f"  🔗 URL: [blue]{doc[4]}[/blue]")
        console.print(f"  📊 Tamanho: [cyan]{len(texto_exibir):,} caracteres[/cyan]")
        
        # Mostrar traduções disponíveis
        if traducoes:
            console.print("\n[bold green]🌐 TRADUÇÕES DISPONÍVEIS:[/bold green]")
            for t in traducoes:
                idioma_nome = {
                    'en': 'Inglês 🇺🇸',
                    'pt': 'Português 🇧🇷',
                    'es': 'Espanhol 🇪🇸',
                    'fr': 'Francês 🇫🇷'
                }.get(t['idioma'], t['idioma'].upper())
                
                # Indicador visual do idioma atual
                if t['idioma'] == idioma_atual:
                    console.print(f"  ▶ [bold green]{t['idioma']}[/bold green] {idioma_nome}: {t['data_traducao'][:10]}")
                else:
                    console.print(f"    [{t['idioma']}] {idioma_nome}: {t['data_traducao'][:10]}")
        
        console.print()
        
        # Conteúdo
        console.print("[bold white]📄 CONTEÚDO[/bold white]")
        console.print("─" * 80)
        
        # Truncar se muito longo
        if len(texto_exibir) > 2000:
            texto_exibir = texto_exibir[:2000] + "\n\n[dim]... (texto truncado, use exportar para ver completo)[/dim]"
        
        console.print(texto_exibir)
        console.print("─" * 80)
        
        # Rodapé com comandos
        console.print("\n[dim]COMANDOS:[/dim]")
        console.print("  [green]⏎ Enter[/green] - Voltar à listagem")
        console.print("  [yellow]e[/yellow] - Exportar texto atual")
        
        if traducoes:
            if idioma_atual == 'original':
                console.print("  [cyan]t[/cyan] - Ver tradução")
            else:
                console.print("  [cyan]t[/cyan] - Voltar ao original")
            console.print("  [blue]n[/blue] - Nova tradução")
        
        console.print()
        
        # Aguardar comando
        cmd = input().strip().lower()
        
        if cmd == '':
            # Resetar idioma ao sair
            visualizar_documento_ui.idioma_atual = 'original'
            break  # Voltar à listagem
        
        elif cmd == 'e':
            exportar_documento_ui(doc_id)
            # Continuar no mesmo documento
            continue
        
        elif cmd == 't' and traducoes:
            # Alternar entre original e tradução
            if idioma_atual == 'original':
                # Vai para o PRIMEIRO idioma disponível
                visualizar_documento_ui.idioma_atual = traducoes[0]['idioma']
            else:
                # Volta para original
                visualizar_documento_ui.idioma_atual = 'original'
            continue  # Recarregar com novo idioma
        
        elif cmd == 'n':
            # Nova tradução
            from app import traduzir_documento_interativo
            traduzir_documento_interativo(doc_id)
            # Atualizar lista de traduções
            traducoes = listar_traducoes_documento(doc_id)
            continue
        
        else:
            mensagem_erro("Comando inválido!")
            time.sleep(1)
            continue

# Inicializar idioma atual como original
visualizar_documento_ui.idioma_atual = 'original'

def exportar_documento_ui(doc_id):
    """Exporta documento com opção de escolher idioma"""
    doc = obter_documento(doc_id)
    
    if not doc:
        mensagem_erro("Documento não encontrado!")
        return
    
    # Verificar se há traduções
    traducoes = listar_traducoes_documento(doc_id)
    
    # Escolher idioma
    console.print("\n[bold cyan]🌐 Escolha o idioma para exportar:[/bold cyan]")
    console.print("  [0] Russo (original)")
    
    opcoes = {'0': ('original', 'ru')}
    i = 1
    for t in traducoes:
        nome = {'en': 'Inglês', 'pt': 'Português', 'es': 'Espanhol', 'fr': 'Francês'}.get(t['idioma'], t['idioma'].upper())
        console.print(f"  [{i}] {nome}")
        opcoes[str(i)] = ('traducao', t['idioma'])
        i += 1
    
    console.print()
    escolha = input("Opção: ").strip()
    
    if escolha not in opcoes:
        mensagem_erro("Opção inválida!")
        return
    
    tipo, idioma = opcoes[escolha]
    
    # Obter texto
    if tipo == 'original':
        texto = doc[5]
        sufixo = "original"
        idioma_nome = "RU"
    else:
        traducao = obter_traducao(doc_id, idioma)
        if not traducao:
            mensagem_erro("Tradução não encontrada!")
            return
        texto = traducao['texto']
        sufixo = f"traducao_{idioma}"
        idioma_nome = idioma.upper()
    
    # Exportar
    pasta = Path("exportados")
    pasta.mkdir(exist_ok=True)
    
    # Sanitizar nome do arquivo
    titulo = "".join(c for c in doc[2] if c.isalnum() or c in (' ', '-', '_')).rstrip()
    nome_arquivo = f"{doc[0]}_{titulo[:30]}_{sufixo}.txt"
    caminho = pasta / nome_arquivo
    
    try:
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(f"Título: {doc[2]}\n")
            f.write(f"Centro: {doc[1]}\n")
            f.write(f"Data original: {doc[3]}\n")
            f.write(f"URL: {doc[4]}\n")
            f.write(f"Idioma: {idioma_nome}\n")
            f.write(f"Exportado em: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 80 + "\n\n")
            f.write(texto)
        
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

def exportar_texto_direto(texto: str, nome_arquivo: str):
    """Exporta texto diretamente sem documento no banco"""
    pasta = Path("exportados")
    pasta.mkdir(exist_ok=True)
    
    caminho = pasta / nome_arquivo
    
    try:
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(texto)
        mensagem_sucesso(f"Texto exportado para: {caminho}")
    except Exception as e:
        mensagem_erro(f"Erro ao exportar: {e}")