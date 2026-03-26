# Protocolo de Git do Projeto

## Objetivo

Este protocolo define as regras operacionais de uso de Git no projeto.

Seu objetivo e:

- manter rastreabilidade entre issue, branch e pull request
- reforcar disciplina de execucao
- reduzir mudancas fora de escopo
- alinhar o uso de Git a politica de governanca do projeto

## Escopo

Este protocolo se aplica a:

- criacao e uso de branches
- relacao entre issue, branch e pull request
- regras para commits
- atualizacao da branch de trabalho
- verificacoes minimas antes de pull request e merge

## Principios Operacionais

As regras operacionais basicas do projeto sao:

- nunca trabalhar diretamente na `main`
- toda alteracao relevante deve estar vinculada a uma issue
- uma branch deve estar associada a uma unica issue
- o fluxo de Git deve respeitar a milestone ativa e a politica de foco do projeto
- mudancas estruturais nao devem entrar de forma implicita em branches de feature

## Politica de Branches

O formato obrigatorio de branch e:

- `engine/<descricao-curta>`
- `infra/<descricao-curta>`
- `feature/<descricao-curta>`
- `docs/<descricao-curta>`
- `refactor/<descricao-curta>`
- `bug/<descricao-curta>`

Regras aplicaveis:

- usar hifen (`-`), nao underscore (`_`)
- manter nome curto e sem ambiguidade
- criar uma branch por issue
- usar tipo de branch coerente com o tipo principal da issue

Exemplos:

- `engine/contexto-pipeline`
- `infra/mypy-fix`
- `docs/revisao-governanca`
- `bug/exportar-id-none`

## Fluxo de Trabalho com Issue, Branch e Pull Request

O fluxo esperado e:

1. selecionar a issue compativel com a governanca vigente
2. criar branch com tipo adequado
3. implementar a mudanca sem ampliar escopo
4. abrir pull request vinculado a issue
5. concluir merge apenas apos revisao e verificacoes minimas

Em termos operacionais:

- a issue deve estar coerente com a milestone ativa quando isso for exigido pela governanca
- a branch deve refletir o tipo principal do trabalho
- o pull request deve descrever a solucao e vincular a issue correspondente

## Regras para Commits

Os commits devem ser:

- pequenos
- descritivos
- semanticamente coerentes com a mudanca
- restritos ao escopo da issue

Exemplos aceitaveis:

```bash
git commit -m "engine: define contrato de transformer"
git commit -m "infra: ajusta configuracao do mypy"
```

Exemplos a evitar:

```bash
git commit -m "ajustes"
git commit -m "engine: pipeline e correcao de bug"
```

## Atualizacao da Branch

A branch de trabalho deve ser mantida atualizada em relacao a `main`.

Quando necessario:

```bash
git fetch origin
git rebase origin/main
```

O objetivo dessa atualizacao e reduzir divergencia desnecessaria e facilitar revisao e integracao.

## Criterios Minimos Antes de Abrir Pull Request

Antes de abrir um pull request, verificar no minimo:

- a mudanca continua dentro do escopo da issue
- os commits estao legiveis e coerentes
- a branch usa tipo e nome adequados
- as verificacoes tecnicas minimas aplicaveis foram executadas
- o impacto arquitetural foi identificado quando existir

## Criterios Minimos Antes de Merge

Antes de concluir o merge, verificar no minimo:

- pull request revisado
- criterios de aceite atendidos
- verificacoes tecnicas essenciais concluidas
- branch razoavelmente atualizada
- ausencia de mudancas fora de escopo

## Pendencias e Validacoes Necessarias

- a configuracao remota de protecao da branch `main` nao foi confirmada nesta frente e deve ser validada em fonte primaria remota
- o historico Git do projeto mostra uso recorrente de merge commits; por isso, esta frente nao sustenta afirmar squash merge como regra consolidada do projeto sem deliberacao posterior
- a estrategia de merge do projeto deve ser reavaliada futuramente em discussao propria de processo e governanca

## Documentos Relacionados

- [Politica de Governanca do Projeto](politica_de_governanca.md)
- [Protocolo de Qualidade do Projeto](protocolo_de_qualidade.md)
- [Automacao Operacional com Taskipy](automacao_operacional_com_taskipy.md)
- [Versionamento e Releases](/home/thiago/coleta_showtrials/docs/projeto/versionamento_e_releases.md)
