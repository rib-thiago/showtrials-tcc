# Documento de Requisitos — Evolução para Engine / Sistema-Alvo

## 1. Introdução

Este documento descreve os requisitos da evolução do ShowTrials para uma arquitetura de **engine ou plataforma configurável de processamento documental**, com base em:

- issues da milestone `MVP - Engine de Pipeline`
- documentos de visão e roadmap arquitetural
- direcionamento arquitetural consolidado do MVP
- contexto histórico e arquitetural já produzido em `docs/ai`

Este documento trata a engine como **estado-alvo e transição planejada**, não como capacidade já plenamente implementada.

## 2. Objetivo da evolução

A evolução arquitetural tem como objetivo transformar o ShowTrials de uma aplicação documento-cêntrica com fluxo fixo em uma plataforma configurável capaz de:

- combinar diferentes fontes
- aplicar diferentes processadores
- persistir ou exportar resultados por múltiplos destinos
- executar fluxos de trabalho distintos conforme o objetivo do usuário
- tornar a evolução mais modular, reutilizável e sustentável

## 3. Escopo da evolução

A evolução contempla, em seu estado-alvo:

- arquitetura baseada em pipeline
- configuração externa
- contexto explícito de execução
- separação entre transformação e persistência
- múltiplas entradas, múltiplos processadores e múltiplos sinks
- suporte a fluxos diversos de processamento documental

## 4. Stakeholders da evolução

- autor/desenvolvedor
- usuário configurador da engine
- pesquisador/historiador
- usuário geral que trabalha com documentos digitalizados
- mantenedor futuro
- avaliadores acadêmicos

## 5. Atores principais

### 5.1 Ator principal do sistema-alvo

- usuário configurador da engine

### 5.2 Atores secundários

- usuário pesquisador que executa fluxos já configurados
- desenvolvedor de plugins/serviços
- mantenedor da plataforma

## 6. Objetivos do sistema futuro

Os usuários da engine futura querem:

- definir pipelines de trabalho conforme a tarefa
- configurar quais ferramentas serão usadas em cada fluxo
- reutilizar componentes em diferentes processos
- processar documentos de diferentes origens
- persistir ou exportar resultados conforme a necessidade
- executar tarefas longas de forma mais robusta
- manter o sistema flexível e bem documentado

## 7. Diretrizes arquiteturais já sustentadas por issues e docs

As decisões mais fortes já identificadas são:

- uso de transformadores puros
- uso de `ContextoPipeline`
- execução baseada em pipeline linear mínima
- configuração externa via YAML/JSON
- suporte futuro a `Iterable` para streaming
- persistência deslocada para sinks
- versionamento incremental de pipelines
- migração de pelo menos um fluxo real para a nova arquitetura

## 8. Requisitos funcionais da evolução / sistema-alvo

### Grupo A — Configuração de pipeline

### RF-EN-01

O sistema deve permitir definir pipelines por configuração externa.

### RF-EN-02

O sistema deve permitir representar formalmente um pipeline como conjunto ordenado de etapas.

### RF-EN-03

O sistema deve permitir salvar e recuperar configurações de pipeline.

### RF-EN-04

O sistema deve permitir versionar pipelines de forma incremental.

### RF-EN-05

O sistema deve permitir reexecutar uma configuração de pipeline de forma determinística.

### Grupo B — Estrutura de execução

### RF-EN-06

O sistema deve possuir uma estrutura central de contexto de execução de pipeline.

### RF-EN-07

O sistema deve permitir que o contexto transporte documentos, artefatos e estado de execução.

### RF-EN-08

O sistema deve permitir execução linear mínima de pipeline no MVP.

### RF-EN-09

O sistema deve suportar evolução futura para processamento via `Iterable`.

### Grupo C — Plugins e composição

### RF-EN-10

O sistema deve permitir definir contratos para fontes, processadores e sinks.

### RF-EN-11

O sistema deve permitir combinar diferentes tipos de fonte em fluxos distintos.

### RF-EN-12

O sistema deve permitir combinar diferentes processadores em fluxos distintos.

### RF-EN-13

O sistema deve permitir combinar diferentes destinos/sinks em fluxos distintos.

### RF-EN-14

O sistema deve permitir carregar apenas os serviços necessários para uma execução.

### Grupo D — Fontes documentais e entradas

### RF-EN-15

O sistema deve suportar aquisição de conteúdo a partir de páginas web.

### RF-EN-16

