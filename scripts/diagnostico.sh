#!/bin/bash

# ShowTrials - Script de Diagnóstico Completo
# Uso: chmod +x diagnostico.sh && ./diagnostico.sh

echo "🔍 ShowTrials - Coletando diagnóstico completo..."
echo "================================================"
echo ""

# Criar pasta para o diagnóstico
PASTA="diagnostico_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$PASTA"
echo "📁 Salvando em: $PASTA/"
echo ""

# ==================================================
# 1. INFORMAÇÕES DO GIT
# ==================================================
echo "📋 1. Coletando informações do Git..."

# Branch atual e status
git branch --show-current > "$PASTA/git_branch_atual.txt" 2>/dev/null || echo "Não em um repositório git" > "$PASTA/git_branch_atual.txt"
git status > "$PASTA/git_status.txt" 2>/dev/null
git log --oneline -50 > "$PASTA/git_log_50.txt" 2>/dev/null
git diff > "$PASTA/git_diff_atual.txt" 2>/dev/null
git diff --staged > "$PASTA/git_diff_staged.txt" 2>/dev/null
git branch -a > "$PASTA/git_branches.txt" 2>/dev/null
git remote -v > "$PASTA/git_remotes.txt" 2>/dev/null

echo "   ✅ Git coletado"
echo ""

# ==================================================
# 2. ESTRUTURA DE ARQUIVOS
# ==================================================
echo "📁 2. Mapeando estrutura de arquivos..."

# Estrutura completa (ignorando lixo)
if command -v tree &> /dev/null; then
    tree -I '__pycache__|*.pyc|.git|.pytest_cache|.mypy_cache|*.egg-info|.ruff_cache|htmlcov|site|dist|build' > "$PASTA/estrutura_completa.txt" 2>/dev/null
else
    echo "tree não instalado, usando find" > "$PASTA/estrutura_completa.txt"
    find . -type f -not -path "*/\.*" -not -path "*/__pycache__/*" -not -path "*/.git/*" | sort >> "$PASTA/estrutura_completa.txt" 2>/dev/null
fi

# Listar apenas diretórios importantes
ls -la > "$PASTA/lista_raiz.txt" 2>/dev/null
[ -d src ] && ls -la src/ > "$PASTA/lista_src.txt" 2>/dev/null
[ -d src/application/use_cases ] && ls -la src/application/use_cases/ > "$PASTA/lista_use_cases.txt" 2>/dev/null
[ -d src/tests ] && ls -la src/tests/ > "$PASTA/lista_tests.txt" 2>/dev/null

echo "   ✅ Estrutura mapeada"
echo ""

# ==================================================
# 3. ARQUIVOS DE CONFIGURAÇÃO
# ==================================================
echo "⚙️ 3. Copiando arquivos de configuração..."

# Configurações (se existirem)
[ -f pyproject.toml ] && cp pyproject.toml "$PASTA/pyproject.toml"
[ -f poetry.lock ] && cp poetry.lock "$PASTA/poetry.lock"
[ -f .pre-commit-config.yaml ] && cp .pre-commit-config.yaml "$PASTA/pre-commit.yaml"
[ -f .ruff.toml ] && cp .ruff.toml "$PASTA/ruff.toml"
[ -f .mypy.ini ] && cp .mypy.ini "$PASTA/mypy.ini"
[ -f .coveragerc ] && cp .coveragerc "$PASTA/coveragerc"
[ -f config.yaml ] && cp config.yaml "$PASTA/config.yaml"
[ -f mkdocs.yml ] && cp mkdocs.yml "$PASTA/mkdocs.yml"

echo "   ✅ Configurações copiadas"
echo ""

# ==================================================
# 4. TESTES E COBERTURA (O MAIS IMPORTANTE)
# ==================================================
echo "🧪 4. Executando testes e coletando cobertura..."

