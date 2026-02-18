# src/interface/cli/app.py
"""
Aplicação principal com injeção de dependência.
"""

import sys
from pathlib import Path

# Adicionar src ao path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.infrastructure.registry import ServiceRegistry
from src.infrastructure.factories import (
    create_translator, 
    create_spacy_analyzer, 
    create_wordcloud_generator
)
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
    cabecalho,
    spinner
)
from src.infrastructure.persistence.sqlite_traducao_repository import SQLiteTraducaoRepository
from src.infrastructure.translation.google_translator import (
    GoogleTranslator, 
    TradutorComPersistenciaAdapter
)
from src.application.use_cases.traduzir_documento import TraduzirDocumento
from src.application.use_cases.listar_traducoes import ListarTraducoes
from src.interface.cli.commands_traducao import ComandoTraduzir, ComandoAlternarIdioma
from src.application.use_cases.exportar_documento import ExportarDocumento
from src.interface.cli.commands_export import ComandoExportar
from src.application.use_cases.gerar_relatorio import GerarRelatorio
from src.interface.cli.commands_relatorio import ComandoRelatorio
from src.application.use_cases.analisar_texto import AnalisarDocumento
from src.application.use_cases.analisar_acervo import AnalisarAcervo
from src.interface.cli.commands_analise import ComandoAnalisarDocumento, ComandoAnalisarAcervo


