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

import time

from nav_ui import (
    exportar_documento_ui,
    navegar_lista,
    reimportar_documento_ui,
    visualizar_documento_ui,
)
from rich import box  # <--- ADICIONAR ESTA LINHA (opcional, mas usado)
from rich.panel import Panel  # <--- ADICIONAR ESTA LINHA
from rich.table import Table  # <--- ADICIONAR ESTA LINHA
from ui import (
    badge_idioma,
    cabecalho,
    console,
    limpar_tela,
    mensagem_aviso,
    mensagem_erro,
    mensagem_sucesso,
    menu_principal,
    spinner_processo,
)

# app.py - Substitua a função mostrar_estatisticas INTEIRA por esta:


def mostrar_estatisticas():
    """Exibe estatísticas completas do acervo com metadados enriquecidos"""
    try:

        from db import conectar
        from translators.nomes import transliterar_nome
        from ui import badge_tipo_documento

        conn = conectar()
        cursor = conn.cursor()

        limpar_tela()
        cabecalho("📊 ESTATÍSTICAS DO ACERVO")

        # =========================================
        # 1. VISÃO GERAL
        # =========================================
        cursor.execute("SELECT COUNT(*) FROM documentos")
        total_docs = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM traducoes")
        total_traducoes = cursor.fetchone()[0]

        console.print(
            Panel.fit(
                f"[bold cyan]📚 TOTAL DE DOCUMENTOS: {total_docs}[/bold cyan]\n"
                f"[bold green]🌐 TOTAL DE TRADUÇÕES: {total_traducoes}[/bold green]",
                border_style="bright_blue",
                padding=(1, 4),
            )
        )
        console.print()

        # =========================================
        # 2. DOCUMENTOS POR CENTRO
        # =========================================
        cursor.execute("SELECT centro, COUNT(*) FROM documentos GROUP BY centro")
        centros = cursor.fetchall()

        if centros:
            console.print("[bold cyan]🏛️  DOCUMENTOS POR CENTRO:[/bold cyan]")
            table_centro = Table(box=box.SIMPLE, header_style="bold yellow")
            table_centro.add_column("Centro", style="yellow")
            table_centro.add_column("Quantidade", justify="right", style="cyan")
            table_centro.add_column("Percentual", justify="right", style="green")

            for centro, count in centros:
                nome_centro = (
                    "Leningrad"
                    if centro == "lencenter"
                    else "Moscow" if centro == "moscenter" else centro
                )
                percentual = (count / total_docs * 100) if total_docs > 0 else 0
                table_centro.add_row(nome_centro, str(count), f"{percentual:.1f}%")

            console.print(table_centro)
            console.print()

        # =========================================
        # 3. DISTRIBUIÇÃO POR TIPO DE DOCUMENTO
        # =========================================
        cursor.execute(
            """
            SELECT
                tipo_documento,
                tipo_descricao,
                COUNT(*) as total
            FROM documentos
            WHERE tipo_documento IS NOT NULL
                AND tipo_documento != ''
                AND tipo_documento != 'desconhecido'
            GROUP BY tipo_documento
            ORDER BY total DESC
        """
        )

        tipos = cursor.fetchall()

        if tipos:
            console.print("[bold magenta]📋 DISTRIBUIÇÃO POR TIPO:[/bold magenta]")
            table_tipos = Table(box=box.SIMPLE, header_style="bold magenta")
            table_tipos.add_column("Tipo", style="white")
            table_tipos.add_column("Quantidade", justify="right", style="cyan")
            table_tipos.add_column("Percentual", justify="right", style="green")

            for tipo, descricao, count in tipos:
                percentual = (count / total_docs * 100) if total_docs > 0 else 0
                badge = badge_tipo_documento(tipo)
                table_tipos.add_row(f"{badge} {descricao}", str(count), f"{percentual:.1f}%")

            console.print(table_tipos)
            console.print()

        # =========================================
        # 4. PESSOAS MAIS FREQUENTES
        # =========================================
        cursor.execute(
            """
            SELECT
                pessoa_principal,
                COUNT(*) as total
            FROM documentos
            WHERE pessoa_principal IS NOT NULL
                AND pessoa_principal != ''
            GROUP BY pessoa_principal
            ORDER BY total DESC
            LIMIT 15
        """
        )

        pessoas = cursor.fetchall()

        if pessoas:
            console.print("[bold yellow]👤 PESSOAS MAIS FREQUENTES:[/bold yellow]")
            table_pessoas = Table(box=box.SIMPLE, header_style="bold yellow")
            table_pessoas.add_column("Nome (Russo)", style="white")
            table_pessoas.add_column("Nome (Traduzido)", style="dim white")
            table_pessoas.add_column("Documentos", justify="right", style="cyan")

            for pessoa, count in pessoas:
                nome_traduzido = transliterar_nome(pessoa)
                table_pessoas.add_row(
                    pessoa[:30] + "…" if len(pessoa) > 30 else pessoa,
                    nome_traduzido[:30] if nome_traduzido else "",
                    str(count),
                )

            console.print(table_pessoas)
            console.print()

        # =========================================
        # 5. CORRESPONDÊNCIAS E ATOS
        # =========================================
        cursor.execute(
            """
            SELECT
                SUM(CASE WHEN tipo_documento = 'carta' THEN 1 ELSE 0 END) as cartas,
                SUM(CASE WHEN tipo_documento = 'declaracao' THEN 1 ELSE 0 END) as declaracoes,
                SUM(CASE WHEN tipo_documento = 'relatorio' THEN 1 ELSE 0 END) as relatorios,
                SUM(CASE WHEN tipo_documento = 'acareacao' THEN 1 ELSE 0 END) as acareacoes,
                SUM(CASE WHEN tipo_documento = 'acusacao' THEN 1 ELSE 0 END) as acusacoes,
                SUM(CASE WHEN tipo_documento = 'laudo' THEN 1 ELSE 0 END) as laudos
            FROM documentos
        """
        )

        stats = cursor.fetchone()

        if stats and any(stats):
            console.print("[bold green]✉️  CORRESPONDÊNCIAS E ATOS ESPECIAIS:[/bold green]")
            table_especiais = Table(box=box.SIMPLE, header_style="bold green")
            table_especiais.add_column("Tipo", style="white")
            table_especiais.add_column("Quantidade", justify="right", style="cyan")
            table_especiais.add_column("Percentual", justify="right", style="dim")

            tipos_especiais = [
                ("✉️ Cartas", stats[0]),
                ("📝 Declarações", stats[1]),
                ("📋 Relatórios NKVD", stats[2]),
                ("⚖️ Acareações", stats[3]),
                ("📜 Acusações", stats[4]),
                ("🏥 Laudos", stats[5]),
            ]

            for nome, valor in tipos_especiais:
                if valor and valor > 0:
                    percentual = (valor / total_docs * 100) if total_docs > 0 else 0
                    table_especiais.add_row(nome, str(valor), f"({percentual:.1f}%)")

            console.print(table_especiais)
            console.print()

        # =========================================
        # 6. DOCUMENTOS COM ANEXOS
        # =========================================
        cursor.execute("SELECT COUNT(*) FROM documentos WHERE tem_anexos = 1")
        total_anexos = cursor.fetchone()[0]

        if total_anexos > 0:
            console.print(
                f"[bold blue]📎 DOCUMENTOS COM ANEXOS: [cyan]{total_anexos}[/cyan] ({total_anexos/total_docs*100:.1f}%)[/bold blue]"
            )
            console.print()

        # =========================================
        # 7. TRADUÇÕES POR IDIOMA
        # =========================================
        if total_traducoes > 0:
            cursor.execute(
                """
                SELECT idioma, COUNT(*)
                FROM traducoes
                GROUP BY idioma
                ORDER BY COUNT(*) DESC
            """
            )

            traducoes_idioma = cursor.fetchall()

            if traducoes_idioma:
                console.print("[bold cyan]🌐 TRADUÇÕES POR IDIOMA:[/bold cyan]")
                table_trad = Table(box=box.SIMPLE, header_style="bold cyan")
                table_trad.add_column("Idioma", style="white")
                table_trad.add_column("Quantidade", justify="right", style="cyan")
                table_trad.add_column("Percentual", justify="right", style="green")

                for idioma, count in traducoes_idioma:
                    percentual = (count / total_traducoes * 100) if total_traducoes > 0 else 0
                    badge = badge_idioma(idioma)
                    table_trad.add_row(badge, str(count), f"{percentual:.1f}%")

                console.print(table_trad)
                console.print()

        # =========================================
        # 8. CUSTO TOTAL DE TRADUÇÕES
        # =========================================
        cursor.execute("SELECT SUM(custo) FROM traducoes")
        custo_total = cursor.fetchone()[0] or 0.0

        if custo_total > 0:
            console.print(
                f"[bold yellow]💰 CUSTO TOTAL DE TRADUÇÕES: [white]${custo_total:.4f} USD[/white][/bold yellow]"
            )
            console.print()

        conn.close()

        # Rodapé
        console.print("[dim]─────────────────────────────────────────────────[/dim]")
        console.print("[bold cyan]📊 Estatísticas atualizadas em tempo real[/bold cyan]")
        console.print("[dim]• Baseado em metadados enriquecidos[/dim]")
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
                    from db import listar_traducoes_documento, obter_documento, obter_traducao
                    from translator import (
                        TradutorComPersistencia,
                        criar_tradutor_da_configuracao,
                        tradutor_global,
                    )

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
                                "en": "Inglês",
                                "pt": "Português",
                                "es": "Espanhol",
                                "fr": "Francês",
                            }.get(t["idioma"], t["idioma"].upper())

                            console.print(
                                f"  • {idioma_nome}: {t['data_traducao'][:10]} "
                                f"(custo: ${t['custo']:.4f})"
                            )
                        console.print()

                    # ESCOLHER IDIOMA
                    console.print("[bold cyan]🌐 Idiomas disponíveis:[/bold cyan]")
                    console.print("  [1] Inglês (en) - Recomendado")
                    console.print("  [2] Português (pt)")
                    console.print("  [3] Espanhol (es)")
                    console.print("  [4] Francês (fr)")
                    console.print("  [0] Cancelar")

                    idioma_opcao = input("\nEscolha o idioma destino (0-4): ").strip()

                    if idioma_opcao == "0":
                        mensagem_aviso("Tradução cancelada")
                        time.sleep(1)
                        continue

                    idiomas = {"1": "en", "2": "pt", "3": "es", "4": "fr"}

                    if idioma_opcao not in idiomas:
                        mensagem_erro("Opção inválida!")
                        time.sleep(1)
                        continue

                    idioma_destino = idiomas[idioma_opcao]

                    # VERIFICAR SE JÁ EXISTE PARA ESTE IDIOMA
                    traducao_existente = obter_traducao(doc_id, idioma_destino)

                    if traducao_existente:
                        console.print(
                            f"\n[bold yellow]⚠ Já existe tradução para {idioma_destino}[/bold yellow]"
                        )
                        console.print(f"   Data: {traducao_existente['data_traducao']}")
                        console.print(f"   Custo: ${traducao_existente['custo']:.4f}")

                        opcao = (
                            input("\n[D] Visualizar existente | [N] Nova tradução | [C] Cancelar: ")
                            .strip()
                            .lower()
                        )

                        if opcao == "d":
                            # Mostrar tradução existente
                            console.print("\n[bold]📄 TRADUÇÃO EXISTENTE:[/bold]")
                            console.print("─" * 80)
                            console.print(traducao_existente["texto"][:2000] + "...")
                            console.print("─" * 80)
                            input("\nPressione Enter para continuar...")
                            continue
                        elif opcao == "c":
                            mensagem_aviso("Operação cancelada")
                            time.sleep(1)
                            continue

                    # CONFIRMAR CUSTO
                    chars = len(doc[5])
                    custo_estimado = chars * 0.000020

                    console.print("\n[bold]📊 Estimativa de custo:[/bold]")
                    console.print(f"  Caracteres: {chars:,}")
                    console.print(f"  Custo: [yellow]${custo_estimado:.4f}[/yellow] (USD)")

                    confirmar = input("\nConfirmar tradução? (s/N): ").strip().lower()

                    if confirmar != "s":
                        mensagem_aviso("Tradução cancelada")
                        time.sleep(1)
                        continue

                    # TRADUZIR E SALVAR
                    console.print(
                        f"\n[bold green]🌐 Traduzindo documento {doc_id} para {idioma_destino}...[/bold green]"
                    )

                    # Usar o Tradutor com persistência
                    persisted_translator = TradutorComPersistencia(tradutor)

                    resultado = spinner_processo(
                        "Traduzindo documento...",
                        persisted_translator.traduzir_e_salvar,
                        doc_id,
                        doc[5],
                        destino=idioma_destino,
                    )

                    # SUCESSO!
                    console.print(
                        "\n[bold green]✅ Tradução concluída e SALVA no banco de dados![/bold green]"
                    )
                    console.print(f"  📊 ID da tradução: {resultado['id']}")
                    console.print(f"  💰 Custo real: ${resultado['custo']:.4f}")

                    # PERGUNTAR SE QUER EXPORTAR
                    exportar = (
                        input("\nExportar texto traduzido para arquivo? (s/N): ").strip().lower()
                    )

                    if exportar == "s":
                        from nav_ui import exportar_texto_direto

                        nome_arquivo = f"doc{doc_id}_{idioma_destino}_traducao.txt"
                        exportar_texto_direto(resultado["texto"], nome_arquivo)

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
        from db import obter_documento
        from translator import (
            TradutorComPersistencia,
            criar_tradutor_da_configuracao,
            tradutor_global,
        )

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

        if idioma_opcao == "0":
            mensagem_aviso("Tradução cancelada")
            return

        idiomas = {"1": "en", "2": "pt", "3": "es", "4": "fr"}
        if idioma_opcao not in idiomas:
            mensagem_erro("Opção inválida!")
            return

        idioma_destino = idiomas[idioma_opcao]

        # Confirmar custo
        chars = len(doc[5])
        custo_estimado = chars * 0.000020

        console.print("\n[bold]📊 Estimativa de custo:[/bold]")
        console.print(f"  Caracteres: {chars:,}")
        console.print(f"  Custo: [yellow]${custo_estimado:.4f}[/yellow]")

        confirmar = input("\nConfirmar tradução? (s/N): ").strip().lower()
        if confirmar != "s":
            mensagem_aviso("Tradução cancelada")
            return

        # Traduzir e salvar
        persisted_translator = TradutorComPersistencia(tradutor)
        resultado = spinner_processo(
            "Traduzindo documento...",
            persisted_translator.traduzir_e_salvar,
            doc_id,
            doc[5],
            destino=idioma_destino,
        )

        mensagem_sucesso(f"Tradução concluída! ID: {resultado['id']}")

    except Exception as e:
        mensagem_erro(f"Erro na tradução: {e}")


if __name__ == "__main__":
    main()
