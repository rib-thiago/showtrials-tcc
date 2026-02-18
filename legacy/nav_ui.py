# nav_ui.py
import sqlite3  # <-- ADICIONAR
import time
from pathlib import Path

from db import DB_PATH  # <-- ADICIONAR
from db import contar_por_filtro  # <-- ADICIONAR
from db import contar_por_tipo  # <-- ADICIONAR
from db import listar_paginado_com_filtros  # <-- ADICIONAR
from db import atualizar_texto, contar, listar_traducoes_documento, obter_documento, obter_traducao
from rich import box
from rich.panel import Panel
from rich.prompt import IntPrompt, Prompt
from rich.table import Table
from translators.nomes import traduzir_tipo_documento, transliterar_nome
from ui import badge_tipo_documento  # <-- AQUI!
from ui import mostrar_metadados_completos  # <-- AQUI!
from ui import (
    cabecalho,
    console,
    limpar_tela,
    mensagem_erro,
    mensagem_sucesso,
    mostrar_status_traducao,
)

# nav_ui.py - SUBSTITUA a função navegar_lista


def navegar_lista(centro=None, filtro_tipo=None):
    """Navegação paginada com FILTROS POR TIPO e BADGES DE TRADUÇÃO"""
    limite = 15
    pagina = 0

    # Montar query com filtros
    if centro and filtro_tipo:
        total = contar_por_filtro(centro, filtro_tipo)
        titulo = f"📋 {centro.upper()} - {traduzir_tipo_documento(filtro_tipo, 'pt')}"
    elif centro:
        total = contar(centro)
        titulo = f"📋 {centro.upper()}"
    elif filtro_tipo:
        total = contar_por_tipo(filtro_tipo)
        titulo = f"📋 {traduzir_tipo_documento(filtro_tipo, 'pt')}"
    else:
        total = contar()
        titulo = "📋 TODOS OS DOCUMENTOS"

    if total == 0:
        console.print("[yellow]⚠ Nenhum documento encontrado.[/yellow]")
        time.sleep(1.5)
        return

    while True:
        limpar_tela()
        cabecalho(titulo)

        offset = pagina * limite
        docs = listar_paginado_com_filtros(
            offset=offset, limite=limite, centro=centro, tipo=filtro_tipo
        )

        # Verificar se há traduções para mostrar coluna
        tem_traducao = False
        for doc in docs[:5]:
            if listar_traducoes_documento(doc[0]):
                tem_traducao = True
                break

        # Criar tabela enriquecida
        table = Table(
            title=f"[bold]📚 {titulo}[/bold]\n[dim]Total: {total} documentos | Página {pagina + 1}[/dim]",
            box=box.ROUNDED,
            header_style="bold cyan",
            border_style="bright_blue",
        )

        # Colunas fixas
        table.add_column("ID", style="dim white", width=4, justify="right")
        table.add_column("Tipo", width=20)
        table.add_column("Data", width=12)
        table.add_column("Pessoa", width=25)
        table.add_column("Título", width=40)

        # COLUNA DE TRADUÇÃO (só se houver alguma)
        if tem_traducao:
            table.add_column("🌐", width=12, justify="center")

        # Adicionar linhas
        for doc in docs:
            # Badge do tipo
            badge = (
                badge_tipo_documento(doc[6])
                if len(doc) > 6
                else badge_tipo_documento("desconhecido")
            )

            # Pessoa principal (traduzida)
            pessoa = ""
            if len(doc) > 7 and doc[7]:
                try:
                    pessoa = transliterar_nome(doc[7]).split()[-1]  # Só sobrenome
                except:
                    pessoa = doc[7][:20]
            elif len(doc) > 8 and doc[8]:  # remetente
                try:
                    pessoa = f"📨 {transliterar_nome(doc[8]).split()[-1]}"
                except:
                    pessoa = f"📨 {doc[8][:15]}"

            # Título truncado
            titulo_doc = doc[2][:37] + "…" if len(doc[2]) > 38 else doc[2]

            # Montar linha base
            linha = [str(doc[0]), badge, doc[3] or "N/D", pessoa[:23], titulo_doc]

            # Adicionar badge de tradução se houver coluna
            if tem_traducao:
                status = mostrar_status_traducao(doc[0])
                linha.append(status)

            table.add_row(*linha)

        console.print(table)

        # Menu de navegação
        console.print("\n[dim]─────────────────────────────────────────────────[/dim]")
        console.print("[bold cyan]COMANDOS[/bold cyan]")
        console.print("  [green]→[/green] [bold]n[/bold] Próxima página")
        console.print("  [green]→[/green] [bold]p[/bold] Página anterior")
        console.print("  [green]→[/green] [bold][número][/bold] Ver documento")
        console.print("  [green]→[/green] [bold]f[/bold] Filtrar por tipo")
        console.print("  [green]→[/green] [bold]m[/bold] Menu principal")
        console.print()

        escolha = input("[bold cyan]Comando[/bold cyan] ").strip().lower()

        if escolha == "n":
            if (pagina + 1) * limite < total:
                pagina += 1
            else:
                mensagem_erro("Última página!")
                time.sleep(1)
        elif escolha == "p":
            if pagina > 0:
                pagina -= 1
            else:
                mensagem_erro("Primeira página!")
                time.sleep(1)
        elif escolha == "f":
            menu_filtro_tipo(centro)
            break
        elif escolha == "m":
            break
        elif escolha.isdigit():
            visualizar_documento_ui(int(escolha))
        else:
            mensagem_erro("Comando inválido!")
            time.sleep(1)


