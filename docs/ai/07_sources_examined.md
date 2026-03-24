# Fontes Examinadas

## 1. Documentação base examinada

Foram lidos integralmente os seguintes documentos de entrada geral do projeto:

- `README.md`
- `docs/index.md`
- `docs/overview.md`
- `docs/ARCHITECTURE.md`

Esses documentos foram utilizados para identificar:

- identidade declarada do ShowTrials
- missão e propósito do sistema
- conceitos centrais do domínio
- narrativa arquitetural declarada
- tensões iniciais entre estado implementado e estado aspiracional

## 2. Fases do projeto examinadas

Foram lidos os seguintes documentos de fases:

- `docs/fases/FASE1_DOMAIN.md`
- `docs/fases/FASE2_APPLICATION.md`
- `docs/fases/FASE3_INFRASTRUCTURE.md`
- `docs/fases/FASE4_CLI.md`
- `docs/fases/FASE5_TRADUCAO.md`
- `docs/fases/FASE6_EXPORTACAO.md`
- `docs/fases/FASE7_RELATORIOS.md`
- `docs/fases/FASE8_ANALISE_TEXTO.md`
- `docs/fases/FASE9_WEB_INTERFACE.md`
- `docs/fases/FASE10_SERVICE_REGISTRY.md`
- `docs/fases/FASE11_CI.md`
- `docs/fases/FASE12.md`
- `docs/fases/FASE13.md`
- `docs/fases/FASE14.md`
- `docs/fases/FASE15.md`
- `docs/fases/FASE16.md`
- `docs/fases/FASE17.md`

Esses documentos foram utilizados para reconstruir:

- evolução funcional por fases
- evolução arquitetural inferida
- distinção preliminar entre fases aparentemente implementadas e fases parcialmente aspiracionais
- mudanças de direção entre expansão funcional, estabilização técnica e reorganização documental

## 3. Documentos de projeto e direção arquitetural examinados

Foram lidos os seguintes documentos de visão, roadmap e orientação arquitetural:

- `docs/projeto/visao_do_projeto.md`
- `docs/projeto/roadmap_arquitetural.md`
- `docs/projeto/analise_arquitetural.md`
- `docs/projeto/direcionamento_arquitetural_engine_mvp.md`
- `docs/projeto/manual_gestao.md`
- `docs/projeto/questionario_levantamento_requisitos.md`

Esses documentos foram utilizados para identificar:

- direção arquitetural explícita futura
- diagnóstico dos limites da arquitetura atual
- transição conceitual entre aplicação específica e plataforma configurável
- restrições não negociáveis de arquitetura e gestão
- separação entre estado atual do ShowTrials e alvo futuro de engine/plataforma

Observação: até esta etapa, os documentos examinados não estabeleceram de forma explícita uma relação documental formal entre ShowTrials e o nome CraftText. Essa relação permanece pendente de confirmação por outras fontes.

## 4. Fluxos e governança examinados

Foram lidos os seguintes documentos de governança, fluxo operacional e disciplina de execução:

- `docs/flows/GOVERNANCA.md`
- `docs/flows/git_flow.md`
- `docs/flows/quality_flow.md`
- `docs/flows/code_review_flow.md`
- `docs/flows/refactoring_flow.md`
- `docs/flows/documentation_flow.md`
- `docs/flows/dependencies_flow.md`
- `docs/flows/telemetry_flow.md`
- `docs/flows/debug_flow.md`
- `docs/flows/emergency_flow.md`
- `docs/flows/fluxo_projects_github_cli.md`

Esses documentos foram utilizados para mapear:

- regras centrais de governança
- política de milestone ativa única
- regras de branch, issue, PR e merge
- critérios obrigatórios de qualidade
- papel dos fluxos auxiliares
- restrições operacionais para sessões futuras do Codex

Também foi identificada uma tensão documental entre convenções antigas e convenções mais recentes, especialmente na nomenclatura de branches e na estratégia de merge. A leitura normativa preliminar favorece `GOVERNANCA.md` e `git_flow.md` como fontes mais atuais.

## 5. Código e configuração inspecionados

Foram inspecionados os seguintes arquivos de código e configuração:

