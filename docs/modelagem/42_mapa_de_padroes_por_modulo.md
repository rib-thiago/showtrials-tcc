# Mapa de Padrões por Módulo

## 1. Objetivo do documento

Este documento registra um **mapa de padrões por módulo ou área arquitetural**.

Seu objetivo é ligar padrões já existentes ou desejáveis às partes mais relevantes da solução.

## 2. Base de evidência utilizada

- [23_visao_de_desenvolvimento_4mais1.md](/home/thiago/coleta_showtrials/docs/modelagem/23_visao_de_desenvolvimento_4mais1.md)
- [30_c4_modelo_de_componentes.md](/home/thiago/coleta_showtrials/docs/modelagem/30_c4_modelo_de_componentes.md)
- [40_analise_de_padroes_de_projeto_existentes.md](/home/thiago/coleta_showtrials/docs/modelagem/40_analise_de_padroes_de_projeto_existentes.md)
- [41_padroes_de_projeto_para_a_evolucao_da_engine.md](/home/thiago/coleta_showtrials/docs/modelagem/41_padroes_de_projeto_para_a_evolucao_da_engine.md)

## 3. Mapa consolidado

## 3.1 Interface CLI e Web

Padrões mais aderentes:

- Command-like
- Presenter
- composição explícita

## 3.2 Aplicação / Casos de uso

Padrões mais aderentes:

- Use Case / Application Service
- Adapter de transição
- coordenação próxima de Facade leve, quando necessário

## 3.3 Domínio atual

Padrões mais aderentes:

- Entity
- Value Object
- Repository (por contrato)

## 3.4 Infraestrutura

Padrões mais aderentes:

- Repository
- Factory
- Adapter
- Registry

## 3.5 Engine de pipeline

Padrões mais aderentes:

- Pipeline / Pipes and Filters
- Strategy
- Factory
- Builder leve
- Specification / validação estruturada

## 3.6 Resultados derivados e revisão

Padrões mais aderentes:

- Adapter
- State leve, se a modelagem de estados se confirmar
- versionamento simples

## 4. Inferências adotadas

- o mapa por módulo ajuda a evitar uso genérico e descontextualizado de padrões
- a engine concentra a maior densidade de padrões futuros, mas isso não implica multiplicação automática de abstrações

## 5. Suposições operacionais

- o mapa foi mantido em nível arquitetural e não pretende prescrever biblioteca, framework ou naming final

## 6. Dívidas técnicas registradas

- verificar mais tarde se o módulo de resultados derivados exigirá padrões próprios adicionais
- decidir se haverá separação mais explícita entre padrões de aplicação e padrões de engine

## 7. Próximos passos

- abrir o documento de riscos de overengineering e trade-offs
