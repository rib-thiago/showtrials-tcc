# C4 — Modelo de Código

## 1. Objetivo do documento

Este documento registra o **modelo de código** da frente segundo o **C4 Model**.

Por decisão metodológica explícita, este nível foi **focalizado** em um recorte arquitetural específico:

- a futura engine de pipeline

Essa escolha evita um pseudo-modelo de código genérico do sistema inteiro e mantém aderência ao que mais precisa de explicitação estrutural nesta frente.

## 2. Base de evidência utilizada

Esta visão se apoia principalmente em:

- [20_decisoes_arquiteturais_iniciais.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/ponte/20_decisoes_arquiteturais_iniciais.md)
- [21_glossario_arquitetural_e_tecnico.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/ponte/21_glossario_arquitetural_e_tecnico.md)
- [22_visao_logica_4mais1.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/visao_4mais1/22_visao_logica_4mais1.md)
- [23_visao_de_desenvolvimento_4mais1.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/visao_4mais1/23_visao_de_desenvolvimento_4mais1.md)
- [24_visao_de_processo_4mais1.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/visao_4mais1/24_visao_de_processo_4mais1.md)
- [30_c4_modelo_de_componentes.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/c4/30_c4_modelo_de_componentes.md)
- [docs/projeto/direcionamento_arquitetural_engine_mvp.md](/home/thiago/coleta_showtrials/docs/projeto/direcionamento_arquitetural_engine_mvp.md)

## 3. Recorte focalizado

O recorte focalizado deste modelo é:

- **criação, configuração e execução de pipelines com contexto explícito**

Ele foi escolhido porque concentra a maior quantidade de decisões arquiteturais ainda não materializadas no código atual.

## 4. Estruturas de código esperadas no recorte

Com base na frente produzida, as estruturas de código mais prováveis e relevantes para esse recorte são:

- `Pipeline`
- `VersaoPipeline`
- `ContextoPipeline`
- `PipelineStep`
- contratos de `Source`, `Processor` e `Sink`
- `PipelineExecutor`
- `PipelineValidator`
- `PipelineRepository`
- adaptadores entre casos de uso legados e execução configurada

## 5. Responsabilidade das estruturas focalizadas

## 5.1 `Pipeline`

### Papel

Representar a configuração estruturada de um fluxo reutilizável.

### Responsabilidades esperadas

- identificar pipeline
- manter configuração ou referência de configuração
- sustentar reexecução e ajuste

## 5.2 `VersaoPipeline`

### Papel

Representar o versionamento simples do pipeline no MVP.

### Responsabilidades esperadas

- permitir histórico mínimo por versão
- sustentar reexecução determinística
- evitar sobrescrita sem rastreabilidade

## 5.3 `ContextoPipeline`

### Papel

Representar o estado de execução do pipeline.

### Responsabilidades esperadas

- carregar documentos ou iteráveis documentais
- manter artefatos intermediários
- manter resultados agregados
- manter estado de execução

## 5.4 `PipelineStep`

### Papel

Representar um passo configurado do fluxo.

### Responsabilidades esperadas

- guardar tipo e ordem do step
- apontar plugin ou processador associado
- carregar configuração específica do passo

## 5.5 Contratos `Source`, `Processor` e `Sink`

### Papel

Separar claramente:

- entrada de dados
- transformação/processamento
- persistência ou saída

### Responsabilidades esperadas

- `Source`: produzir entrada documental ou contextual
- `Processor`: transformar documento ou contexto
- `Sink`: persistir ou exportar resultados

## 5.6 `PipelineExecutor`

### Papel

Executar o fluxo configurado segundo a ordem de steps e o contexto de execução.

### Responsabilidades esperadas

- validar pré-condições de execução
- iniciar e acompanhar o contexto
- executar steps em ordem
- registrar estados e resultados
- lidar com falhas parciais ou totais

## 5.7 `PipelineValidator`

### Papel

Validar se um pipeline configurado é executável.

### Responsabilidades esperadas

- checar compatibilidade entre entrada e steps
- checar presença de recursos obrigatórios
- checar coerência mínima da configuração

## 5.8 `PipelineRepository`

### Papel

Persistir e recuperar pipelines e versões.

### Responsabilidades esperadas

- salvar pipeline
- recuperar versões
- permitir reexecução posterior

## 5.9 Adaptadores de transição

### Papel

Fazer a ponte entre os casos de uso atuais e a futura execução configurada.

### Responsabilidades esperadas

- reaproveitar transformações já existentes
- evitar reescrita destrutiva
- permitir evolução incremental

## 6. Relações de código mais importantes

As relações mais importantes neste recorte são:

1. `Pipeline` referencia uma configuração composta por `PipelineStep`.
2. `PipelineExecutor` consome `Pipeline` e `ContextoPipeline`.
3. `PipelineValidator` valida `Pipeline` antes da execução.
4. `PipelineExecutor` aciona contratos de `Source`, `Processor` e `Sink`.
5. `PipelineRepository` persiste `Pipeline` e suas versões.
6. adaptadores de transição conectam casos atuais ao novo fluxo configurado.

## 7. O que este modelo de código não pretende fazer

Este documento não pretende:

- descrever classes concretas já inexistentes como se estivessem implementadas
- substituir futuros diagramas UML de classes ou sequência
- congelar nomes finais de arquivos, pacotes e classes

Ele pretende:

- explicitar a malha estrutural mínima que a engine precisará materializar

## 8. Inferências adotadas

As principais inferências adotadas neste modelo foram:

- `VersaoPipeline` foi tratada como estrutura relevante, ainda que sua forma concreta no código possa variar
- `PipelineValidator` foi explicitado como estrutura própria por coerência com a relevância da validação configurável nos casos de uso
- adaptadores de transição foram tratados como parte importante do código, e não apenas detalhe de migração

## 9. Dívidas técnicas registradas

Permanecem como pontos futuros:

- definição concreta de pacotes e módulos da engine
- fronteira exata entre contratos de domínio e implementações de infraestrutura
- modelagem concreta de estados de execução e de resultados derivados
- decisão futura sobre separação entre executor síncrono e executor background

## 10. Próximos passos

Os próximos passos recomendados são:

- abrir o bloco UML complementar
- usar este modelo como ponte para diagramas de classes, componentes e sequência