- `src/domain/entities/documento.py`
- `src/application/use_cases/base.py`
- `src/application/use_cases/traduzir_documento.py`
- `src/application/use_cases/analisar_acervo.py`
- `src/infrastructure/factories.py`
- `src/infrastructure/registry.py`
- `src/infrastructure/persistence/sqlite_repository.py`
- `src/interface/cli/app.py`
- `src/interface/web/app.py`
- `run.py`
- `pyproject.toml`
- `config.yaml`

Esses arquivos foram utilizados para confirmar, no código real:

- forma concreta da arquitetura atual
- papel prático do `ServiceRegistry`
- papel prático das factories
- relação entre CLI/Web e os casos de uso
- sinais de acoplamento com persistência
- coexistência entre elementos mais novos de modularização e traços da arquitetura anterior

## 6. Fontes ainda pendentes de inspeção

Até esta etapa, ainda não foram examinadas de forma sistemática as seguintes classes de fontes:

- demais entidades, value objects e interfaces do domínio
- conjunto mais amplo de casos de uso da camada application
- rotas, templates e arquivos auxiliares completos da interface web
- comandos, presenters e menus da CLI além do arquivo principal
- implementação completa de `sqlite_traducao_repository.py`
- arquivos de configuração e carregamento associados a `ApplicationConfig`
- workflow real de CI em `.github/workflows/ci.yml`
- testes automatizados e cobertura real do repositório
- documentos em `docs/metricas/`
- documentos de planejamento em `docs/planejamento/`, além do contexto já visível nas abas
- estado completo do diretório `docs/ai/` como conjunto coerente
- comparação detalhada entre branches relevantes
- workflow real de CI em execução no GitHub
- estrutura real de GitHub Projects v2, pendente de comandos compatíveis com o ambiente atual

Também permanece pendente a confirmação documental ou histórica de qualquer relação formal entre ShowTrials e uma eventual identidade futura chamada CraftText.

## 7. Limitações desta etapa da análise

Esta etapa possui as seguintes limitações:

- embora o histórico Git tenha sido aprofundado, ainda não houve reconstrução exaustiva por arquivo com `git log --follow`
- ainda não houve validação sistemática do estado do CI, dos testes e da cobertura a partir de execução local ou workflow inspecionado
- a inspeção de código concentrou-se em arquivos centrais e representativos, não no conjunto completo do repositório
- parte da documentação utiliza linguagem de entrega concluída, mas isso ainda precisa ser confirmado contra o código e o histórico
- a distinção entre estado atual, transição em andamento e alvo futuro foi fortalecida nesta sessão, mas ainda pode exigir nova revisão em documentos não revalidados
- embora comandos Git e GitHub relevantes já tenham sido executados, ainda há lacunas operacionais importantes, especialmente em Projects e no workflow real de CI

## 8. Comandos Git executados nesta sessão

Foram executados os seguintes comandos Git:

- `git status --short`
- `git branch --show-current`
- `git branch`
- `git log --oneline --decorate -10`
- `git diff --name-only`
- `git ls-files --others --exclude-standard docs/projeto/manual_colaboracao_codex.md docs/planejamento/rodadas/TEMPLATE_RODADA.md docs/planejamento/rodadas/RODADA_20260322_01.md`
- `git log --graph --decorate --oneline --all`
- `git log --pretty=format:"%h | %ad | %s" --date=short`
- `git log --reverse`
- `git log --stat --reverse`
- `git log -- docs/projeto/`
- `git log -- docs/flows/`
- `git log -- src/`
- `git status --short --untracked-files=all`
- `git diff --cached --name-only`

Esses comandos foram usados para inspecionar:

- estado do working tree local
- branch atual
- branches locais existentes
- histórico recente de commits
- histórico completo do repositório em ordem cronológica e em grafo
- fases reais do projeto com base em commits
- evolução específica de `src/`, `docs/projeto/` e `docs/flows/`
- arquivos modificados no working tree
- existência ou não de arquivos staged
- existência ou não de arquivos não rastreados
- situação de três documentos específicos quanto a estarem ou não como arquivos não rastreados

## 9. Comandos GitHub executados nesta sessão

Foram executados os seguintes comandos `gh`:

