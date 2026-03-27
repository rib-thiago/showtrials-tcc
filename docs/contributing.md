# Guia de Contribuicao

## Objetivo

Este guia resume o fluxo atual de contribuicao do projeto e aponta para os documentos especializados quando o detalhe pertence a outro artefato.

## Preparacao do ambiente

### Clone e instalacao

```bash
git clone https://github.com/rib-thiago/showtrials-tcc.git
cd showtrials-tcc
poetry install
cp .env.example .env
```

### Hooks

```bash
pre-commit install
pre-commit install --hook-type pre-push
```

### Observacao importante sobre NLP

O projeto ainda usa um arranjo hibrido para parte das dependencias de NLP. Para executar analise de texto, gerar wordclouds ou rodar a suite completa com o mesmo lastro do CI, consulte antes [Dependencias NLP: Estado Atual e Transicao](projeto/dependencias_nlp_estado_e_transicao.md).

## Fluxo basico de contribuicao

1. abra ou escolha a issue que vai orientar a mudanca
2. crie a branch seguindo o regime atual do projeto
3. implemente a mudanca com commits pequenos e rastreaveis
4. rode as verificacoes aplicaveis
5. faca a auto-revisao antes de abrir PR

Para as regras de governanca e Git, consulte:

- [Politica de Governanca](flows/politica_de_governanca.md)
- [Protocolo de Git](flows/protocolo_de_git.md)
- [Guia de Auto-Revisao](flows/guia_de_auto_revisao.md)

## Comandos atuais do projeto

```bash
poetry run task lint
poetry run task type
poetry run task test
poetry run task test-cov
poetry run task run-cli
poetry run task run-web
poetry run task docs
poetry run task pre-push
```

## Testes

### Suite completa

```bash
poetry run task test
poetry run task test-cov
```

Resultado validado localmente em `2026-03-27`:

- `235` testes passando
- cobertura total de `75.51%`

### Nota operacional sobre a coleta

Quando o ambiente NLP esta corretamente preparado, a suite completa roda normalmente. Mesmo assim, a fase inicial de `collecting` pode parecer lenta por causa de imports pesados de modulos como `matplotlib`, `spacy` e integracoes de traducao. Essa lentidao inicial nao indica, por si so, travamento.

## Qualidade e revisao

Antes de abrir um PR, use como referencia:

- [Protocolo de Qualidade](flows/protocolo_de_qualidade.md)
- [Guia de Auto-Revisao](flows/guia_de_auto_revisao.md)
- [Guia de Debug](flows/guia_de_debug.md), se a mudanca exigir investigacao adicional

## Documentacao

Para alteracoes documentais:

- [Guia de Documentacao do Projeto](flows/guia_de_documentacao_do_projeto.md)
- [Guia de Atualizacao do Changelog](flows/guia_de_atualizacao_do_changelog.md)
- [Regime Documental de Fases e Rodadas](projeto/regime_documental_de_fases_e_rodadas.md)

## Commits

O projeto segue Conventional Commits. Tipos comuns:

- `feat`
- `fix`
- `docs`
- `refactor`
- `test`
- `chore`

## Documentos relacionados

- [Politica de Governanca](flows/politica_de_governanca.md)
- [Protocolo de Git](flows/protocolo_de_git.md)
- [Protocolo de Qualidade](flows/protocolo_de_qualidade.md)
- [Dependencias NLP: Estado Atual e Transicao](projeto/dependencias_nlp_estado_e_transicao.md)
