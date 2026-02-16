# ui/console.py
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.layout import Layout
from rich.prompt import Prompt, IntPrompt
from rich import box
from rich.text import Text
from rich.columns import Columns
from datetime import datetime
import os
import time

# Console global
console = Console()

def limpar_tela():
    """Limpa o terminal de forma cross-platform"""
    os.system('cls' if os.name == 'nt' else 'clear')
    # ADICIONE ESTAS 2 LINHAS ABAIXO:
    if os.name != 'nt':  # Linux/Mac
        print('\033[3J', end='')  # Limpa histórico de rolagem
        print('\033[H', end='')   # Posiciona cursor no topo

def cabecalho(titulo):
    """Exibe cabeçalho padronizado"""
    console.rule(f"[bold cyan]{titulo}[/bold cyan]")
    console.print()

def criar_tabela_documentos(documentos, total, pagina, por_pagina=20):
    """Cria uma tabela formatada para documentos"""
    table = Table(
        title=f"[bold]📚 ACERVO DE DOCUMENTOS[/bold]\n[dim]Total: {total} documentos | Página {pagina}[/dim]",
        box=box.ROUNDED,
        header_style="bold cyan",
        border_style="bright_blue",
        padding=(0, 1)
    )
    
    table.add_column("ID", style="dim white", width=6, justify="right")
    table.add_column("🏛️ Centro", style="yellow", width=12)
    table.add_column("📅 Data", style="green", width=12)
    table.add_column("📄 Título", style="white", width=50)
    table.add_column("📊 Tamanho", style="blue", width=10, justify="right")
    
    for doc in documentos:
        titulo = doc[2][:47] + "…" if len(doc[2]) > 48 else doc[2]
        
        tamanho = int(doc[5])
        if tamanho < 1000:
            tamanho_str = f"{tamanho}c"
        elif tamanho < 1000000:
            tamanho_str = f"{tamanho/1000:.1f}K"
        else:
            tamanho_str = f"{tamanho/1000000:.1f}M"
        
        centro = doc[1].upper() if doc[1] else "N/A"
        
        table.add_row(
            str(doc[0]),
            centro,
            doc[3] or "N/D",
            titulo,
            tamanho_str
        )
    
    return table

def mostrar_tabela_documentos(documentos, total, pagina, por_pagina=20):
    """Exibe a tabela de documentos no console"""
    table = criar_tabela_documentos(documentos, total, pagina, por_pagina)
    console.print(table)
    
    total_paginas = (total + por_pagina - 1) // por_pagina
    
    nav_bar = Panel(
        f"[bold cyan]📌 Página {pagina} de {total_paginas} • Total: {total} documentos[/bold cyan]",
        border_style="bright_blue",
        padding=(1, 2)
    )
    console.print(nav_bar)

