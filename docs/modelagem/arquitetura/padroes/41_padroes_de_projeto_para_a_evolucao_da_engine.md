# Padrões de Projeto para a Evolução da Engine

## 1. Objetivo do documento

Este documento registra os **padrões de projeto desejáveis para a evolução da engine**, com base no que a frente já consolidou.

## 2. Base de evidência utilizada

- [17_drivers_arquiteturais.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/ponte/17_drivers_arquiteturais.md)
- [20_decisoes_arquiteturais_iniciais.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/ponte/20_decisoes_arquiteturais_iniciais.md)
- [31_c4_modelo_de_codigo.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/c4/31_c4_modelo_de_codigo.md)
- [40_analise_de_padroes_de_projeto_existentes.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/padroes/40_analise_de_padroes_de_projeto_existentes.md)
- [docs/projeto/direcionamento_arquitetural_engine_mvp.md](/home/thiago/coleta_showtrials/docs/projeto/direcionamento_arquitetural_engine_mvp.md)

## 3. Critério adotado

Os padrões listados aqui não são tratados como obrigação automática de implementação, mas como **candidatos fortes** para resolver problemas que a frente já explicitou.

## 4. Padrões mais promissores

## 4.1 Strategy

### Papel desejado

Permitir seleção e substituição de comportamentos de processamento conforme tipo de step, entrada ou contexto.

### Aplicação provável

- processadores documentais
- políticas de validação
- estratégias de persistência opcional

## 4.2 Pipeline / Pipes and Filters

### Papel desejado

Representar a execução encadeada e configurável de passos de processamento.

### Aplicação provável

- executor da engine
- encadeamento de `Source`, `Processor` e `Sink`

## 4.3 Factory / Abstract Factory leve

### Papel desejado

Criar componentes configurados da engine sem acoplamento excessivo a implementações concretas.

### Aplicação provável

- criação de steps
- resolução de serviços por tipo
- construção de pipelines a partir de configuração

## 4.4 Adapter

### Papel desejado

Permitir reuso incremental dos casos de uso e serviços atuais dentro da engine futura.

### Aplicação provável

- adaptadores de transição entre legado e pipeline

## 4.5 Template Method ou Executor Base

### Papel desejado

Uniformizar a estrutura da execução de passos, deixando variações em pontos específicos.

### Aplicação provável

- esqueleto de execução de steps
- validação padronizada com pontos de extensão

## 4.6 Specification ou Validação estruturada

### Papel desejado

Expressar regras de compatibilidade entre entrada, contexto e steps.

### Aplicação provável

- `PipelineValidator`
- validação de composição do fluxo

## 4.7 Builder leve

### Papel desejado

Facilitar montagem de pipelines ou configurações complexas sem inflar construtores.

### Aplicação provável

- presets
- montagem incremental de pipeline

## 5. Padrões a tratar com cautela

Devem ser tratados com cautela:

- Observer/Event Bus
- Mediator
- Plugin discovery excessivamente sofisticado
- Abstract Factory pesada demais
- State como hierarquia exuberante antes da necessidade real

## 6. Inferências adotadas

As principais inferências adotadas nesta análise foram:

- `Strategy`, `Pipeline` e `Adapter` são hoje os padrões mais naturalmente alinhados à evolução da engine
- `Specification` ou uma variação de validação estruturada parece mais aderente do que validações ad hoc espalhadas
- alguns padrões podem ser úteis apenas em forma leve, e não em sua versão mais elaborada

## 7. Suposições operacionais

- a evolução da engine continuará incremental e, por isso, padrões de transição e composição tendem a ser mais valiosos que padrões de abstração excessivamente amplos

## 8. Dívidas técnicas registradas

- decidir futuramente se a engine usará plugin system explícito ou apenas combinação de factories, registry e contratos
- decidir o grau de formalização do validador de pipeline

## 9. Próximos passos

- abrir o mapa de padrões por módulo
