# src/interface/cli/commands_export.py
"""
Comandos de exportação para a CLI.
"""

from src.interface.console import console, mostrar_erro, mostrar_sucesso


class ComandoExportar:
    """Comando para exportar documento."""

    def __init__(self, exportar_use_case):
        self.exportar_use_case = exportar_use_case

    def executar(self, documento_id: int):
        """Executa exportação interativa."""
        # 1. Listar idiomas disponíveis
        idiomas = self.exportar_use_case.listar_idiomas_disponiveis(documento_id)

        console.print("\n[bold cyan]📥 EXPORTAR DOCUMENTO[/bold cyan]")
        console.print("\n[bold]Idiomas disponíveis:[/bold]")

        for i, idioma in enumerate(idiomas, 1):
            if idioma["codigo"] == "original":
                console.print(f"  [{i}] 🇷🇺 {idioma['nome']}")
            else:
                console.print(f"  [{i}] {idioma['icone']} {idioma['nome']}")

        console.print("  [0] Cancelar")

        opcao = input("\nEscolha o idioma: ").strip()

        if opcao == "0":
            return

        try:
            idx = int(opcao) - 1
            if idx < 0 or idx >= len(idiomas):
                mostrar_erro("Opção inválida!")
                return
        except ValueError:
            mostrar_erro("Opção inválida!")
            return

        idioma = idiomas[idx]["codigo"]

        # 2. Escolher formato
        console.print("\n[bold]Formatos disponíveis:[/bold]")
        console.print("  [1] 📄 TXT (recomendado)")
        console.print("  [2] 📑 PDF (em breve)")
        console.print("  [0] Cancelar")

        opcao = input("\nEscolha o formato: ").strip()

        if opcao == "0":
            return

        if opcao == "1":
            formato = "txt"
        elif opcao == "2":
            console.print("[yellow]📑 Exportação PDF será implementada em breve[/yellow]")
            return
        else:
            mostrar_erro("Opção inválida!")
            return

        # 3. Incluir metadados?
        console.print("\n[bold]Incluir metadados no arquivo?[/bold]")
        console.print("  [1] Sim (recomendado)")
        console.print("  [2] Não (só o texto)")

        opcao = input("\nEscolha: ").strip()

        incluir_metadados = opcao == "1"

        # 4. Confirmar
        console.print("\n[bold]Resumo da exportação:[/bold]")
        console.print(f"  • Documento ID: {documento_id}")
        console.print(f"  • Idioma: {idiomas[idx]['nome']}")
        console.print(f"  • Formato: {formato.upper()}")
        console.print(f"  • Metadados: {'Sim' if incluir_metadados else 'Não'}")

        confirmar = input("\nConfirmar exportação? (s/N): ").strip().lower()

        if confirmar != "s":
            return

        # 5. Exportar
        try:
            resultado = self.exportar_use_case.executar(
                documento_id=documento_id,
                formato=formato,
                idioma=idioma,
                incluir_metadados=incluir_metadados,
            )

            if resultado["sucesso"]:
                mostrar_sucesso("Documento exportado com sucesso!")
                console.print(f"  📁 {resultado['caminho']}")
                if "tamanho" in resultado:
                    console.print(f"  📊 Tamanho: {resultado['tamanho']} caracteres")
            else:
                mostrar_erro(resultado["erro"])

        except Exception as e:
            mostrar_erro(f"Erro na exportação: {e}")
