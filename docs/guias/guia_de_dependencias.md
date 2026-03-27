# Guia de Dependencias do Projeto

## Objetivo

Este guia organiza o gerenciamento de dependencias do projeto, com foco em `pyproject.toml`, `poetry.lock`, instalacao local e impacto no CI.

Seu objetivo e:

- usar Poetry como mecanismo principal de declaracao e instalacao
- manter rastreabilidade das mudancas de dependencias
- reduzir divergencias entre ambiente local, lock file e CI
- orientar quando uma mudanca exige consulta ao caso especial de NLP

## Contexto de Uso

Este documento deve ser usado quando houver necessidade de:

- adicionar uma dependencia nova
- remover ou atualizar dependencia existente
- revisar `pyproject.toml` ou `poetry.lock`
- entender impacto de mudancas de dependencias no CI

O projeto possui um caso especial ligado ao bloco de NLP. Esse caso nao deve ser tratado automaticamente como dependencia comum. Quando a mudanca envolver `spacy`, `numpy`, modelos ou bibliotecas correlatas, consultar o documento especifico de estado e transicao.

## Estrutura Atual de Dependencias

O estado atual do projeto gira em torno de:

- dependencias principais declaradas em `[tool.poetry.dependencies]`
- dependencias de desenvolvimento declaradas em `[tool.poetry.group.dev.dependencies]`
- lock file como referencia de reproducao

Em termos praticos:

- `pyproject.toml` declara o que o projeto precisa
- `poetry.lock` fixa a resolucao concreta
- CI e ambiente local devem depender dessa mesma base o maximo possivel

## Fluxo Basico com Poetry

Comandos uteis:

```bash
poetry add requests
poetry add --dev pytest
poetry remove requests
poetry update
poetry update requests
poetry install
poetry show
poetry show --tree
poetry show --outdated
```

Boas praticas ao alterar dependencias:

- preferir declaracao explicita no `pyproject.toml`
- revisar o impacto no `poetry.lock`
- testar import ou execucao minima da dependencia adicionada
- evitar alteracoes paralelas sem necessidade no mesmo commit

## Impacto em Lock e CI

Mudancas em dependencias normalmente exigem atencao a:

- `pyproject.toml`
- `poetry.lock`
- tarefas do projeto que dependem do ambiente configurado
- etapas do CI que assumem determinada instalacao

Se uma mudanca afetar o bloco de NLP ou qualquer workaround do CI, ela nao deve ser tratada como mudanca comum de dependencia. Nesse caso, consultar o documento especifico de estado e transicao das dependencias NLP.

## Verificacao Antes de Commitar Mudancas de Dependencias

Antes de commitar, verificar no minimo:

- `pyproject.toml` ficou coerente com a mudanca desejada
- `poetry.lock` foi atualizado quando necessario
- instalacao local continua funcionando
- a mudanca nao quebra verificacoes tecnicas minimas relevantes
- impacto no CI foi considerado

Exemplos uteis:

```bash
poetry install
poetry show --tree
poetry run python -c "import modulo"
task check
```

## Caso NLP: Consultar Documento Especifico

O bloco de NLP possui historico proprio de conflitos, workaround no CI e trilha de transicao ainda aberta.

Antes de alterar dependencias como:

- `numpy`
- `spacy`
- `textblob`
- `nltk`
- `wordcloud`
- `matplotlib`
- modelos `spacy`

consultar:

- [Dependencias NLP: Estado Atual e Transicao](../projeto/dependencias_nlp_estado_e_transicao.md)

## Pendencias e Validacoes Necessarias

- o `pyproject.toml` atual ainda possui residuos editoriais antigos e merece saneamento proprio em momento posterior
- o caso NLP nao deve ser descrito como se ja estivesse totalmente consolidado no Poetry
- mudancas no bloco de NLP devem continuar sendo avaliadas tambem frente ao CI e a issue `#1`

## Documentos Relacionados

- [Dependencias NLP: Estado Atual e Transicao](../projeto/dependencias_nlp_estado_e_transicao.md)
- [Protocolo de Qualidade do Projeto](../protocolos/protocolo_de_qualidade.md)
- [Guia de Auto-Revisao antes de PR e Merge](guia_de_auto_revisao.md)
- [Guia de Debug do Projeto](guia_de_debug.md)
- [Poetry Documentation](https://python-poetry.org/docs/)
