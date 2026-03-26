# Politica de Governanca do Projeto

## Objetivo

Esta politica define as regras de governanca que orientam a organizacao do trabalho no projeto.

Seu objetivo e:

- preservar foco arquitetural
- manter rastreabilidade tecnica
- reduzir dispersao de escopo
- reforcar entregaveis estruturais
- disciplinar a evolucao incremental do projeto

## Escopo

Esta politica se aplica a:

- milestones
- labels
- fluxo de status no project
- criacao e encerramento de issues
- branches
- pull requests
- mudancas estruturais

## Principios de Governanca

O projeto adota os principios abaixo:

- foco arquitetural
- rastreabilidade tecnica
- entregaveis estruturais
- reducao de dispersao
- evolucao incremental controlada

Toda organizacao de trabalho deve preservar coerencia arquitetural e evitar feature creep.

## Politica de Milestones

Apenas **1 milestone estrategica pode estar ativa simultaneamente**.

Milestone representa um **entregavel estrutural relevante**, nunca um periodo temporal.

Exemplos validos:

- `MVP - Engine de Pipeline`
- `M2 - Migracao completa`
- `M3 - Evolucao do CLI`

Exemplos invalidos:

- `Semanas 1-2`
- `Sprint X`
- `Marco 2026`

Regras aplicaveis:

- issues estruturais devem estar vinculadas a milestone ativa
- issues nao estruturais nao devem competir com a milestone estrategica
- milestones antigas devem ser encerradas, nunca apagadas

## Politica de Labels

### Tipos

Toda issue deve possuir exatamente um tipo principal:

- `type:engine`
- `type:infra`
- `type:feature`
- `type:docs`
- `type:refactor`
- `type:bug`

### Prioridades

- `priority:P0`: bloqueia arquitetura
- `priority:P1`: necessaria para a milestone ativa
- `priority:P2`: melhoria incremental ou nao urgente

Durante milestone estrutural:

- apenas `P0` e `P1` podem ir para `Ready`
- `P2` permanece em `Backlog`

### Status estrategico

- `strategic`: faz parte da milestone ativa
- `frozen`: fica congelada ate a conclusao da milestone ativa

## Fluxo de Status

O fluxo oficial de status no project e:

`Backlog -> Ready -> In Progress -> In Review -> Done`

Regras aplicaveis:

- maximo de **1 issue em `In Progress` por vez**
- nenhuma issue vai para `Ready` sem criterios de aceite claros
- `In Review` exige checklist tecnico minimo
- apenas issues da milestone ativa podem entrar em `In Progress`

## Criterios para Gestao de Issues

### Criacao de issue

Uma issue so deve ser criada se:

- exigir mais de uma sessao de trabalho
- possuir criterio de aceite objetivo
- for rastreavel e mensuravel
- nao for microajuste trivial

Toda issue deve conter:

1. contexto
2. problema
3. objetivo
4. criterios de aceite
5. fora de escopo
6. tipo
7. prioridade
8. milestone, se aplicavel

### Encerramento de issue

Uma issue so pode ser movida para `Done` se:

- criterios de aceite tiverem sido cumpridos
- codigo estiver revisado
- pull request estiver mergeado
- nao houver pendencias tecnicas ocultas

## Politica de Foco

Durante execucao de uma milestone estrategica:

- features paralelas devem ser marcadas como `frozen`
- apenas trabalho relacionado a milestone ativa pode avancar
- alternancia de contexto deve ser evitada

## Politica de Branches

O formato obrigatorio de branch e:

- `engine/<descricao>`
- `infra/<descricao>`
- `feature/<descricao>`
- `docs/<descricao>`
- `refactor/<descricao>`
- `bug/<descricao>`

Exemplos:

- `engine/transformer-contract`
- `infra/mypy-fix`
- `feature/dark-mode`

Nunca se deve trabalhar diretamente na `main`.

## Politica de Pull Requests

Todo pull request deve:

- referenciar a issue correspondente
- descrever a solucao adotada
- explicar impacto arquitetural, quando houver
- confirmar criterios de aceite
- estar vinculado a milestone ativa, quando for `strategic`

## Regra de Evolucao Arquitetural

Mudancas estruturais:

- devem ser discutidas antes da implementacao
- devem ser rastreadas como `type:engine` ou `type:refactor`
- nunca devem ocorrer implicitamente dentro de issues de feature

## Documentos Relacionados

- [Protocolo de Git do Projeto](protocolo_de_git.md)
- [Protocolo de Qualidade do Projeto](protocolo_de_qualidade.md)
- [Automacao Operacional com Taskipy](automacao_operacional_com_taskipy.md)
