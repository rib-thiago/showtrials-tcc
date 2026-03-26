# Diagrama de Componentes

## 1. Objetivo do documento

Este documento registra o recorte do **diagrama de componentes** da frente.

Seu objetivo é mostrar, em linguagem UML, os componentes principais da solução e suas dependências mais relevantes.

Nesta estabilização, o diagrama correspondente foi **materializado em PlantUML**, e este documento passa a funcionar como leitura explicativa do recorte escolhido.

## 2. Base de evidência utilizada

- [22_visao_logica_4mais1.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/visao_4mais1/22_visao_logica_4mais1.md)
- [30_c4_modelo_de_componentes.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/c4/30_c4_modelo_de_componentes.md)
- estrutura atual do código em `src/`
- [34_diagrama_de_componentes.puml](../fontes/34_diagrama_de_componentes.puml)
- [34_diagrama_de_componentes.svg](../renderizados/34_diagrama_de_componentes.svg)

## 3. Componentes principais a representar

- Adaptadores CLI e Web
- Casos de uso e orquestração
- Domínio
- Persistência e recuperação
- Integrações externas
- Service registry e factories
- Catálogo/configuração de pipeline
- Execução de pipeline
- Resultados derivados e revisão

## 4. Dependências principais a representar

- interfaces dependem da aplicação
- aplicação depende do domínio
- infraestrutura implementa contratos do domínio e da aplicação
- engine futura dialoga com aplicação, domínio e persistência

## 5. Leitura recomendada do diagrama

O diagrama deve separar claramente:

- componentes já implementados
- componentes futuros já exigidos

Sem misturar:

- dependência lógica
- relação de runtime
- detalhe de classe

## 6. Inferências adotadas

- o diagrama de componentes foi tratado como complemento UML do que já foi consolidado no C4 nível componentes

## 7. Dívidas técnicas registradas

- fronteira concreta entre orquestração legada e engine
- eventual separação futura entre resultados derivados e revisão

## 8. Situação do artefato nesta estabilização

- o diagrama de componentes foi materializado em `PlantUML`
- o recorte distingue componentes já implementados dos blocos futuros exigidos pela frente
- o diagrama de pacotes permanece como artefato preparatório para etapa posterior
