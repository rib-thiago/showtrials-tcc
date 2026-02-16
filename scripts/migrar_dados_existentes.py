#!/usr/bin/env python3
# scripts/migrar_dados_existentes.py
"""
Script para migrar dados do banco antigo para a nova arquitetura.
"""

import sys
from pathlib import Path

# Adicionar src ao path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.infrastructure.persistence.sqlite_repository import SQLiteDocumentoRepository
from src.infrastructure.persistence.migrations import criar_tabelas, migrar_banco_existente, estatisticas_banco
from src.application.use_cases.classificar_documento import ClassificarDocumento
from src.interface.console import console


def main():
    """Migra dados existentes e classifica documentos."""
    console.print("[bold cyan]🔧 Migração de Dados Existentes[/bold cyan]")
    
    # 1. Criar tabelas e colunas
    console.print("\n📦 Criando estrutura do banco...")
    criar_tabelas()
    migrar_banco_existente()
    
    # 2. Repositório e caso de uso
    repo = SQLiteDocumentoRepository()
    classificador = ClassificarDocumento(repo)
    
    # 3. Classificar documentos não classificados
    console.print("\n🔍 Classificando documentos...")
    total = classificador.executar_em_lote()
    console.print(f"[green]✅ {total} documentos classificados[/green]")
    
    # 4. Estatísticas finais
    console.print("\n📊 Estatísticas pós-migração:")
    stats = estatisticas_banco()
    console.print(f"  • Total de documentos: {stats['total_docs']}")
    console.print(f"  • Documentos classificados: {stats.get('docs_classificados', 0)}")
    console.print(f"  • Total de traduções: {stats.get('total_traducoes', 0)}")
    
    console.print("\n[green]✅ Migração concluída![/green]")


if __name__ == "__main__":
    main()