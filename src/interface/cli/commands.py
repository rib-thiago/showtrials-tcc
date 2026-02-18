# src/interface/cli/commands.py
"""
Comandos da CLI - Cada comando é uma ação do usuário.
"""

from typing import Optional

from src.interface.cli.presenters import DocumentoPresenter
from src.interface.console import cabecalho, console, limpar_tela, mostrar_erro


class ComandoListar:
    """Comando para listar documentos."""

    def __init__(self, listar_use_case):
        self.listar_use_case = listar_use_case
        self.presenter = DocumentoPresenter()

    def executar(self, centro: Optional[str] = None, tipo: Optional[str] = None):
        """Executa listagem interativa."""
        pagina = 1
        limite = 15

        while True:
            limpar_tela()
            cabecalho(f"📋 Documentos - {centro or 'Todos'}")

            # Buscar documentos
            resultados = self.listar_use_case.executar(
                pagina=pagina, limite=limite, centro=centro, tipo=tipo
            )

            # Mostrar tabela
            self.presenter.tabela_documentos(resultados)

            # Menu de navegação
            console.print("\n[dim]─────────────────────────────────[/dim]")
            console.print("[bold cyan]COMANDOS[/bold cyan]")
            console.print("  [green]n[/green] - Próxima página")
            console.print("  [green]p[/green] - Página anterior")
            console.print("  [green][número][/green] - Ver documento")
            console.print("  [green]m[/green] - Menu principal")

            cmd = input("\nComando: ").strip().lower()

            if cmd == "n" and pagina < resultados["total_paginas"]:
                pagina += 1
            elif cmd == "p" and pagina > 1:
                pagina -= 1
            elif cmd == "m":
                break
            elif cmd.isdigit():
                return int(cmd)  # Retorna ID para visualização
            else:
                mostrar_erro("Comando inválido")


class ComandoVisualizar:
    """Comando para visualizar documento."""

    def __init__(self, obter_use_case):
        self.obter_use_case = obter_use_case
        self.presenter = DocumentoPresenter()

    def executar(self, documento_id: int):
        """Executa visualização de documento."""
        dto = self.obter_use_case.executar(documento_id)

        if not dto:
            mostrar_erro("Documento não encontrado!")
            return None

        limpar_tela()
        self.presenter.documento_completo(dto)

        console.print("\n[dim]⏎ Enter para voltar | [yellow]e[/yellow] para exportar[/dim]")
        return input().strip().lower()


class ComandoEstatisticas:
    """Comando para mostrar estatísticas."""

    def __init__(self, estatisticas_use_case):
        self.estatisticas_use_case = estatisticas_use_case
        self.presenter = DocumentoPresenter()

    def executar(self):
        """Executa visualização de estatísticas."""
        limpar_tela()
        stats = self.estatisticas_use_case.executar()
        self.presenter.estatisticas(stats)
        input("\n[cyan]Pressione Enter para voltar...[/cyan]")


# src/interface/cli/commands.py (ADICIONAR ESTA CLASSE)


class ComandoAlternarIdioma:
    """Comando para alternar entre idiomas durante visualização."""

    def __init__(self, listar_traducoes_use_case, obter_documento_use_case):
        self.listar_traducoes = listar_traducoes_use_case
        self.obter_documento = obter_documento_use_case

    def executar(self, documento_id: int, idioma_atual: str = "original") -> str:
        """
        Alterna entre original e traduções disponíveis.
        Retorna o novo idioma selecionado.
        """
        # Buscar traduções disponíveis
        traducoes = self.listar_traducoes(documento_id)

        if not traducoes:
            return "original"

        # Determinar próximo idioma
        if idioma_atual == "original":
            # Vai para primeira tradução
            return traducoes[0].idioma
        else:
            # Encontra índice atual e vai para o próximo
            idiomas = [t.idioma for t in traducoes]
            try:
                idx = idiomas.index(idioma_atual)
                if idx + 1 < len(idiomas):
                    return idiomas[idx + 1]
                else:
                    # Volta para original
                    return "original"
            except ValueError:
                return traducoes[0].idioma
