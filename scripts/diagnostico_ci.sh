#!/bin/bash

# ShowTrials - Script de Diagnóstico do CI
# Uso: chmod +x diagnostico_ci.sh && ./diagnostico_ci.sh

echo "🔍 ShowTrials - Diagnóstico do CI"
echo "================================================"
echo ""

# Criar pasta para o diagnóstico
PASTA="diagnostico_ci_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$PASTA"
echo "📁 Salvando em: $PASTA/"
echo ""

# ==================================================
# 1. ARQUIVO DE WORKFLOW
# ==================================================
echo "📋 1. Coletando arquivo de workflow..."

if [ -f ".github/workflows/ci.yml" ]; then
    cp .github/workflows/ci.yml "$PASTA/ci.yml"
    echo "   ✅ workflow copiado"
else
    echo "   ⚠️ Arquivo .github/workflows/ci.yml não encontrado"
fi

echo ""

# ==================================================
# 2. TESTES IGUAL AO CI
# ==================================================
echo "🧪 2. Executando testes no modo CI (com falha se cobertura < 45%)..."

if command -v poetry &> /dev/null; then
    # Testes com cobertura e meta de falha
    poetry run pytest src/tests/ -v --cov=src --cov-report=xml --cov-fail-under=45 > "$PASTA/testes_ci.txt" 2>&1
    echo "   ✅ Testes executados (resultado em testes_ci.txt)"

    # Cobertura resumida
    poetry run pytest src/tests/ --cov=src --cov-report=term-missing 2>/dev/null | grep "TOTAL" > "$PASTA/cobertura_atual.txt"
    echo "   📊 Cobertura atual: $(cat "$PASTA/cobertura_atual.txt")"
else
    echo "   ⚠️ Poetry não encontrado"
fi

echo ""

# ==================================================
# 3. LOG DA ÚLTIMA FALHA DO CI
# ==================================================
echo "📜 3. Coletando logs do GitHub Actions..."

if command -v gh &> /dev/null; then
    # Listar últimas execuções
    gh run list -L 20 > "$PASTA/gh_run_list.txt"
    echo "   ✅ Lista de runs salva"

    # Pegar o ID da última execução com falha
    ULTIMO_FALHA=$(gh run list -L 20 --json databaseId,conclusion --jq '.[] | select(.conclusion=="failure") | .databaseId' | head -1)

    if [ -n "$ULTIMO_FALHA" ]; then
        echo "   🔍 Última falha: Run ID $ULTIMO_FALHA"
        gh run view "$ULTIMO_FALHA" --log > "$PASTA/ci_log_falha.txt" 2>&1
        echo "   ✅ Log da falha salvo em ci_log_falha.txt"

        # Resumo da falha
        echo "   📋 Resumo da falha:" > "$PASTA/resumo_falha.txt"
        grep -E "FAILED|ERROR|ModuleNotFoundError|ImportError|AssertionError" "$PASTA/ci_log_falha.txt" | head -20 >> "$PASTA/resumo_falha.txt" 2>/dev/null
    else
        echo "   ⚠️ Nenhuma execução com falha encontrada"
    fi
else
    echo "   ⚠️ GitHub CLI (gh) não instalado"
    echo "   💡 Para instalar: https://cli.github.com/"
fi

echo ""

# ==================================================
# 4. META DE COBERTURA
# ==================================================
echo "🎯 4. Verificando meta de cobertura..."

if [ -f "pyproject.toml" ]; then
    grep -A 5 "cov-fail-under" pyproject.toml > "$PASTA/meta_cobertura.txt" 2>/dev/null
    echo "   ✅ Meta de cobertura:"
    cat "$PASTA/meta_cobertura.txt"
fi

echo ""

# ==================================================
# 5. MYPY SEM IGNORE
# ==================================================
echo "🔤 5. Executando MyPy puro (sem ignore)..."

if command -v poetry &> /dev/null; then
    poetry run mypy src/ > "$PASTA/mypy_completo.txt" 2>&1

    # Contar erros
    TOTAL_ERROS=$(grep -c "error:" "$PASTA/mypy_completo.txt" 2>/dev/null || echo "0")
    echo "   🔤 MyPy: $TOTAL_ERROS erros encontrados"

    # Erros que podem quebrar o CI
    grep -E "error:.*\[" "$PASTA/mypy_completo.txt" | head -10 > "$PASTA/mypy_erros_principais.txt"
else
    echo "   ⚠️ Poetry não encontrado"
fi

echo ""

# ==================================================
# 6. DEPENDÊNCIAS (versões)
# ==================================================
echo "📦 6. Coletando versões das dependências..."

if command -v poetry &> /dev/null; then
    poetry show > "$PASTA/versoes_locais.txt"
    echo "   ✅ Versões locais salvas"

    # Principais dependências
    echo "   Principais:" > "$PASTA/dependencias_principais.txt"
    grep -E "^(pytest|coverage|mypy|ruff|black|isort|fastapi|uvicorn|spacy|textblob|wordcloud|matplotlib)" "$PASTA/versoes_locais.txt" >> "$PASTA/dependencias_principais.txt" 2>/dev/null
    cat "$PASTA/dependencias_principais.txt"
