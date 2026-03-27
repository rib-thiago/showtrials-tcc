# ShowTrials

<div align="center">

![Python](https://img.shields.io/badge/python-3.12-blue)
![CI](https://github.com/rib-thiago/showtrials-tcc/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/badge/license-MIT-green)
![Coverage](https://img.shields.io/badge/coverage-75.51%25-yellowgreen)
![Code style](https://img.shields.io/badge/code%20style-black-000000.svg)
![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)
![FastAPI](https://img.shields.io/badge/FastAPI-0.129.0-009688)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57)

Sistema para coleta, armazenamento, traducao e analise de documentos historicos do acervo ShowTrials.

[Documentacao](docs/index.md) | [Changelog](docs/changelog.md) | [Contribuicao](docs/contributing.md)

</div>

## O que o projeto faz hoje

- coleta e persiste documentos historicos em SQLite
- classifica documentos por tipo e organiza metadados do acervo
- traduz documentos com integracao ao Google Cloud Translation
- executa analise textual, incluindo entidades, sentimentos e nuvens de palavras
- oferece interface CLI e interface web baseada em FastAPI
- gera exportacoes e relatorios do acervo

## Estado atual do projeto

O repositorio combina um sistema funcional ja implementado com uma frente arquitetural de evolucao para uma engine mais configuravel. A leitura publica mais segura hoje e:

- sistema atual e fluxo tecnico: este `README`, [overview](docs/overview.md) e [changelog](docs/changelog.md)
- documentacao geral: [index](docs/index.md)
- direcionamento arquitetural imediato: [Direcionamento Arquitetural do MVP da Engine](docs/projeto/direcionamento_arquitetural_engine_mvp.md)
- visao ampla e roadmap: [Visao Ampla do Projeto](docs/projeto/visao_do_projeto.md) e [Roadmap Arquitetural Amplo](docs/projeto/roadmap_arquitetural.md)

## Arquitetura em alto nivel

O sistema atual segue uma separacao em camadas, enquanto a documentacao arquitetural mais recente prepara a transicao para uma engine mais extensivel.

```text
Interface -> Application -> Domain -> Infrastructure

CLI/Web/API -> Casos de uso -> Entidades e interfaces -> SQLite, traducao, NLP
```

## Como comecar

### Pre-requisitos

- Python 3.12+
- Poetry
- Git

### Instalacao basica

```bash
git clone https://github.com/rib-thiago/showtrials-tcc.git
cd showtrials-tcc
poetry install
cp .env.example .env
```

Se voce pretende usar analise de texto, gerar wordclouds ou executar a suite completa de testes, consulte primeiro [Dependencias NLP: Estado Atual e Transicao](docs/projeto/dependencias_nlp_estado_e_transicao.md), porque o bloco NLP ainda exige um workaround complementar ao `poetry install`.

### Execucao

```bash
poetry run task run-cli
poetry run task run-web
poetry run task docs
```

- `task run-cli`: inicia a interface de linha de comando
- `task run-web`: inicia a interface web
- `task docs`: sobe a documentacao local com MkDocs

## Testes e qualidade

Comandos atuais do projeto:

```bash
poetry run task lint
poetry run task type
poetry run task test
poetry run task test-cov
poetry run task pre-push
```

Suite validada localmente em `2026-03-27` com:

- `235` testes passando
- cobertura total de `75.51%`

Se a execucao envolver modulos de NLP, a coleta inicial dos testes pode demorar perceptivelmente por imports pesados. Consulte [docs/contributing.md](docs/contributing.md) para o fluxo recomendado.

## Estrutura principal

```text
src/
  application/
  domain/
  infrastructure/
  interface/
  tests/
docs/
  fases/
  politicas/
  protocolos/
  guias/
  modelagem/
  planejamento/
  projeto/
data/
scripts/
run.py
web_run.py
pyproject.toml
```

## Documentacao

- [Pagina inicial da documentacao](docs/index.md)
- [Visao geral](docs/overview.md)
- [Guia de contribuicao](docs/contributing.md)
- [Changelog](docs/changelog.md)
- [Guia de documentacao do projeto](docs/guias/guia_de_documentacao_do_projeto.md)
- [Guia de atualizacao do changelog](docs/guias/guia_de_atualizacao_do_changelog.md)

## Historico e rastreabilidade

O historico detalhado do projeto fica distribuido entre:

- [Changelog](docs/changelog.md), para marcos publicos resumidos
- [docs/fases](docs/fases), para historicos consolidados de intervencoes
- [docs/planejamento/rodadas](docs/planejamento/rodadas), para execucao curta e rastreavel

## Licenca

Projeto sob licenca MIT.
