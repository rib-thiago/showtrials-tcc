# src/interface/cli/commands_analise.py
"""
Comandos de análise de texto para a CLI.
"""

from src.interface.console import console, mostrar_erro, mostrar_sucesso, spinner
from src.interface.cli.presenters_analise import AnalisePresenter


class ComandoAnalisarDocumento:
    """Comando para analisar um documento específico."""
    
    def __init__(self, analisar_documento_use_case):
        self.analisar = analisar_documento_use_case
        self.presenter = AnalisePresenter()
    
    def executar(self, documento_id: int):
        """Executa análise interativa."""
        console.print("\n[bold cyan]🔍 ANÁLISE DE DOCUMENTO[/bold cyan]")
        console.print()
        
        # 1. Escolher idioma
        console.print("[bold]Idioma para análise:[/bold]")
        console.print("  [1] 🇷🇺 Original (Russo)")
        console.print("  [2] 🇺🇸 Inglês (se disponível)")
        console.print("  [3] 🇧🇷 Português (se disponível)")
        console.print("  [0] Cancelar")
        
        opcao = input("\nEscolha: ").strip()
        
        idiomas = {
            '1': 'ru',
            '2': 'en',
            '3': 'pt'
        }
        
        if opcao == '0':
            return
        if opcao not in idiomas:
            mostrar_erro("Opção inválida!")
            return
        
        idioma = idiomas[opcao]
        
        # 2. Gerar wordcloud?
        console.print("\n[bold]Gerar nuvem de palavras?[/bold]")
        console.print("  [1] Sim")
        console.print("  [2] Não")
        
        opcao = input("\nEscolha: ").strip()
        gerar_wordcloud = (opcao == '1')
        
        # 3. Confirmar
        console.print(f"\n[bold]Analisando documento {documento_id}...[/bold]")
        console.print(f"  • Idioma: {idioma}")
        console.print(f"  • Nuvem de palavras: {'Sim' if gerar_wordcloud else 'Não'}")
        
        confirmar = input("\nConfirmar? (s/N): ").strip().lower()
        if confirmar != 's':
            return
        
        # 4. Analisar
        try:
            with console.status("[cyan]Processando texto..."):
                resultado = spinner(
                    "Analisando documento...",
                    self.analisar.executar,
                    documento_id,
                    idioma,
                    gerar_wordcloud
                )
            
            if resultado:
                self.presenter.mostrar_analise(resultado)
            else:
                mostrar_erro("Documento ou tradução não encontrado!")
                
        except Exception as e:
            mostrar_erro(f"Erro na análise: {e}")
        
        input("\nPressione Enter para continuar...")


class ComandoAnalisarAcervo:
    """Comando para análise global do acervo."""
    
    def __init__(self, analisar_acervo_use_case):
        self.analisar = analisar_acervo_use_case
        self.presenter = AnalisePresenter()
    
    def executar(self):
        """Executa análise global."""
        console.print("\n[bold cyan]📊 ANÁLISE GLOBAL DO ACERVO[/bold cyan]")
        console.print()
        
        console.print("[bold]Opções:[/bold]")
        console.print("  [1] Estatísticas globais")
        console.print("  [2] Nuvem de palavras do acervo")
        console.print("  [0] Cancelar")
        
        opcao = input("\nEscolha: ").strip()
        
        if opcao == '0':
            return
        
        elif opcao == '1':
            with console.status("[cyan]Calculando estatísticas..."):
                stats = self.analisar.estatisticas_globais()
            self.presenter.mostrar_estatisticas_globais(stats)
        
        elif opcao == '2':
            console.print("\n[bold]Idioma para nuvem de palavras:[/bold]")
            console.print("  [1] 🇷🇺 Russo")
            console.print("  [2] 🇺🇸 Inglês")
            
            opcao_idioma = input("\nEscolha: ").strip()
            idioma = 'ru' if opcao_idioma == '1' else 'en'
            
            with console.status("[cyan]Gerando nuvem de palavras..."):
                caminho = self.analisar.gerar_wordcloud_geral(idioma)
            
            mostrar_sucesso(f"Nuvem de palavras gerada em: {caminho}")
        
        input("\nPressione Enter para continuar...")