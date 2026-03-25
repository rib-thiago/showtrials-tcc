# Riscos de Overengineering e Trade-offs

## 1. Objetivo do documento

Este documento registra os principais **riscos de overengineering** já visíveis na frente e os **trade-offs** arquiteturais mais relevantes.

## 2. Base de evidência utilizada

- [17_drivers_arquiteturais.md](/home/thiago/coleta_showtrials/docs/modelagem/17_drivers_arquiteturais.md)
- [20_decisoes_arquiteturais_iniciais.md](/home/thiago/coleta_showtrials/docs/modelagem/20_decisoes_arquiteturais_iniciais.md)
- [41_padroes_de_projeto_para_a_evolucao_da_engine.md](/home/thiago/coleta_showtrials/docs/modelagem/41_padroes_de_projeto_para_a_evolucao_da_engine.md)
- [42_mapa_de_padroes_por_modulo.md](/home/thiago/coleta_showtrials/docs/modelagem/42_mapa_de_padroes_por_modulo.md)

## 3. Riscos principais de overengineering

## 3.1 Separar cedo demais o que ainda é coeso

Risco:

- transformar o monólito evolutivo em fragmentação prematura

## 3.2 Formalizar plugin system antes da necessidade real

Risco:

- criar discovery, registro e carregamento dinâmico mais complexos do que o projeto precisa agora

## 3.3 Multiplicar abstrações de padrões sem ganho claro

Risco:

- criar `Strategy`, `Builder`, `Specification`, `Factory` e `State` ao mesmo tempo, mesmo onde um design mais simples bastaria

## 3.4 Modelar estados demais cedo demais

Risco:

- transformar estados de execução em hierarquia desnecessariamente complexa antes de entender o fluxo real de background, persistência e revisão

## 3.5 Tentar apagar o legado em vez de adaptá-lo

Risco:

- perder a base factual e funcional do projeto atual

## 4. Trade-offs principais

## 4.1 Simplicidade atual versus configurabilidade futura

Trade-off:

- quanto mais configurável a engine, maior a pressão por validação, estados e composição

## 4.2 Persistência forte atual versus persistência opcional futura

Trade-off:

- a engine ganha flexibilidade, mas perde algumas certezas operacionais do sistema atual

## 4.3 Generalização da plataforma versus especialização histórica

Trade-off:

- a plataforma precisa generalizar sem apagar o caso histórico que lhe deu forma

## 4.4 Execução síncrona simples versus background e auditoria

Trade-off:

- a flexibilidade processual aumenta, mas também aumenta a complexidade de estados, observabilidade e recuperação

## 5. Leitura recomendada

A frente deve continuar adotando:

- evolução incremental
- abstrações justificadas por necessidade
- uso leve de padrões
- preservação do legado como base de adaptação

## 6. Inferências adotadas

- o maior risco da frente hoje não é falta de arquitetura, mas sim sofisticar cedo demais a engine
- a melhor defesa contra overengineering continua sendo vincular cada abstração a um caso de uso, driver ou decisão arquitetural já consolidada

## 7. Suposições operacionais

- os trade-offs registrados aqui devem ser reavaliados na fase de revisão crítica final, antes de qualquer saneamento arquitetural mais agressivo

## 8. Dívidas técnicas registradas

- decidir o momento correto de introdução de background real
- decidir o grau real de formalização do sistema de plugins
- decidir o grau de persistência obrigatória ou opcional no MVP evolutivo

## 9. Próximos passos

- abrir a revisão crítica final da frente
