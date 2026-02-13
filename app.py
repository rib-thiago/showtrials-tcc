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
    mensagem_sucesso, mensagem_erro, mensagem_aviso, spinner_processo,
    exibir_estatisticas
)
from db import contar
from nav_ui import (
    navegar_lista, visualizar_documento_ui, 
    exportar_documento_ui, reimportar_documento_ui
)
import time

def mostrar_estatisticas():
    """Wrapper para exibir estatísticas"""
    try:
        stats = {
            'total_docs': contar(),
            'total_traducoes': 0,
            'docs_por_centro': {},
            'docs_por_tipo': {},
            'tags_mais_usadas': []
        }
        
        # Contar por centro
        total_len = contar('lencenter')
        total_mos = contar('moscenter')
        
        if total_len > 0:
            stats['docs_por_centro']['Leningrad Center'] = total_len
        if total_mos > 0:
            stats['docs_por_centro']['Moscow Center'] = total_mos
        
        exibir_estatisticas(stats)
        
    except Exception as e:
        mensagem_erro(f"Erro ao carregar estatísticas: {e}")
        time.sleep(2)

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
            
            elif escolha == "6":
                mensagem_aviso("Módulo de tradução em desenvolvimento!")
                time.sleep(1.5)
            
            elif escolha == "7":
                mostrar_estatisticas()
    
    except KeyboardInterrupt:
        console.print()
        console.print("[bold yellow]⚠ Operação interrompida pelo usuário[/bold yellow]")
        console.print("[bold cyan]Até logo! 👋[/bold cyan]")
        sys.exit(0)

if __name__ == "__main__":
    main()