# Diagrama de Sequência — Fluxos da Engine

## 1. Objetivo do documento

Este documento registra o recorte do **diagrama de sequência dos fluxos da engine**.

Seu objetivo é explicitar a sequência principal dos casos de uso:

- `ConfigurarPipeline`
- `ExecutarPipelineDocumental`
- `RevisarTraducao`

Nesta etapa, o artefato deve ser lido como **especificação textual preparatória** do diagrama, e não como o diagrama materializado em si.

## 2. Base de evidência utilizada

- [13_especificacoes_textuais_de_casos_de_uso_prioritarios.md](/home/thiago/coleta_showtrials/docs/modelagem/analise/principais/13_especificacoes_textuais_de_casos_de_uso_prioritarios.md)
- [31_c4_modelo_de_codigo.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/c4/31_c4_modelo_de_codigo.md)

## 3. Participantes principais

- `usuario configurador`
- interface de operação
- caso de uso ou adaptador de aplicação
- `PipelineValidator`
- `PipelineRepository`
- `PipelineExecutor`
- `ContextoPipeline`
- `Source` / `Processor` / `Sink`
- persistência e resultados derivados

## 4. Leitura recomendada do diagrama

O diagrama deve mostrar:

- validação antes da execução
- criação ou recuperação de contexto
- execução ordenada de steps
- atualização de estado
- persistência opcional
- eventual ponto de revisão humana

## 5. Inferências adotadas

- a sequência da engine foi tratada como explicitamente mais rica em estados e variações do que os fluxos atuais

## 6. Dívidas técnicas registradas

- representação futura de execução background
- pontos exatos de intervenção humana durante a execução

## 7. Próximos passos

- abrir o diagrama de atividades de pipelines
