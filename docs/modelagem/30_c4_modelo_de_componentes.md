# C4 — Modelo de Componentes

## 1. Objetivo do documento

Este documento registra o **modelo de componentes** da frente segundo o **C4 Model**.

Seu objetivo é detalhar os principais componentes internos do container central da solução:

- o núcleo da aplicação ShowTrials

## 2. Base de evidência utilizada

Esta visão se apoia principalmente em:

- [19_mapeamento_casos_de_uso_para_blocos_arquiteturais.md](/home/thiago/coleta_showtrials/docs/modelagem/19_mapeamento_casos_de_uso_para_blocos_arquiteturais.md)
- [20_decisoes_arquiteturais_iniciais.md](/home/thiago/coleta_showtrials/docs/modelagem/20_decisoes_arquiteturais_iniciais.md)
- [22_visao_logica_4mais1.md](/home/thiago/coleta_showtrials/docs/modelagem/22_visao_logica_4mais1.md)
- [23_visao_de_desenvolvimento_4mais1.md](/home/thiago/coleta_showtrials/docs/modelagem/23_visao_de_desenvolvimento_4mais1.md)
- [29_c4_modelo_de_containers.md](/home/thiago/coleta_showtrials/docs/modelagem/29_c4_modelo_de_containers.md)
- estrutura atual do código em `src/`

## 3. Container focalizado

O container focalizado neste modelo é:

- **núcleo da aplicação ShowTrials**

Ele foi escolhido porque concentra hoje a maior parte da lógica e também o ponto de convergência da evolução para a engine.

## 4. Componentes arquiteturalmente relevantes

Com base na frente consolidada, os componentes mais relevantes desse container são:

- adaptadores de interface
- orquestração de casos de uso
- núcleo de domínio
- persistência e recuperação
- integrações e serviços externos
- service registry e factories
- catálogo/configuração de pipeline
- execução de pipeline
- resultados derivados e revisão

## 5. Descrição dos componentes

## 5.1 Adaptadores de interface

### Papel

Conectar CLI e Web aos serviços do núcleo da aplicação.

### Evidência atual

- `src/interface/cli/`
- `src/interface/web/`

### Relações principais

- acionam orquestração de casos de uso
- consomem consultas, traduções, análises e outras operações do núcleo

## 5.2 Orquestração de casos de uso

### Papel

Realizar a coordenação das operações do sistema atual e da transição.

### Evidência atual

- `src/application/use_cases/`

### Relações principais

- consome domínio
- consome persistência
- consome integrações externas
- deve acomodar progressivamente a engine de pipeline

## 5.3 Núcleo de domínio

### Papel

Concentrar entidades, value objects e contratos do problema.

### Evidência atual

- `src/domain/entities/`
- `src/domain/value_objects/`
- `src/domain/interfaces/`

### Relações principais

- é consumido pela aplicação
- define contratos implementados pela infraestrutura

## 5.4 Persistência e recuperação

### Papel

Persistir e recuperar documentos, traduções e demais artefatos persistíveis.

### Evidência atual

- `src/infrastructure/persistence/`

### Relações principais

- implementa contratos do domínio e da aplicação
- sustenta os casos de uso atuais
- deverá sustentar pipelines e produtos derivados futuros

## 5.5 Integrações e serviços externos

### Papel

Encapsular tradução, análise, OCR e demais serviços especializados externos ou semi-externos.

### Evidência atual

- `src/infrastructure/translation/`
- `src/infrastructure/analysis/`

### Relações principais

- são consumidos pela orquestração de casos de uso
- podem ser consumidos pela futura execução de pipeline

## 5.6 Service registry e factories

### Papel

Centralizar inicialização, lazy loading e composição de serviços.

### Evidência atual

- `src/infrastructure/registry.py`
- `src/infrastructure/factories.py`

### Relações principais

- sustenta composição da aplicação atual
- funciona como ponte arquitetural importante para evolução incremental

## 5.7 Catálogo e configuração de pipeline

### Papel

Representar criação, ajuste, validação e recuperação de pipelines configuráveis.

### Evidência atual

Ainda não está implementado como componente explícito, mas está amplamente sustentado pelos documentos desta frente.

### Relações principais

- dialoga com orquestração de casos de uso
- fornece insumo para execução de pipeline
- dependerá de persistência e recuperação

## 5.8 Execução de pipeline

### Papel

Executar fluxos configurados com contexto explícito, ordem de steps e persistência configurável.

### Evidência atual

Ainda não está implementado como componente explícito, mas está sustentado por:

- drivers arquiteturais
- decisões arquiteturais
- 4+1

### Relações principais

- consome configuração de pipeline
- aciona processamento e integrações
- pode produzir resultados derivados e acionar persistência

## 5.9 Resultados derivados e revisão

### Papel

Tratar artefatos analíticos, traduções, estados de revisão e distinção entre automático e revisado.

### Evidência atual

É componente parcialmente distribuído no sistema atual, mas já forte o suficiente na frente para ser tratado como componente arquitetural.

### Relações principais

- recebe dados do processamento e da execução
- usa persistência
- é consumido pelas interfaces

## 6. Relações mais importantes entre componentes

As relações mais importantes são:

1. adaptadores de interface acionam a orquestração de casos de uso;
2. orquestração usa domínio, persistência, integrações e service registry;
3. catálogo/configuração de pipeline fornece definição para execução de pipeline;
4. execução de pipeline consome processamento, integrações e persistência;
5. resultados derivados e revisão recebem artefatos de processamento e de execução;
6. service registry e factories funcionam como mecanismo de composição transversal.

## 7. Inferências adotadas

As principais inferências adotadas neste modelo foram:

- componentes ainda não implementados da engine foram mantidos porque sua necessidade já está suficientemente consolidada pelos artefatos anteriores
- `resultados derivados e revisão` foi mantido como componente próprio, mesmo ainda distribuído no sistema atual, por seu peso arquitetural crescente
- `service registry` foi tratado como componente de relevância arquitetural, e não mero detalhe utilitário

## 8. Dívidas técnicas registradas

Permanecem como pontos futuros:

- forma concreta de materialização dos componentes da engine no código
- fronteira exata entre orquestração legada e executor de pipeline
- eventual separação futura entre resultados derivados e revisão em componentes diferentes

## 9. Próximos passos

Os próximos passos recomendados são:

- abrir o modelo de código do C4
- escolher recorte focalizado e aderente para esse nível
