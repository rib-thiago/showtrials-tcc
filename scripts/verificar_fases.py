#!/usr/bin/env python
"""
Script para verificar se as FASE*.md seguem o template oficial.
Baseado no histórico real de commits do projeto.
"""

import os
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple

# Template sections in order (based on TEMPLATE_FASE.md)
SECOES_OBRIGATORIAS = [
    "## 📅 **Informações da Fase**",
    "## 🎯 **Objetivo**",
    "## 📁 **Estrutura Criada/Modificada**",
    "## 🧩 **Componentes Implementados**",
    "## 🧪 **Testes**",
    "## 📊 **Métricas da Fase**",
    "## 📚 **Princípios Aplicados**",
    "## 🔗 **Integração com Fases**",
    "## 🔄 **Evolução do Código**",
    "## 🔍 **Lições Aprendidas**",
    "## 📋 **Issues Relacionadas**",
    "## 👤 **Autor**",
]

# Campos obrigatórios na tabela de informações
CAMPOS_TABELA = [
    "**Status**",
    "**Data de Conclusão**",
    "**Artefatos**",
    "**Dependências**",
    "**Issue principal**",
    "**Commit principal**",
]


def verificar_arquivo(caminho: Path) -> Tuple[List[str], List[str], Dict]:
    """
    Verifica se arquivo segue o template.

    Returns:
        - seções_faltando: lista de seções obrigatórias ausentes
        - campos_faltando: lista de campos obrigatórios ausentes na tabela
        - metadados: dicionário com informações extraídas
    """
    with open(caminho, "r", encoding="utf-8") as f:
        conteudo = f.read()

    # Verificar seções
    seções_faltando = []
    for secao in SECOES_OBRIGATORIAS:
        if secao not in conteudo:
            seções_faltando.append(secao)

    # Extrair e verificar tabela de informações
    tabela_pattern = r"\|\|.*?\|\|(.*?)\|\|"
    tabela_match = re.search(tabela_pattern, conteudo, re.DOTALL)

    campos_faltando = []
    metadados = {}

    if tabela_match:
        tabela = tabela_match.group(1)
        for campo in CAMPOS_TABELA:
            if campo not in tabela:
                campos_faltando.append(campo)
            else:
                # Extrair valor do campo
                valor_match = re.search(rf"{campo}\s*\|\s*([^|\n]+)", tabela)
                if valor_match:
                    metadados[campo] = valor_match.group(1).strip()

    # Extrair métricas
    metrics = {}
    metricas_section = re.search(r"## 📊 \*\*Métricas da Fase\*\*(.*?)##", conteudo, re.DOTALL)
    if metricas_section:
        # Procurar por padrão "Antes | Depois | Evolução"
        linhas = metricas_section.group(1).split("\n")
        for linha in linhas:
            if "|" in linha and "Antes" not in linha and "---" not in linha:
                parts = linha.split("|")
                if len(parts) >= 4:
                    nome = parts[1].strip()
                    antes = parts[2].strip()
                    depois = parts[3].strip()
                    if antes not in ["-", ""] and depois not in ["-", ""]:
                        metrics[nome] = {"antes": antes, "depois": depois}

    metadados["metricas"] = metrics

    return seções_faltando, campos_faltando, metadados


def gerar_relatorio():
    """Gera relatório de verificação no terminal."""
    docs_dir = Path("docs/fases")

    print("=" * 80)
    print("📋 RELATÓRIO DE VERIFICAÇÃO DAS FASES")
    print("=" * 80)
    print(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")

    total_arquivos = 0
    total_problemas = 0

    for arquivo in sorted(docs_dir.glob("FASE*.md")):
        if arquivo.name == "FASE11_CI.md":
            print(f"\n⚠️  {arquivo.name} (em processo de refatoração)")
            continue

        total_arquivos += 1
        seções_faltando, campos_faltando, metadados = verificar_arquivo(arquivo)

        if not seções_faltando and not campos_faltando:
            print(f"\n✅ {arquivo.name}")
        else:
            total_problemas += 1
            print(f"\n❌ {arquivo.name}")

            if seções_faltando:
                print(f"   Seções faltantes ({len(seções_faltando)}):")
                for s in seções_faltando[:3]:  # Mostrar apenas as primeiras
                    print(f"     - {s}")
                if len(seções_faltando) > 3:
                    print(f"     ... e mais {len(seções_faltando) - 3}")

            if campos_faltando:
                print("   Campos faltantes na tabela:")
                for c in campos_faltando:
                    print(f"     - {c}")

    print("\n" + "=" * 80)
    print(f"📊 RESUMO: {total_arquivos} arquivos verificados, {total_problemas} com problemas")
    print("=" * 80)

    # Sugestões de correção
    print("\n🔧 SUGESTÕES DE CORREÇÃO:")
    print("-" * 40)
    print("1. Para adicionar seções faltantes, edite o arquivo com nano")
    print("2. Para atualizar métricas, use os dados dos commits:")
    print("   git log --oneline --grep='FASE'")
    print("3. Commits recentes por fase:")
    os.system("git log --oneline --grep='FASE' | head -10")


if __name__ == "__main__":
    gerar_relatorio()
