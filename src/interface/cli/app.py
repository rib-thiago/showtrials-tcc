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
from src.interface.console import (
    console, 
    limpar_tela, 
    mostrar_erro,
    mostrar_sucesso,
    mostrar_aviso,
    spinner
)
from src.infrastructure.persistence.sqlite_traducao_repository import SQLiteTraducaoRepository
from src.infrastructure.translation.google_translator import (
    GoogleTranslatorAdapter, 
    TradutorComPersistenciaAdapter
)
from src.application.use_cases.traduzir_documento import TraduzirDocumento
from src.application.use_cases.listar_traducoes import ListarTraducoes
from src.interface.cli.commands_traducao import ComandoTraduzir, ComandoAlternarIdioma

class ShowTrialsApp:
    """
    Aplicação principal com injeção de dependência.
    """
    
    def __init__(self):
        # 1. Infraestrutura
        self.repo = SQLiteDocumentoRepository()
        self.repo_traducao = SQLiteTraducaoRepository()
        self.tradutor_service = GoogleTranslatorAdapter()  # Adaptador
        self.tradutor_persistente = TradutorComPersistenciaAdapter(
            self.tradutor_service, 
            self.repo_traducao
        )
        
        # 2. Casos de uso
        self.listar_use_case = ListarDocumentos(self.repo).com_traducao_nomes(True)
        self.obter_use_case = ObterDocumento(
            self.repo,
            self.repo_traducao  # <-- ADICIONAR AQUI!
        ).com_traducao_nomes(True)
        self.estatisticas_use_case = ObterEstatisticas(self.repo)
        self.traduzir_use_case = TraduzirDocumento(
            self.repo,
            self.repo_traducao,
            self.tradutor_service
        )
        self.listar_traducoes_use_case = ListarTraducoes(self.repo_traducao)
        
        # 3. Comandos
        self.cmd_listar = ComandoListar(self.listar_use_case)
        self.cmd_visualizar = ComandoVisualizar(self.obter_use_case)
        self.cmd_estatisticas = ComandoEstatisticas(self.estatisticas_use_case)
        self.cmd_traduzir = ComandoTraduzir(
            self.traduzir_use_case,
            self.listar_traducoes_use_case
        )
        self.cmd_alternar_idioma = ComandoAlternarIdioma(
            self.listar_traducoes_use_case,
            self.obter_use_case
        )
        
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
    
# src/interface/cli/app.py (SUBSTITUIR O MÉTODO _visualizar_e_aguardar)
    def _visualizar_e_aguardar(self, doc_id: int):
        """Visualiza documento com suporte a alternância de idiomas e nova tradução."""
        idioma_atual = 'original'
        
        while True:
            # Buscar documento (pode ser original ou tradução)
            if idioma_atual == 'original':
                dto = self.obter_use_case.executar(doc_id)
                texto = dto.texto if dto else None
            else:
                # Buscar tradução específica
                from src.application.use_cases.listar_traducoes import ListarTraducoes
                listar_trad = ListarTraducoes(self.repo_traducao)
                traducoes = listar_trad.executar(doc_id)
                
                traducao = next((t for t in traducoes if t.idioma == idioma_atual), None)
                if traducao:
                    # Criar um DTO temporário com o texto traduzido
                    dto = self.obter_use_case.executar(doc_id)
                    if dto:
                        dto.texto = traducao.texto_traduzido
                        # Marcar que é uma tradução
                        dto.titulo = f"{dto.titulo} [{traducao.idioma_nome}]"
                else:
                    dto = self.obter_use_case.executar(doc_id)
                    idioma_atual = 'original'
            
            if not dto:
                mostrar_erro("Documento não encontrado!")
                return
            
            # Mostrar badge do idioma atual
            from src.interface.cli.presenters_traducao import TraducaoPresenter
            console.print(TraducaoPresenter.badge_idioma_atual(idioma_atual))
            
            # Mostrar documento (sem comandos - o presenter não deve ter comandos)
            from src.interface.cli.presenters import DocumentoPresenter
            DocumentoPresenter.documento_completo(dto)
            
            # Listar traduções disponíveis (se houver)
            from src.application.use_cases.listar_traducoes import ListarTraducoes
            listar_trad = ListarTraducoes(self.repo_traducao)
            traducoes = listar_trad.executar(doc_id)
            
            if traducoes:
                console.print("\n[bold cyan]🌐 TRADUÇÕES DISPONÍVEIS:[/bold cyan]")
                for t in traducoes:
                    if t.idioma == idioma_atual and idioma_atual != 'original':
                        console.print(f"  ▶ {t.idioma_icone} {t.idioma_nome} - {t.data_traducao} [dim](atual)[/dim]")
                    else:
                        console.print(f"    {t.idioma_icone} {t.idioma_nome} - {t.data_traducao}")
            
            # COMANDOS (APENAS UMA VEZ)
            console.print("\n[dim]─────────────────────────────────────────────────[/dim]")
            console.print("[bold cyan]COMANDOS[/bold cyan]")
            console.print("  [green]⏎ Enter[/green] - Voltar à listagem")
            console.print("  [yellow]e[/yellow] - Exportar documento")
            
            if idioma_atual == 'original':
                if traducoes:
                    console.print("  [cyan]t[/cyan] - Ver tradução")
                console.print("  [blue]n[/blue] - Nova tradução")
            else:
                console.print("  [cyan]t[/cyan] - Voltar ao original")
                console.print("  [blue]n[/blue] - Nova tradução (outro idioma)")
            
            console.print()
            
            cmd = input("Comando: ").strip().lower()
            
            if cmd == '':
                break
                
            elif cmd == 't':
                # Alternar idioma
                from src.application.use_cases.listar_traducoes import ListarTraducoes
                listar_trad = ListarTraducoes(self.repo_traducao)
                
                if idioma_atual == 'original':
                    traducoes = listar_trad.executar(doc_id)
                    if traducoes:
                        idioma_atual = traducoes[0].idioma
                    else:
                        mostrar_erro("Este documento não tem traduções!")
                        continue
                else:
                    idioma_atual = 'original'
                    
            elif cmd == 'n':
                # Nova tradução
                from src.interface.cli.commands_traducao import ComandoTraduzir
                cmd_traduzir = ComandoTraduzir(
                    self.traduzir_use_case,
                    self.listar_traducoes_use_case
                )
                try:
                    resultado = cmd_traduzir.executar(doc_id)
                    if resultado:
                        idioma_atual = resultado.idioma
                        mostrar_sucesso(f"Tradução para {resultado.idioma_nome} concluída!")
                except Exception as e:
                    mostrar_erro(f"Erro durante tradução: {e}")
                    
            elif cmd == 'e':
                # Exportar (placeholder para FASE 6)
                console.print("[yellow]📥 Exportação será implementada na FASE 6[/yellow]")
                input("Pressione Enter para continuar...")
                
            else:
                mostrar_erro("Comando inválido!")


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