# src/interface/cli/commands_traducao.py
"""
Comandos de tradução para a CLI.
"""

from typing import Optional
from src.interface import console
from src.interface.cli.presenters import DocumentoPresenter
from src.interface.cli.presenters_traducao import TraducaoPresenter


class ComandoTraduzir:
    """Comando para criar nova tradução."""
    
    def __init__(self, traduzir_use_case, listar_trad_use_case):
        self.traduzir_use_case = traduzir_use_case
        self.listar_trad_use_case = listar_trad_use_case
        self.presenter = TraducaoPresenter()
    
    def executar(self, documento_id: int):
        """Executa tradução interativa."""
        # 1. Mostrar traduções existentes
        traducoes = self.listar_trad_use_case.executar(documento_id)
        
        if traducoes:
            console.console.print("\n[bold cyan]🌐 Traduções existentes:[/bold cyan]")
            for t in traducoes:
                console.console.print(
                    f"  • {self.presenter.badge_idioma(t.idioma)} - "
                    f"{t.idioma_nome} [dim]({t.data_traducao})[/dim]"
                )
        
        # 2. Escolher idioma
        console.console.print("\n[bold cyan]Idiomas disponíveis para nova tradução:[/bold cyan]")
        console.console.print("  [1] 🇺🇸 Inglês (en)")
        console.console.print("  [2] 🇧🇷 Português (pt)")
        console.console.print("  [3] 🇪🇸 Espanhol (es)")
        console.console.print("  [4] 🇫🇷 Francês (fr)")
        console.console.print("  [0] Cancelar")
        
        opcao = input("\nEscolha o idioma: ").strip()
        
        idiomas = {
            '1': 'en',
            '2': 'pt',
            '3': 'es',
            '4': 'fr'
        }
        
        if opcao == '0':
            return None
        if opcao not in idiomas:
            console.mostrar_erro("Opção inválida!")
            return None
        
        idioma = idiomas[opcao]
        
        # 3. Verificar se já existe (confirmar substituição)
        existente = next((t for t in traducoes if t.idioma == idioma), None)
        if existente:
            console.console.print(f"\n[yellow]⚠ Já existe tradução para {existente.idioma_nome}[/yellow]")
            console.console.print(f"   Data: {existente.data_traducao}")
            console.console.print(f"   Custo: ${existente.custo:.4f}")
            
            confirmar = input("Substituir? (s/N): ").strip().lower()
            if confirmar != 's':
                return None
        
        # 4. Estimar custo
        console.console.print("\n[bold]📊 Estimativa de custo:[/bold]")
        console.console.print("  • Preço: $0.000020 por caractere")
        console.console.print("  • Confirme na próxima etapa")
        
        confirmar = input("\nConfirmar tradução? (s/N): ").strip().lower()
        if confirmar != 's':
            return None
        
        # 5. Traduzir (com spinner)
        try:
            resultado = console.spinner(
                f"🌐 Traduzindo para {idioma}...",
                self.traduzir_use_case.executar,
                documento_id,
                idioma,
                forcar_novo=True
            )
            
            console.mostrar_sucesso(f"✅ Tradução concluída! ({resultado.idioma_nome})")
            console.mostrar_sucesso(f"   Custo: ${resultado.custo:.4f}")
            
            return resultado
            
        except Exception as e:
            console.mostrar_erro(f"Erro na tradução: {e}")
            return None


class ComandoAlternarIdioma:
    """Comando para alternar entre idiomas durante visualização."""
    
    def __init__(self, listar_trad_use_case, obter_documento_use_case):
        self.listar_trad_use_case = listar_trad_use_case
        self.obter_documento_use_case = obter_documento_use_case
        self.presenter_doc = DocumentoPresenter()
        self.presenter_trad = TraducaoPresenter()
    
    def executar(self, documento_id: int, idioma_atual: str = 'original') -> str:
        """
        Alterna entre original e traduções disponíveis.
        Retorna o novo idioma selecionado.
        """
        traducoes = self.listar_trad_use_case.executar(documento_id)
        
        if not traducoes:
            console.mostrar_erro("Este documento não tem traduções.")
            return 'original'
        
        # Determinar próximo idioma
        if idioma_atual == 'original':
            return traducoes[0].idioma
        else:
            idiomas = [t.idioma for t in traducoes]
            try:
                idx = idiomas.index(idioma_atual)
                if idx + 1 < len(idiomas):
                    return idiomas[idx + 1]
                else:
                    return 'original'
            except ValueError:
                return traducoes[0].idioma