fi

echo ""

# ==================================================
# 7. VERIFICAR TESTES QUE CRIAM ARQUIVOS
# ==================================================
echo "📁 7. Verificando testes que criam arquivos..."

# Procurar por wordcloud, export, relatório nos testes
grep -l "wordcloud\|exportar\|relatorio" src/tests/test_*.py 2>/dev/null > "$PASTA/testes_com_arquivos.txt"
TOTAL_COM_ARQUIVOS=$(wc -l < "$PASTA/testes_com_arquivos.txt" 2>/dev/null || echo "0")
echo "   📄 Testes que criam arquivos: $TOTAL_COM_ARQUIVOS"
if [ "$TOTAL_COM_ARQUIVOS" -gt 0 ]; then
    echo "   Lista:" >> "$PASTA/testes_com_arquivos.txt"
    cat "$PASTA/testes_com_arquivos.txt"
fi

echo ""

# ==================================================
# 8. COMPARAR COM ÚLTIMO COMMIT QUE PASSOU
# ==================================================
echo "✅ 8. Buscando último commit que passou no CI..."

if command -v gh &> /dev/null; then
    # Último commit com sucesso
    ULTIMO_SUCESSO=$(gh run list -L 50 --json databaseId,conclusion,headSha --jq '.[] | select(.conclusion=="success") | .headSha' | head -1)

    if [ -n "$ULTIMO_SUCESSO" ]; then
        echo "   ✅ Último commit com sucesso: $ULTIMO_SUCESSO"
        git show --stat "$ULTIMO_SUCESSO" > "$PASTA/ultimo_commit_sucesso.txt" 2>/dev/null
        echo "   📋 Detalhes salvos em ultimo_commit_sucesso.txt"

        # Comparar com o commit atual
        git diff --stat "$ULTIMO_SUCESSO"..HEAD > "$PASTA/diff_desde_ultimo_sucesso.txt" 2>/dev/null
        echo "   📊 Diff desde o último sucesso:"
        cat "$PASTA/diff_desde_ultimo_sucesso.txt" | head -20
    else
        echo "   ⚠️ Nenhum commit com sucesso encontrado"
    fi
fi

echo ""

# ==================================================
# 9. RESUMO RÁPIDO
# ==================================================
echo "📊 9. GERANDO RESUMO RÁPIDO"
echo "================================================"

cat > "$PASTA/0_RESUMO_RAPIDO_CI.txt" << EOF
SHOWTRIALS - DIAGNÓSTICO DO CI
Data: $(date)
=======================================

📊 COBERTURA ATUAL
$(cat "$PASTA/cobertura_atual.txt" 2>/dev/null || echo "Não disponível")

🎯 META DE COBERTURA
$(cat "$PASTA/meta_cobertura.txt" 2>/dev/null || echo "Não disponível")

🔤 MYPY
Total de erros: $(grep -c "error:" "$PASTA/mypy_completo.txt" 2>/dev/null || echo "0")

📋 ÚLTIMA FALHA DO CI
$(cat "$PASTA/resumo_falha.txt" 2>/dev/null | head -5 || echo "Não disponível")

📁 TESTES QUE CRIAM ARQUIVOS: $TOTAL_COM_ARQUIVOS

📦 PRINCIPAIS DEPENDÊNCIAS
$(cat "$PASTA/dependencias_principais.txt" 2>/dev/null || echo "Não disponível")

✅ ÚLTIMO COMMIT COM SUCESSO: ${ULTIMO_SUCESSO:-Não encontrado}
=======================================
EOF

echo "📋 Resumo salvo em: $PASTA/0_RESUMO_RAPIDO_CI.txt"
echo ""

# ==================================================
# 10. COMPACTAR
# ==================================================
echo "📦 10. Compactando diagnóstico..."

NOME_ARQUIVO="showtrials_diagnostico_ci_$(date +%Y%m%d_%H%M%S).tar.gz"
tar -czf "$NOME_ARQUIVO" "$PASTA/" 2>/dev/null

if [ -f "$NOME_ARQUIVO" ]; then
    echo ""
    echo "✅ DIAGNÓSTICO DO CI COMPLETO!"
    echo "================================================"
    echo "📁 Pasta temporária: $PASTA/"
    echo "📦 Arquivo compactado: $NOME_ARQUIVO"
    echo "📦 Tamanho: $(du -h "$NOME_ARQUIVO" | cut -f1)"
    echo ""
    echo "👉 Faça o upload do arquivo: $NOME_ARQUIVO"
    echo "================================================"
else
    echo ""
    echo "❌ ERRO: Falha ao criar arquivo compactado"
    echo "================================================"
    echo "📁 Os arquivos estão em: $PASTA/"
    echo "👉 Compacte manualmente e faça o upload"
    echo "================================================"
fi
