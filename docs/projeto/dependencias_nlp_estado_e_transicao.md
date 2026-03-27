# Dependencias NLP: Estado Atual e Transicao

## Objetivo

Este documento consolida o estado atual das dependencias NLP do projeto, o historico do workaround adotado e a transicao ainda aberta para gerenciamento mais completo via Poetry.

## Contexto Historico

O problema surgiu na implementacao da analise de texto, registrada em [FASE 8 - Analise de Texto](../fases/FASE8_ANALISE_TEXTO.md).

Naquela fase, o projeto encontrou conflitos praticos ligados a:

- versao de Python
- `numpy`
- `spacy` e dependencias correlatas
- modelos de idioma
- bibliotecas auxiliares como `textblob`, `nltk`, `wordcloud` e `matplotlib`

A solucao adotada na epoca foi instalar esse bloco via `pip` dentro do ambiente do Poetry, como workaround operacional.

## Estado Atual

Hoje o projeto convive com uma situacao hibrida:

- o nucleo principal do ambiente e gerenciado por Poetry
- o bloco de NLP ainda tem historico de instalacao e estabilizacao fora do fluxo puramente declarativo
- a documentacao historica e o CI registram esse arranjo como solucao provisoria

Esse estado nao deve ser lido como politica definitiva. Ele representa um estado de transicao ainda aberto.

## Workaround Vigente no CI

A fase [FASE 11 - CI: Estabilizacao do Pipeline de Integracao Continua](../fases/FASE11_CI.md) documenta a solucao que destravou o pipeline:

- `poetry install` para o ambiente principal
- complemento com instalacao das dependencias NLP
- download dos modelos `spacy`

Esse workaround foi importante para restaurar reproducibilidade pratica do CI, mas tambem cristalizou uma divida tecnica de dependencia hibrida.

## Execucao Local de Testes e NLP

Na pratica, o mesmo arranjo do CI ainda precisa ser considerado quando se quer:

- executar a suite completa de testes
- usar analise de texto em ambiente local
- gerar wordclouds e outros artefatos dependentes do bloco NLP

Sem esse complemento, o ambiente gerado apenas por `poetry install` pode nao reproduzir integralmente o comportamento esperado para NLP e testes.

Tambem e importante notar que, mesmo com o workaround aplicado, a fase inicial de coleta da suite pode parecer lenta por causa de imports pesados de modulos como `spacy`, `matplotlib`, `wordcloud` e integracoes de traducao. Essa lentidao inicial nao deve ser confundida automaticamente com travamento.

## Limites e Riscos do Estado Atual

Os principais limites do estado atual sao:

- divergencia potencial entre ambiente local e CI
- dependencia de passos adicionais fora do fluxo declarativo principal
- manutencao mais fragil de versoes e modelos
- maior custo para evoluir ou substituir bibliotecas NLP

Esse conjunto explica por que o caso NLP nao deve ser tratado como mudanca comum de dependencia.

## Transicao Esperada

A trilha formal para superar esse estado esta registrada na issue aberta [#1 - Migrar dependencias NLP para Poetry](https://github.com/rib-thiago/showtrials-tcc/issues/1).

A transicao esperada inclui:

- declarar o bloco NLP em `pyproject.toml` de forma compativel com Python 3.12
- reduzir ou eliminar `pip install` manual no CI
- tornar o ambiente mais reproduzivel a partir de `poetry install`
- tratar os modelos `spacy` de forma previsivel e documentada

Enquanto essa issue permanecer aberta, qualquer mudanca nesse bloco deve ser tratada com validacao mais cuidadosa.

## Referencias e Rastreabilidade

- [FASE 8 - Analise de Texto](../fases/FASE8_ANALISE_TEXTO.md)
- [FASE 11 - CI: Estabilizacao do Pipeline de Integracao Continua](../fases/FASE11_CI.md)
- [Guia de Contribuicao](../contributing.md)
- [Guia de Dependencias do Projeto](../flows/guia_de_dependencias.md)
- [Issue #1 - Migrar dependencias NLP para Poetry](https://github.com/rib-thiago/showtrials-tcc/issues/1)
- `pyproject.toml`
- `.github/workflows/ci.yml`
