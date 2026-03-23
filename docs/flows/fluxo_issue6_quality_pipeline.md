# Playbook — Consolidação do pipeline de qualidade (Issue #6) + Project v2

Repo (detectado): `rib-thiago/showtrials-tcc`
Issue alvo: `#6`
Project v2 (user) usado: **number `1`** (id `PVT_kwHOBE0jLc4BPrP8`)
Campo kanban: `Status` (single select)
Opção alvo: `In progress`

> Objetivo: registrar **do zero ao fim** o fluxo “descobrir informações → capturar variáveis → executar comandos GH/GraphQL → iniciar branch”, para repetir no futuro sem adivinhação.

---

## 0) Pré-requisitos

- GitHub CLI autenticado:
  ```bash
  gh auth status
  ```
- Você está dentro do repositório local (onde existe `origin`).

---

## 1) Descobrir OWNER/REPO automaticamente (via remote origin)

```bash
REPO_FULL="$(git remote get-url origin | sed -E 's#(git@github.com:|https://github.com/)([^/]+/[^.]+)(\.git)?#\2#')"
OWNER="${REPO_FULL%/*}"
REPO="${REPO_FULL#*/}"
echo "Repo detectado: $OWNER/$REPO"
```

(Se preferir fixar manualmente, pule o bloco acima e defina diretamente.)

---

## 2) Descobrir seus Projects v2 (user) e escolher o correto

Listar projects do usuário `OWNER`:

```bash
gh api graphql -f query='
query($login:String!){
  user(login:$login){
    projectsV2(first:50){
      nodes{ title number id }
    }
  }
}' -f login="$OWNER" --jq '.data.user.projectsV2.nodes'
```

A partir da saída, selecione:
- `PROJECT_NUMBER` (ex.: `1`)
- `PROJECT_ID` (ex.: `PVT_kwHOBE0jLc4BPrP8`)

---

## 3) Variáveis base (após descoberta)

```bash
PROJECT_NUMBER=1
PROJECT_ID="PVT_kwHOBE0jLc4BPrP8"

ISSUE_NUMBER=6
```

---

## 4) (Opcional) Conferir issue antes de editar

```bash
gh issue view "$ISSUE_NUMBER" --repo "$OWNER/$REPO"   --json number,title,state,labels,milestone,assignees,body
```

---

## 5) Reescrever a issue (#6) — título + body via arquivo

Criar body (arquivo temporário) **sem corromper heredoc**:

```bash
cat > /tmp/issue-6-body.md <<'MD'
## 🎯 Objetivo
Consolidar o pipeline de qualidade do projeto (lint, type-check, testes, cobertura, Taskipy e CI), garantindo **coerência entre execução local e GitHub Actions** e alinhamento com o **Quality Flow v2.0**.

## ✅ Escopo (IN)
1) Definir **fonte única de verdade** para comandos de qualidade: **Taskipy**
2) Garantir que **local e CI** rodam o **mesmo pipeline** (mesmos targets e flags)
3) Consolidar tasks atômicas e agregadoras:
   - `task lint`
   - `task type`
   - `task test`
   - `task check` (agregador oficial)
4) Consolidar MyPy:
   - Config consistente (sem `Any` não justificado)
   - Stubs necessários instalados e travados no lock
   - Execução padrão em `src/`
5) Consolidar Pytest:
   - Config única (sem duplicidade desnecessária)
   - Execução padrão previsível
6) Consolidar Ruff/Lint:
   - Config única e comando oficial via Taskipy
7) Consolidar cobertura:
   - Política mínima definida (threshold) e aplicada no CI (se adotado)
8) Documentar “como rodar qualidade” em 1 lugar (ex.: `CONTRIBUTING.md` ou `docs/quality.md`)

## 🚫 Fora de escopo (OUT)
- Troca de ferramentas (ruff→outro, pytest→outro, etc.)
- Mudanças arquiteturais core da engine (contratos, refactors amplos)
- Reorganização de pastas do projeto
- Enforcement arquitetural avançado (scripts complexos)

## ✅ Critérios de Aceite
- [ ] Existe `task check` como **entrada única** do pipeline local
- [ ] `task check` executa lint + type + tests (e coverage se adotado)
- [ ] CI executa o **mesmo pipeline** (mesmos comandos/targets)
- [ ] MyPy roda sem erros no target definido (ex.: `src/`)
- [ ] Configurações não estão duplicadas sem justificativa
- [ ] Documentação mínima descrevendo os comandos oficiais

## 🗺️ Plano (macro)
1) Levantar estado atual (configs + tasks + workflows)
2) Ajustar Taskipy para refletir o pipeline oficial
3) Ajustar configs (ruff/mypy/pytest/coverage) com mínima intervenção
4) Ajustar GitHub Actions para usar as tasks oficiais
5) Documentar e encerrar
MD
```

Aplicar título + body:

```bash
gh issue edit "$ISSUE_NUMBER"   --repo "$OWNER/$REPO"   --title "Infra: Consolidar pipeline de qualidade (lint, type, test, taskipy e CI)"   --body-file /tmp/issue-6-body.md
```

> Correção de corpo (caso o texto tenha ficado corrompido): basta recriar o arquivo e rodar novamente o `gh issue edit ... --body-file`.

---

