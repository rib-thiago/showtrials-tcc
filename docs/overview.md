# Visao Geral do Projeto

## Objetivo

ShowTrials apoia pesquisa historica documental por meio de coleta, armazenamento, traducao, analise textual e visualizacao de documentos do acervo ShowTrials.

## O que o sistema faz hoje

O sistema atual oferece:

- coleta e persistencia de documentos historicos
- classificacao por tipo e organizacao de metadados
- traducao com integracao ao Google Cloud Translation
- analise textual, incluindo entidades, sentimentos e wordclouds
- interface CLI e interface web
- exportacao e geracao de relatorios

## Estrutura em alto nivel

O nucleo atual do projeto segue uma separacao em camadas:

```text
Interface -> Application -> Domain -> Infrastructure
```

Essa estrutura sustenta o sistema funcional atual e tambem serve como base para a evolucao arquitetural documentada no bloco `docs/projeto/`.

## Estado atual e evolucao

O projeto nao deve ser lido apenas como aplicacao pronta e fechada. Hoje ele combina:

- um sistema funcional documentado e validado por testes
- uma frente arquitetural voltada a evolucao para uma engine mais configuravel
- uma trilha historica consistente entre fases, rodadas, changelog e modelagem

Para a leitura mais forte do horizonte tecnico atual, consulte:

- [Direcionamento Arquitetural do MVP da Engine](projeto/direcionamento_arquitetural_engine_mvp.md)
- [Visao Ampla do Projeto](projeto/visao_do_projeto.md)
- [Roadmap Arquitetural Amplo](projeto/roadmap_arquitetural.md)

## Principais conjuntos documentais

### Entrada publica

- [Repositorio no GitHub](https://github.com/rib-thiago/showtrials-tcc)
- [Pagina inicial da documentacao](index.md)
- [Changelog](changelog.md)

### Contribuicao e operacao

- [Guia de Contribuicao](contributing.md)
- [Guia de Documentacao do Projeto](guias/guia_de_documentacao_do_projeto.md)
- [Guia de Atualizacao do Changelog](guias/guia_de_atualizacao_do_changelog.md)

### Projeto e arquitetura

- [Visao Ampla do Projeto](projeto/visao_do_projeto.md)
- [Indice geral da frente de modelagem](modelagem/revisao/47_indice_geral_da_frente_de_modelagem.md)

### Historico

- [Changelog](changelog.md)
- [Plano operacional da reorganizacao semantica](planejamento/plano_operacional_da_reorganizacao_semantica_dos_diretorios.md)

## Como contribuir e acompanhar a evolucao

Para contribuir:

- comece por [Guia de Contribuicao](contributing.md)
- consulte o [repositorio no GitHub](https://github.com/rib-thiago/showtrials-tcc) para instalacao e comandos atuais
- acompanhe mudancas publicas relevantes no [Changelog](changelog.md)
