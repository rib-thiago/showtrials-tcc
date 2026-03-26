# Diagrama de Casos de Uso — Cenários Especializados

## 1. Objetivo do diagrama

Este documento apresenta o diagrama complementar de casos de uso dos **cenários especializados** da futura engine configurável.

Seu objetivo é representar:

- exemplos concretos de execução especializada de pipelines
- a relação entre esses cenários e o caso de uso geral `ExecutarPipelineDocumental`
- um caso complementar de consulta de resultados

## 2. Escopo adotado

Este diagrama complementa o diagrama principal do sistema-alvo.

Ele não substitui o núcleo da futura engine, mas o detalha por meio de cenários exemplares que ajudam a comunicar usos especializados da arquitetura configurável.

Foram mantidos fora deste diagrama:

- os casos centrais de criação, listagem e edição de pipelines
- as decisões mais finas sobre persistência obrigatória ou opcional
- relações formais de `<<include>>` e `<<extend>>` ainda não amadurecidas

## 3. Ator considerado

Foi considerado como ator principal:

- `usuario configurador`

## 4. Casos de uso representados

### 4.1 Caso base

O caso de uso geral incluído para sustentar as especializações foi:

- `ExecutarPipelineDocumental`

### 4.2 Casos especializados

Foram incluídos como especializações do caso geral:

- `ProcessarPDFcomOCR`
- `ExecutarPipelineDeTraducao`
- `ExecutarPipelineDeRaspagemEAnalise`
- `ExecutarPipelinePorID`

### 4.3 Caso complementar

Também foi incluído:

- `ConsultarResultadosDePipeline`

Esse caso foi mantido como caso lateral independente, e não como especialização de execução.

## 5. Relações representadas

### 5.1 Associações do ator

O `usuario configurador` foi associado diretamente a:

- `ExecutarPipelineDocumental`
- `ConsultarResultadosDePipeline`

### 5.2 Generalização entre casos de uso

Nesta etapa, foi considerada madura o suficiente a leitura de que alguns cenários especializados funcionam como variações do caso de uso geral `ExecutarPipelineDocumental`.

Por isso, foram registradas as seguintes especializações:

- `ProcessarPDFcomOCR` especializa `ExecutarPipelineDocumental`
- `ExecutarPipelineDeTraducao` especializa `ExecutarPipelineDocumental`
- `ExecutarPipelineDeRaspagemEAnalise` especializa `ExecutarPipelineDocumental`
- `ExecutarPipelinePorID` especializa `ExecutarPipelineDocumental`

### 5.3 Relações não representadas

Não foram registradas, nesta etapa:

- relações formais de `<<include>>`
- relações formais de `<<extend>>`

Essa decisão foi tomada para preservar clareza e evitar sugerir vínculos internos de execução ainda não suficientemente estabilizados.

## 6. Estratégia visual adotada

O diagrama foi organizado com:

- o caso geral `ExecutarPipelineDocumental` em posição superior dentro da fronteira
- os casos especializados abaixo dele
- o caso `ConsultarResultadosDePipeline` em posição lateral

Essa estratégia busca facilitar a leitura da generalização e evitar que o caso complementar pareça mais uma especialização.

## 7. Arquivo-fonte do diagrama

O diagrama foi registrado em:

- [11_diagrama_casos_de_uso_cenarios_especializados.puml](../../diagramas/fontes/11_diagrama_casos_de_uso_cenarios_especializados.puml)

## 8. Dívidas técnicas registradas

Permanecem como pontos para análise crítica futura:

- avaliar se `ConsultarResultadosDePipeline` deve continuar no diagrama complementar ou subir para o principal
- avaliar se `ExecutarPipelinePorID` é especialização real ou apenas detalhe operacional
- avaliar se alguns cenários especializados devem virar casos de uso centrais no futuro
- avaliar se haverá relações formais de `<<include>>` ou `<<extend>>` entre execução especializada, persistência e consulta de resultados

## 9. Próximos passos

Os próximos passos recomendados são:

- revisar os quatro diagramas de casos de uso em conjunto
- decidir quais casos de uso prioritários passarão à especificação textual
- preparar a próxima camada da frente, conectando casos de uso e arquitetura
