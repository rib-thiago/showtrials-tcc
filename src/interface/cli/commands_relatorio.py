# src/interface/cli/commands_relatorio.py
"""
Comandos de relatório para a CLI.
"""

from src.interface.console import console, mostrar_erro, mostrar_sucesso


class ComandoRelatorio:
    """Comando para gerar relatórios."""

    def __init__(self, gerar_relatorio_use_case):
        self.gerar_relatorio = gerar_relatorio_use_case

    def executar(self):
        """Executa geração de relatório interativa."""
        console.print("\n[bold cyan]📊 GERAR RELATÓRIO[/bold cyan]")
        console.print()

        # 1. Escolher formato
        console.print("[bold]Formatos disponíveis:[/bold]")
        console.print("  [1] 📄 TXT (texto simples)")
        console.print("  [2] 🌐 HTML (com gráficos - em breve)")
        console.print("  [0] Cancelar")

        opcao = input("\nEscolha o formato: ").strip()

        if opcao == "0":
            return

        if opcao == "1":
            formato = "txt"
        elif opcao == "2":
            console.print("[yellow]🌐 Relatório HTML será implementado em breve[/yellow]")
            input("Pressione Enter para continuar...")
            return
        else:
            mostrar_erro("Opção inválida!")
            return

        # 2. Confirmar
        console.print(f"\n[bold]Gerando relatório em formato {formato.upper()}...[/bold]")
        console.print("Isso pode levar alguns segundos.")

        confirmar = input("\nConfirmar? (s/N): ").strip().lower()

        if confirmar != "s":
            return

        # 3. Gerar
        try:
            with console.status("[cyan]Coletando dados e gerando relatório...[/cyan]"):
                if formato == "txt":
                    # Mostrar preview
                    console.print("\n[dim]Prévia do relatório:[/dim]")
                    console.print("-" * 40)

                    # Gerar e mostrar primeiras linhas
                    relatorio = self.gerar_relatorio.gerar_relatorio_txt()
                    linhas = relatorio.split("\n")
                    for linha in linhas[:15]:
                        console.print(linha[:80])
                    console.print("[dim]...[/dim]")

                    # Salvar
                    caminho = self.gerar_relatorio.salvar_relatorio(formato="txt")

                    if caminho:
                        mostrar_sucesso(f"Relatório salvo em: {caminho}")
                        console.print(f"  📁 {caminho}")
                    else:
                        mostrar_erro("Erro ao salvar relatório!")

        except Exception as e:
            mostrar_erro(f"Erro ao gerar relatório: {e}")

        input("\nPressione Enter para continuar...")
