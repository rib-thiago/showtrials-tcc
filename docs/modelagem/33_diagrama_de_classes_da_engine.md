# Diagrama de Classes da Engine

## 1. Objetivo do documento

Este documento registra o recorte do **diagrama de classes da engine**.

Seu objetivo é explicitar as classes e contratos mínimos esperados para a futura engine de pipeline.

Nesta etapa, o artefato deve ser lido como **especificação textual preparatória** do diagrama, e não como o diagrama materializado em si.

## 2. Base de evidência utilizada

- [20_decisoes_arquiteturais_iniciais.md](/home/thiago/coleta_showtrials/docs/modelagem/20_decisoes_arquiteturais_iniciais.md)
- [31_c4_modelo_de_codigo.md](/home/thiago/coleta_showtrials/docs/modelagem/31_c4_modelo_de_codigo.md)
- [docs/projeto/direcionamento_arquitetural_engine_mvp.md](/home/thiago/coleta_showtrials/docs/projeto/direcionamento_arquitetural_engine_mvp.md)

## 3. Classes principais da engine

As classes e contratos principais esperados são:

- `Pipeline`
- `VersaoPipeline`
- `PipelineStep`
- `ContextoPipeline`
- `PipelineExecutor`
- `PipelineValidator`
- `PipelineRepository`
- `Source`
- `Processor`
- `Sink`

## 4. Relações principais esperadas

- `Pipeline` agrega `PipelineStep`
- `Pipeline` possui uma ou mais `VersaoPipeline`
- `PipelineExecutor` executa um `Pipeline` sobre `ContextoPipeline`
- `PipelineValidator` valida `Pipeline`
- `PipelineRepository` persiste `Pipeline` e versões
- `PipelineStep` referencia um contrato do tipo `Source`, `Processor` ou `Sink`

## 5. Leitura recomendada do diagrama

O diagrama deve mostrar:

- agregação entre `Pipeline` e `PipelineStep`
- associação entre `Pipeline` e `VersaoPipeline`
- dependência de `PipelineExecutor` em `PipelineValidator`
- uso de contratos `Source`, `Processor` e `Sink`

## 6. Inferências adotadas

- `VersaoPipeline` foi tratado como classe própria, e não apenas atributo, por coerência com versionamento simples previsto
- contratos `Source`, `Processor` e `Sink` foram mantidos no núcleo do diagrama por sustentarem a separação fundamental da engine

## 7. Dívidas técnicas registradas

- nomes finais de classes e módulos
- papel futuro de presets e templates de pipeline
- lugar exato de adaptação dos casos de uso legados

## 8. Próximos passos

- abrir o diagrama de componentes
