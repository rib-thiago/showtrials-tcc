# Visão Lógica — 4+1

## 1. Objetivo do documento

Este documento registra a **visão lógica** da arquitetura da frente, no contexto do modelo **4+1**.

Seu objetivo é descrever a organização lógica do sistema em termos de:

- responsabilidades principais
- relações entre blocos arquiteturais
- papéis que esses blocos desempenham na solução

## 2. Base de evidência utilizada

Esta visão se apoia principalmente em:

- [19_mapeamento_casos_de_uso_para_blocos_arquiteturais.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/ponte/19_mapeamento_casos_de_uso_para_blocos_arquiteturais.md)
- [20_decisoes_arquiteturais_iniciais.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/ponte/20_decisoes_arquiteturais_iniciais.md)
- [21_glossario_arquitetural_e_tecnico.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/ponte/21_glossario_arquitetural_e_tecnico.md)
- [docs/projeto/analise_arquitetural.md](/home/thiago/coleta_showtrials/docs/projeto/analise_arquitetural.md)
- [docs/projeto/direcionamento_arquitetural_engine_mvp.md](/home/thiago/coleta_showtrials/docs/projeto/direcionamento_arquitetural_engine_mvp.md)

## 3. Escopo da visão lógica

Esta visão lógica não descreve:

- deployment
- topologia física
- containers C4 formais
- detalhes de código ou classes específicas

Ela descreve a solução em nível de blocos lógicos e suas responsabilidades centrais.

## 4. Estrutura lógica consolidada

Com base na frente já produzida, a estrutura lógica consolidada pode ser entendida em oito blocos principais:

- Interfaces de operação
- Orquestração de casos de uso
- Catálogo e configuração de pipeline
- Execução de pipeline
- Processamento documental
- Persistência e recuperação
- Resultados derivados e revisão
- Integrações e serviços externos

## 5. Blocos lógicos da solução

## 5.1 Interfaces de operação

### Responsabilidade

Fornecer os pontos de interação do sistema com o usuário e, futuramente, com canais programáticos de acesso.

### Elementos típicos

- CLI
- Web
- possíveis endpoints ou interfaces adicionais futuras

### Relações principais

- consome orquestração de casos de uso
- consome catálogo/configuração de pipeline
- consome execução de pipeline

## 5.2 Orquestração de casos de uso

### Responsabilidade

Orquestrar a realização dos casos de uso do sistema atual e da transição, articulando domínio, persistência e serviços.

### Elementos típicos

- casos de uso atuais
- adaptadores de casos legados
- coordenação entre operações documentais

### Relações principais

- recebe chamadas das interfaces de operação
- usa persistência e recuperação
- usa processamento documental
- usa integrações externas quando necessário

## 5.3 Catálogo e configuração de pipeline

### Responsabilidade

Representar, criar, listar, editar, validar e recuperar pipelines configuráveis.

### Elementos típicos

- entidade/configuração de pipeline
- presets
- versionamento básico
- validação de configuração

### Relações principais

- recebe chamadas das interfaces de operação
- usa persistência e recuperação
- fornece configuração para o bloco de execução

## 5.4 Execução de pipeline

### Responsabilidade

Executar fluxos configurados, controlando contexto de execução, ordem dos steps e acompanhamento da execução.

### Elementos típicos

- executor de pipeline
- contexto de execução
- controle de fluxo
- estado de execução

### Relações principais

- recebe configuração do catálogo/configuração de pipeline
- invoca processamento documental
- aciona persistência configurável
- pode depender de integrações externas

## 5.5 Processamento documental

### Responsabilidade

Executar transformações, classificações, traduções, análises e enriquecimentos sobre documentos e contexto.

### Elementos típicos

- transformadores
- classificadores
- tradutores
- analisadores
- steps orientados a documento ou contexto

### Relações principais

- é acionado pela orquestração de casos de uso
- é acionado pela execução de pipeline
- pode consumir integrações externas
- produz resultados documentais e derivados

## 5.6 Persistência e recuperação

### Responsabilidade

Armazenar e recuperar documentos, pipelines, traduções, resultados derivados e demais artefatos persistíveis.

### Elementos típicos

- repositórios
- mecanismos de leitura e escrita
- abstrações de persistência

### Relações principais

- atende interfaces e orquestração do sistema atual
- atende catálogo de pipelines
- atende execução de pipeline
- fornece base para consulta posterior de resultados

## 5.7 Resultados derivados e revisão

### Responsabilidade

Tratar resultados produzidos pelo sistema que exigem qualificação semântica adicional, persistência controlada, consulta posterior ou revisão humana.

### Elementos típicos

- traduções produzidas
- artefatos analíticos
- estados de revisão
- resultados automáticos versus revisados

### Relações principais

- recebe produtos do processamento documental
- interage com persistência e recuperação
- é consumido por interfaces de operação

## 5.8 Integrações e serviços externos

### Responsabilidade

Encapsular dependências externas relevantes à solução, como tradução, OCR, fontes documentais externas e outros serviços especializados.

### Elementos típicos

- serviços de tradução
- OCR
- scraping/coleta externa
- serviços analíticos externos quando aplicável

### Relações principais

- é consumido por orquestração de casos de uso
- é consumido por processamento documental
- é consumido por execução de pipeline

## 6. Relações lógicas principais

As relações mais relevantes entre os blocos lógicos são as seguintes:

1. Interfaces de operação acionam orquestração de casos de uso e, progressivamente, catálogo/configuração e execução de pipeline.
2. Orquestração de casos de uso depende de persistência/recuperação e de processamento documental.
3. Catálogo/configuração de pipeline fornece insumo estrutural para a execução de pipeline.
4. Execução de pipeline aciona processamento documental e decide, conforme configuração, persistência e tratamento de resultados derivados.
5. Processamento documental produz documentos transformados e resultados derivados, podendo depender de integrações externas.
6. Resultados derivados e revisão funcionam como bloco transversal entre processamento, persistência e consumo posterior.

## 7. Leitura lógica do sistema atual, transição e sistema-alvo

### 7.1 Sistema atual

O sistema atual concentra sua lógica principalmente em:

- interfaces de operação
- orquestração de casos de uso
- persistência e recuperação
- processamento documental ainda acoplado em vários pontos

### 7.2 Transição

A transição introduz de forma mais explícita:

- catálogo/configuração de pipeline
- execução de pipeline

sem eliminar imediatamente a orquestração imperativa dos casos de uso atuais.

### 7.3 Sistema-alvo

O sistema-alvo desloca o centro lógico da solução para:

- catálogo/configuração de pipeline
- execução de pipeline
- processamento documental modular
- persistência configurável de resultados derivados

## 8. Inferências adotadas

As principais inferências adotadas nesta visão lógica foram:

- o bloco “Resultados derivados e revisão” foi mantido como bloco único nesta etapa por ser forte o suficiente para a modelagem atual, embora ainda possa ser dividido futuramente
- a orquestração de casos de uso do sistema atual foi preservada como bloco lógico próprio para não apagar a história arquitetural do ShowTrials
- o executor de pipeline foi tratado como bloco central distinto do catálogo/configuração

## 9. Dívidas técnicas registradas

Permanecem como pontos futuros:

- decidir se resultados derivados e revisão devem continuar juntos na visão lógica
- decidir o papel arquitetural de telemetria e acompanhamento de execução
- refinar melhor a fronteira entre orquestração de casos atuais e execução da engine futura

## 10. Próximos passos

Os próximos passos recomendados são:

- abrir a visão de desenvolvimento do 4+1
- depois a visão de processo
- seguir progressivamente até consolidar a síntese 4+1