def mostrar_documento(doc):
    """Exibe documento completo com formatação"""
    limpar_tela()
    
    # Cabeçalho
    titulo_texto = Text()
    titulo_texto.append("📄 ", style="bold white")
    titulo_texto.append(doc[2], style="bold yellow")
    
    header_panel = Panel(
        titulo_texto,
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
    console.print(f"  📊 Tamanho: [cyan]{len(doc[5]):,} caracteres[/cyan]")
    console.print(f"  📝 Palavras: [cyan]{len(doc[5].split()):,} palavras[/cyan]")
    console.print()
    
    # Conteúdo
    console.print("[bold white]📄 CONTEÚDO[/bold white]")
    console.print("─" * 80)
    
    texto = doc[5]
    if len(texto) > 2000:
        texto = texto[:2000] + "\n\n[dim]... (texto truncado, use exportar para ver completo)[/dim]"
    
    console.print(texto)
    console.print("─" * 80)
    
    # Rodapé
    console.print("[dim]⏎ Enter para voltar | [yellow]e[/yellow] para exportar | [green]t[/green] para traduzir[/dim]")

def menu_principal():
    """Menu principal estilizado"""
    limpar_tela()
    
    # Banner ASCII estilizado
    banner = """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ║
║   ▓                                                        ▓ ║
║   ▓     ███████╗ ██████╗ ██╗   ██╗██╗███████╗████████╗   ▓ ║
║   ▓     ██╔════╝██╔═══██╗██║   ██║██║██╔════╝╚══██╔══╝   ▓ ║
║   ▓     ███████╗██║   ██║██║   ██║██║█████╗     ██║      ▓ ║
║   ▓     ╚════██║██║   ██║╚██╗ ██╔╝██║██╔══╝     ██║      ▓ ║
║   ▓     ███████║╚██████╔╝ ╚████╔╝ ██║███████╗   ██║      ▓ ║
║   ▓     ╚══════╝ ╚═════╝   ╚═══╝  ╚═╝╚══════╝   ╚═╝      ▓ ║
║   ▓          ████████╗██████╗ ██╗ █████╗ ██╗     ███████╗ ▓ ║
║   ▓          ╚══██╔══╝██╔══██╗██║██╔══██╗██║     ██╔════╝ ▓ ║
║   ▓             ██║   ██████╔╝██║███████║██║     ███████╗ ▓ ║
║   ▓             ██║   ██╔══██╗██║██╔══██║██║     ╚════██║ ▓ ║
║   ▓             ██║   ██║  ██║██║██║  ██║███████╗███████║ ▓ ║
║   ▓             ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚══════╝╚══════╝ ▓ ║
║   ▓                                                        ▓ ║
║   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ║
║                                                              ║
║        ►   DOCUMENT ANALYSIS • ARCHIVAL SOURCES • USSR      ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""
    console.print(banner, style="bold cyan")
    console.print()
    
    console.print("[bold cyan]MENU PRINCIPAL[/bold cyan]")
    console.print()
    console.print("  [1] 📋 Listar todos os documentos")
    console.print("  [2] 🏛️  Listar por centro")
    console.print("  [3] 👁️  Visualizar documento")
    console.print("  [4] 💾 Exportar documento")
    console.print("  [5] 🔄 Reimportar texto editado")
    console.print("  [6] 🌐 Traduzir documento")
    console.print("  [7] 📊 Estatísticas")
    console.print("  [0] 🚪 Sair")
    console.print()
    
    return Prompt.ask("[bold cyan]➤ Escolha uma opção[/bold cyan]", 
                     choices=["0","1","2","3","4","5","6","7"])

def menu_navegacao():
    """Menu de navegação durante listagem"""
    console.print()
    console.print("[dim]─────────────────────────────────────────────────[/dim]")
    console.print("[bold cyan]COMANDOS[/bold cyan]")
    console.print("  [green]→[/green] [bold]n[/bold] - Próxima página")
    console.print("  [green]→[/green] [bold]p[/bold] - Página anterior")
    console.print("  [green]→[/green] [bold][número][/bold] - Ver documento")
    console.print("  [green]→[/green] [bold]m[/bold] - Menu principal")
    console.print()
    
    return Prompt.ask("[bold cyan]Comando[/bold cyan]").strip().lower()

def spinner_processo(mensagem, funcao, *args, **kwargs):
    """Executa função com spinner de carregamento"""
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
        transient=True
    ) as progress:
        task = progress.add_task(
            description=f"[bold cyan]{mensagem}[/bold cyan]",
            total=None
        )
        resultado = funcao(*args, **kwargs)
        progress.update(task, completed=True)
    return resultado

def exibir_estatisticas(stats):
    """Exibe estatísticas do acervo"""
    limpar_tela()
    cabecalho("📊 ESTATÍSTICAS DO ACERVO")
    
    console.print(f"[bold]Total de documentos:[/bold] [cyan]{stats['total_docs']}[/cyan]")
    console.print(f"[bold]Total de traduções:[/bold] [green]{stats['total_traducoes']}[/green]")
    console.print()
    
    if stats['docs_por_centro']:
        console.print("[bold]Documentos por centro:[/bold]")
        for centro, count in stats['docs_por_centro'].items():
            console.print(f"  • {centro}: [cyan]{count}[/cyan]")
        console.print()
    
    if stats['docs_por_tipo']:
        console.print("[bold]Documentos por tipo:[/bold]")
        for tipo, count in stats['docs_por_tipo'].items():
            console.print(f"  • {tipo}: [green]{count}[/green]")
        console.print()
    
    if stats['tags_mais_usadas']:
        console.print("[bold]Tags mais utilizadas:[/bold]")
        for tag, count in stats['tags_mais_usadas']:
            console.print(f"  • #{tag}: [yellow]{count}[/yellow]")
    
    console.print()
    input("[bold cyan]Pressione Enter para voltar...[/bold cyan]")

def mensagem_sucesso(texto):
    """Exibe mensagem de sucesso"""
    console.print(f"[bold green]✓[/bold green] {texto}")

def mensagem_erro(texto):
    """Exibe mensagem de erro"""
    console.print(f"[bold red]✗[/bold red] {texto}")

def mensagem_aviso(texto):
    """Exibe mensagem de aviso"""
    console.print(f"[bold yellow]⚠[/bold yellow] {texto}")

# ui/console.py - Adicione esta função nova

def mostrar_status_traducao(documento_id: int):
    """
    Exibe badge de status de tradução para um documento.
    """
    from db import listar_traducoes_documento
    
    traducoes = listar_traducoes_documento(documento_id)
    
    if not traducoes:
        return "[dim]📭 Sem traduções[/dim]"
    
    badges = []
    for t in traducoes:
        if t['idioma'] == 'en':
            badges.append("[bold green]🇺🇸 EN[/bold green]")
        elif t['idioma'] == 'pt':
            badges.append("[bold green]🇧🇷 PT[/bold green]")
        elif t['idioma'] == 'es':
            badges.append("[bold green]🇪🇸 ES[/bold green]")
        else:
            badges.append(f"[bold green]{t['idioma'].upper()}[/bold green]")
    
    return " ".join(badges)

# ui/console.py - ADICIONE NO FINAL DO ARQUIVO

def badge_tipo_documento(tipo: str) -> str:
    """Retorna badge colorido para tipo de documento"""
    badges = {
        'interrogatorio': '[bold cyan]🔍 INTERROGATÓRIO[/bold cyan]',
        'acareacao': '[bold yellow]⚖️ ACAREAÇÃO[/bold yellow]',
        'acusacao': '[bold red]📜 ACUSAÇÃO[/bold red]',
        'declaracao': '[bold blue]📝 DECLARAÇÃO[/bold blue]',
        'carta': '[bold green]✉️ CARTA[/bold green]',
        'relatorio': '[bold magenta]📋 RELATÓRIO NKVD[/bold magenta]',
        'depoimento': '[bold purple]🗣️ DEPOIMENTO[/bold purple]',
        'laudo': '[bold white]🏥 LAUDO[/bold white]',
        'desconhecido': '[dim]📄 DOCUMENTO[/dim]'
    }
    return badges.get(tipo, badges['desconhecido'])

def badge_idioma(idioma: str) -> str:
    """Retorna badge de idioma"""
    badges = {
        'ru': '[bold white]🇷🇺 RU[/bold white]',
        'en': '[bold blue]🇺🇸 EN[/bold blue]',
        'pt': '[bold green]🇧🇷 PT[/bold green]',
    }
    return badges.get(idioma, f'[dim]{idioma}[/dim]')

def mostrar_metadados_completos(doc):
    """Exibe TODOS os metadados do documento formatados"""
    from rich.panel import Panel
    from rich.table import Table
    from rich.console import Console
    console = Console()
    
    metadados = Panel(
        f"""[bold cyan]📋 METADADOS COMPLETOS[/bold cyan]
        
[bold]Tipo:[/bold] {badge_tipo_documento(doc[6]) if len(doc) > 6 else badge_tipo_documento('desconhecido')}
[bold]Centro:[/bold] {'🏛️ Leningrado' if doc[1] == 'lencenter' else '🏛️ Moscou'}
[bold]Data original:[/bold] {doc[3] or 'Não informada'}
[bold]ID do documento:[/bold] {doc[0]}

[bold yellow]👤 PESSOAS ENVOLVIDAS:[/bold yellow]""",
        border_style="cyan",
        padding=(1, 2)
    )
    console.print(metadados)