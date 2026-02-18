#!/bin/bash
# diagnostico_legado.sh
# Script para gerar diagnóstico do código legado no projeto ShowTrials
# Uso: chmod +x diagnostico_legado.sh && ./diagnostico_legado.sh

set -e

OUTPUT_FILE="diagnostico_legado_$(date +%Y%m%d_%H%M%S).txt"

echo "====================================================="
echo "🔍 DIAGNÓSTICO DE CÓDIGO LEGADO - SHOWTRIALS"
echo "====================================================="
echo ""
echo "📁 Gerando relatório em: $OUTPUT_FILE"
echo ""

# Função para adicionar seção ao relatório
add_section() {
    echo "" >> $OUTPUT_FILE
    echo "=====================================================" >> $OUTPUT_FILE
    echo "$1" >> $OUTPUT_FILE
    echo "=====================================================" >> $OUTPUT_FILE
    echo "" >> $OUTPUT_FILE
}

# Iniciar relatório
echo "RELATÓRIO DE DIAGNÓSTICO DE CÓDIGO LEGADO" > $OUTPUT_FILE
echo "Gerado em: $(date)" >> $OUTPUT_FILE
echo "Projeto: ShowTrials" >> $OUTPUT_FILE
echo "" >> $OUTPUT_FILE

# =====================================================
# 1. LISTA DE ARQUIVOS LEGADO CANDIDATOS
# =====================================================
add_section "1. ARQUIVOS LEGADO CANDIDATOS"

ARQUIVOS_LEGADO=(
    "app.py"
    "coleta.py"
    "db.py"
    "extractor.py"
    "nav_ui.py"
    "translator.py"
    "translators"
    "ui"
)

echo "Arquivos/pastas considerados legado:" >> $OUTPUT_FILE
for item in "${ARQUIVOS_LEGADO[@]}"; do
    if [ -e "$item" ]; then
        echo "  ✅ $item (existe)" >> $OUTPUT_FILE
    else
        echo "  ❌ $item (não encontrado)" >> $OUTPUT_FILE
    fi
done

# =====================================================
# 2. VERIFICAR IMPORTAÇÕES DOS ARQUIVOS LEGADO
# =====================================================
add_section "2. IMPORTAÇÕES DE ARQUIVOS LEGADO NO CÓDIGO NOVO"

echo "Buscando referências a arquivos legado no diretório src/..." >> $OUTPUT_FILE
echo "" >> $OUTPUT_FILE

for item in app coleta db extractor nav_ui translator; do
    echo "🔍 Importações de '$item':" >> $OUTPUT_FILE
    grep -r "import.*$item\|from.*$item" --include="*.py" src/ 2>/dev/null | sed 's/^/    /' >> $OUTPUT_FILE
    if [ $? -ne 0 ]; then
        echo "    Nenhuma referência encontrada" >> $OUTPUT_FILE
    fi
    echo "" >> $OUTPUT_FILE
done

# Verificar pastas
for pasta in translators ui; do
    echo "🔍 Importações da pasta '$pasta':" >> $OUTPUT_FILE
    grep -r "from.*$pasta\|import.*$pasta" --include="*.py" src/ 2>/dev/null | sed 's/^/    /' >> $OUTPUT_FILE
    if [ $? -ne 0 ]; then
        echo "    Nenhuma referência encontrada" >> $OUTPUT_FILE
    fi
    echo "" >> $OUTPUT_FILE
done

# =====================================================
# 3. ARQUIVOS NA RAIZ
# =====================================================
add_section "3. ARQUIVOS PYTHON NA RAIZ DO PROJETO"

echo "Arquivos .py na raiz:" >> $OUTPUT_FILE
ls -la *.py 2>/dev/null | awk '{print "  " $9 " (" $5 " bytes)"}' >> $OUTPUT_FILE
echo "" >> $OUTPUT_FILE

echo "Scripts shell na raiz:" >> $OUTPUT_FILE
ls -la *.sh 2>/dev/null | awk '{print "  " $9 " (" $5 " bytes)"}' >> $OUTPUT_FILE

# =====================================================
# 4. DEPENDÊNCIAS DO PYPROJECT.TOML
# =====================================================
add_section "4. DEPENDÊNCIAS DO PYPROJECT.TOML"

if [ -f "pyproject.toml" ]; then
    echo "Dependências principais:" >> $OUTPUT_FILE
    grep -A 20 "\[tool.poetry.dependencies\]" pyproject.toml | grep -v "^\[" | grep -v "^#" | sed 's/^/  /' >> $OUTPUT_FILE
    
    echo "" >> $OUTPUT_FILE
    echo "Dependências de desenvolvimento:" >> $OUTPUT_FILE
    if grep -q "\[tool.poetry.group.dev.dependencies\]" pyproject.toml; then
        grep -A 20 "\[tool.poetry.group.dev.dependencies\]" pyproject.toml | grep -v "^\[" | grep -v "^#" | sed 's/^/  /' >> $OUTPUT_FILE
    else
        echo "  Nenhuma dependência de desenvolvimento encontrada" >> $OUTPUT_FILE
    fi
else
    echo "pyproject.toml não encontrado!" >> $OUTPUT_FILE
fi

# =====================================================
# 5. VERIFICAR SE ARQUIVOS LEGADO SÃO EXECUTÁVEIS
# =====================================================
add_section "5. ARQUIVOS LEGADO EXECUTÁVEIS"

