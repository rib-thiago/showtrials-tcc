# app.py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SHOWTRIALS - Sistema de Coleta e Gestão de Documentos
Versão 2.0 - UI Aprimorada
"""

import sys
from pathlib import Path

# Adicionar diretório atual ao path
sys.path.insert(0, str(Path(__file__).parent))

from ui import (
    console, limpar_tela, cabecalho, menu_principal,
    mensagem_sucesso, mensagem_erro, mensagem_aviso, spinner_processo
)
from db import contar
from nav_ui import (
    navegar_lista, visualizar_documento_ui, 
    exportar_documento_ui, reimportar_documento_ui
)
from rich.panel import Panel  # <--- ADICIONAR ESTA LINHA
from rich.table import Table  # <--- ADICIONAR ESTA LINHA
from rich import box          # <--- ADICIONAR ESTA LINHA (opcional, mas usado)
import time


# app.py - Substitua a função mostrar_estatisticas INTEIRA por esta:

def mostrar_estatisticas():
    """Wrapper para exibir estatísticas completas do acervo"""
    try:
        from db import estatisticas_completas
        
        # Buscar estatísticas completas do banco
        stats = estatisticas_completas()
        
        limpar_tela()
        cabecalho("📊 ESTATÍSTICAS DO ACERVO")
        
        # CARD PRINCIPAL
        console.print(Panel.fit(
            f"[bold cyan]📚 TOTAL DE DOCUMENTOS: {stats['total_docs']}[/bold cyan]\n"
            f"[bold green]🌐 TOTAL DE TRADUÇÕES: {stats['total_traducoes']}[/bold green]",
            border_style="bright_blue",
            padding=(1, 4)
        ))
        console.print()
        
        # GRID DE ESTATÍSTICAS
        from rich.table import Table
        from rich import box
        
        # Documentos por centro
        if stats['docs_por_centro']:
            console.print("[bold cyan]🏛️ DOCUMENTOS POR CENTRO:[/bold cyan]")
            table_centro = Table(box=box.SIMPLE, header_style="bold yellow")
            table_centro.add_column("Centro", style="yellow")
            table_centro.add_column("Quantidade", justify="right", style="cyan")
            
            for centro, count in stats['docs_por_centro'].items():
                nome_centro = "Leningrad Center" if centro == "lencenter" else "Moscow Center"
                table_centro.add_row(nome_centro, str(count))
            
            console.print(table_centro)
            console.print()
        
        # Traduções por idioma
        if stats['traducoes_por_idioma']:
            console.print("[bold green]🌐 TRADUÇÕES POR IDIOMA:[/bold green]")
            table_idioma = Table(box=box.SIMPLE, header_style="bold green")
            table_idioma.add_column("Idioma", style="green")
            table_idioma.add_column("Quantidade", justify="right", style="cyan")
            table_idioma.add_column("Custo Total", justify="right", style="yellow")
            
            idiomas_nomes = {
                'en': 'Inglês 🇺🇸',
                'pt': 'Português 🇧🇷', 
                'es': 'Espanhol 🇪🇸',
                'fr': 'Francês 🇫🇷'
            }
            
            for idioma, count in stats['traducoes_por_idioma'].items():
                nome = idiomas_nomes.get(idioma, idioma.upper())
                # Calcular custo aproximado por idioma
                custo_idioma = 0
                if stats.get('custo_total'):
                    # Distribuição proporcional simples
                    custo_idioma = (count / stats['total_traducoes']) * stats['custo_total']
                
                table_idioma.add_row(
                    nome, 
                    str(count),
                    f"${custo_idioma:.4f}"
                )
            
            console.print(table_idioma)
            console.print()
        
        # MÉTRICAS DE TRADUÇÃO
        console.print("[bold magenta]📈 MÉTRICAS DE TRADUÇÃO:[/bold magenta]")
        
        metrics_table = Table(box=box.SIMPLE, header_style="bold magenta")
        metrics_table.add_column("Métrica", style="white")
        metrics_table.add_column("Valor", justify="right", style="cyan")
        
        # Documentos traduzidos (pelo menos 1 tradução)
        percentual = (stats['docs_com_traducao'] / stats['total_docs'] * 100) if stats['total_docs'] > 0 else 0
        metrics_table.add_row(
            "📄 Documentos com tradução",
            f"{stats['docs_com_traducao']} ({percentual:.1f}%)"
        )
        
        # Média de traduções por documento traduzido
        if stats['docs_com_traducao'] > 0:
            media = stats['total_traducoes'] / stats['docs_com_traducao']
            metrics_table.add_row(
                "🔄 Média de traduções por documento",
                f"{media:.1f}"
            )
        
        # Custo total
        metrics_table.add_row(
            "💰 Custo total estimado",
            f"${stats['custo_total']:.4f} USD"
        )
        
        console.print(metrics_table)
        console.print()
        
        # TAGS (placeholder para versão futura)
        if stats.get('tags_mais_usadas'):
            console.print("[bold yellow]🏷️ TAGS MAIS UTILIZADAS:[/bold yellow]")
            tags_text = " • ".join([f"#{tag}" for tag, _ in stats['tags_mais_usadas'][:5]])
            console.print(Panel(tags_text, border_style="yellow", padding=(1, 2)))
            console.print()
        
        # RODAPÉ
        console.print("[dim]─────────────────────────────────────────────────[/dim]")
        console.print("[bold cyan]📊 Estatísticas atualizadas em tempo real[/bold cyan]")
        console.print()
        
        input("[bold cyan]Pressione Enter para voltar ao menu...[/bold cyan]")
        
    except Exception as e:
        mensagem_erro(f"Erro ao carregar estatísticas: {e}")
        import traceback
        traceback.print_exc()
        time.sleep(3)

def main():
    """Função principal da aplicação"""
    try:
        while True:
            escolha = menu_principal()
            
            if escolha == "0":
                console.print()
                console.print("[bold green]✓ Encerrando sistema...[/bold green]")
                console.print("[bold cyan]Até logo! 👋[/bold cyan]")
                console.print()
                break
            
            elif escolha == "1":
                navegar_lista()
            
            elif escolha == "2":
                console.print()
                console.print("[bold cyan]Centros disponíveis:[/bold cyan]")
                console.print("  [1] 🏛️ Leningrad Center")
                console.print("  [2] 🏛️ Moscow Center")
                console.print()
                
                opcao = input("Escolha o centro (1/2): ").strip()
                
                if opcao == "1":
                    navegar_lista("lencenter")
                elif opcao == "2":
                    navegar_lista("moscenter")
                else:
                    mensagem_erro("Opção inválida!")
                    time.sleep(1)
            
            elif escolha == "3":
                try:
                    doc_id = int(input("ID do documento: ").strip())
                    visualizar_documento_ui(doc_id)
                except ValueError:
                    mensagem_erro("ID inválido!")
                    time.sleep(1)
            
            elif escolha == "4":
                try:
                    doc_id = int(input("ID do documento: ").strip())
                    exportar_documento_ui(doc_id)
                except ValueError:
                    mensagem_erro("ID inválido!")
                    time.sleep(1)
            
            elif escolha == "5":
                reimportar_documento_ui()
            
    # app.py - Substitua a opção 6 (tradução) por este código

            elif escolha == "6":
                # TRADUZIR DOCUMENTO COM PERSISTÊNCIA
                try:
                    doc_id = int(input("ID do documento para traduzir: ").strip())
                    
                    # Importar módulos
                    from translator import tradutor_global, criar_tradutor_da_configuracao, TradutorComPersistencia
                    from db import obter_documento, obter_traducao, listar_traducoes_documento
                    
                    # Verificar tradutor
                    tradutor = tradutor_global or criar_tradutor_da_configuracao()
                    if not tradutor:
                        mensagem_erro("Tradutor não configurado!")
                        time.sleep(2)
                        continue
                    
                    # Buscar documento
                    doc = obter_documento(doc_id)
                    if not doc:
                        mensagem_erro("Documento não encontrado!")
                        time.sleep(1.5)
                        continue
                    
                    # MOSTRAR TRADUÇÕES EXISTENTES
                    traducoes_existentes = listar_traducoes_documento(doc_id)
                    
                    if traducoes_existentes:
                        console.print("\n[bold green]📚 Traduções existentes:[/bold green]")
                        for t in traducoes_existentes:
                            idioma_nome = {
                                'en': 'Inglês',
                                'pt': 'Português',
                                'es': 'Espanhol',
                                'fr': 'Francês'
                            }.get(t['idioma'], t['idioma'].upper())
                            
                            console.print(f"  • {idioma_nome}: {t['data_traducao'][:10]} "
                                        f"(custo: ${t['custo']:.4f})")
                        console.print()
                    
                    # ESCOLHER IDIOMA
                    console.print("[bold cyan]🌐 Idiomas disponíveis:[/bold cyan]")
                    console.print("  [1] Inglês (en) - Recomendado")
                    console.print("  [2] Português (pt)")
                    console.print("  [3] Espanhol (es)")
                    console.print("  [4] Francês (fr)")
                    console.print("  [0] Cancelar")
                    
                    idioma_opcao = input("\nEscolha o idioma destino (0-4): ").strip()
                    
                    if idioma_opcao == '0':
                        mensagem_aviso("Tradução cancelada")
                        time.sleep(1)
                        continue
                    
                    idiomas = {
                        '1': 'en',
                        '2': 'pt', 
                        '3': 'es',
                        '4': 'fr'
                    }
                    
                    if idioma_opcao not in idiomas:
                        mensagem_erro("Opção inválida!")
                        time.sleep(1)
                        continue
                    
                    idioma_destino = idiomas[idioma_opcao]
                    
                    # VERIFICAR SE JÁ EXISTE PARA ESTE IDIOMA
                    traducao_existente = obter_traducao(doc_id, idioma_destino)
                    
                    if traducao_existente:
                        console.print(f"\n[bold yellow]⚠ Já existe tradução para {idioma_destino}[/bold yellow]")
                        console.print(f"   Data: {traducao_existente['data_traducao']}")
                        console.print(f"   Custo: ${traducao_existente['custo']:.4f}")
                        
                        opcao = input("\n[D] Visualizar existente | [N] Nova tradução | [C] Cancelar: ").strip().lower()
                        
                        if opcao == 'd':
                            # Mostrar tradução existente
                            console.print("\n[bold]📄 TRADUÇÃO EXISTENTE:[/bold]")
                            console.print("─" * 80)
                            console.print(traducao_existente['texto'][:2000] + "...")
                            console.print("─" * 80)
                            input("\nPressione Enter para continuar...")
                            continue
                        elif opcao == 'c':
                            mensagem_aviso("Operação cancelada")
                            time.sleep(1)
                            continue
                    
                    # CONFIRMAR CUSTO
                    chars = len(doc[5])
                    custo_estimado = chars * 0.000020
                    
                    console.print(f"\n[bold]📊 Estimativa de custo:[/bold]")
                    console.print(f"  Caracteres: {chars:,}")
                    console.print(f"  Custo: [yellow]${custo_estimado:.4f}[/yellow] (USD)")
                    
                    confirmar = input("\nConfirmar tradução? (s/N): ").strip().lower()
                    
                    if confirmar != 's':
                        mensagem_aviso("Tradução cancelada")
                        time.sleep(1)
                        continue
                    
                    # TRADUZIR E SALVAR
                    console.print(f"\n[bold green]🌐 Traduzindo documento {doc_id} para {idioma_destino}...[/bold green]")
                    
                    # Usar o Tradutor com persistência
                    persisted_translator = TradutorComPersistencia(tradutor)
                    
                    resultado = spinner_processo(
                        "Traduzindo documento...",
                        persisted_translator.traduzir_e_salvar,
                        doc_id,
                        doc[5],
                        destino=idioma_destino
                    )
                    
                    # SUCESSO!
                    console.print("\n[bold green]✅ Tradução concluída e SALVA no banco de dados![/bold green]")
                    console.print(f"  📊 ID da tradução: {resultado['id']}")
                    console.print(f"  💰 Custo real: ${resultado['custo']:.4f}")
                    
                    # PERGUNTAR SE QUER EXPORTAR
                    exportar = input("\nExportar texto traduzido para arquivo? (s/N): ").strip().lower()
                    
                    if exportar == 's':
                        from nav_ui import exportar_texto_direto
                        nome_arquivo = f"doc{doc_id}_{idioma_destino}_traducao.txt"
                        exportar_texto_direto(resultado['texto'], nome_arquivo)
                    
                except ValueError:
                    mensagem_erro("ID inválido!")
                except Exception as e:
                    mensagem_erro(f"Erro na tradução: {e}")
                    import traceback
                    traceback.print_exc()
                
                time.sleep(2)
            
            elif escolha == "7":
                mostrar_estatisticas()
    
    except KeyboardInterrupt:
        console.print()
        console.print("[bold yellow]⚠ Operação interrompida pelo usuário[/bold yellow]")
        console.print("[bold cyan]Até logo! 👋[/bold cyan]")
        sys.exit(0)


# app.py - Adicione esta função no final, antes do if __name__

def traduzir_documento_interativo(doc_id):
    """Função auxiliar chamada pelo nav_ui.py para nova tradução"""
    try:
        from translator import tradutor_global, criar_tradutor_da_configuracao, TradutorComPersistencia
        from db import obter_documento, obter_traducao
        
        # Verificar tradutor
        tradutor = tradutor_global or criar_tradutor_da_configuracao()
        if not tradutor:
            mensagem_erro("Tradutor não configurado!")
            return
        
        # Buscar documento
        doc = obter_documento(doc_id)
        if not doc:
            mensagem_erro("Documento não encontrado!")
            return
        
        # Escolher idioma
        console.print("\n[bold cyan]🌐 Idiomas disponíveis:[/bold cyan]")
        console.print("  [1] Inglês (en)")
        console.print("  [2] Português (pt)")
        console.print("  [3] Espanhol (es)")
        console.print("  [4] Francês (fr)")
        console.print("  [0] Cancelar")
        
        idioma_opcao = input("\nEscolha o idioma destino (0-4): ").strip()
        
        if idioma_opcao == '0':
            mensagem_aviso("Tradução cancelada")
            return
        
        idiomas = {'1': 'en', '2': 'pt', '3': 'es', '4': 'fr'}
        if idioma_opcao not in idiomas:
            mensagem_erro("Opção inválida!")
            return
        
        idioma_destino = idiomas[idioma_opcao]
        
        # Confirmar custo
        chars = len(doc[5])
        custo_estimado = chars * 0.000020
        
        console.print(f"\n[bold]📊 Estimativa de custo:[/bold]")
        console.print(f"  Caracteres: {chars:,}")
        console.print(f"  Custo: [yellow]${custo_estimado:.4f}[/yellow]")
        
        confirmar = input("\nConfirmar tradução? (s/N): ").strip().lower()
        if confirmar != 's':
            mensagem_aviso("Tradução cancelada")
            return
        
        # Traduzir e salvar
        persisted_translator = TradutorComPersistencia(tradutor)
        resultado = spinner_processo(
            "Traduzindo documento...",
            persisted_translator.traduzir_e_salvar,
            doc_id,
            doc[5],
            destino=idioma_destino
        )
        
        mensagem_sucesso(f"Tradução concluída! ID: {resultado['id']}")
        
    except Exception as e:
        mensagem_erro(f"Erro na tradução: {e}")

if __name__ == "__main__":
    main()