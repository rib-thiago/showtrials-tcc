# src/interface/cli/presenters_analise.py
"""
Presenters para análise de texto.
"""

from rich import box
from rich.panel import Panel
from rich.table import Table

from src.interface.console import console


class AnalisePresenter:
    """Formata resultados de análise para exibição."""

    @staticmethod
    def mostrar_analise(analise):
        """Exibe análise completa de um documento."""
        # Cabeçalho
        console.print(
            Panel(
                f"[bold cyan]🔍 ANÁLISE DO DOCUMENTO {analise.documento_id}[/bold cyan]",
                border_style="cyan",
            )
        )

        # 1. Estatísticas básicas
        console.print("\n[bold]📊 ESTATÍSTICAS DO TEXTO[/bold]")
        stats_table = Table(box=box.SIMPLE)
        stats_table.add_column("Métrica", style="cyan")
        stats_table.add_column("Valor", style="white")

        e = analise.estatisticas
        stats_table.add_row("Total de caracteres", f"{e.total_caracteres:,}")
        stats_table.add_row("Total de palavras", f"{e.total_palavras:,}")
        stats_table.add_row("Total de parágrafos", f"{e.total_paragrafos}")
        stats_table.add_row("Total de frases", f"{e.total_frases}")
        stats_table.add_row("Palavras únicas", f"{e.palavras_unicas:,}")
        stats_table.add_row("Densidade léxica", f"{e.densidade_lexica:.2f}")
        stats_table.add_row("Tamanho médio da palavra", f"{e.tamanho_medio_palavra:.1f}")
        stats_table.add_row("Tamanho médio da frase", f"{e.tamanho_medio_frase:.1f}")

        console.print(stats_table)

        # 2. Sentimento
        console.print("\n[bold]😊 ANÁLISE DE SENTIMENTO[/bold]")
        s = analise.sentimento
        cor = {"positivo": "green", "negativo": "red", "neutro": "yellow"}.get(
            s.classificacao, "white"
        )

        console.print(f"  Classificação: [{cor}]{s.classificacao.upper()}[/{cor}]")
        console.print(f"  Polaridade: {s.polaridade:.2f} (-1 a +1)")
        console.print(f"  Subjetividade: {s.subjetividade:.2f} (0 a 1)")

        # 3. Entidades
        if analise.entidades_por_tipo:
            console.print("\n[bold]🏷️  ENTIDADES ENCONTRADAS[/bold]")

            for tipo, entidades in analise.entidades_por_tipo.items():
                if entidades:
                    console.print(f"\n  [cyan]{tipo}:[/cyan]")
                    # Mostrar até 10 entidades por tipo
                    for ent in entidades[:10]:
                        console.print(f"    • {ent}")
                    if len(entidades) > 10:
                        console.print(f"    [dim]... e mais {len(entidades)-10}[/dim]")

        # 4. Palavras mais frequentes
        if analise.palavras_frequentes:
            console.print("\n[bold]📈 PALAVRAS MAIS FREQUENTES[/bold]")

            freq_table = Table(box=box.SIMPLE)
            freq_table.add_column("#", style="dim", width=3)
            freq_table.add_column("Palavra", style="white")
            freq_table.add_column("Frequência", style="cyan", justify="right")

            for i, (palavra, freq) in enumerate(analise.palavras_frequentes[:15], 1):
                freq_table.add_row(str(i), palavra, str(freq))

            console.print(freq_table)

        # 5. Metadados da análise
        console.print("\n[dim]─────────────────────────────────────[/dim]")
        console.print(f"[dim]Modelo: {analise.modelo_utilizado}[/dim]")
        console.print(f"[dim]Tempo de processamento: {analise.tempo_processamento:.2f}s[/dim]")
        console.print(f"[dim]Data: {analise.data_analise.strftime('%Y-%m-%d %H:%M')}[/dim]")

        if hasattr(analise, "wordcloud_path") and analise.wordcloud_path:
            console.print(f"[dim]Nuvem de palavras: {analise.wordcloud_path}[/dim]")

    @staticmethod
    def mostrar_estatisticas_globais(stats):
        """Exibe estatísticas globais do acervo."""
        console.print(
            Panel("[bold cyan]📊 ESTATÍSTICAS GLOBAIS DO ACERVO[/bold cyan]", border_style="cyan")
        )

        # Visão geral
        console.print("\n[bold]📈 VISÃO GERAL[/bold]")
        console.print(f"  • Total de documentos analisados: {stats['total_docs']}")
        console.print(f"  • Total de palavras: {stats['total_palavras']:,}")
        console.print(f"  • Média de palavras por documento: {stats['media_palavras_por_doc']:.1f}")

        # Distribuição por tamanho
        console.print("\n[bold]📏 DISTRIBUIÇÃO POR TAMANHO[/bold]")
        for categoria, total in stats["documentos_por_tamanho"].items():
            console.print(f"  • {categoria}: {total}")

        # Top pessoas
        if stats["top_pessoas"]:
            console.print("\n[bold]👤 PESSOAS MAIS CITADAS[/bold]")
            for pessoa, freq in stats["top_pessoas"][:10]:
                console.print(f"  • {pessoa}: {freq}")

        # Top locais
        if stats["top_locais"]:
            console.print("\n[bold]📍 LOCAIS MAIS CITADOS[/bold]")
            for local, freq in stats["top_locais"][:5]:
                console.print(f"  • {local}: {freq}")
