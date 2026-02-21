## 📄 **FASE13.md - Limpeza e Organização do Repositório**

```markdown
# FASE 13 - Limpeza e Organização do Repositório

<div align="center">

**Remoção de arquivos obsoletos, código legado e organização da estrutura do projeto**

</div>

## 📅 **Informações da Fase**

| Item | Descrição |
|------|-----------|
| **Status** | ✅ Concluída |
| **Data de Conclusão** | 20 de Fevereiro de 2026 |
| **Artefatos** | Repositório limpo, scripts organizados, .gitignore atualizado |
| **Dependências** | FASE 11 (CI), FASE 12 (Telemetria) |
| **Branch principal** | `chore/cleanup-repository` |

---

## 🎯 **Objetivo**

Realizar uma limpeza completa no repositório, removendo arquivos desnecessários, código legado e artefatos gerados pela aplicação, além de organizar scripts e documentação para melhor manutenibilidade do projeto.

---

## 🔍 **Contexto e Motivação**

Após várias fases de desenvolvimento, correções de CI e implementações de telemetria, o repositório acumulou diversos arquivos que não deveriam estar versionados:

1. **Artefatos gerados pela aplicação**: Wordclouds, documentos exportados, relatórios
2. **Pastas de diagnóstico**: Múltiplas pastas `diagnostico_*/` com logs e relatórios temporários
3. **Código legado**: Pasta `legacy/` com código anterior à refatoração
4. **Arquivos de backup**: `*.bak` espalhados pelo código
5. **Banco de dados duplicado**: `showtrials.db` vazio na raiz versus o banco real em `data/`
6. **Scripts soltos**: Vários scripts bash na raiz do projeto

---

## 📊 **Diagnóstico Inicial**

Antes da limpeza, utilizamos o script `diagnostico_limpeza.sh` para mapear todos os itens:

### 📋 **Itens Identificados**

| Categoria | Quantidade | Exemplos |
|-----------|------------|----------|
| **Arquivos .bak** | 11 | `analise.py.bak`, `presenters.py.bak`, `spacy_analyzer.py.bak` |
| **Pastas de diagnóstico** | 4 | `diagnostico_20260219_225218/`, `diagnostico_ci_20260219_231532/` |
| **Arquivos .tar.gz** | 2 | `showtrials_diagnostico_*.tar.gz` |
| **Artefatos da aplicação** | 3 pastas | `analises/`, `exportados/`, `relatorios/` |
| **Código legado** | 1 pasta | `legacy/` (10+ arquivos) |
| **Banco duplicado** | 1 arquivo | `showtrials.db` (0 bytes na raiz) |
| **Scripts na raiz** | 3 | `diagnostico.sh`, `diagnostico_ci.sh`, `diagnostico_limpeza.sh` |

### 🔬 **Análise Crítica**

#### **Banco de Dados**
```bash
# Comparação entre os dois bancos
ls -lh showtrials.db
> -rw-r--r-- 0 bytes - 12 fev

ls -lh data/showtrials.db
> -rw-r--r-- 4.7M - 20 fev (519 documentos)

# Verificação de referência no código
grep -r "showtrials.db" src/
> src/infrastructure/config/settings.py: DB_PATH = BASE_DIR / "data" / "showtrials.db"
```

**Conclusão:** O banco na raiz é um resquício vazio. O banco correto está em `data/`.

#### **Código Legado**
```bash
# Verificar referências a legacy no código atual
grep -r "legacy" --include="*.py" src/
> Nenhuma referência encontrada
```

**Conclusão:** A pasta `legacy/` pode ser removida com segurança.

---

## 🛠️ **Estratégia de Limpeza**

### **Princípios Adotados**

1. **Segurança primeiro**: Verificar referências antes de remover
2. **Organização**: Mover, não apenas deletar quando fizer sentido
3. **Documentação**: Registrar decisões para referência futura
4. **Git hygiene**: Commits atômicos e mensagens claras

### **Decisões por Categoria**

| Categoria | Decisão | Justificativa |
|-----------|---------|---------------|
| **Artefatos da aplicação** | ✅ Remover | Podem ser recriados pela aplicação |
| **Pastas de diagnóstico** | ✅ Remover | Temporárias, específicas de debug |
| **Arquivos .tar.gz** | ✅ Remover | Compactados, já extraídos |
| **Código legado** | ✅ Remover | Sem referências no código atual |
| **Banco na raiz** | ✅ Remover | Duplicado e vazio |
| **Scripts de diagnóstico** | 📦 Mover para `scripts/` | Organização |
| **Documentação .md** | 📦 Manter em `docs/` | Já organizada em branch separada |

---

## 📝 **Plano de Execução**

### **Fase 1: Preparação**

```bash
# Criar branch específica
git checkout -b chore/cleanup-repository

# Verificar estado atual
git status
```

### **Fase 2: Remoção de Artefatos**

```bash
# Pastas geradas pela aplicação
rm -rf analises/ exportados/ relatorios/

# Pastas de diagnóstico
rm -rf diagnostico_20260219_225218/ diagnostico_20260219_225619/
rm -rf diagnostico_ci_20260219_231532/ limpeza_20260220_002943/

# Arquivos .tar.gz
rm -f showtrials_diagnostico_*.tar.gz
```

### **Fase 3: Remoção de Código Morto**

```bash
# Código legado
rm -rf legacy/

