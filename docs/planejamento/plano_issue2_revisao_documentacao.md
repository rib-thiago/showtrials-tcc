## ✅ **PLANO PERFEITO! Vamos seguir o fluxo que criamos hoje.**

### **1. IDENTIFICAR A ISSUE DE DOCUMENTAÇÃO**

Primeiro, vamos descobrir qual é a issue que já existe:

```bash
# Listar issues abertas com label de documentação
gh issue list --label "tipo/documentação"

# Ou listar todas as issues abertas
gh issue list --state open

# Ou buscar por título
gh issue list --state all | grep -i "doc"
```

**Provavelmente é a Issue #2** que criamos mais cedo:
```
#2  Revisar documentação (.md files)  tipo/documentação, prioridade:media
```

---

### **2. VERIFICAR O ESTADO DA ISSUE**

```bash
# Ver detalhes da issue #2
gh issue view 2
```

Deve mostrar algo como:
```markdown
Revisar documentação (.md files) #2

Revisar e consolidar arquivos .md em docs/:

[ ] Verificar duplicatas (cobertura.md vs cobertura.md (versão histórica))
[ ] Atualizar índices se necessário
[ ] Garantir que todas as fases estão documentadas
[ ] Fazer merge da branch docs/organizacao após revisão
```

---

### **3. ATUALIZAR A ISSUE COM AS NOVAS TAREFAS**

Vamos editar a issue para incluir a consolidação dos 15 novos documentos:

```bash
# Editar a issue #2 com as novas tarefas
gh issue edit 2 --body "$(cat << 'EOF'
## 🎯 Objetivo
Revisar e consolidar toda a documentação do projeto.

## 📋 Tarefas

### Documentação Existente (docs/)
- [ ] Verificar duplicatas (cobertura.md vs cobertura.md (versão histórica))
- [ ] Garantir que todas as FASE*.md estão atualizadas
- [ ] Padronizar formatação entre todos os arquivos
- [ ] Verificar links internos

### Novos Documentos (15 arquivos)
Os seguintes documentos foram criados e precisam ser revisados:

#### Flows de Processo
- [ ] git_flow.md
- [ ] quality_flow.md
- [ ] telemetry_flow.md
- [ ] code_review_flow.md
- [ ] dependencies_flow.md
- [ ] debug_flow.md
- [ ] documentation_flow.md
- [ ] refactoring_flow.md
- [ ] emergency_flow.md

#### Documentos de Projeto
- [ ] analise_arquitetural.md
- [ ] visao_do_projeto.md
- [ ] roadmap_arquitetural.md
- [ ] plano_issues_documentacao.md
- [ ] manual_gestao.md
- [ ] questionario_levantamento_requisitos.md

### Organização
- [ ] Decidir local apropriado para cada documento
- [ ] Atualizar mkdocs.yml para incluir novos documentos
- [ ] Criar índice/navegação entre documentos
- [ ] Fazer merge da branch docs/organizacao

### Revisão Final
- [ ] Verificar consistência entre documentos
- [ ] Garantir que não há informações contraditórias
- [ ] Atualizar README.md com links para nova documentação

## 📊 Definição de Pronto
- [ ] Todos os arquivos revisados
- [ ] Documentos organizados em local adequado
- [ ] mkdocs.yml atualizado
- [ ] Site de documentação publicado
- [ ] Issue fechada

## ⏱️ Estimativa: 4-6 horas
EOF
)" --add-label "prioridade:alta"
```

---

### **4. MOVER ISSUE PARA "EM ANDAMENTO" NO KANBAN**

```bash
# Adicionar ao project se ainda não estiver
gh project item-add 2 --owner rib-thiago --url https://github.com/rib-thiago/showtrials-tcc/issues/2

# No site, arraste a issue #2 para "In Progress"
```

Acesse: `https://github.com/users/rib-thiago/projects/1`

---

### **5. CRIAR BRANCH PARA A DOCUMENTAÇÃO**

```bash
# Criar branch seguindo o padrão
git checkout -b docs/organizacao-final

# Ou se a branch docs/organizacao já existe, atualize-a
git checkout docs/organizacao
git pull origin main
```

---

### **6. ORGANIZAR OS DOCUMENTOS**

Proponho a seguinte estrutura:

