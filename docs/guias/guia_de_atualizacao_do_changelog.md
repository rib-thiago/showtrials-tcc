# Guia de Atualizacao do Changelog

## Objetivo

Este guia define como manter [changelog.md](../changelog.md) como artefato publico, resumido e fiel aos marcos reais do projeto.

## Papel do Changelog no Projeto

O changelog registra mudancas notaveis em nivel publico e de consulta rapida.

Ele nao substitui:

- o historico fino de commits no Git;
- os documentos de fase em `docs/historico/fases/`;
- os documentos de rodada em `docs/planejamento/rodadas/`.

Seu papel e destacar marcos suficientemente relevantes para ajudar leitura retrospectiva do projeto sem exigir reconstituicao completa do historico.

## O Que Deve Entrar

Entram no changelog:

- marcos arquiteturais relevantes;
- blocos importantes de funcionalidades consolidadas;
- endurecimento relevante de qualidade, CI ou governanca;
- reorganizacoes documentais ou estruturais com impacto amplo;
- consolidacoes de frentes inteiras, quando elas alteram significativamente a leitura publica do projeto.

## O Que Nao Deve Entrar

Nao entram no changelog:

- dump de commits;
- cada rodada individual;
- correcoes triviais ou locais sem impacto amplo;
- detalhes tecnicos que ja ficam melhor descritos em `FASE*`, `RODADA_*` ou guias especializados;
- releases formais inventadas sem lastro real em tags, versoes ou politica consolidada de release.

## Fontes de Evidencia

Ao atualizar o changelog, consultar preferencialmente:

- historico Git;
- `docs/historico/fases/`;
- `docs/planejamento/rodadas/`;
- documentos vivos relevantes em `docs/guias/`, `docs/projeto/` e `docs/modelagem/`.

Quando houver conflito factual, prevalecem Git, codigo e documentos saneados mais recentes.

## Como Escrever uma Entrada

Cada entrada do changelog deve:

- usar data ou intervalo de datas claramente identificado;
- representar um marco historico reconhecivel;
- trazer poucas categorias de alto valor, como `Arquitetura`, `Funcionalidades`, `Qualidade`, `Documentacao`, `Operacao` ou `Correcao`;
- resumir o suficiente para leitura publica, sem virar duplicata de fase ou rodada;
- incluir, quando util, uma pequena secao de `Rastreabilidade`.

## Quando Atualizar

O changelog deve ser atualizado:

- ao final de um marco claramente consolidado;
- ao final de uma frente relevante;
- quando houver mudanca publica importante perceptivel no projeto.

Ele nao precisa ser atualizado a cada commit nem a cada rodada.

## Relacao com Fases, Rodadas e Git

Regra pratica:

- `Git` preserva granularidade fina;
- `RODADA_*` preserva execucao curta e memoria operacional;
- `FASE*` preserva historicos consolidados de intervencoes relevantes;
- `changelog.md` preserva leitura publica resumida dos marcos notaveis.

O changelog deve apontar para essas camadas quando a rastreabilidade fina for importante, mas sem tentar absorve-las.

## Documentos Relacionados

- [Changelog](../changelog.md)
- [Guia de Documentacao do Projeto](../guias/guia_de_documentacao_do_projeto.md)
- [Regime Documental de Fases e Rodadas](../projeto/regime_documental_de_fases_e_rodadas.md)
- [Versionamento e Releases](../projeto/versionamento_e_releases.md)
