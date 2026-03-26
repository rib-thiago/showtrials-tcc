# Versionamento e Releases

## Objetivo

Este documento registra a estrategia documental atual de versionamento e releases associada ao projeto.

Seu objetivo e:

- separar versionamento e releases do protocolo cotidiano de Git
- preservar o conteudo util originalmente presente em `git_flow.md`
- explicitar o que e diretriz, o que e historico e o que ainda pode exigir validacao futura

## Contexto

O documento original de `git_flow` reunia, no mesmo corpo:

- regras de branches e pull requests
- estrategia de merge
- versionamento semantico
- criacao de releases

Durante o saneamento documental, optou-se por separar o tema de versionamento e releases em artefato proprio, por se tratar de assunto distinto do protocolo diario de Git.

## Estrutura Basica de Versao

O projeto adotou formulacao baseada em versionamento semantico:

```text
vMAJOR.MINOR.PATCH
```

Leitura pretendida:

- `major`: mudancas que quebram compatibilidade
- `minor`: novas funcionalidades
- `patch`: correcoes

## Observacoes Sobre Lastro

O projeto possui tags e mecanica de versionamento no historico, mas a associacao rigida entre milestones especificas e versoes exatas deve ser tratada com cautela.

Ela pode refletir:

- planejamento de epoca
- intencao de release
- ou diretriz parcial, e nao necessariamente pratica consolidada em todos os ciclos do projeto

## Pendencias de Validacao e Refinamento

- revisar futuramente a estrategia real de release do projeto contra o historico Git e GitHub
- decidir se este tema deve virar politica mais formal de release ou permanecer como guia/proposta
- reavaliar a relacao entre milestones, tags e entregas reais em discussao posterior de processo
