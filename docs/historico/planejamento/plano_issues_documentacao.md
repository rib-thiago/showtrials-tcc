# Plano Historico de Issues da Documentacao

## Objetivo

Este documento preserva o plano historico de estruturacao do backlog documental formulado no inicio da organizacao mais sistematica da documentacao do projeto.

Seu papel atual nao e reger a operacao vigente, mas registrar:

- como o backlog documental foi imaginado naquele momento;
- como issues, milestones, flows e fases eram relacionados entre si;
- quais blocos de trabalho foram propostos;
- o que desse plano chegou a se materializar no projeto.

## Contexto Historico

O plano original foi elaborado em um momento em que o projeto ainda operava com um regime mais antigo de organizacao do trabalho, marcado por:

- milestones temporais;
- taxonomia antiga de labels e tipos;
- forte aproximacao entre issue e fase;
- backlog de `flows` ainda em fase de criacao;
- previsao de automacao em lote para abertura de issues.

Desde entao, a frente de saneamento documental consolidou um regime diferente, com:

- milestones estruturais, e nao temporais;
- taxonomia atual de labels e branches;
- `flows` ja saneados e redistribuidos;
- documentos de fase tratados como historicos consolidados;
- rodadas tratadas como registros operacionais curtos.

## Estrutura do Plano Original

O plano original previa um backlog de 29 issues distribuidas em cinco blocos:

1. Fundacao
2. Qualidade e testes
3. Dependencias e infra
4. Novas funcionalidades
5. Documentacao e finalizacao

Ele combinava:

- tabelas de backlog;
- proposta de labels;
- estimativas;
- milestones por semanas;
- e um script extenso para abertura automatica das issues.

## Relacao com Fases, Issues e Milestones

No plano original, fases, issues e milestones apareciam muito proximas entre si.

Em especial:

- algumas issues eram formuladas diretamente como `FASE 17`, `FASE 18`, `FASE 19` e `FASE 20`;
- milestones eram tratadas como janelas temporais de execucao;
- o backlog documental era apresentado como roteiro operacional futuro.

Na leitura atual do projeto, essa aproximacao precisa ser reinterpretada:

- issue e unidade rastreavel de trabalho;
- milestone e entregavel estrutural;
- documento de fase e historico consolidado;
- rodada e registro operacional curto.

Essa leitura atual esta formalizada em [regime_documental_de_fases_e_rodadas.md](/home/thiago/coleta_showtrials/docs/projeto/regime_documental_de_fases_e_rodadas.md) e articulada com [politica_de_governanca.md](/home/thiago/coleta_showtrials/docs/politicas/politica_de_governanca.md).

## O Que se Materializou

Parte importante do plano original de fato se materializou, ainda que nao exatamente na forma prevista.

Entre os pontos que ganharam existencia real no projeto estao:

- a criacao e o saneamento progressivo do bloco `docs/flows/`;
- a consolidacao de guias e protocolos especificos para Git, qualidade, telemetria, debug, dependencias, refatoracao, correcoes urgentes, auto-revisao e documentacao;
- a preservacao de historicos de fase relevantes;
- a formalizacao posterior do regime entre fases e rodadas;
- a existencia de issues reais relacionadas a documentacao, qualidade e dependencias NLP.

## O Que Ficou Superado

Os pontos abaixo pertencem ao plano original, mas nao devem ser lidos como regra vigente:

- milestones temporais como `Semanas 1-2`, `Semanas 3-4` e similares;
- taxonomia antiga como `fase`, `tipo/testes`, `tipo/qualidade` e `type/*`;
- backlog de `flows` como se ainda estivesse por ser criado;
- integracao com `mkdocs.yml` como tarefa atual desta rodada;
- script massivo para criar 29 issues como operacao recomendada no presente;
- uso de `FASE*.md` como unidade universal do backlog corrente.

## Leitura Atual do Documento

Hoje este arquivo deve ser lido como:

- registro historico de um plano de organizacao do backlog documental;
- evidencia de uma fase de transicao do regime de documentacao do projeto;
- fonte de contexto para entender como surgiram certas issues, fases e prioridades.

Ele nao deve ser lido como:

- plano operacional vigente;
- template atual para criacao de backlog;
- guia de governanca;
- regra viva de milestones, labels ou branches.

## Documentos Relacionados

- [manual_gestao.md](/home/thiago/coleta_showtrials/docs/projeto/manual_gestao.md)
- [politica_de_governanca.md](/home/thiago/coleta_showtrials/docs/politicas/politica_de_governanca.md)
- [guia_de_documentacao_do_projeto.md](/home/thiago/coleta_showtrials/docs/guias/guia_de_documentacao_do_projeto.md)
- [regime_documental_de_fases_e_rodadas.md](/home/thiago/coleta_showtrials/docs/projeto/regime_documental_de_fases_e_rodadas.md)
- [versionamento_e_releases.md](/home/thiago/coleta_showtrials/docs/projeto/versionamento_e_releases.md)
