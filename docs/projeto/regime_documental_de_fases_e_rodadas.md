# Regime Documental de Fases e Rodadas

## Objetivo

Este documento formaliza a relacao entre documentos de fase e documentos de rodada no projeto.

Seu objetivo e:

- preservar a documentacao historica sem trata-la como norma vigente
- explicitar o papel operacional das rodadas
- orientar a rastreabilidade entre trabalho executado, historico e artefatos finais

## Natureza dos Documentos de Fase

Documentos de fase devem ser lidos como historicos consolidados de intervencoes relevantes.

Seu papel principal e:

- registrar uma entrega, consolidacao ou intervencao com peso proprio
- preservar contexto historico de um bloco importante de trabalho
- permitir leitura retrospectiva do que foi feito, por que foi feito e como se conectou ao projeto

Documentos de fase nao devem ser lidos automaticamente como:

- politica vigente
- template universal para qualquer novo trabalho
- prova unica do estado atual implementado

## Natureza dos Documentos de Rodada

Documentos de rodada sao registros operacionais curtos de analise, execucao, decisao e fechamento.

Seu papel principal e:

- registrar o contexto de uma sessao ou bloco curto de trabalho
- explicitar fontes lidas, decisoes tomadas e limites da rodada
- apoiar rastreabilidade de curto prazo
- servir como memoria operacional da evolucao de uma frente

## Relacao entre Fases e Rodadas

Fases e rodadas tem granularidades diferentes.

- uma fase consolida uma intervencao historica maior
- uma rodada registra um passo operacional curto

Regra pratica:

- varias rodadas podem alimentar uma unica fase
- nem toda rodada precisa gerar uma fase
- uma fase pode ser melhor compreendida a partir do conjunto de rodadas, commits, issues e PRs que a cercam

## Quando uma Rodada Deve Alimentar uma Fase

Uma rodada deve alimentar ou motivar um documento de fase quando:

- o trabalho produziu uma intervencao relevante e relativamente consolidada
- ha valor em preservar o resultado como historico proprio
- o bloco executado faz sentido como entrega retrospectivamente identificavel
- a rastreabilidade historica ganhara clareza com esse nivel adicional de consolidacao

## Quando uma Rodada Nao Precisa Gerar Fase

Uma rodada nao precisa gerar fase quando:

- o trabalho foi exploratorio, corretivo ou intermediario
- o resultado e melhor lido apenas como parte da trilha operacional da frente
- ainda nao existe consolidacao suficiente para um historico proprio
- a rodada ja fornece rastreabilidade suficiente para o passo realizado

## Rastreabilidade e Inspecao dos Historicos

Idealmente, um documento de fase deve permitir inspecao de:

- objetivo da intervencao
- artefatos afetados
- branch ou branches relacionadas, quando identificaveis
- commits relacionados, quando identificaveis
- issues relacionadas
- PRs relacionados, quando houver
- contexto historico minimo da intervencao

Isso nao significa exigir perfeicao retroativa imediata de todos os historicos antigos.

Significa, sim, adotar uma regua de leitura e saneamento segundo a qual documentos de fase devem tender a se tornar historicos mais inspecionaveis, mais rastreaveis e menos ambiguos.

## Limites e Observacoes

- o historico principal do projeto continua distribuido entre Git, issues, PRs e documentos de rodada
- documentos finais vivos nao devem carregar narrativa historica paralela quando essa rastreabilidade ja estiver suficientemente preservada nessas camadas
- documentos de fase permanecem relevantes como camada historica interpretavel, e nao como substitutos de Git ou de backlog

## Documentos Relacionados

- [Guia de Documentacao do Projeto](/home/thiago/coleta_showtrials/docs/flows/guia_de_documentacao_do_projeto.md)
- [Padrao Minimo Documental da Etapa 5](/home/thiago/coleta_showtrials/docs/planejamento/padrao_minimo_documental_etapa_5.md)
- [Plano Operacional da Frente de Saneamento da Documentacao Legada](/home/thiago/coleta_showtrials/docs/planejamento/plano_frente_saneamento_documentacao_legacy.md)