# Verificar se poetry está instalado
if command -v poetry &> /dev/null; then
    # Verificar se pytest está disponível
    poetry run pytest --version > /dev/null 2>&1

    if [ $? -eq 0 ]; then
        # Testes com cobertura - formato completo
        echo "   Executando testes (pode levar alguns minutos)..."
        poetry run pytest src/tests/ -v --cov=src --cov-report=term-missing > "$PASTA/testes_completos.txt" 2>&1

        # Apenas resumo de cobertura
        poetry run pytest src/tests/ --cov=src --cov-report=term-missing 2>/dev/null | grep -E "^src/|^TOTAL" > "$PASTA/cobertura_resumo.txt"

        # Arquivos com cobertura baixa (< 80%)
        poetry run pytest src/tests/ --cov=src --cov-report=term-missing 2>/dev/null | grep -E "src/.*[0-9]+%[^0-9]+[0-9]{1,2}-" > "$PASTA/cobertura_baixa.txt"

        # Total de testes (corrigido)
        TOTAL_TESTES=$(poetry run pytest src/tests/ --collect-only 2>/dev/null | grep "collected" | awk '{print $1}')
        echo "${TOTAL_TESTES:-0} testes" > "$PASTA/total_testes.txt"

        echo "   ✅ Testes executados ($TOTAL_TESTES testes coletados)"
    else
        echo "   ⚠️ Pytest não encontrado no ambiente Poetry."
        poetry run pip list > "$PASTA/pip_list.txt" 2>&1
    fi
else
    echo "   ⚠️ Poetry não encontrado. Pulando testes."
fi

echo ""

# ==================================================
# 5. MYPY - TYPE CHECKING
# ==================================================
echo "🔤 5. Verificando types com MyPy..."

if command -v poetry &> /dev/null; then
    # MyPy completo
    poetry run mypy src/ > "$PASTA/mypy_completo.txt" 2>&1

    # Apenas erros
    grep "error:" "$PASTA/mypy_completo.txt" > "$PASTA/mypy_erros.txt" 2>/dev/null || touch "$PASTA/mypy_erros.txt"

    # Contagem de erros
    TOTAL_ERROS=$(grep -c "error:" "$PASTA/mypy_completo.txt" 2>/dev/null || echo "0")
    echo "   ✅ MyPy executado ($TOTAL_ERROS erros encontrados)"
else
    echo "   ⚠️ Poetry não encontrado. Pulando MyPy."
fi

echo ""

# ==================================================
# 6. TELEMETRIA - MAPEAMENTO (CORRIGIDO)
# ==================================================
echo "📊 6. Mapeando implementação de telemetria..."

# Use cases com telemetria
if [ -d "src/application/use_cases" ]; then
    # Com telemetria
    for file in src/application/use_cases/*.py; do
        if [ -f "$file" ] && [[ "$file" != *"__init__.py"* ]] && grep -q "_telemetry" "$file" 2>/dev/null; then
            basename "$file"
        fi
    done > "$PASTA/telemetria_use_cases_com.txt"

    # SEM telemetria
    for file in src/application/use_cases/*.py; do
        if [ -f "$file" ] && [[ "$file" != *"__init__.py"* ]] && ! grep -q "_telemetry" "$file" 2>/dev/null; then
            basename "$file"
        fi
    done > "$PASTA/telemetria_use_cases_sem.txt"

    # Testes de telemetria
    if [ -d "src/tests" ]; then
        find src/tests -name "test_*telemetry*.py" -exec basename {} \; > "$PASTA/telemetria_testes.txt" 2>/dev/null
    fi
else
    echo "Nenhum use case encontrado" > "$PASTA/telemetria_use_cases_com.txt"
    echo "Nenhum use case encontrado" > "$PASTA/telemetria_use_cases_sem.txt"
fi

# Contagens
TOTAL_USE_CASES=$(find src/application/use_cases -name "*.py" ! -name "__init__.py" 2>/dev/null | wc -l | tr -d ' ')
COM_TELEMETRIA=$(wc -l < "$PASTA/telemetria_use_cases_com.txt" 2>/dev/null | tr -d ' ')
SEM_TELEMETRIA=$(wc -l < "$PASTA/telemetria_use_cases_sem.txt" 2>/dev/null | tr -d ' ')
TESTES_TELEMETRIA=$(find src/tests -name "test_*telemetry*.py" 2>/dev/null | wc -l | tr -d ' ')

# Valores padrão se vazio
COM_TELEMETRIA=${COM_TELEMETRIA:-0}
SEM_TELEMETRIA=${SEM_TELEMETRIA:-0}
TESTES_TELEMETRIA=${TESTES_TELEMETRIA:-0}

echo "   📊 Use cases totais: $TOTAL_USE_CASES"
echo "   ✅ Com telemetria: $COM_TELEMETRIA"
echo "   ❌ Sem telemetria: $SEM_TELEMETRIA"
echo "   🧪 Testes de telemetria: $TESTES_TELEMETRIA"

# Salvar resumo
cat > "$PASTA/telemetria_resumo.txt" << EOF
USE CASES COM TELEMETRIA: $COM_TELEMETRIA
USE CASES SEM TELEMETRIA: $SEM_TELEMETRIA
TESTES DE TELEMETRIA: $TESTES_TELEMETRIA
TOTAL USE CASES: $TOTAL_USE_CASES

COM TELEMETRIA:
$(cat "$PASTA/telemetria_use_cases_com.txt" 2>/dev/null || echo "Nenhum")

SEM TELEMETRIA:
$(cat "$PASTA/telemetria_use_cases_sem.txt" 2>/dev/null || echo "Nenhum")

TESTES DE TELEMETRIA:
$(cat "$PASTA/telemetria_testes.txt" 2>/dev/null || echo "Nenhum")
EOF

echo "   ✅ Telemetria mapeada"
echo ""

# ==================================================
# 7. VERIFICAÇÕES ADICIONAIS
# ==================================================
echo "🔧 7. Verificações adicionais..."

# Arquivos .bak esquecidos
find . -name "*.bak" -not -path "*/\.*" 2>/dev/null > "$PASTA/arquivos_bak.txt"
TOTAL_BAK=$(wc -l < "$PASTA/arquivos_bak.txt" 2>/dev/null | tr -d ' ')
TOTAL_BAK=${TOTAL_BAK:-0}
echo "   📦 Arquivos .bak: $TOTAL_BAK"

