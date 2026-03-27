# Diagnostico Historico da Crise Inicial de CI por Dependencias NLP

## Natureza do Documento

Este documento registra historicamente o diagnostico da crise inicial do
pipeline de CI provocada pela ausencia de dependencias de NLP no ambiente do
GitHub Actions.

Ele deve ser lido como diagnostico historico de uma falha concreta de epoca, e
nao como descricao completa do estado atual das dependencias NLP ou do
tratamento vigente do problema.

## Problema Diagnosticado

O pipeline de integracao continua passou a falhar com erro de importacao no
bloco NLP:

```text
ModuleNotFoundError: No module named 'spacy'
```

Esse erro afetava testes ligados ao subsistema de analise de texto e bloqueava
o funcionamento regular do pipeline no periodo.

## Evidencias Principais

### Cadeia de Importacao

```text
test_analisar_acervo.py
  -> src.application.use_cases.analisar_acervo
    -> src.infrastructure.analysis.spacy_analyzer
      -> import spacy
```

### Assimetria entre Ambientes

O diagnostico historico mostrou uma diferenca relevante entre:

- ambiente local, onde o bloco NLP estava sendo completado por instalacao
  complementar fora do `poetry install`;
- ambiente de CI, que executava apenas o fluxo padrao do Poetry.

Essa assimetria explicava por que funcionalidades de NLP podiam funcionar
localmente e falhar no GitHub Actions.

## Causa Raiz Identificada

A causa raiz identificada naquele momento foi:

- o subsistema de NLP introduzido anteriormente dependia de bibliotecas e
  modelos nao plenamente representados no fluxo padrao de instalacao;
- o CI reproduzia apenas `poetry install`;
- o GitHub Actions nao replicava o workaround local usado para o bloco NLP.

## Solucao Historica Aplicada

A solucao historica adotada foi complementar o CI com instalacao via `pip` das
dependencias NLP necessarias para destravar o pipeline.

O lastro tecnico principal dessa solucao esta em:

- [`c87fc9e`](https://github.com/rib-thiago/showtrials-tcc/commit/c87fc9eac947b9748c53beaed12de293d173203a) - `fix: adiciona dependências NLP via pip no CI`
- [FASE11_ESTABILIZACAO_INICIAL_DO_CI.md](/home/thiago/coleta_showtrials/docs/fases/FASE11_ESTABILIZACAO_INICIAL_DO_CI.md)

## Impacto Historico

Historicamente, este diagnostico importa por tres motivos:

- mostrou com clareza a divergencia entre ambiente local e ambiente de CI;
- justificou a solucao provisoria implementada na fase correspondente;
- revelou que o problema de dependencias NLP era estrutural e nao uma falha
  isolada de configuracao.

## Limites de Leitura no Estado Atual

Este documento nao deve ser lido como fonte viva principal para:

- uso atual do Poetry;
- execucao atual dos testes;
- manutencao atual do pipeline;
- estado atual da transicao das dependencias NLP.

Para isso, a leitura mais forte hoje deve ser feita em:

- [dependencias_nlp_estado_e_transicao.md](/home/thiago/coleta_showtrials/docs/projeto/dependencias_nlp_estado_e_transicao.md)
- [FASE11_ESTABILIZACAO_INICIAL_DO_CI.md](/home/thiago/coleta_showtrials/docs/fases/FASE11_ESTABILIZACAO_INICIAL_DO_CI.md)
- [contributing.md](/home/thiago/coleta_showtrials/docs/contributing.md)

## Documentos Relacionados

- [FASE08_INTRODUCAO_DO_SUBSISTEMA_DE_ANALISE_DE_TEXTO.md](/home/thiago/coleta_showtrials/docs/fases/FASE08_INTRODUCAO_DO_SUBSISTEMA_DE_ANALISE_DE_TEXTO.md)
- [FASE11_ESTABILIZACAO_INICIAL_DO_CI.md](/home/thiago/coleta_showtrials/docs/fases/FASE11_ESTABILIZACAO_INICIAL_DO_CI.md)
- [dependencias_nlp_estado_e_transicao.md](/home/thiago/coleta_showtrials/docs/projeto/dependencias_nlp_estado_e_transicao.md)
- [guia_de_dependencias.md](/home/thiago/coleta_showtrials/docs/flows/guia_de_dependencias.md)
