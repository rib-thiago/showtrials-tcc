# Diagrama de Atividades de Pipelines

## 1. Objetivo do documento

Este documento registra o recorte do **diagrama de atividades de pipelines**.

Seu objetivo é mostrar a lógica de alto nível da atividade:

- configurar
- validar
- executar
- persistir
- revisar

Nesta etapa, o artefato deve ser lido como **especificação textual preparatória** do diagrama, e não como o diagrama materializado em si.

## 2. Base de evidência utilizada

- [24_visao_de_processo_4mais1.md](/home/thiago/coleta_showtrials/docs/modelagem/24_visao_de_processo_4mais1.md)
- [13_especificacoes_textuais_de_casos_de_uso_prioritarios.md](/home/thiago/coleta_showtrials/docs/modelagem/13_especificacoes_textuais_de_casos_de_uso_prioritarios.md)

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

## 7. Próximos passos

- avaliar o diagrama de estados
