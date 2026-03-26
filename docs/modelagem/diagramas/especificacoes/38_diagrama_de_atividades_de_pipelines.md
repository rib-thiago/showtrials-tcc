# Diagrama de Atividades de Pipelines

## 1. Objetivo do documento

Este documento registra o recorte do **diagrama de atividades de pipelines**.

Seu objetivo é mostrar a lógica de alto nível da atividade:

- configurar
- validar
- executar
- persistir
- revisar

Nesta estabilização, o diagrama correspondente foi **materializado em PlantUML**, e este documento passa a funcionar como leitura textual do fluxo que o diagrama representa.

## 2. Base de evidência utilizada

- [24_visao_de_processo_4mais1.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/visao_4mais1/24_visao_de_processo_4mais1.md)
- [13_especificacoes_textuais_de_casos_de_uso_prioritarios.md](/home/thiago/coleta_showtrials/docs/modelagem/analise/principais/13_especificacoes_textuais_de_casos_de_uso_prioritarios.md)
- [38_diagrama_de_atividades_de_pipelines.puml](../fontes/38_diagrama_de_atividades_de_pipelines.puml)

## 3. Atividades centrais a representar

- escolher ou criar pipeline
- configurar pipeline
- validar pipeline
- fornecer entrada
- executar steps
- decidir sobre persistência
- decidir sobre revisão/intervenção
- encerrar execução com sucesso ou falha

## 4. Decisões de fluxo mais importantes

O diagrama deve mostrar:

- bifurcação entre configuração válida e inválida
- bifurcação entre persistir e não persistir
- bifurcação entre fluxo automático e fluxo com revisão
- saída por sucesso, falha parcial ou falha total

## 5. Inferências adotadas

- o diagrama de atividades foi tratado como artefato especialmente importante para a engine por causa da natureza processual do problema

## 6. Dívidas técnicas registradas

- detalhamento futuro de atividades em background
- eventual separação de atividades por tipo especializado de pipeline

## 7. Situação do artefato nesta estabilização

- o diagrama de atividades de pipelines foi materializado em `PlantUML`
- o recorte manteve foco em fluxo de alto nível, sem detalhar cenários especializados ou execução em background
- o diagrama de estados continua como artefato preparatório para decisão posterior