```bash
# Criar subpastas para organização
mkdir -p docs/flows
mkdir -p docs/projeto
mkdir -p docs/fases

# Mover os flows
mv git_flow.md quality_flow.md telemetry_flow.md code_review_flow.md \
   dependencies_flow.md debug_flow.md documentation_flow.md \
   refactoring_flow.md emergency_flow.md docs/flows/

# Mover documentos de projeto
mv analise_arquitetural.md visao_do_projeto.md roadmap_arquitetural.md \
   plano_issues_documentacao.md manual_gestao.md \
   questionario_levantamento_requisitos.md docs/projeto/

# As FASE*.md já estão em docs/, mas podemos deixar lá
# ou mover para docs/fases/ se preferir
```

---

### **7. ATUALIZAR O MKdocs.yml**

```yaml
# Adicione no mkdocs.yml
nav:
  - Início: index.md
  - Visão Geral: overview.md
  - Arquitetura: ARCHITECTURE.md

  - Fases do Projeto:
    - FASE 1 - Domain: fases/FASE1_DOMAIN.md
    - FASE 2 - Application: fases/FASE2_APPLICATION.md
    # ... todas as fases
    - FASE 16 - ListarDocumentos: fases/FASE16_LISTAR_DOCUMENTOS.md

  - Flows de Trabalho:
    - Git Flow: flows/git_flow.md
    - Quality Flow: flows/quality_flow.md
    - Telemetry Flow: flows/telemetry_flow.md
    - Code Review Flow: flows/code_review_flow.md
    - Dependencies Flow: flows/dependencies_flow.md
    - Debug Flow: flows/debug_flow.md
    - Documentation Flow: flows/documentation_flow.md
    - Refactoring Flow: flows/refactoring_flow.md
    - Emergency Flow: flows/emergency_flow.md

  - Documentos do Projeto:
    - Visão do Projeto: projeto/visao_do_projeto.md
    - Análise Arquitetural: projeto/analise_arquitetural.md
    - Roadmap Arquitetural: projeto/roadmap_arquitetural.md
    - Plano de Issues: projeto/plano_issues_documentacao.md
    - Manual de Gestão: projeto/manual_gestao.md
    - Questionário: projeto/questionario_levantamento_requisitos.md

  - Como Contribuir: contributing.md
  - Changelog: changelog.md
```

---

### **8. TESTAR LOCALMENTE**

```bash
# Verificar se tudo funciona
task docs
# Acesse http://127.0.0.1:8000
```

---

### **9. COMMIT E PUSH**

```bash
# Adicionar tudo
git add docs/
git add mkdocs.yml

# Commit com referência à issue
git commit -m "docs: organiza documentação do projeto

- Move 9 flows para docs/flows/
- Move 6 documentos de projeto para docs/projeto/
- Atualiza mkdocs.yml com nova estrutura
- Padroniza formatação dos documentos

Closes #2"

# Push
git push origin docs/organizacao-final
```

---

### **10. VERIFICAR CI E MERGE**

```bash
# Acompanhar CI
gh run watch

# Após CI passar, fazer merge
git checkout main
git pull origin main
git merge --ff-only docs/organizacao-final
git push origin main
```

---

### **11. PUBLICAR DOCUMENTAÇÃO**

```bash
# Publicar site atualizado
poetry run mkdocs gh-deploy
```

---

### **12. MOVER ISSUE PARA "DONE" NO KANBAN**

Acesse o project e arraste a issue #2 para "Done".

---

## 📋 **CHECKLIST RESUMIDO**

```markdown
## ✅ Checklist da Issue #2

### Preparação
[ ] Verificar issue #2 no GitHub
[ ] Atualizar descrição com novas tarefas
[ ] Mover issue para "In Progress" no Kanban
[ ] Criar/atualizar branch `docs/organizacao-final`

### Organização
[ ] Mover flows para `docs/flows/`
[ ] Mover docs de projeto para `docs/projeto/`
[ ] Decidir sobre FASE*.md (manter em docs/ ou mover)
[ ] Atualizar `mkdocs.yml`

### Revisão
[ ] Verificar links internos
[ ] Verificar formatação
[ ] Testar localmente com `task docs`

### Finalização
[ ] Commit com "Closes #2"
[ ] Push
[ ] CI verde
[ ] Merge
[ ] Publicar documentação
[ ] Mover issue para "Done"
```

---

## 📚 **PLANO DA ISSUE #2 - Documentação**

**Nome do arquivo sugerido:** `plano_issue2_revisao_documentacao.md`

---

## 📋 **ETAPA 1: ATUALIZAR A ISSUE COM AS NOVAS TAREFAS**

