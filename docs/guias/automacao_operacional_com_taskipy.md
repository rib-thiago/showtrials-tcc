# Automacao Operacional com Taskipy

## Objetivo

Este documento registra a automacao operacional do projeto baseada em `taskipy`.

Seu objetivo e:

- concentrar comandos recorrentes de qualidade, teste e execucao
- servir como referencia tecnica complementar aos protocolos operacionais
- evitar que detalhes de automacao fiquem misturados ao protocolo principal de Git

## Contexto

O projeto incorporou `taskipy` como mecanismo de automacao de tarefas recorrentes e, em momentos posteriores, passou a reforcar esse uso como parte importante do pipeline local.

Essa automacao nao substitui a governanca nem o protocolo de Git, mas apoia sua execucao pratica.

## Tarefas Relevantes Atuais

Com base no estado atual de [pyproject.toml](/home/thiago/coleta_showtrials/pyproject.toml), as tarefas principais incluem:

- `task lint`
- `task type`
- `task format`
- `task quality`
- `task test`
- `task test-cov`
- `task test-html`
- `task check`
- `task pre-push`
- `task docs`

## Relacao com o Fluxo de Trabalho

As tarefas acima ajudam principalmente em:

- verificacoes antes de abrir pull request
- verificacoes antes de push
- padronizacao de comandos de qualidade
- reducao de variacao manual no fluxo local

## Dividas Tecnicas Relacionadas

O documento legado de qualidade mencionava comandos e rotinas que nao estao confirmados no estado atual de `taskipy`.

Esses itens devem ser tratados como divida tecnica ou candidatos a futura implementacao, e nao como fluxo vigente:

- `task check-file`
- `task lint-file`
- `task type-file`
- `task test-file`
- `task cov-file`
- `task check-structural`
- `task check-scope`
- `task validate-issue`
- `task check-milestone`

Enquanto nao houver lastro no `pyproject.toml` ou em outra fonte primaria suficiente, esses comandos nao devem ser tratados como automacao efetivamente disponivel.

## Observacao Importante

O uso de `taskipy` possui lastro real no historico do projeto, mas sua automacao detalhada pode evoluir.

Por isso, este documento deve ser lido como guia tecnico do estado atual da automacao, e nao como politica imutavel.

## Documentos Relacionados

- [Politica de Governanca do Projeto](../politicas/politica_de_governanca.md)
- [Protocolo de Git do Projeto](../protocolos/protocolo_de_git.md)
- [Protocolo de Qualidade do Projeto](../protocolos/protocolo_de_qualidade.md)
