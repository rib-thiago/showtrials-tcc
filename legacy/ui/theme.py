from rich.console import Console
from rich.theme import Theme

# Tema personalizado para o projeto
TEMA_SHOWTRIALS = Theme(
    {
        # Cores principais
        "primary": "bold cyan",
        "secondary": "bold yellow",
        "success": "bold green",
        "error": "bold red",
        "warning": "bold yellow",
        "info": "dim white",
        # Tipos de documento
        "interrogatorio": "cyan",
        "acusacao": "red",
        "sentenca": "yellow",
        "outro": "white",
        # Centros
        "lencenter": "blue",
        "moscenter": "magenta",
        # Status
        "traduzido": "green",
        "nao_traduzido": "red",
        "revisado": "bright_green",
        # Navegação
        "comando": "bold cyan",
        "destaque": "reverse white",
        "separador": "dim",
    }
)


def configurar_console():
    """Configura console com tema personalizado"""
    return Console(theme=TEMA_SHOWTRIALS)
