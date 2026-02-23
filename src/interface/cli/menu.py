# src/interface/cli/menu.py
"""
Menus interativos da aplicação.
"""

from src.interface.console import console, limpar_tela


class MenuPrincipal:
    """Menu principal da aplicação."""

    def __init__(self, app):
        self.app = app

    def mostrar(self) -> str:
        """Exibe menu e retorna opção escolhida."""
        limpar_tela()

        banner = """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                    ◈ ◈ ◈ SHOW TRIALS ◈ ◈ ◈                 ║
║                    Coleta • Tradução • Análise              ║
╚══════════════════════════════════════════════════════════════╝
"""
        console.print(banner, style="bold cyan")
        console.print()

        console.print("[bold cyan]MENU PRINCIPAL[/bold cyan]")
        console.print()
        console.print("  [1] 📋 Listar todos os documentos")
        console.print("  [2] 🏛️  Listar por centro")
        console.print("  [3] 👁️  Visualizar documento")
        console.print("  [4] 📊 Estatísticas")
        console.print("  [5] 📈 Relatórios avançados")
        console.print("  [6] 🔍 Análise de texto")  # <-- NOVO
        console.print("  [7] 🔄 Sair")
        console.print()

        escolha = input("Escolha: ").strip()  # Sem cor no input
        return escolha


class MenuCentro:
    """Menu para escolha de centro."""

    @staticmethod
    def mostrar() -> str | None:
        """Exibe opções de centro."""
        console.print()
        console.print("[bold cyan]Centros disponíveis:[/bold cyan]")
        console.print("  [1] 🏛️ Leningrad Center")
        console.print("  [2] 🏛️ Moscow Center")
        console.print("  [0] ↩️  Voltar")
        console.print()

        opcao = input("Escolha o centro: ").strip()

        if opcao == "1":
            return "lencenter"
        elif opcao == "2":
            return "moscenter"
        return None