## 6) Labels / Assignee / Milestone

Adicionar labels recomendadas:

```bash
gh issue edit "$ISSUE_NUMBER" --repo "$OWNER/$REPO"   --add-label "type:infra"   --add-label "priority:P1"
```

Ver labels atuais:

```bash
gh issue view "$ISSUE_NUMBER" --repo "$OWNER/$REPO" --json labels -q '.labels[].name'
```

Remover label indesejada (exemplo):

```bash
gh issue edit "$ISSUE_NUMBER" --repo "$OWNER/$REPO" --remove-label "priority:P2"
```

Assumir a issue:

```bash
gh issue edit "$ISSUE_NUMBER" --repo "$OWNER/$REPO" --add-assignee "@me"
```

Listar milestones abertas e escolher a ativa:

```bash
gh api "repos/$OWNER/$REPO/milestones?state=open&per_page=100" --jq '.[] | {number,title,due_on}'
```

Setar milestone pelo título:

```bash
MILESTONE_TITLE="MVP - Engine de Pipeline"
gh issue edit "$ISSUE_NUMBER" --repo "$OWNER/$REPO" --milestone "$MILESTONE_TITLE"
```

---

## 7) Project v2 — obter IDs necessários

### 7.1) Capturar `ISSUE_NODE_ID` (GraphQL exige Int; use `-F`)

```bash
ISSUE_NODE_ID="$(
  gh api graphql -f query='
query($owner:String!, $repo:String!, $number:Int!){
  repository(owner:$owner, name:$repo){
    issue(number:$number){ id }
  }
}' -f owner="$OWNER" -f repo="$REPO" -F number="$ISSUE_NUMBER" --jq '.data.repository.issue.id'
)"
echo "ISSUE_NODE_ID=$ISSUE_NODE_ID"
```

### 7.2) Adicionar issue ao Project v2

```bash
gh api graphql -f query='
mutation($projectId:ID!, $contentId:ID!){
  addProjectV2ItemById(input:{projectId:$projectId, contentId:$contentId}){
    item{ id }
  }
}' -f projectId="$PROJECT_ID" -f contentId="$ISSUE_NODE_ID"
```

### 7.3) Capturar `ITEM_ID` do Project (para a issue #6)

```bash
ITEM_ID="$(
  gh api graphql -f query='
query($login:String!, $projectNumber:Int!){
  user(login:$login){
    projectV2(number:$projectNumber){
      items(first:100){
        nodes{
          id
          content{ ... on Issue { number } }
        }
      }
    }
  }
}' -f login="$OWNER" -F projectNumber="$PROJECT_NUMBER" --jq '
.data.user.projectV2.items.nodes[]
| select(.content.number==6)
| .id'
)"
echo "ITEM_ID=$ITEM_ID"
```

> Se `ITEM_ID` vier vazio e seu Project tiver muitos itens, será necessário paginar (`after:`). (Não foi necessário no caso documentado.)

---

## 8) Project v2 — descobrir campo `Status` e a opção `In progress`

Listar **Single Select fields** e opções do Project (para descobrir os IDs):

```bash
gh api graphql -f query='
query($projectId:ID!){
  node(id:$projectId){
    ... on ProjectV2{
      fields(first:50){
        nodes{
          ... on ProjectV2SingleSelectField{
            id
            name
            options{ id name }
          }
        }
      }
    }
  }
}' -f projectId="$PROJECT_ID" --jq '.data.node.fields.nodes[] | select(.name != null)'
```

No caso do ShowTrials, a inspeção retornou:

- Campo `Status` id: `PVTSSF_lAHOBE0jLc4BPrP8zg-BEh0`
- Option `In progress` id: `47fc9ee4`

Definir:

```bash
STATUS_FIELD_ID="PVTSSF_lAHOBE0jLc4BPrP8zg-BEh0"
INPROGRESS_OPTION_ID="47fc9ee4"
```

---

## 9) Project v2 — mover a issue para *In progress* (GraphQL mutation)

```bash
gh api graphql -f query='
mutation($projectId:ID!, $itemId:ID!, $fieldId:ID!, $optionId:String!){
  updateProjectV2ItemFieldValue(input:{
    projectId:$projectId,
    itemId:$itemId,
    fieldId:$fieldId,
    value:{ singleSelectOptionId:$optionId }
  }){
    projectV2Item{ id }
  }
}' -f projectId="$PROJECT_ID" -f itemId="$ITEM_ID" -f fieldId="$STATUS_FIELD_ID" -f optionId="$INPROGRESS_OPTION_ID"
```

Verificar no browser:

```bash
gh issue view "$ISSUE_NUMBER" --repo "$OWNER/$REPO" --web
```

---

## 10) Retomar fluxo Git: criar branch e iniciar trabalho

Como a issue está em *In progress*, prossiga:

```bash
git checkout main
git pull origin main
git checkout -b infra/quality-pipeline-6
git push -u origin infra/quality-pipeline-6
```

---

## 11) Checklist operacional para esta issue (escopo controlado)

- Alterar apenas configs/scripts/CI/docs relacionados ao pipeline de qualidade
- Manter uma única entrada local: `task check`
- CI deve chamar tasks oficiais (evitar divergência local vs CI)
- Evitar refatorações oportunistas fora do escopo
