# Historico da Fase 13 - Limpeza e Organizacao do Repositorio

## Natureza do Documento

Este documento registra historicamente a intervencao de limpeza e organizacao do
repositorio do projeto. Ele deve ser lido como memoria tecnica e operacional de
um marco de higiene estrutural, e nao como tutorial vigente de comandos de
limpeza ou como checklist atual de manutencao do repositorio.

## Objetivo da Intervencao

Reduzir o acoplamento do repositorio a artefatos temporarios, remover codigo
legado sem uso, reforcar a organizacao de scripts e consolidar uma estrutura de
versionamento mais disciplinada.

## Contexto

Depois da introducao de varias capacidades tecnicas e da estabilizacao inicial
de CI e telemetria, o repositorio acumulou:

- artefatos gerados pela aplicacao;
- arquivos de backup espalhados;
- scripts de diagnostico fora de lugar;
- codigo legado ainda preservado no arvore principal;
- um banco de dados vazio duplicado na raiz;
- regras de exclusao ainda insuficientes no `.gitignore`.

Esta fase registra o momento em que o projeto passou a tratar explicitamente a
organizacao do repositorio como parte da sua qualidade tecnica.

Tambem e importante registrar que o documento legado parece ter sido redigido
posteriormente sobre um conjunto de mudancas ja realizadas em Git, e nao como
o registro literal e contemporaneo de um unico commit-fase fechado no mesmo
padrao das fases anteriores.

## Intervencoes Aplicadas

As intervencoes historicamente centrais deste marco foram:

- remocao de codigo legado remanescente;
- remocao de arquivos `.bak` e artefatos gerados pela aplicacao;
- remocao de um banco de dados vazio duplicado na raiz;
- reorganizacao de scripts de diagnostico sob `scripts/`;
- reforco inicial do `.gitignore`;
- reducao de ruido estrutural no repositorio.

Do ponto de vista tecnico, a fase ajudou a separar melhor:

- codigo ativo;
- codigo legado;
- artefatos gerados;
- scripts utilitarios;
- dados persistidos em local padronizado.

## Esquema ASCII Preservado

```text
[Repositorio Inflado]
      |
      v
[Remocao de legado, backups e artefatos]
      |
      v
[Scripts movidos para scripts/]
      |
      v
[.gitignore reforcado + estrutura mais limpa]
```

O esquema preserva a ideia central da fase: o foco nao foi adicionar uma nova
capacidade funcional, mas tornar o repositorio mais confiavel e governavel.

## Artefatos Afetados

Artefatos com lastro forte no commit principal e no commit relacionado mais
proximo:

- [.gitignore](/home/thiago/coleta_showtrials/.gitignore)
- [data/showtrials.db](/home/thiago/coleta_showtrials/data/showtrials.db)
- [scripts/diagnostico.sh](/home/thiago/coleta_showtrials/scripts/diagnostico.sh)
- [scripts/diagnostico_ci.sh](/home/thiago/coleta_showtrials/scripts/diagnostico_ci.sh)
- [scripts/diagnostico_limpeza.sh](/home/thiago/coleta_showtrials/scripts/diagnostico_limpeza.sh)

Tambem fizeram parte do marco historico:

- remocao da arvore `legacy/`;
- remocao de `showtrials.db` na raiz;
- remocao de arquivos `.bak` distribuidos pelo codigo.

## Rastreabilidade Git e GitHub

- Commit principal identificado com seguranca:
  - `607ef3e` - `chore: limpeza geral do repositório`
- Commit relacionado importante:
  - `b93f91b` - `clean: remove código legado e atualiza .gitignore`
- Branch principal identificada com seguranca:
  - `chore/cleanup-repository`
- PR:
  - nenhum PR identificado com seguranca
- Issue principal:
  - nenhuma issue principal numerada confirmada com seguranca

## Impacto Tecnico

Historicamente, a fase teve impacto importante em quatro frentes:

- reduziu ruido estrutural no repositorio;
- reforcou a separacao entre codigo ativo e codigo legado;
- melhorou a disciplina de versionamento de artefatos gerados;
- preparou o projeto para uma manutencao mais previsivel do diretorio raiz e
  da arvore utilitaria.

Mesmo nao sendo uma fase de feature, ela teve papel relevante na qualidade
global do projeto, porque atacou a confiabilidade do proprio ambiente de
trabalho.

## Limites de Leitura no Estado Atual

Esta fase registra um marco historico de limpeza e organizacao do repositorio.
Ela nao deve ser lida isoladamente como politica vigente completa sobre
documentacao, scripts, dependencias ou manutencao estrutural.

Para a leitura atual mais forte desses temas, devem ser considerados tambem:

- [Guia de Documentacao do Projeto](/home/thiago/coleta_showtrials/docs/guias/guia_de_documentacao_do_projeto.md)
- [Guia de Manutencao do Site Documental](/home/thiago/coleta_showtrials/docs/guias/guia_de_manutencao_do_site_documental.md)
- [manual_gestao.md](/home/thiago/coleta_showtrials/docs/projeto/manual_gestao.md)
- [FASE17_PRIMEIRA_REORGANIZACAO_DOCUMENTAL_AMPLA.md](/home/thiago/coleta_showtrials/docs/fases/FASE17_PRIMEIRA_REORGANIZACAO_DOCUMENTAL_AMPLA.md)

## Documentos Relacionados

- [FASE11_ESTABILIZACAO_INICIAL_DO_CI.md](/home/thiago/coleta_showtrials/docs/fases/FASE11_ESTABILIZACAO_INICIAL_DO_CI.md)
- [FASE12_PADRONIZACAO_DA_TELEMETRIA_EM_TIPODOCUMENTO.md](/home/thiago/coleta_showtrials/docs/fases/FASE12_PADRONIZACAO_DA_TELEMETRIA_EM_TIPODOCUMENTO.md)
- [FASE17_PRIMEIRA_REORGANIZACAO_DOCUMENTAL_AMPLA.md](/home/thiago/coleta_showtrials/docs/fases/FASE17_PRIMEIRA_REORGANIZACAO_DOCUMENTAL_AMPLA.md)
- [manual_gestao.md](/home/thiago/coleta_showtrials/docs/projeto/manual_gestao.md)