class ShowTrialsApp:
    """
    Aplicação principal com injeção de dependência.
    """
    
    def __init__(self):
        # =====================================================
        # 1. INFRAESTRUTURA
        # =====================================================
        self.repo = SQLiteDocumentoRepository()
        self.repo_traducao = SQLiteTraducaoRepository()
        
        # Service Registry (para lazy loading)
        self.registry = ServiceRegistry()
        
        # Registrar serviços no registry
        self.registry.register('translator', create_translator, lazy=True)
        self.registry.register('spacy', create_spacy_analyzer, lazy=True)
        self.registry.register('wordcloud', create_wordcloud_generator, lazy=True)
        
        # Tradutor (pode ser usado diretamente ou via registry)
        self.tradutor_service = GoogleTranslator()
        self.tradutor_persistente = TradutorComPersistenciaAdapter(
            self.tradutor_service, 
            self.repo_traducao
        )
        
        # =====================================================
        # 2. CASOS DE USO
        # =====================================================
        
        # Casos que não precisam de registry
        self.listar_use_case = ListarDocumentos(self.repo).com_traducao_nomes(True)
        self.obter_use_case = ObterDocumento(
            self.repo,
            self.repo_traducao
        ).com_traducao_nomes(True)
        self.estatisticas_use_case = ObterEstatisticas(self.repo)
        self.exportar_use_case = ExportarDocumento(self.repo, self.repo_traducao)
        self.relatorio_use_case = GerarRelatorio(self.repo, self.repo_traducao)
        
        # Casos que usam registry (CORRIGIDOS!)
        self.traduzir_use_case = TraduzirDocumento(
            repo_doc=self.repo,
            repo_trad=self.repo_traducao,
            registry=self.registry  # ← Agora passa o registry
        )
        
        self.analisar_documento_use_case = AnalisarDocumento(
            repo_doc=self.repo,
            repo_trad=self.repo_traducao,
            registry=self.registry  # ← Corrigido também (opcional, mas consistente)
        )
        
        self.analisar_acervo_use_case = AnalisarAcervo(
            repo_doc=self.repo,
            registry=self.registry  # ← Corrigido também
        )
        
        # Casos auxiliares
        self.listar_traducoes_use_case = ListarTraducoes(self.repo_traducao)
        
        # =====================================================
        # 3. COMANDOS
        # =====================================================
        self.cmd_listar = ComandoListar(self.listar_use_case)
        self.cmd_visualizar = ComandoVisualizar(self.obter_use_case)
        self.cmd_estatisticas = ComandoEstatisticas(self.estatisticas_use_case)
        self.cmd_exportar = ComandoExportar(self.exportar_use_case)
        self.cmd_relatorio = ComandoRelatorio(self.relatorio_use_case)
        
        # Comandos de tradução
        self.cmd_traduzir = ComandoTraduzir(
            self.traduzir_use_case,
            self.listar_traducoes_use_case
        )
        self.cmd_alternar_idioma = ComandoAlternarIdioma(
            self.listar_traducoes_use_case,
            self.obter_use_case
        )
        
        # Comandos de análise
        self.cmd_analisar_doc = ComandoAnalisarDocumento(self.analisar_documento_use_case)
        self.cmd_analisar_acervo = ComandoAnalisarAcervo(self.analisar_acervo_use_case)
        
        # =====================================================
        # 4. MENUS
        # =====================================================
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
            
            if escolha == '7':
                console.print("\n[green]Até logo![/green]")
                break
            
            elif escolha == '1':
                doc_id = self.cmd_listar.executar()
                if doc_id:
                    self._visualizar_e_aguardar(doc_id)
            
            elif escolha == '2':
                centro = self.menu_centro.mostrar()
                if centro:
                    doc_id = self.cmd_listar.executar(centro=centro)
                    if doc_id:
                        self._visualizar_e_aguardar(doc_id)
            
            elif escolha == '3':
                try:
                    doc_id = int(input("ID do documento: "))
                    self._visualizar_e_aguardar(doc_id)
                except ValueError:
                    mostrar_erro("ID inválido!")
            
            elif escolha == '4':
                self.cmd_estatisticas.executar()

            elif escolha == '5':
                self.cmd_relatorio.executar()

            elif escolha == '6':
                self._menu_analise()
    
    def _menu_analise(self):
        """Menu de análise de texto."""
        while True:
            limpar_tela()
            cabecalho("🔍 ANÁLISE DE TEXTO")
            
            console.print("[bold cyan]Opções:[/bold cyan]")
            console.print("  [1] Analisar documento específico")
            console.print("  [2] Análise global do acervo")
            console.print("  [3] Nuvem de palavras do acervo")
            console.print("  [0] Voltar")
            
            opcao = input("\nEscolha: ").strip()
            
            if opcao == '0':
                break
            elif opcao == '1':
                try:
                    doc_id = int(input("ID do documento: "))
                    self.cmd_analisar_doc.executar(doc_id)
                except ValueError:
                    mostrar_erro("ID inválido!")
            elif opcao == '2':
                self.cmd_analisar_acervo.executar()
            elif opcao == '3':
                console.print("[yellow]Gerando nuvem de palavras do acervo...[/yellow]")
                try:
                    caminho = self.analisar_acervo_use_case.gerar_wordcloud_geral()
                    mostrar_sucesso(f"Nuvem gerada em: {caminho}")
                except Exception as e:
                    mostrar_erro(f"Erro: {e}")
                input("\nPressione Enter...")
            else:
                mostrar_erro("Opção inválida!")
    
    def _visualizar_e_aguardar(self, doc_id: int):
        """Visualiza documento com suporte a alternância de idiomas e nova tradução."""
        idioma_atual = 'original'
        
        while True:
            # Buscar documento (pode ser original ou tradução)
            if idioma_atual == 'original':
                dto = self.obter_use_case.executar(doc_id)
                texto = dto.texto if dto else None
            else:
                from src.application.use_cases.listar_traducoes import ListarTraducoes
                listar_trad = ListarTraducoes(self.repo_traducao)
                traducoes = listar_trad.executar(doc_id)
                
                traducao = next((t for t in traducoes if t.idioma == idioma_atual), None)
                if traducao:
                    dto = self.obter_use_case.executar(doc_id)
                    if dto:
                        dto.texto = traducao.texto_traduzido
                        dto.titulo = f"{dto.titulo} [{traducao.idioma_nome}]"
                else:
                    dto = self.obter_use_case.executar(doc_id)
                    idioma_atual = 'original'
            
            if not dto:
                mostrar_erro("Documento não encontrado!")
                return
            
            from src.interface.cli.presenters_traducao import TraducaoPresenter
            console.print(TraducaoPresenter.badge_idioma_atual(idioma_atual))
            
            from src.interface.cli.presenters import DocumentoPresenter
            DocumentoPresenter.documento_completo(dto)
            
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
                self.cmd_exportar.executar(doc_id)
                input("\nPressione Enter para continuar...")
                
            else:
                mostrar_erro("Comando inválido!")
    
    def _exportar_documento(self, doc_id: int):
        """Exporta documento (placeholder)."""
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