# src/interface/cli/presenters_traducao.py
"""
Presenters para traduções.
"""

from rich.panel import Panel

from src.interface.console import console


class TraducaoPresenter:
    """Formata traduções para exibição."""

    @staticmethod
    def badge_idioma(idioma: str) -> str:
        """Retorna badge colorido para idioma."""
        badges = {
            "en": "[bold blue]🇺🇸 EN[/bold blue]",
            "pt": "[bold green]🇧🇷 PT[/bold green]",
            "es": "[bold yellow]🇪🇸 ES[/bold yellow]",
            "fr": "[bold magenta]🇫🇷 FR[/bold magenta]",
        }
        return badges.get(idioma, f"[dim]{idioma}[/dim]")

    @classmethod
    def lista_traducoes(cls, traducoes, documento_id: int):
        """Exibe lista de traduções disponíveis."""
        if not traducoes:
            return

        console.print("\n[bold cyan]🌐 TRADUÇÕES DISPONÍVEIS:[/bold cyan]")

        for t in traducoes:
            console.print(
                f"  • {cls.badge_idioma(t['idioma'])} - "
                f"{t['data_traducao']} "
                f"[dim](custo: ${t['custo']:.4f})[/dim]"
            )

        console.print("\n[dim]Digite 't' para alternar entre os idiomas[/dim]")

    @classmethod
    def badge_idioma_atual(cls, idioma: str):
        """Exibe badge indicando idioma atual."""
        if idioma == "original":
            return Panel("[bold blue]📄 ORIGINAL (Russo)[/bold blue]", border_style="blue")
        else:
            return Panel(
                f"[bold green]🌐 TRADUÇÃO {cls.badge_idioma(idioma)}[/bold green]",
                border_style="green",
            )
