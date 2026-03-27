# Documento de Requisitos — ShowTrials Atual

## 1. Introdução

Este documento descreve os requisitos do sistema historicamente conhecido como **ShowTrials**, entendido aqui como a aplicação documental já implementada e consolidada ao longo das fases iniciais do projeto.

Ele se baseia principalmente em:

- fases do projeto, especialmente FASE 1, 4, 5, 8, 9 e 10
- código central já inspecionado
- histórico Git consolidado
- documentos de contexto e arquitetura já produzidos

## 2. Objetivo do sistema

O ShowTrials atual tem como objetivo apoiar o trabalho de leitura, coleta, organização, tradução, consulta e análise de documentos digitalizados, especialmente no contexto de documentos históricos em russo, reduzindo trabalho manual e concentrando essas operações em uma aplicação unificada.

## 3. Escopo do sistema

O sistema atual compreende:

- coleta e ingestão de conteúdo documental
- persistência de documentos em banco de dados
- classificação e enriquecimento básico
- tradução persistida
- análise textual e estatística
- acesso por CLI
- acesso por interface Web

## 4. Stakeholders

- autor/desenvolvedor
- usuário pesquisador/historiador
- usuário interessado em documentos digitalizados
- mantenedor futuro
- banca/professor como stakeholder acadêmico indireto

## 5. Atores principais

### 5.1 Ator principal

- usuário pesquisador/historiador

### 5.2 Atores secundários

- desenvolvedor/administrador do sistema
- mantenedor técnico

## 6. Objetivos dos usuários

Os usuários do sistema atual querem:

- coletar conteúdos de fontes digitais
- armazenar documentos para uso posterior
- consultar documentos e metadados
- traduzir documentos
- consultar traduções persistidas
- analisar texto e extrair estatísticas
- visualizar resultados em CLI ou Web

## 7. Capacidades centrais observadas

Com base nas fases e no código, o ShowTrials atual oferece ou busca oferecer:

- coleta de conteúdo de fonte web específica
- persistência documental em SQLite
- classificação tipológica de documentos
- extração e representação de metadados
- tradução para múltiplos idiomas com persistência
- consulta ao acervo documental
- análise textual com NLP
- visualização terminal rica via CLI
- interface Web com FastAPI
- uso parcial de `ServiceRegistry` e lazy loading

## 8. Requisitos funcionais do ShowTrials atual

### RF-ST-01

O sistema deve permitir armazenar documentos históricos digitais com seus conteúdos textuais e metadados principais.

### RF-ST-02

O sistema deve permitir representar documentos por meio de uma entidade documental com identidade, origem, texto e metadados associados.

### RF-ST-03

O sistema deve permitir classificar documentos em tipos documentais reconhecidos pelo sistema.

### RF-ST-04

O sistema deve permitir consultar documentos por listagem e por identificador.

### RF-ST-05

O sistema deve permitir persistir traduções associadas a documentos.

### RF-ST-06

O sistema deve permitir traduzir documentos para idiomas suportados.

### RF-ST-07

O sistema deve permitir listar traduções existentes de um documento.

### RF-ST-08

O sistema deve permitir alternar entre conteúdo original e conteúdo traduzido nas interfaces disponíveis.

### RF-ST-09

O sistema deve permitir aplicar análises textuais individuais a documentos.

### RF-ST-10

O sistema deve permitir realizar análise global do acervo.

### RF-ST-11

O sistema deve permitir extrair entidades nomeadas de textos.

### RF-ST-12

O sistema deve permitir calcular estatísticas textuais básicas.

### RF-ST-13

O sistema deve permitir gerar artefatos analíticos como visualizações e wordcloud quando o recurso estiver disponível.

### RF-ST-14

O sistema deve permitir acesso por CLI com navegação orientada por menus e exibição rica.

### RF-ST-15

O sistema deve permitir acesso por interface Web para as funcionalidades principais.

### RF-ST-16

O sistema deve disponibilizar rota ou mecanismo de status operacional dos serviços da aplicação Web.

## 9. Requisitos não funcionais do ShowTrials atual

### RNF-ST-01

O sistema deve manter separação arquitetural em camadas entre domínio, aplicação, infraestrutura e interface.

### RNF-ST-02

O núcleo de domínio deve permanecer sem dependências externas diretas.

### RNF-ST-03

O sistema deve usar Python como linguagem principal.

### RNF-ST-04

O sistema deve usar SQLite como persistência central da implementação atual.

### RNF-ST-05

O sistema deve oferecer boa experiência de uso na CLI, com apresentação legível e navegação clara.

### RNF-ST-06

O sistema deve manter persistência das traduções e dos dados documentais para uso posterior.

### RNF-ST-07

O sistema deve suportar carregamento sob demanda de serviços pesados quando possível.

### RNF-ST-08

O sistema deve preservar rastreabilidade entre funcionalidades e camadas arquiteturais.

### RNF-ST-09

O sistema deve manter documentação e organização suficientes para evolução incremental.

## 10. Restrições do ShowTrials atual

- base atual centrada em SQLite
- forte acoplamento entre processamento e persistência
- foco histórico inicial em acervo documental específico
- maturidade desigual entre CLI e Web
- diversas capacidades ainda com caráter de MVP/prova de conceito
- dependência de serviços e bibliotecas pesadas para NLP e tradução

## 11. Limitações estruturais do ShowTrials atual

Com base no contexto já produzido, as principais limitações são:

- arquitetura dominante ainda documento-cêntrica e orientada a persistência
- pouca generalidade para múltiplas fontes/processos
- forte orquestração imperativa em casos de uso
- dificuldade de compor fluxos diferentes sem reuso ad hoc
- Web menos madura que CLI
- ausência de modelo dominante de pipeline configurável

## 12. Fora de escopo do ShowTrials atual

- configuração declarativa geral de pipelines
- versionamento formal de pipelines
- múltiplos bancos de dados como capacidade dominante
- execução em filas/background como arquitetura central
- plugins formais de source/processor/sink como modelo dominante

## 13. Síntese

O ShowTrials atual é um sistema documental especializado, útil e funcional em capacidades centrais como persistência, tradução, consulta e análise, mas estruturalmente ainda orientado a um fluxo fixo de trabalho e a um domínio inicial específico.
