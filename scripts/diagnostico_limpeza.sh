#!/bin/bash

# ShowTrials - Script de Diagnóstico para Limpeza
# Uso: chmod +x diagnostico_limpeza.sh && ./diagnostico_limpeza.sh

echo "🔍 ShowTrials - Coletando informações para limpeza..."
echo "=================================================="
echo ""

# Criar pasta para os arquivos de texto
PASTA="limpeza_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$PASTA"
echo "📁 Salvando arquivos em: $PASTA/"
echo ""

# 1. ARQUIVOS .BAK
echo "📁 1. Coletando lista de arquivos .bak..."
find . -name "*.bak" -type f > "$PASTA/arquivos_bak.txt"
echo "   ✅ $(wc -l < "$PASTA/arquivos_bak.txt") arquivos encontrados"
echo ""

# 2. CONTEÚDO DA PASTA LEGACY
echo "📁 2. Coletando informações da pasta legacy..."
if [ -d "legacy" ]; then
    ls -la legacy/ > "$PASTA/legacy_lista.txt"
    find legacy -type f > "$PASTA/legacy_arquivos.txt"
    echo "   ✅ Pasta legacy encontrada"
    echo "   📄 Lista salva em legacy_lista.txt"
else
    echo "   ⚠️ Pasta legacy não encontrada" > "$PASTA/legacy_lista.txt"
fi
echo ""

# 3. REFERÊNCIAS A LEGACY NO CÓDIGO
echo "📁 3. Procurando referências a legacy no código..."
grep -r "legacy" --include="*.py" src/ 2>/dev/null > "$PASTA/referencias_legacy.txt"
if [ -s "$PASTA/referencias_legacy.txt" ]; then
    echo "   ✅ $(wc -l < "$PASTA/referencias_legacy.txt") referências encontradas"
else
    echo "   ✅ Nenhuma referência encontrada"
    echo "Nenhuma referência encontrada" > "$PASTA/referencias_legacy.txt"
fi
echo ""

# 4. PASTAS DE DIAGNÓSTICO
echo "📁 4. Coletando pastas de diagnóstico..."
ls -d diagnostico_*/ 2>/dev/null > "$PASTA/pastas_diagnostico.txt"
if [ -s "$PASTA/pastas_diagnostico.txt" ]; then
    echo "   ✅ Pastas encontradas:"
    cat "$PASTA/pastas_diagnostico.txt"
else
    echo "   ⚠️ Nenhuma pasta de diagnóstico encontrada"
    echo "Nenhuma pasta encontrada" > "$PASTA/pastas_diagnostico.txt"
fi
echo ""

# 5. ARQUIVOS COMPACTADOS DE DIAGNÓSTICO
echo "📁 5. Coletando arquivos .tar.gz de diagnóstico..."
ls showtrials_diagnostico_*.tar.gz 2>/dev/null > "$PASTA/arquivos_tar_gz.txt"
if [ -s "$PASTA/arquivos_tar_gz.txt" ]; then
    echo "   ✅ $(wc -l < "$PASTA/arquivos_tar_gz.txt") arquivos encontrados"
else
    echo "   ⚠️ Nenhum arquivo .tar.gz encontrado"
    echo "Nenhum arquivo encontrado" > "$PASTA/arquivos_tar_gz.txt"
fi
echo ""

# 6. ARQUIVOS SOLTOS NA RAIZ
echo "📁 6. Coletando arquivos soltos na raiz..."
ls -la *.txt *.log *.db 2>/dev/null > "$PASTA/arquivos_raiz.txt"
if [ -s "$PASTA/arquivos_raiz.txt" ]; then
    echo "   ✅ Arquivos encontrados:"
    cat "$PASTA/arquivos_raiz.txt"
else
    echo "   ⚠️ Nenhum arquivo .txt, .log ou .db na raiz"
    echo "Nenhum arquivo encontrado" > "$PASTA/arquivos_raiz.txt"
fi
echo ""

# 7. ARQUIVOS DE BACKUP DO PYTHON (outros padrões)
echo "📁 7. Coletando outros arquivos de backup..."
find . -name "*~" -type f 2>/dev/null > "$PASTA/arquivos_tilde.txt"
find . -name "*.py~" -type f 2>/dev/null >> "$PASTA/arquivos_tilde.txt"
echo "   ✅ Verificação concluída"
echo ""

# 8. RESUMO RÁPIDO
echo "📊 8. GERANDO RESUMO"
echo "=================================================="

cat > "$PASTA/0_RESUMO_LIMPEZA.txt" << EOF
SHOWTRIALS - DIAGNÓSTICO PARA LIMPEZA
Data: $(date)
=======================================

📁 ARQUIVOS .BAK: $(wc -l < "$PASTA/arquivos_bak.txt" | tr -d ' ') arquivos

📁 PASTA LEGACY: $([ -d "legacy" ] && echo "Existe" || echo "Não existe")

📁 REFERÊNCIAS A LEGACY: $(wc -l < "$PASTA/referencias_legacy.txt" | tr -d ' ') linhas

📁 PASTAS DE DIAGNÓSTICO: $(wc -l < "$PASTA/pastas_diagnostico.txt" | tr -d ' ') pastas

📁 ARQUIVOS .tar.gz: $(wc -l < "$PASTA/arquivos_tar_gz.txt" | tr -d ' ') arquivos

📁 ARQUIVOS NA RAIZ: $(wc -l < "$PASTA/arquivos_raiz.txt" | tr -d ' ') arquivos

=======================================
Os arquivos detalhados estão nesta pasta.
EOF

echo "📋 Resumo salvo em: $PASTA/0_RESUMO_LIMPEZA.txt"
echo ""
echo "✅ DIAGNÓSTICO CONCLUÍDO!"
echo "=================================================="
echo "📁 Pasta com os arquivos: $PASTA/"
echo ""
echo "👉 Agora faça o upload dos arquivos desta pasta:"
ls -la "$PASTA/"
echo "=================================================="