def menu_filtro_tipo(centro=None):
    """Menu de filtros por tipo de documento"""
    limpar_tela()
    cabecalho("🔍 FILTRAR POR TIPO DE DOCUMENTO")

    console.print("\n[bold cyan]Tipos disponíveis:[/bold cyan]\n")

    # Buscar tipos existentes no banco
    from db import listar_tipos_documento

    tipos = listar_tipos_documento(centro)

    opcoes = {}
    for i, (tipo, count) in enumerate(tipos, 1):
        badge = badge_tipo_documento(tipo)
        nome_pt = traduzir_tipo_documento(tipo, "pt")
        console.print(f"  [{i}] {badge} - {nome_pt} [dim]({count})[/dim]")
        opcoes[str(i)] = tipo

    console.print("  [0] 🔄 Limpar filtro")
    console.print()

    escolha = input("[bold cyan]Escolha o tipo[/bold cyan] ").strip()

    if escolha == "0":
        navegar_lista(centro=centro, filtro_tipo=None)
    elif escolha in opcoes:
        navegar_lista(centro=centro, filtro_tipo=opcoes[escolha])
    else:
        mensagem_erro("Opção inválida!")
        time.sleep(1)
        navegar_lista(centro=centro)


# nav_ui.py - ATUALIZE a função visualizar_documento_ui


