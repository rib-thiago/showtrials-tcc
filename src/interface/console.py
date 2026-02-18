# src/interface/console.py
"""
Configuração do Rich console para toda a interface.
Reutiliza e adapta o que já existia.
"""

import os

from rich import print  # <-- ADICIONAR ESTA LINHA!
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.theme import Theme

# Tema personalizado
tema = Theme(
    {
        "primary": "bold cyan",
        "secondary": "bold yellow",
        "success": "bold green",
        "error": "bold red",
        "warning": "bold yellow",
        "info": "dim white",
        "destaque": "reverse white",
    }
)

# Console global
console = Console(theme=tema)


def limpar_tela():
    """Limpa o terminal."""
    os.system("cls" if os.name == "nt" else "clear")
    if os.name != "nt":
        print("\033[3J", end="")  # Limpa scrollback
        print("\033[H", end="")  # Posiciona cursor


def cabecalho(titulo: str):
    """Exibe cabeçalho padronizado."""
    console.rule(f"[primary]{titulo}[/primary]")
    console.print()


def mostrar_erro(mensagem: str):
    """Exibe mensagem de erro."""
    console.print(f"[error]✗[/error] {mensagem}")


def mostrar_sucesso(mensagem: str):
    """Exibe mensagem de sucesso."""
    console.print(f"[success]✓[/success] {mensagem}")


def mostrar_aviso(mensagem: str):
    """Exibe mensagem de aviso."""
    console.print(f"[warning]⚠[/warning] {mensagem}")


def spinner(mensagem: str, funcao, *args, **kwargs):
    """
    Executa função com spinner de carregamento.
    Captura exceções e as relança após o spinner.
    """
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
        transient=True,
    ) as progress:
        progress.add_task(f"[cyan]{mensagem}[/cyan]", total=None)
        try:
            resultado = funcao(*args, **kwargs)
            return resultado
        except Exception as e:
            # Relançar a exceção após o spinner
            raise e


# Garantir que as funções estejam disponíveis globalmente
__all__ = [
    "console",
    "limpar_tela",
    "cabecalho",
    "mostrar_erro",
    "mostrar_sucesso",
    "mostrar_aviso",
    "spinner",
]