```bash
# Editar a issue #2 com o corpo completo
gh issue edit 2 --body "$(cat << 'EOF'
## 🎯 Objetivo
Revisar e consolidar toda a documentação do projeto, incluindo os 15 novos artefatos criados.

## 📋 Tarefas

### 1. Documentação Existente (docs/)
- [ ] Verificar duplicatas (cobertura.md vs cobertura.md (versão histórica))
- [ ] Garantir que todas as FASE*.md estão atualizadas
- [ ] Padronizar formatação entre todos os arquivos
- [ ] Verificar links internos

### 2. Novos Documentos (15 arquivos)
Os seguintes documentos precisam ser revisados e integrados:

#### Flows de Processo
- [ ] git_flow.md
- [ ] quality_flow.md
- [ ] telemetry_flow.md
- [ ] code_review_flow.md
- [ ] dependencies_flow.md
- [ ] debug_flow.md
- [ ] documentation_flow.md
- [ ] refactoring_flow.md
- [ ] emergency_flow.md

#### Documentos de Projeto
- [ ] analise_arquitetural.md
- [ ] visao_do_projeto.md
- [ ] roadmap_arquitetural.md
- [ ] plano_issues_documentacao.md
- [ ] manual_gestao.md
- [ ] questionario_levantamento_requisitos.md

### 3. Organização
- [ ] Criar estrutura de pastas: `docs/flows/` e `docs/projeto/`
- [ ] Mover cada documento para seu local apropriado
- [ ] Atualizar `mkdocs.yml` com nova estrutura
- [ ] Criar índice/navegação entre documentos

### 4. Branch e Merge
- [ ] Criar branch `docs/organizacao-final`
- [ ] Mover issue para "In Progress" no Kanban
- [ ] Commit das alterações com "Closes #2"
- [ ] Push e CI
- [ ] Merge na main
- [ ] Publicar documentação com `mkdocs gh-deploy`

### 5. Revisão Final
- [ ] Verificar consistência entre documentos
- [ ] Garantir que não há informações contraditórias
- [ ] Atualizar README.md com links para nova documentação

## 📊 Definição de Pronto
- [ ] Todos os 15 novos documentos revisados
- [ ] Documentos organizados em pastas apropriadas
- [ ] mkdocs.yml atualizado
- [ ] Site de documentação publicado
- [ ] Issue #2 fechada

## ⏱️ Estimativa: 4-6 horas
EOF
)" --add-label "prioridade:alta"
```

---

## 📋 **ETAPA 2: MOVER ISSUE PARA "IN PROGRESS"**

```bash
# 1. Primeiro, liste seus projects para pegar o ID
gh project list --owner rib-thiago

# Deve mostrar algo como:
# NUMBER  TITLE                           STATE  ID
# 1       @rib-thiago's untitled project  open   PVT_kwHOBE0jLc4BPrP8

# 2. Adicionar a issue ao project (se já não estiver)
gh project item-add 2 --owner rib-thiago --url https://github.com/rib-thiago/showtrials-tcc/issues/2

# 3. Agora, pelo site, mova a issue para "In Progress"
# Acesse: https://github.com/users/rib-thiago/projects/1
# Arraste a issue #2 da coluna "Backlog" para "In Progress"
```

---

## 📋 **ETAPA 3: CRIAR BRANCH**

```bash
# Criar branch seguindo o padrão de documentação
git checkout -b docs/organizacao-final

# Verificar se está na branch correta
git branch
# * docs/organizacao-final
#   main
```

---

## 📋 **ETAPA 4: CRIAR ESTRUTURA DE PASTAS**

```bash
# Criar subpastas para organização
mkdir -p docs/flows
mkdir -p docs/projeto

# Verificar se as pastas foram criadas
ls -la docs/
# Deve mostrar: flows/ projeto/
```

---

## 📋 **PRÓXIMOS PASSOS (APÓS ESTAS ETAPAS)**

Depois de executar esses comandos, me mostre os resultados e seguiremos com:

**ETAPA 5:** Upload dos 15 arquivos para você analisar
**ETAPA 6:** Revisão e organização propriamente dita
**ETAPA 7:** Atualização do mkdocs.yml
**ETAPA 8:** Commit e finalização

---

## 📊 **RESUMO DO QUE VAMOS FAZER AGORA**

| Passo | Comando | Status |
|-------|---------|--------|
| 1 | Atualizar issue #2 | ⏳ |
| 2 | Mover para "In Progress" | ⏳ |
| 3 | Criar branch `docs/organizacao-final` | ⏳ |
| 4 | Criar pastas `docs/flows/` e `docs/projeto/` | ⏳ |

**Pode executar esses passos e me mostrar o resultado?** 🚀

---
