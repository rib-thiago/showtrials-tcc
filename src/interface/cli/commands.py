# src/interface/cli/commands.py
"""
Comandos da CLI - Cada comando é uma ação do usuário.
"""

from typing import Optional
from src.interface.console import console, limpar_tela, cabecalho, mostrar_erro
from src.interface.cli.presenters import DocumentoPresenter


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
                pagina=pagina,
                limite=limite,
                centro=centro,
                tipo=tipo
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
            
            if cmd == 'n' and pagina < resultados['total_paginas']:
                pagina += 1
            elif cmd == 'p' and pagina > 1:
                pagina -= 1
            elif cmd == 'm':
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