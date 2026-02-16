# src/interface/cli/app.py
"""
Aplicação principal com injeção de dependência.
"""

import sys
from pathlib import Path

# Adicionar src ao path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.infrastructure.persistence.sqlite_repository import SQLiteDocumentoRepository
from src.infrastructure.persistence.migrations import criar_tabelas, migrar_banco_existente
from src.application.use_cases.listar_documentos import ListarDocumentos
from src.application.use_cases.obter_documento import ObterDocumento
from src.application.use_cases.estatisticas import ObterEstatisticas
from src.interface.cli.menu import MenuPrincipal, MenuCentro
from src.interface.cli.commands import ComandoListar, ComandoVisualizar, ComandoEstatisticas
from src.interface.console import console, limpar_tela, mostrar_erro


class ShowTrialsApp:
    """
    Aplicação principal com injeção de dependência.
    """
    
    def __init__(self):
        # 1. Infraestrutura
        self.repo = SQLiteDocumentoRepository()
        
        # 2. Casos de uso
        self.listar_use_case = ListarDocumentos(self.repo).com_traducao_nomes(True)
        self.obter_use_case = ObterDocumento(self.repo).com_traducao_nomes(True)
        self.estatisticas_use_case = ObterEstatisticas(self.repo)
        
        # 3. Comandos
        self.cmd_listar = ComandoListar(self.listar_use_case)
        self.cmd_visualizar = ComandoVisualizar(self.obter_use_case)
        self.cmd_estatisticas = ComandoEstatisticas(self.estatisticas_use_case)
        
        # 4. Menus
        self.menu_principal = MenuPrincipal(self)
        self.menu_centro = MenuCentro()
    
    def inicializar_banco(self):
        """Garante que o banco está pronto."""
        criar_tabelas()
        migrar_banco_existente()
        console.print("[green]✅ Banco de dados pronto[/green]")
    
    def run(self):
        """Loop principal da aplicação."""
        self.inicializar_banco()
        
        while True:
            escolha = self.menu_principal.mostrar()
            
            if escolha == '5':
                console.print("\n[green]Até logo![/green]")
                break
            
            elif escolha == '1':
                # Listar todos
                doc_id = self.cmd_listar.executar()
                if doc_id:
                    self._visualizar_e_aguardar(doc_id)
            
            elif escolha == '2':
                # Listar por centro
                centro = self.menu_centro.mostrar()
                if centro:
                    doc_id = self.cmd_listar.executar(centro=centro)
                    if doc_id:
                        self._visualizar_e_aguardar(doc_id)
            
            elif escolha == '3':
                # Visualizar direto por ID
                try:
                    doc_id = int(input("ID do documento: "))
                    self._visualizar_e_aguardar(doc_id)
                except ValueError:
                    mostrar_erro("ID inválido!")
            
            elif escolha == '4':
                # Estatísticas
                self.cmd_estatisticas.executar()
    
    def _visualizar_e_aguardar(self, doc_id: int):
        """Visualiza documento e trata retorno."""
        cmd = self.cmd_visualizar.executar(doc_id)
        if cmd == 'e':
            self._exportar_documento(doc_id)
    
    def _exportar_documento(self, doc_id: int):
        """Exporta documento (placeholder - será implementado)."""
        console.print("[yellow]Exportação será implementada[/yellow]")
        input("Pressione Enter...")


def main():
    """Ponto de entrada da aplicação."""
    try:
        app = ShowTrialsApp()
        app.run()
    except KeyboardInterrupt:
        console.print("\n[yellow]Operação interrompida[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"[red]Erro fatal: {e}[/red]")
        sys.exit(1)


if __name__ == "__main__":
    main()