# Arquivos .bak
find . -name "*.bak" -type f -delete
```

### **Fase 4: Organização de Scripts**

```bash
# Mover scripts para pasta apropriada
mkdir -p scripts
mv diagnostico.sh scripts/
mv diagnostico_ci.sh scripts/
mv diagnostico_limpeza.sh scripts/
```

### **Fase 5: Limpeza do Banco**

```bash
# Remover banco vazio da raiz
rm -f showtrials.db
```

### **Fase 6: Atualização do .gitignore**

```bash
# Adicionar padrões que não devem ser versionados
cat >> .gitignore << EOF

# Artefatos gerados
/analises/
/exportados/
/relatorios/
/site/

# Relatórios de teste
coverage.xml
htmlcov/

# Python
__pycache__/
*.pyc
EOF
```

---

## 🤔 **Desafios Encontrados**

### **Desafio 1: Identificar o Banco Correto**

Inicialmente, não estava claro qual dos dois arquivos `showtrials.db` (raiz vs `data/`) era o banco de dados ativo.

**Solução:**
```bash
# Verificar tamanho e conteúdo
ls -lh showtrials.db data/showtrials.db
sqlite3 data/showtrials.db "SELECT COUNT(*) FROM documentos;"

# Verificar referência no código
grep -r "showtrials.db" src/
```

O banco em `data/` tinha 4.7MB e 519 documentos, enquanto o da raiz tinha 0 bytes. O código referenciava explicitamente `data/showtrials.db`.

### **Desafio 2: Segurança na Remoção do Legacy**

A pasta `legacy/` continha código antigo que poderia estar sendo importado em algum lugar.

**Solução:**
```bash
# Busca exaustiva por referências
grep -r "legacy" --include="*.py" src/
grep -r "from legacy\|import legacy" --include="*.py" src/
```

Nenhuma referência foi encontrada, confirmando que o código não é mais utilizado.

### **Desafio 3: Organização sem Perda de Informação**

Os scripts de diagnóstico eram úteis, mas poluíam a raiz do projeto.

**Solução:**
Criamos a pasta `scripts/` (que já existia) e movemos todos os scripts para lá, mantendo a funcionalidade mas organizando a estrutura.

### **Desafio 4: Documentação em Andamento**

Arquivos como `FASE12.md` e `cobertura.md (versão histórica)` não deveriam ser simplesmente deletados, mas também não estavam prontos para versão final.

**Solução:**
Criamos uma branch separada `docs/organizacao` e uma issue para revisão posterior, seguindo o fluxo:
1. Branch `docs/organizacao` com os arquivos .md
2. Issue criada para revisão e consolidação
3. Limpeza principal focou apenas no que era inequivocamente temporário

---

## 📊 **Resultados da Limpeza**

### **Antes da Limpeza**
```
91 directories, 439 files
```

### **Depois da Limpeza**
```
? directories, ~350 files (estimado)
```

### **Itens Removidos/Organizados**

| Tipo | Quantidade | Espaço liberado |
|------|------------|-----------------|
| Pastas de artefatos | 3 | ~15 MB |
| Pastas de diagnóstico | 4 | ~50 MB |
| Arquivos .tar.gz | 2 | ~40 MB |
| Arquivos .bak | 11 | ~200 KB |
| Código legado | 1 pasta | ~500 KB |
| Banco duplicado | 1 | 0 bytes (vazio) |
| **TOTAL** | **~20+ itens** | **~105 MB** |

---

## 📝 **Lições Aprendidas**

1. **Versionamento seletivo**: Nem tudo que está na pasta do projeto precisa estar no Git. Artefatos gerados devem ser ignorados.

2. **Organização preventiva**: Manter scripts em `scripts/` desde o início evita acúmulo na raiz.

3. **Banco de dados**: Manter apenas uma cópia do banco, em local padronizado (`data/`).

4. **.gitignore proativo**: Configurar corretamente no início do projeto evita commits de arquivos temporários.

5. **Branches para documentação**: Usar branches separadas para documentação em andamento permite commits sem poluir a main.

---

## 📚 **Arquivos Modificados/Criados**

```
Modificados:
├── .gitignore (adicionados padrões de exclusão)

Removidos:
├── analises/
├── exportados/
├── relatorios/
├── diagnostico_20260219_225218/
├── diagnostico_20260219_225619/
├── diagnostico_ci_20260219_231532/
├── limpeza_20260220_002943/
├── legacy/
├── showtrials.db (raiz)
├── *.bak (11 arquivos)
└── *.tar.gz (2 arquivos)

Movidos para scripts/:
├── diagnostico.sh
├── diagnostico_ci.sh
├── diagnostico_limpeza.sh
```

---

## 🎯 **Impacto no Projeto**

### **Positivos**
- ✅ Repositório mais limpo e navegável
- ✅ Menos arquivos para versionar
- ✅ Scripts organizados em local apropriado
- ✅ .gitignore mais robusto
- ✅ Banco de dados único e consistente

### **Futuros**
- 📌 Documentação .md será revisada em branch específica
- 📌 Issue #? criada para consolidação da documentação

---

## 👤 **Autor**

**Thiago Ribeiro** - Projeto de TCC

---

## 📜 **Histórico de Revisões**

| Versão | Data | Autor | Alterações |
|--------|------|-------|------------|
| 1.0 | 20/02/2026 | Thiago Ribeiro | Documento inicial da FASE 13 |

---

<div align="center">
  <sub>FASE 13 - Limpeza e Organização do Repositório</sub>
  <br>
  <sub>Versão 1.0 - 20 de Fevereiro de 2026</sub>
  <br>
  <sub>✅ Fase concluída com sucesso</sub>
</div>
```

---