- `gh issue list --state open --limit 30`
- `gh issue list --state open --json number,title,labels,milestone`
- `gh pr list --state all --limit 20`
- `gh pr view 18 --comments`
- `gh label list`
- `gh project list --owner rib-thiago`
- `gh project item-list 1 --owner rib-thiago`
- `gh project field-list 1 --owner rib-thiago --format json`
- `gh api repos/rib-thiago/showtrials-tcc/milestones`
- `gh issue view 6 --comments`
- `gh issue list --state all --limit 100 --json number,title,body,labels,milestone,state`
- `gh issue view 6 --json number,title,body,comments,labels,milestone,state`
- `gh issue view 10 --json number,title,body,comments,labels,milestone,state`
- `gh issue view 11 --json number,title,body,comments,labels,milestone,state`
- `gh issue view 12 --json number,title,body,comments,labels,milestone,state`
- `gh issue view 13 --json number,title,body,comments,labels,milestone,state`
- `gh issue view 14 --json number,title,body,comments,labels,milestone,state`
- `gh issue view 15 --json number,title,body,comments,labels,milestone,state`
- `gh issue view 16 --json number,title,body,comments,labels,milestone,state`
- `gh issue view 17 --json number,title,body,comments,labels,milestone,state`
- `gh issue view 1 --json number,title,body,comments,labels,milestone,state`
- `gh issue view 2 --json number,title,body,comments,labels,milestone,state`
- `gh issue view 21 --json number,title,body,comments,labels,milestone,state`

Resultados observados:

- os comandos de issues, PRs, labels, milestones e issue/PR específicos produziram resposta útil após execução com acesso à API
- os comandos de Project falharam com `unknown owner type`
- houve falha inicial de acesso à API do GitHub no sandbox, seguida de repetição com autorização externa
- a listagem completa de issues permitiu distinguir backlog histórico, backlog documental e backlog estratégico atual de engine
- as issues de engine confirmaram a arquitetura-alvo futura em termos de contratos e componentes mínimos
- não foi encontrada, nas issues consultadas, formalização explícita do nome `CraftText`

## 10. Documentos relidos nesta etapa operacional

Foram relidos cuidadosamente, nesta etapa operacional:

- `docs/flows/git_flow.md`
- `docs/flows/GOVERNANCA.md`
- `docs/flows/documentation_flow.md`
- `.github/workflows/ci.yml`
- `docs/ai/00_project_context.md`
- `docs/ai/03_current_state.md`
- `docs/ai/06_git_history.md`
- `docs/ai/09_operational_status.md`

Objetivo da releitura:

- confrontar o estado Git/GitHub observado com as regras normativas de governança
- enquadrar novos documentos dentro da estrutura documental do projeto
- avaliar aderência da branch e do working tree local ao Git Flow oficial
- alinhar narrativa, estado atual e histórico com base em Git e issues
- substituir inferência de CI por leitura direta do workflow real

## 11. O que foi inferido diretamente dos comandos

### 11.1 A partir dos comandos Git

Foi inferido diretamente que:

- o working tree local possui modificações apenas em arquivos de `docs/ai/`
- a branch atual é `docs/ai-context-bootstrap`
- existe diversidade de branches locais, incluindo padrões antigos (`type/*`, `feat/*`, `feature/*`) e padrões mais novos (`docs/*`, `infra/*`, etc.)
- o histórico recente está fortemente concentrado em documentação, governança e colaboração com Codex
- o histórico mais antigo mostra origem monolítica do projeto antes da refatoração para `src/`
- o principal marco arquitetural implementado é a reorganização para arquitetura em camadas em `src/`
- a engine de pipeline não aparece como implementação consolidada no histórico de `src/`
- a governança formal atual surge tardiamente no histórico, principalmente em `docs/flows/` e `docs/projeto/`
- os arquivos:
  - `docs/projeto/manual_colaboracao_codex.md`
  - `docs/planejamento/rodadas/TEMPLATE_RODADA.md`
  - `docs/planejamento/rodadas/RODADA_20260322_01.md`
  não aparecem como arquivos não rastreados via `git ls-files --others --exclude-standard ...`
- no estado atual observado mais ao fim da sessão:
  - não há arquivos staged
  - não há arquivos não rastreados visíveis
  - há nove arquivos modificados em `docs/ai/`

### 11.2 A partir dos comandos GitHub

Foi inferido diretamente que:

- existe uma milestone aberta:
  - `MVP - Engine de Pipeline`
- há conjunto consistente de issues abertas alinhadas a essa milestone, especialmente:
  - `type:engine`
  - `priority:P0`
  - `priority:P1`
  - `strategic`