def visualizar_documento_ui(doc_id):
    """Visualização de documento com METADADOS COMPLETOS e TRADUÇÕES"""
    # Buscar documento
    doc = obter_documento(doc_id)

    if not doc:
        mensagem_erro("Documento não encontrado!")
        time.sleep(1.5)
        return

    # Buscar metadados adicionais
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT
            tipo_documento, pessoa_principal, remetente,
            destinatario, destinatario_orgao, envolvidos, tem_anexos
        FROM documentos
        WHERE id = ?
    """,
        (doc_id,),
    )

    metadados = cursor.fetchone()
    conn.close()

    # Combinar doc + metadados
    if metadados:
        doc_completo = list(doc) + list(metadados)
    else:
        doc_completo = list(doc) + [None] * 7

    # Buscar traduções disponíveis
    traducoes = listar_traducoes_documento(doc_id)

    # Inicializar idioma atual se não existir
    if not hasattr(visualizar_documento_ui, "idioma_atual"):
        visualizar_documento_ui.idioma_atual = "original"

    while True:  # Loop para alternar entre original/traduções
        limpar_tela()

        # Buscar idioma atual
        idioma_atual = visualizar_documento_ui.idioma_atual

        # Definir qual texto mostrar
        if idioma_atual == "original":
            texto_exibir = doc_completo[5]
            badge_idioma_atual = "[bold blue]📄 ORIGINAL (Russo)[/bold blue]"
        else:
            traducao = obter_traducao(doc_id, idioma_atual)
            if traducao:
                texto_exibir = traducao["texto"]
                badge_idioma_atual = (
                    f"[bold green]🌐 TRADUÇÃO ({idioma_atual.upper()})[/bold green]"
                )
            else:
                # Se a tradução não existir, volta para original
                visualizar_documento_ui.idioma_atual = "original"
                idioma_atual = "original"
                texto_exibir = doc_completo[5]
                badge_idioma_atual = "[bold blue]📄 ORIGINAL (Russo)[/bold blue]"

        # Título com badge
        titulo_badge = f"{badge_tipo_documento(doc_completo[6])} [bold yellow]{doc_completo[2]}[/bold yellow]\n\n{badge_idioma_atual}"
        console.print(Panel(titulo_badge, border_style="bright_green", padding=(1, 2)))

        # METADADOS COMPLETOS
        try:
            mostrar_metadados_completos(doc_completo)
        except Exception as e:
            console.print(f"[red]Erro ao mostrar metadados: {e}[/red]")

        # MOSTRAR TRADUÇÕES DISPONÍVEIS
        if traducoes:
            console.print("\n[bold cyan]🌐 TRADUÇÕES DISPONÍVEIS:[/bold cyan]")
            for t in traducoes:
                idioma_nome = {
                    "en": "Inglês 🇺🇸",
                    "pt": "Português 🇧🇷",
                    "es": "Espanhol 🇪🇸",
                    "fr": "Francês 🇫🇷",
                }.get(t["idioma"], t["idioma"].upper())

                # Indicador visual do idioma atual
                if t["idioma"] == idioma_atual:
                    console.print(
                        f"  ▶ [bold green]{t['idioma']}[/bold green] {idioma_nome}: {t['data_traducao'][:10]}"
                    )
                else:
                    console.print(f"    [{t['idioma']}] {idioma_nome}: {t['data_traducao'][:10]}")

        # Conteúdo
        console.print("\n[bold white]📄 CONTEÚDO[/bold white]")
        console.print("─" * 80)

        if len(texto_exibir) > 2000:
            texto_exibir = texto_exibir[:2000] + "\n\n[dim]... (texto truncado)[/dim]"

        console.print(texto_exibir)
        console.print("─" * 80)

        # COMANDOS
        console.print("\n[dim]COMANDOS:[/dim]")
        console.print("  [green]⏎ Enter[/green] - Voltar à listagem")
        console.print("  [yellow]e[/yellow] - Exportar texto atual")

        if traducoes:
            if idioma_atual == "original":
                console.print("  [cyan]t[/cyan] - Ver tradução")
            else:
                console.print("  [cyan]t[/cyan] - Voltar ao original")
            console.print("  [blue]n[/blue] - Nova tradução")

        console.print()

        # Aguardar comando
        cmd = input().strip().lower()

        if cmd == "":
            # Resetar idioma ao sair
            visualizar_documento_ui.idioma_atual = "original"
            break

        elif cmd == "e":
            exportar_documento_ui(doc_id)
            continue

        elif cmd == "t" and traducoes:
            # Alternar entre original e tradução
            if idioma_atual == "original":
                # Vai para o PRIMEIRO idioma disponível
                visualizar_documento_ui.idioma_atual = traducoes[0]["idioma"]
            else:
                # Volta para original
                visualizar_documento_ui.idioma_atual = "original"
            continue

        elif cmd == "n":
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
visualizar_documento_ui.idioma_atual = "original"


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

    opcoes = {"0": ("original", "ru")}
    i = 1
    for t in traducoes:
        nome = {"en": "Inglês", "pt": "Português", "es": "Espanhol", "fr": "Francês"}.get(
            t["idioma"], t["idioma"].upper()
        )
        console.print(f"  [{i}] {nome}")
        opcoes[str(i)] = ("traducao", t["idioma"])
        i += 1

    console.print()
    escolha = input("Opção: ").strip()

    if escolha not in opcoes:
        mensagem_erro("Opção inválida!")
        return

    tipo, idioma = opcoes[escolha]

    # Obter texto
    if tipo == "original":
        texto = doc[5]
        sufixo = "original"
        idioma_nome = "RU"
    else:
        traducao = obter_traducao(doc_id, idioma)
        if not traducao:
            mensagem_erro("Tradução não encontrada!")
            return
        texto = traducao["texto"]
        sufixo = f"traducao_{idioma}"
        idioma_nome = idioma.upper()

    # Exportar
    pasta = Path("exportados")
    pasta.mkdir(exist_ok=True)

    # Sanitizar nome do arquivo
    titulo = "".join(c for c in doc[2] if c.isalnum() or c in (" ", "-", "_")).rstrip()
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
