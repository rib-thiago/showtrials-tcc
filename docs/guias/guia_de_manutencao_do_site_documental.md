# Guia de Manutencao do Site Documental

## Objetivo

Este guia organiza a manutencao do site documental do projeto baseado em MkDocs.

Seu objetivo e:

- orientar verificacao local, build e publicacao
- reduzir quebra de navegacao e links
- separar manutencao do site documental da manutencao documental geral

## Contexto de Uso

Este guia deve ser consultado quando houver:

- alteracao de navegacao ou paginas publicas
- necessidade de revisar build local da documentacao
- preparacao de publicacao do site documental
- conferencia de links ou estrutura do MkDocs

## Papel do MkDocs no Projeto

O MkDocs e a camada de navegacao publica da documentacao.

Ele nao substitui a classificacao semantica dos documentos nem define, por si so, o estatuto de cada artefato. Sua funcao aqui e:

- organizar leitura publica
- expor paginas relevantes
- manter navegacao previsivel

## Verificacao Local do Site

Comandos uteis:

```bash
task docs
poetry run mkdocs serve
poetry run mkdocs build
```

Antes de considerar a manutencao do site adequada, vale verificar:

- se o site sobe localmente
- se a navegacao principal funciona
- se links internos importantes continuam validos
- se a build nao quebra

## Navegacao e Links

Mudancas de nome, caminho ou papel de documentos costumam exigir revisao da navegacao publica.

Boas praticas minimas:

- revisar links relativos apos renames
- evitar manter no nav nomes fisicos ultrapassados
- confirmar se documentos publicos ainda correspondem ao estatuto semantico atual

## Build e Publicacao

Comandos usuais:

```bash
poetry run mkdocs build
poetry run mkdocs gh-deploy
```

Publicacao nao deve ocorrer sem:

- build local funcional
- revisao minima da navegacao
- confianca razoavel de que o conjunto publico nao ficou incoerente

## Limites desta Frente

Nesta frente de saneamento documental, a manutencao do site deve ser tratada com cautela.

Isso significa:

- separar saneamento semantico de implementacao de navegacao
- evitar grandes alteracoes em `mkdocs.yml` no mesmo passo em que o estatuto documental ainda esta sendo consolidado
- deixar ajustes estruturais mais amplos de navegacao para etapa posterior, quando o bloco saneado estiver estabilizado

## Documentos Relacionados

- [Guia de Documentacao do Projeto](guia_de_documentacao_do_projeto.md)
- [Regime Documental de Fases e Rodadas](../projeto/regime_documental_de_fases_e_rodadas.md)
- [Guia de Contribuicao](../contributing.md)