- existem labels customizadas coerentes com a governança documentada:
  - `type:*`
  - `priority:*`
  - `strategic`
  - `frozen`
- existem PRs abertos para:
  - spike documental/técnico
  - documentação relacionada a Codex
  - consolidação do pipeline de qualidade
- o PR `#18` foi fechado em favor do PR `#19`
- os comentários do PR `#18` e da issue `#6` confirmam preocupação prática com:
  - escopo excessivo
  - mistura de linhas de trabalho
  - necessidade de reapresentar a solução em branch/PR mais saneados
- as issues `#10` a `#17` confirmam a arquitetura-alvo futura como engine de pipeline configurável
- a issue `#6` funciona como infraestrutura habilitadora da milestone da engine, não apenas como backlog genérico de qualidade
- a issue `#21` confirma interesse em fontes externas/coletores, mas explicitamente fora da integração imediata com a engine
- a issue `#1` confirma que o problema de dependências NLP ainda é pendência de infraestrutura
- não há, nas issues examinadas, confirmação explícita de renomeação ou formalização de `CraftText`

### 11.3 A partir da comparação entre comandos e governança

Foi inferido diretamente que:

- o GitHub real já reflete parte substancial da governança formalizada em `GOVERNANCA.md`
- a milestone ativa efetivamente é estrutural, não temporal
- o uso de labels estratégicas e prioridades já está operacionalizado no GitHub
- a governança atual é posterior à maior parte da evolução funcional do produto
- as regras normativas atuais não podem ser retroprojetadas automaticamente para todo o histórico anterior

## 12. Issues examinadas explicitamente

Foram examinadas explicitamente, com conteúdo suficiente para análise, as seguintes issues:

- `#1` `Migrar dependências NLP para Poetry`
- `#2` `Revisar documentação (.md files)`
- `#6` `Infra: Consolidar pipeline de qualidade (lint, type, test, taskipy e CI)`
- `#10` `Engine: Definir contrato de Transformer`
- `#11` `Engine: Definir contrato de Sink`
- `#12` `Engine: Implementar ContextoPipeline`
- `#13` `Engine: Implementar Executor mínimo`
- `#14` `Engine: Pipeline configurável via YAML/JSON`
- `#15` `Engine: Suporte a Iterable para streaming`
- `#16` `Engine: Versionamento incremental de pipeline`
- `#17` `Engine: Migrar 1 caso de uso real para nova arquitetura`
- `#21` `Spike: formalizar prototipo de coletores para fontes documentais externas`

Essas issues foram usadas para:

- distinguir backlog estratégico atual do backlog histórico
- confirmar a arquitetura-alvo futura da milestone ativa
- identificar pendências de infraestrutura que sustentam a transição
- separar o que está no código do que existe apenas como decisão ou intenção rastreável

## 13. Fontes que mudaram o entendimento do projeto

As seguintes fontes alteraram ou refinaram de forma relevante o entendimento do projeto nesta sessão:

### 13.1 Histórico Git completo

Os comandos:

- `git log --graph --decorate --oneline --all`
- `git log --pretty=format:"%h | %ad | %s" --date=short`
- `git log --reverse`
- `git log --stat --reverse`

mudaram a leitura do projeto porque mostraram que:

- o projeto começou como protótipo monolítico funcional
- a arquitetura em camadas surgiu depois como grande refatoração
- a governança formal atual é bem mais recente que a maior parte da evolução funcional
- `FASE11` a `FASE17` não podem ser lidas automaticamente como fases homogêneas de implementação da mesma natureza que `FASE1` a `FASE10`

### 13.2 Logs por diretório

Os comandos:

- `git log -- docs/projeto/`
- `git log -- docs/flows/`
- `git log -- src/`

mudaram a leitura do projeto porque permitiram separar:

- implementação real em `src/`
- formalização documental de visão e governança
- surgimento tardio de `docs/flows/` e `docs/projeto/`

Isso foi decisivo para não confundir documentação posterior com estado implementado no mesmo momento.

### 13.3 Issues da milestone de engine

As issues `#10` a `#17` mudaram a leitura do projeto porque confirmaram, com rastreabilidade formal:

- a arquitetura-alvo futura
- os componentes mínimos da engine
- a estratégia de migração incremental