for item in app.py coleta.py nav_ui.py translator.py; do
    if [ -f "$item" ]; then
        if [ -x "$item" ]; then
            echo "  ✅ $item é executável" >> $OUTPUT_FILE
        else
            echo "  ⚠️ $item não é executável" >> $OUTPUT_FILE
        fi
    fi
done

# =====================================================
# 6. VERIFICAR BACKUP NA PASTA LEGACY
# =====================================================
add_section "6. VERIFICAÇÃO DE BACKUP (PASTA LEGACY)"

if [ -d "legacy" ]; then
    echo "✅ Pasta legacy existe" >> $OUTPUT_FILE
    echo "" >> $OUTPUT_FILE
    echo "Arquivos em legacy/:" >> $OUTPUT_FILE
    ls -la legacy/ 2>/dev/null | grep -v "^total" | sed 's/^/  /' >> $OUTPUT_FILE
else
    echo "❌ Pasta legacy NÃO encontrada" >> $OUTPUT_FILE
    echo "" >> $OUTPUT_FILE
    echo "⚠️  Crie a pasta legacy com:" >> $OUTPUT_FILE
    echo "    mkdir -p legacy" >> $OUTPUT_FILE
    echo "    cp app.py coleta.py db.py extractor.py nav_ui.py translator.py legacy/ 2>/dev/null || true" >> $OUTPUT_FILE
    echo "    cp -r translators/ ui/ legacy/ 2>/dev/null || true" >> $OUTPUT_FILE
fi

# =====================================================
# 7. VERIFICAR GIT STATUS
# =====================================================
add_section "7. GIT STATUS"

if [ -d ".git" ]; then
    echo "Branch atual:" >> $OUTPUT_FILE
    git branch --show-current | sed 's/^/  /' >> $OUTPUT_FILE
    echo "" >> $OUTPUT_FILE
    
    echo "Arquivos não commitados:" >> $OUTPUT_FILE
    git status --porcelain | sed 's/^/  /' >> $OUTPUT_FILE
else
    echo "❌ Não é um repositório Git" >> $OUTPUT_FILE
fi

# =====================================================
# 8. RESUMO E RECOMENDAÇÕES
# =====================================================
add_section "8. RESUMO E RECOMENDAÇÕES"

echo "📊 Contagem de arquivos legado:" >> $OUTPUT_FILE
TOTAL_LEGADO=0
for item in "${ARQUIVOS_LEGADO[@]}"; do
    if [ -e "$item" ]; then
        TOTAL_LEGADO=$((TOTAL_LEGADO + 1))
    fi
done
echo "  Total de itens legado encontrados: $TOTAL_LEGADO" >> $OUTPUT_FILE
echo "" >> $OUTPUT_FILE

echo "🔍 Referências encontradas:" >> $OUTPUT_FILE
REF_COUNT=$(grep -r "import.*app\|import.*coleta\|import.*db\|import.*extractor\|import.*nav_ui\|import.*translator\|from.*translators\|from.*ui" --include="*.py" src/ 2>/dev/null | wc -l)
echo "  Referências em src/: $REF_COUNT" >> $OUTPUT_FILE

echo "" >> $OUTPUT_FILE
echo "⚠️  RECOMENDAÇÕES:" >> $OUTPUT_FILE
echo "" >> $OUTPUT_FILE

if [ $REF_COUNT -eq 0 ]; then
    echo "  ✅ PARECE SEGURO REMOVER! Nenhuma referência encontrada." >> $OUTPUT_FILE
    echo "" >> $OUTPUT_FILE
    echo "  Comando para remover:" >> $OUTPUT_FILE
    echo "    rm -f app.py coleta.py db.py extractor.py nav_ui.py translator.py" >> $OUTPUT_FILE
    echo "    rm -rf translators/ ui/" >> $OUTPUT_FILE
else
    echo "  ⚠️  CUIDADO: Ainda existem $REF_COUNT referências aos arquivos legado!" >> $OUTPUT_FILE
    echo "" >> $OUTPUT_FILE
    echo "  Revise as seções 2 e 3 para identificar o que ainda depende do código legado." >> $OUTPUT_FILE
fi

# =====================================================
# 9. SUGESTÃO DE PRÓXIMOS PASSOS
# =====================================================
add_section "9. PRÓXIMOS PASSOS SUGERIDOS"

cat >> $OUTPUT_FILE << 'EOF'
1. Se o relatório indicar que é seguro remover:
   git rm app.py coleta.py db.py extractor.py nav_ui.py translator.py
   git rm -rf translators/ ui/
   git commit -m "clean: remove código legado (agora em legacy/)"

2. Verificar dependências não utilizadas:
   poetry show | grep -E "requests|beautifulsoup4|lxml"
   (se não forem mais usadas, remova do pyproject.toml)

3. Atualizar documentação:
   - README.md (remover referências a arquivos antigos)
   - docs/ (atualizar arquitetura)

4. Testar a aplicação após remoção:
   python run.py
   python web_run.py

5. Se algo quebrar, restaurar com:
   git checkout -- app.py  (para arquivos individuais)
   ou
   git reset HEAD~1  (desfaz o último commit)
EOF

# =====================================================
# FINALIZAR
# =====================================================
echo ""
echo "====================================================="
echo "✅ RELATÓRIO GERADO COM SUCESSO!"
echo "====================================================="
echo ""
echo "📄 Arquivo: $OUTPUT_FILE"
echo "📏 Tamanho: $(wc -l < $OUTPUT_FILE) linhas"
echo ""
echo "👉 Faça o upload do arquivo $OUTPUT_FILE aqui no chat."
echo ""