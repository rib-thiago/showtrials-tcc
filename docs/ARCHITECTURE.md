# Arquitetura do Sistema Atual

## Objetivo

Este documento apresenta a arquitetura em alto nivel do sistema atual do ShowTrials.

Seu papel aqui e:

- explicar a organizacao principal do codigo ja implementado
- dar uma leitura publica e introdutoria da separacao em camadas
- servir de ponte para os documentos arquiteturais mais fortes do bloco `docs/projeto/`

Ele nao deve ser lido como o direcionamento arquitetural mais forte da evolucao futura da engine.

## Visao Geral

O sistema atual foi estruturado com separacao entre interface, aplicacao, dominio e infraestrutura.

Essa organizacao sustenta:

- casos de uso documentais
- persistencia em SQLite
- traducao e analise textual
- interface CLI e interface web

## Camadas Principais

```text
INTERFACE -> APPLICATION -> DOMAIN -> INFRASTRUCTURE
```

```text
┌─────────────────────────────────────────────────────────────┐
│                    INTERFACE LAYER                         │
│  CLI, Web e adaptadores para interacao externa            │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   APPLICATION LAYER                        │
│  Casos de uso, orquestracao e DTOs                        │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      DOMAIN LAYER                          │
│  Entidades, value objects e interfaces                    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                  INFRASTRUCTURE LAYER                      │
│  Repositorios, servicos externos e configuracao           │
└─────────────────────────────────────────────────────────────┘
```

### Domain

Em `src/domain/`, ficam:

- entidades como `Documento` e `Traducao`
- value objects como `TipoDocumento`, `NomeRusso` e `AnaliseTexto`
- contratos que desacoplam o nucleo de implementacoes concretas

### Application

Em `src/application/`, ficam:

- casos de uso
- DTOs
- orquestracao do fluxo entre repositorios, servicos e regras do sistema

### Interface

Em `src/interface/`, ficam:

- CLI
- Web
- adaptadores de entrada e saida

### Infrastructure

Em `src/infrastructure/`, ficam:

- repositorios SQLite
- integracao com traducao
- componentes de NLP
- configuracao e `ServiceRegistry`

## Fluxo Geral de Dados

```text
Usuario -> Interface -> Caso de Uso -> Interface de Repositorio
                                     -> Servico/Infraestrutura
```

Leitura resumida do sistema atual:

```text
Banco -> Documento -> Mutacao -> Banco
```

Essa leitura ajuda a entender por que o sistema atual e documento-centrico e orientado a persistencia, mesmo antes da transicao para a engine de pipeline.

## Service Registry e Dependencias

O sistema utiliza `ServiceRegistry` para organizar servicos e reduzir acoplamento direto entre pontos de entrada e componentes concretos.

Leitura sintetica:

```text
Configuracao -> Factories -> ServiceRegistry -> Casos de Uso e Interfaces
```

Esse arranjo ajuda no crescimento incremental do sistema atual, embora nao deva ser confundido com a futura arquitetura da engine.

## Estado Atual e Evolucao

Este documento descreve a arquitetura do sistema atual.

Para a evolucao futura, a leitura mais forte hoje deve ser feita em:

- [Direcionamento Arquitetural do MVP da Engine](projeto/direcionamento_arquitetural_engine_mvp.md)
- [Analise Arquitetural da Transicao para a Engine](projeto/analise_arquitetural.md)
- [Visao Ampla do Projeto](projeto/visao_do_projeto.md)
- [Conferencia de Aderencia ao Projeto Real](modelagem/revisao/49_conferencia_de_aderencia_ao_projeto_real.md)

Esses documentos distinguem com mais rigor:

- o que ja existe no sistema atual
- o que e direcionamento arquitetural vivo
- o que permanece como horizonte amplo ou hipotese de transicao

## Documentos Relacionados

- [Visao Geral](overview.md)
- [README do repositorio](/home/thiago/coleta_showtrials/README.md)
- [Direcionamento Arquitetural do MVP da Engine](projeto/direcionamento_arquitetural_engine_mvp.md)
- [Analise Arquitetural da Transicao para a Engine](projeto/analise_arquitetural.md)
- [Visao Ampla do Projeto](projeto/visao_do_projeto.md)
