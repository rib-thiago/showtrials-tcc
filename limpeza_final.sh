#!/bin/bash
# limpeza_final.sh
# Script para remover código legado e consolidar mudanças no Git
# Uso: chmod +x limpeza_final.sh && ./limpeza_final.sh

set -e  # Para o script se qualquer comando falhar

echo "====================================================="
echo "🧹 LIMPEZA FINAL - SHOWTRIALS"
echo "====================================================="
echo ""

# =====================================================
# 1. VERIFICAR BACKUP
# =====================================================
echo "📦 Verificando backup na pasta legacy/..."

if [ ! -d "legacy" ]; then
    echo "❌ ERRO: Pasta legacy não encontrada!"
    echo "   Criando backup agora..."
    mkdir -p legacy
    cp app.py coleta.py db.py extractor.py nav_ui.py translator.py legacy/ 2>/dev/null || true
    cp -r translators/ ui/ legacy/ 2>/dev/null || true
    echo "✅ Backup criado em legacy/"
else
    echo "✅ Pasta legacy já existe"
fi

# =====================================================
# 2. REMOVER ARQUIVOS LEGADO
# =====================================================
echo ""
echo "🗑️ Removendo arquivos legado..."

# Lista de arquivos/pastas para remover
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

for item in "${ARQUIVOS_LEGADO[@]}"; do
    if [ -e "$item" ]; then
        echo "   Removendo: $item"
        git rm -rf "$item" 2>/dev/null || rm -rf "$item"
    else
        echo "   ⏩ $item já não existe"
    fi
done

# =====================================================
# 3. ATUALIZAR .GITIGNORE
# =====================================================
echo ""
echo "📝 Atualizando .gitignore..."

# Criar .gitignore se não existir
touch .gitignore

# Adicionar entradas se não existirem
ENTRADAS_GITIGNORE=(
    "legacy/"
    "*.db"
    "*.db-journal"
    "__pycache__/"
    "*.pyc"
    ".pytest_cache/"
    ".coverage"
    "htmlcov/"
    ".env"
    "config.local.yaml"
    "exportados/"
    "analises/"
    "relatorios/"
    ".DS_Store"
    "diagnostico_*.txt"
    "*.log"
)

for entrada in "${ENTRADAS_GITIGNORE[@]}"; do
    if ! grep -q "^$entrada$" .gitignore; then
        echo "$entrada" >> .gitignore
        echo "   Adicionado: $entrada"
    else
        echo "   ⏩ $entrada já existe"
    fi
done

# =====================================================
# 4. VERIFICAR DEPENDÊNCIAS NÃO UTILIZADAS
# =====================================================
echo ""
echo "🔍 Verificando dependências..."

# Verificar se requests ainda é usado
if grep -r "requests" --include="*.py" src/ > /dev/null 2>&1; then
    echo "   ✅ requests ainda é utilizado (manter)"
else
    echo "   ⚠️ requests parece não ser utilizado (verificar)"
fi

# Verificar se beautifulsoup4 ainda é usado
if grep -r "BeautifulSoup\|bs4" --include="*.py" src/ > /dev/null 2>&1; then
    echo "   ✅ beautifulsoup4 ainda é utilizado (manter)"
else
    echo "   ⚠️ beautifulsoup4 parece não ser utilizado (verificar)"
fi

# Verificar se lxml ainda é usado
if grep -r "lxml" --include="*.py" src/ > /dev/null 2>&1; then
    echo "   ✅ lxml ainda é utilizado (manter)"
else
    echo "   ⚠️ lxml parece não ser utilizado (verificar)"
fi

echo ""
echo "📋 Para remover dependências não utilizadas:"
echo "   poetry remove requests beautifulsoup4 lxml  # só se confirmar que não são usadas"

# =====================================================
# 5. VERIFICAR ESTADO DO GIT
# =====================================================
echo ""
echo "📊 Status do Git:"
git status

# =====================================================
# 6. COMMIT DAS MUDANÇAS
# =====================================================
echo ""
echo "====================================================="
echo "✅ PRONTO PARA COMMIT"
echo "====================================================="
echo ""
echo "As mudanças estão prontas para serem commitadas."
echo ""
echo "Para commitar, execute:"
echo ""
echo "  git add ."
echo "  git commit -m \"clean: remove código legado e atualiza .gitignore\""
echo ""
echo "  git push origin main"
echo ""
echo "====================================================="

# Perguntar se quer commitar agora
read -p "❓ Deseja commitar agora? (s/N) " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Ss]$ ]]; then
    echo ""
    echo "📦 Adicionando arquivos..."
    git add .
    
    echo "📝 Criando commit..."
    git commit -m "clean: remove código legado e atualiza .gitignore

- Remove arquivos legado: app.py, coleta.py, db.py, extractor.py, nav_ui.py, translator.py
- Remove pastas: translators/, ui/
- Adiciona legacy/ ao .gitignore
- Atualiza .gitignore com padrões para Python, logs, exports
- Código agora totalmente migrado para src/
- Backup mantido em legacy/ para referência"
    
    echo ""
    echo "🚀 Enviando para o GitHub..."
    git push origin main
    
    echo ""
    echo "✅ COMMIT REALIZADO COM SUCESSO!"
else
    echo ""
    echo "⏸️ Commit cancelado. Você pode commitar manualmente depois."
fi

# =====================================================
# 7. INSTRUÇÕES FINAIS
# =====================================================
echo ""
echo "====================================================="
echo "📋 PRÓXIMOS PASSOS"
echo "====================================================="
echo ""
echo "1️⃣  Testar a aplicação:"
echo "   python run.py      # CLI"
echo "   python web_run.py  # Web"
echo ""
echo "2️⃣  Verificar serviços no admin:"
echo "   http://localhost:8000/admin/services"
echo ""
echo "3️⃣  Se tudo estiver ok, pode deletar a branch de feature:"
echo "   git branch -d feature/service-registry"
echo "   git push origin --delete feature/service-registry  # se existir no remoto"
echo ""
echo "4️⃣  Para restaurar em caso de emergência:"
echo "   git checkout HEAD~1 -- app.py coleta.py db.py extractor.py nav_ui.py translator.py"
echo "   git checkout HEAD~1 -- translators/ ui/"
echo ""
echo "====================================================="
echo "🎉 LIMPEZA CONCLUÍDA!"
echo "====================================================="