O sistema deve suportar processamento de PDFs.

### RF-EN-17

O sistema deve suportar OCR sobre imagens ou documentos digitalizados.

### RF-EN-18

O sistema deve permitir evolução futura para conectores adicionais, como APIs e pastas locais.

### Grupo E — Processamento documental

### RF-EN-19

O sistema deve permitir aplicar tradução como etapa configurável do pipeline.

### RF-EN-20

O sistema deve permitir aplicar processamento NLP como etapa configurável do pipeline.

### RF-EN-21

O sistema deve permitir aplicar classificação documental como etapa configurável do pipeline.

### RF-EN-22

O sistema deve permitir aplicar extração de entidades como etapa configurável do pipeline.

### RF-EN-23

O sistema deve permitir aplicar análises estatísticas como etapa configurável do pipeline.

### RF-EN-24

O sistema deve permitir evolução futura para revisão de tradução, sumarização e enriquecimento adicional.

### Grupo F — Persistência e saída

### RF-EN-25

O sistema deve permitir persistência opcional dos documentos processados.

### RF-EN-26

O sistema deve permitir persistência de produtos derivados de processamento.

### RF-EN-27

O sistema deve permitir múltiplos destinos de saída, incluindo banco de dados e artefatos exportáveis.

### RF-EN-28

A responsabilidade de persistência deve estar concentrada em sinks, e não nos transformadores.

### Grupo G — Operação do sistema

### RF-EN-29

O sistema deve continuar oferecendo acesso por CLI.

### RF-EN-30

O sistema deve continuar oferecendo acesso por Web.

### RF-EN-31

O sistema deve permitir diferentes distribuições do produto, como versão Web-only e versão completa.

### RF-EN-32

O sistema deve suportar evolução futura para execução em segundo plano e filas.

## 9. Requisitos de transição

### RT-01

A evolução deve ocorrer de forma incremental, sem reescrita total do projeto.

### RT-02

A base atual do ShowTrials deve servir como origem de migração para a nova arquitetura.

### RT-03

Pelo menos um fluxo real já existente deve ser migrado para a execução via `ContextoPipeline`.

### RT-04

A CLI e a Web devem ser preservadas como interfaces relevantes durante a transição.

### RT-05

A separação entre transformação e persistência deve ser introduzida sem apagar de imediato os casos de uso atuais.

### RT-06

Os casos de uso atuais devem poder atuar como adaptadores durante a transição.

## 10. Requisitos não funcionais da evolução

### RNF-EN-01

A arquitetura futura deve favorecer modularidade.

### RNF-EN-02

A arquitetura futura deve favorecer extensibilidade.

### RNF-EN-03

A arquitetura futura deve favorecer reuso de componentes.

### RNF-EN-04

O sistema deve continuar em Python.

### RNF-EN-05

O sistema deve minimizar carregamento desnecessário de serviços pesados.

### RNF-EN-06

O sistema deve oferecer ergonomia na configuração e execução dos fluxos.

### RNF-EN-07

O sistema deve ser bem documentado para desenvolvimento, manutenção e uso acadêmico.

### RNF-EN-08

O sistema deve ser compatível com evolução progressiva da arquitetura atual.

### RNF-EN-09

O sistema deve favorecer manutenção e testabilidade dos componentes.

### RNF-EN-10

A configuração dos pipelines deve ser clara, explícita e reprodutível.

## 11. Restrições da evolução

- não reescrever o sistema do zero
- preservar continuidade com ShowTrials
- manter CLI e Web como interfaces relevantes
- iniciar pelo MVP estrutural, não por recursos avançados
- evitar discovery complexo, execução distribuída ou paralela no MVP inicial
- manter versionamento simples de pipeline no começo
- preservar governança e rastreabilidade

## 12. Fora de escopo do MVP estrutural da engine

Com base no direcionamento já existente, ficam fora do MVP inicial:

- execução distribuída
- engine assíncrona completa
- paralelismo avançado
- discovery automático complexo
- versionamento estilo Git
- todos os plugins avançados desde o início
- fechamento definitivo da camada comercial/produto

## 13. Síntese

A evolução para engine já possui um núcleo claro de requisitos arquiteturais: pipeline configurável, contexto explícito, plugins mínimos de source/processor/sink, separação entre transformação e persistência, configuração externa e migração incremental de fluxos reais. O desafio agora não é descobrir se há direção, mas transformar essa direção em requisitos mais granulares, casos de uso e arquitetura formal.
