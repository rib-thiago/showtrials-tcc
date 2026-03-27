# Historico da Fase 11 - Estabilizacao Inicial do CI

## Natureza do Documento

Este documento registra historicamente a intervencao que estabilizou o pipeline inicial de integracao continua do projeto diante do problema das dependencias de NLP no CI.

Ele nao deve ser lido como definicao vigente e definitiva do tratamento de dependencias NLP. O estado atual dessa questao deve ser consultado principalmente em:

- [Dependencias NLP: Estado Atual e Transicao](../projeto/dependencias_nlp_estado_e_transicao.md)
- [Guia de Dependencias do Projeto](../flows/guia_de_dependencias.md)
- [Guia de Contribuicao](../contributing.md)

## Objetivo da Intervencao

Desbloquear o pipeline de CI que havia passado a falhar por ausencia de dependencias de NLP no ambiente do GitHub Actions.

## Contexto

O problema surgiu depois da introducao das funcionalidades de analise de texto, que passaram a depender de:

- `numpy`
- `spacy`
- modelos de idioma do `spacy`
- bibliotecas auxiliares como `textblob`, `nltk`, `wordcloud` e `matplotlib`

O ambiente local e o ambiente do CI deixaram de se comportar de forma equivalente, e o pipeline passou a falhar com erros de importacao ligados ao bloco NLP.

## Problema Enfrentado

O nucleo do problema era que o fluxo padrao de `poetry install` nao bastava, naquele momento, para reproduzir no CI o conjunto de dependencias exigido pelo bloco de analise de texto.

Historicamente, isso impactava:

- execucao da suite automatizada
- verificacoes de merge
- confianca no pipeline

## Solucao Aplicada

A intervencao historica adicionou ao workflow de CI um complemento via `pip` dentro do ambiente do Poetry para instalar o bloco NLP e baixar modelos do `spacy`.

Como historico, a solucao aplicada pode ser resumida assim:

- `poetry install` para o ambiente principal
- `pip install` complementar para as dependencias NLP
- download dos modelos `en_core_web_sm` e `ru_core_news_sm`

Essa decisao destravou o pipeline, mas ao mesmo tempo consolidou uma forma hibrida de gerenciamento de dependencias que permaneceu como divida tecnica posterior.

## Artefatos Afetados

Com lastro direto no commit principal identificado:

- `.github/workflows/ci.yml`

Artefatos historicamente relacionados:

- [diagnostico_ci.md](../metricas/diagnostico_ci.md)
- [Dependencias NLP: Estado Atual e Transicao](../projeto/dependencias_nlp_estado_e_transicao.md)

## Rastreabilidade Git e GitHub

### Commit principal

- [`c87fc9e`](https://github.com/rib-thiago/showtrials-tcc/commit/c87fc9eac947b9748c53beaed12de293d173203a) - `fix: adiciona dependências NLP via pip no CI`

### Branch principal

- `fix/ci-dependencies-pip`

### Issue principal historica

- `#CI`, conforme registrado na mensagem do commit principal e no documento legado

### Issue relacionada ainda aberta

- [#1 - Migrar dependencias NLP para Poetry](https://github.com/rib-thiago/showtrials-tcc/issues/1)

### Pull Request

- nenhum pull request foi identificado com seguranca a partir do commit principal analisado

## Impacto Tecnico

Como historico, esta fase registra um momento em que:

- o CI deixou de ficar bloqueado pelo bloco NLP
- o projeto recuperou capacidade pratica de verificar a suite automatizada no GitHub Actions
- o tratamento do problema deixou de ser implícito e passou a ficar documentado

Ao mesmo tempo, a fase tambem marca a origem de uma divida tecnica importante:

- a estabilizacao do CI foi obtida por um workaround hibrido, e nao por resolucao definitiva no `pyproject.toml`

## Relacao com o Estado Atual das Dependencias NLP

Hoje, a leitura correta desta fase e:

- ela documenta a estabilizacao inicial do CI
- ela nao resolve definitivamente o gerenciamento do bloco NLP
- ela explica por que a issue [#1 - Migrar dependencias NLP para Poetry](https://github.com/rib-thiago/showtrials-tcc/issues/1) continua relevante

O documento vivo mais forte para essa questao hoje e [Dependencias NLP: Estado Atual e Transicao](../projeto/dependencias_nlp_estado_e_transicao.md).

## Documentos Relacionados

- [FASE 8 - Analise de Texto](FASE08_INTRODUCAO_DO_SUBSISTEMA_DE_ANALISE_DE_TEXTO.md)
- [Dependencias NLP: Estado Atual e Transicao](../projeto/dependencias_nlp_estado_e_transicao.md)
- [Guia de Dependencias do Projeto](../flows/guia_de_dependencias.md)
- [diagnostico_ci.md](../metricas/diagnostico_ci.md)
- [Guia de Contribuicao](../contributing.md)
