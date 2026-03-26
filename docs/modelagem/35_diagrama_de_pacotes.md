# Diagrama de Pacotes

## 1. Objetivo do documento

Este documento registra o recorte do **diagrama de pacotes** da frente.

Seu objetivo é mostrar:

- como os grandes agrupamentos de código se relacionam
- como a direção de dependências deve permanecer organizada
- como a engine futura se encaixa na estrutura atual

Nesta etapa, o artefato deve ser lido como **especificação textual preparatória** do diagrama, e não como o diagrama materializado em si.

## 2. Base de evidência utilizada

- [23_visao_de_desenvolvimento_4mais1.md](/home/thiago/coleta_showtrials/docs/modelagem/23_visao_de_desenvolvimento_4mais1.md)
- estrutura atual do código em `src/`

## 3. Pacotes principais atuais

Os pacotes principais atuais são:

- `src/interface`
- `src/application`
- `src/domain`
- `src/infrastructure`
- `src/tests`

## 4. Pacote futuro relevante

O pacote futuro mais relevante já exigido pela frente é:

- pacote ou subárvore da **engine de pipeline**

## 5. Relações principais entre pacotes

- `interface` depende de `application`
- `application` depende de `domain`
- `infrastructure` implementa contratos consumidos por `application` e `domain`
- `tests` exercitam os demais pacotes
- a futura `engine` deve se integrar sem inverter a direção principal de dependências

## 6. Inferências adotadas

- a engine foi tratada como pacote futuro relevante, ainda sem fixar caminho definitivo no código

## 7. Dívidas técnicas registradas

- estrutura final de pacotes da engine
- papel futuro de subpacotes específicos para pipeline, execução, configuração e resultados derivados

## 8. Próximos passos

- abrir os diagramas de sequência
