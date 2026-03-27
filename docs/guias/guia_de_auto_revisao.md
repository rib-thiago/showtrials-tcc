# Guia de Auto-Revisao antes de PR e Merge

## Objetivo

Este guia apoia a auto-revisao de uma mudanca antes de pull request e merge.

Seu objetivo e:

- integrar, de forma pratica, os criterios ja definidos em governanca, Git e qualidade
- reduzir erros bobos, dispersao de escopo e pendencias ocultas antes de revisao
- ajudar a verificar se a mudanca esta pronta para seguir no fluxo normal do projeto

## Contexto de Uso

Este documento nao substitui a politica de governanca, o protocolo de Git nem o protocolo de qualidade.

Ele deve ser usado como guia operacional curto para revisar uma mudanca antes de abrir pull request ou concluir merge.

Quando a mudanca envolver automacao, telemetria, depuracao, refatoracao ou movimentacao de status no Project, este guia deve ser complementado pelos documentos especificos dos blocos `docs/guias/`, `docs/politicas/` e `docs/protocolos/`.

## Checklist de Escopo e Estrutura

Antes de seguir para revisao:

- a mudanca continua dentro do escopo da issue
- a branch representa corretamente o tipo principal do trabalho
- nao ha codigo comentado, debug residual ou artefatos temporarios esquecidos
- nomes e responsabilidades permanecem claros
- nao houve mudanca estrutural implicita escondida em alteracao pequena

## Checklist Tecnico Minimo

Antes de considerar a mudanca pronta para revisao:

- criterios de aceite continuam atendidos
- verificacoes tecnicas minimas aplicaveis foram executadas
- tipagem e clareza estrutural permanecem coerentes
- nao ha codigo morto, `TODO` sem justificativa ou efeitos colaterais nao documentados
- testabilidade foi preservada
- quando houver impacto observavel, instrumentacao ou testes de telemetria, a mudanca foi verificada com apoio do guia especifico de telemetria

## Checklist de Commit, Branch e Pull Request

Antes de abrir pull request ou concluir merge, verificar no minimo:

- commits legiveis, descritivos e coerentes com a mudanca
- branch atualizada em nivel suficiente para evitar divergencia desnecessaria
- pull request vinculado a issue correta
- descricao do pull request explica a solucao e o impacto arquitetural quando necessario
- CI e validacoes essenciais nao apresentam bloqueios conhecidos

## Quando Consultar Outros Guias

- consultar [Protocolo de Git do Projeto](../protocolos/protocolo_de_git.md) para branch, commit, pull request, merge e duvidas operacionais de Git
- consultar [Protocolo de Qualidade do Projeto](../protocolos/protocolo_de_qualidade.md) para criterios tecnicos minimos e coerencia arquitetural
- consultar [Automacao Operacional com Taskipy](automacao_operacional_com_taskipy.md) para a automacao atualmente disponivel
- consultar [Guia de Telemetria do Projeto](guia_de_telemetria.md) quando a mudanca envolver contadores, instrumentacao ou testes de telemetria
- consultar [Guia de GitHub Projects com gh CLI](guia_github_projects_cli.md) para movimentacao operacional de status no Project

## Pendencias e Validacoes Necessarias

- comandos por arquivo mencionados no documento legado nao estao confirmados no `taskipy` atual e nao devem ser tratados como fluxo vigente neste guia
- este guia nao define estrategia especifica de merge; essa decisao permanece ancorada no protocolo de Git e em discussoes futuras de processo
- exemplos historicos do documento legado, incluindo branches antigas e fluxos centrados em fases especificas, nao representam mais o estado normativo atual do projeto

## Documentos Relacionados

- [Politica de Governanca do Projeto](../politicas/politica_de_governanca.md)
- [Protocolo de Git do Projeto](../protocolos/protocolo_de_git.md)
- [Protocolo de Qualidade do Projeto](../protocolos/protocolo_de_qualidade.md)
- [Automacao Operacional com Taskipy](automacao_operacional_com_taskipy.md)
- [Guia de Telemetria do Projeto](guia_de_telemetria.md)
- [Guia de GitHub Projects com gh CLI](guia_github_projects_cli.md)
- [Conventional Commits](https://www.conventionalcommits.org/)