# Dependências instaladas
if command -v poetry &> /dev/null; then
    poetry show > "$PASTA/dependencias.txt" 2>/dev/null || echo "Erro ao listar dependências" > "$PASTA/dependencias.txt"
fi

# Versão do Python
python --version > "$PASTA/python_version.txt" 2>&1

# Verificar se há módulos legacy
if [ -d "legacy" ]; then
    find legacy -name "*.py" 2>/dev/null | wc -l > "$PASTA/legacy_total.txt"
    echo "   🏚️ Código legacy detectado"
fi

echo "   ✅ Verificações concluídas"
echo ""

# ==================================================
# 8. ARQUIVOS IMPORTANTES (README, DOCS)
# ==================================================
echo "📚 8. Coletando documentação..."

# README e docs
[ -f README.md ] && cp README.md "$PASTA/README.md"
[ -d docs ] && cp -r docs "$PASTA/docs" 2>/dev/null

echo "   ✅ Documentação coletada"
echo ""

# ==================================================
# 9. COMPACTAR TUDO
# ==================================================
echo "📦 9. Compactando diagnóstico..."

# Criar um arquivo de resumo rápido
cat > "$PASTA/0_RESUMO_RAPIDO.txt" << EOF
SHOWTRIALS - DIAGNÓSTICO RÁPIDO
Data: $(date)
=======================================

📊 COBERTURA DE TESTES
$(grep "TOTAL" "$PASTA/cobertura_resumo.txt" 2>/dev/null | head -1)

🔤 MYPY
Total de erros: $(grep -c "error:" "$PASTA/mypy_erros.txt" 2>/dev/null || echo "0")

📋 TELEMETRIA
Use cases com telemetria: $COM_TELEMETRIA
Use cases sem telemetria: $SEM_TELEMETRIA
Testes de telemetria: $TESTES_TELEMETRIA

🏷️ GIT
Branch atual: $(cat "$PASTA/git_branch_atual.txt" 2>/dev/null || echo "N/A")
Último commit: $(head -1 "$PASTA/git_log_50.txt" 2>/dev/null || echo "N/A")

⚙️ CONFIGURAÇÕES
Python: $(cat "$PASTA/python_version.txt" 2>/dev/null || echo "N/A")

📁 Arquivos .bak: $TOTAL_BAK
=======================================
EOF

# Compactar tudo
NOME_ARQUIVO="showtrials_diagnostico_$(date +%Y%m%d_%H%M%S).tar.gz"
tar -czf "$NOME_ARQUIVO" "$PASTA/" 2>/dev/null

# Verificar se o arquivo foi criado
if [ -f "$NOME_ARQUIVO" ]; then
    echo ""
    echo "✅ DIAGNÓSTICO COMPLETO!"
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
