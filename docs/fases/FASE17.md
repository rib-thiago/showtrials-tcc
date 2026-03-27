# Historico da Fase 17 - Primeira Reorganizacao Documental Ampla

## Natureza do Documento

Este documento registra historicamente a primeira grande reorganizacao documental do projeto.

Ele nao deve ser lido como fonte normativa principal do regime documental atual. Hoje, a leitura vigente sobre documentacao, fases e rodadas deve ser feita principalmente em:

- [Guia de Documentacao do Projeto](../flows/guia_de_documentacao_do_projeto.md)
- [Guia de Manutencao do Site Documental](../flows/guia_de_manutencao_do_site_documental.md)
- [Regime Documental de Fases e Rodadas](../projeto/regime_documental_de_fases_e_rodadas.md)

## Objetivo da Intervencao

Consolidar e reorganizar a documentacao do projeto em um momento em que o conjunto de arquivos havia crescido de forma organica e apresentava problemas de estrutura, links e navegacao.

## Contexto

Depois das primeiras fases de implementacao e do crescimento do bloco documental, o projeto passou a conviver com:

- muitos arquivos Markdown dispersos na raiz de `docs/`
- links internos quebrados ou fragilizados
- mistura entre historicos de fase, diagnosticos e documentos gerais
- navegacao desatualizada no site documental

Essa fase representou a primeira grande tentativa de tratar documentacao como frente propria de organizacao e manutencao.

## Problemas Enfrentados

Como historico, a fase registra principalmente estes problemas:

- desorganizacao fisica da arvore documental
- documentos com dupla finalidade
- links internos quebrados
- navegacao desatualizada
- ausencia de padrao minimo para novas fases

## Intervencoes Aplicadas

A intervencao historica consolidou, entre outros movimentos:

- reorganizacao fisica inicial de arquivos em subpastas como `docs/fases/` e `docs/metricas/`
- separacao entre diagnosticos e historicos de implementacao em alguns casos
- correcao de links internos
- primeira tentativa de consolidar melhor a navegacao documental
- criacao de template e script de verificacao para fases

Esses movimentos tiveram peso proprio porque ajudaram a transformar a documentacao em um bloco mais legivel e mais governavel naquele momento do projeto.

## Artefatos Afetados

Com base no lastro historico identificado, esta fase se relaciona fortemente com:

- `docs/fases/FASE17.md`
- `mkdocs.yml`
- `docs/planejamento/plano_issue2_revisao_documentacao.md`
- `docs/index.md`
- `docs/metricas/cobertura.md`

O historico da branch tambem mostra relacao ampla com a reorganizacao de `docs/flows/` e `docs/projeto/` naquela etapa inicial.

## Rastreabilidade Git e GitHub

### Commit principal

- [`d6b7cb6`](https://github.com/rib-thiago/showtrials-tcc/commit/d6b7cb62fb7dd5bd65422cc75f8ba39c5c0a3aa0) - `docs: adiciona documentação da FASE 17 - Revisão da Issue #2`

### Branch principal

- `docs/organizacao-final`

### Issue principal

- [#2 - Revisar documentação (.md files)](https://github.com/rib-thiago/showtrials-tcc/issues/2)

### Issue relacionada

- [#9 - Criar páginas índice para as pastas de documentação](https://github.com/rib-thiago/showtrials-tcc/issues/9)

### Pull Request

- nenhum pull request foi identificado com seguranca para a branch `docs/organizacao-final`

## Impacto Historico

Como historico, esta fase marca:

- a primeira reorganizacao documental ampla de todo o projeto
- a formalizacao inicial de uma preocupacao com estrutura, navegacao e padronizacao
- a abertura de caminho para frentes posteriores mais maduras de modelagem e saneamento documental

Mesmo quando varias decisoes daquela epoca foram depois revistas ou refinadas, esta fase continua importante como marco de transicao entre documentacao organica e documentacao mais conscientemente organizada.

## Limites de Leitura no Estado Atual

Esta fase nao deve ser lida hoje como:

- definicao final da navegacao do site
- politica vigente de documentacao
- regime atual de relacao entre fases e rodadas
- fotografia fiel do estado atual de `mkdocs.yml`

Ela deve ser lida como historico de uma reorganizacao importante, cuja interpretacao atual precisa ser complementada por:

- [Guia de Documentacao do Projeto](../flows/guia_de_documentacao_do_projeto.md)
- [Guia de Manutencao do Site Documental](../flows/guia_de_manutencao_do_site_documental.md)
- [Regime Documental de Fases e Rodadas](../projeto/regime_documental_de_fases_e_rodadas.md)
- [plano_issues_documentacao.md](../projeto/plano_issues_documentacao.md), hoje reclassificado como plano historico

## Documentos Relacionados

- [plano_issue2_revisao_documentacao.md](../planejamento/plano_issue2_revisao_documentacao.md)
- [plano_issues_documentacao.md](../projeto/plano_issues_documentacao.md)
- [Guia de Documentacao do Projeto](../flows/guia_de_documentacao_do_projeto.md)
- [Guia de Manutencao do Site Documental](../flows/guia_de_manutencao_do_site_documental.md)
- [Regime Documental de Fases e Rodadas](../projeto/regime_documental_de_fases_e_rodadas.md)