Elas reforçaram que a engine de pipeline é um plano arquitetural real, e não apenas texto solto em documentação.

### 13.4 Ausência de CraftText nas issues

A busca e leitura das issues relevantes também mudaram a interpretação porque mostraram ausência de:

- issue formal de renomeação
- decisão rastreável sobre transição nominal para `CraftText`

Isso reduziu a força de qualquer narrativa que tratasse `CraftText` como identidade já consolidada.

### 13.5 Issue `#6` e comentários relacionados

A issue `#6` e seus comentários mudaram a leitura operacional porque mostraram:

- uso real da governança para conter escopo
- reapresentação de solução após revisão estrutural
- papel da qualidade como infraestrutura habilitadora da fase atual

Isso fortaleceu a leitura de que a governança atual já está sendo aplicada na prática, não apenas documentada.

### 13.6 Workflow real de CI

A leitura direta de `.github/workflows/ci.yml` mudou a interpretação de qualidade/CI porque confirmou, por evidência direta:

- gatilhos reais do workflow
- existência de um único job visível `test`
- uso explícito de `ruff`, `mypy` e `pytest`
- cobertura mínima de `45%` também no CI
- instalação complementar de dependências NLP via `pip`
- download de modelos spaCy no workflow

Também corrigiu inferências anteriores ao mostrar que:

- o CI **não** usa `task pre-push` como entrypoint
- `mypy` roda no CI, mas em modo tolerante a falha

### 13.7 Revisão de `docs/ai/02_governance.md`

Os ajustes em `docs/ai/02_governance.md` mudaram a qualidade da documentação porque passaram a separar explicitamente:

- norma documental
- evidência real observada
- pontos não confirmados

Isso foi importante para reduzir o risco de tratar governança normativa como enforcement já provado.

### 13.8 Revisão de `docs/ai/08_quality_and_ci.md`

Os ajustes em `docs/ai/08_quality_and_ci.md` mudaram a leitura do projeto porque:

- substituíram descrição inferida do CI por descrição baseada no YAML real
- distinguiram fluxo local confirmado, CI real confirmado e norma documental
- deixaram explícito que local e remoto têm convergência parcial, mas não identidade perfeita

### 13.9 Revalidação de `docs/ai/09_operational_status.md`

A revalidação de `docs/ai/09_operational_status.md` foi relevante porque:

- confirmou que o working tree seguia restrito a `docs/ai/`
- confirmou que não havia mudança no conjunto de arquivos modificados naquele momento
- ajustou a leitura operacional para refletir as revisões recentes em `01`, `02` e `08`
- há evidência concreta de aplicação prática da disciplina de escopo em PRs e issues

## 12. O que permaneceu incerto

Permaneceram incertos, após esta etapa:

- a estrutura real do GitHub Project v2 associado ao fluxo documental
- os fields e options exatos do Project, devido à falha dos comandos de Project com `unknown owner type`
- a coluna/status atual das issues no Project, embora haja indícios textuais de uso de `In review`
- o workflow real de CI em `.github/workflows/ci.yml`, ainda não inspecionado diretamente
- a relação exata entre a branch local `docs/ai-context-bootstrap` e uma issue formal específica
- se o trabalho documental atual está formalmente enquadrado na governança do GitHub ou ainda em preparação local pré-issue/pre-PR
- se os documentos de colaboração e rodadas já estão completamente estabilizados editorialmente, embora não estejam como untracked

## 13. Áreas que ainda mereceriam investigação adicional

As seguintes áreas ainda merecem investigação adicional nesta sessão:

- comparação entre `docs/ai-context-bootstrap`, `main` e branches documentais recentes
- inspeção do workflow real em `.github/workflows/ci.yml`
- inspeção de commits e diff associados ao PR `#19`
- relação concreta entre issue `#6`, branch `infra/quality-pipeline-core` e estado local do repositório
- investigação compatível do GitHub Project v2, possivelmente com comandos ajustados ao comportamento atual do `gh`
- verificação se existe issue formal ou enquadramento explícito para o trabalho em `docs/ai/`
- aprofundamento do histórico Git para localizar:
  - introdução de `ServiceRegistry`
  - reorganização de governança
  - formalização da milestone da engine
- investigação adicional sobre qualquer evidência documental ou histórica da relação entre ShowTrials e CraftText
