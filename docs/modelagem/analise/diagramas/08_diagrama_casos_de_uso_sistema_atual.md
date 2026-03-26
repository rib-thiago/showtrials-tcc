# Diagrama de Casos de Uso — Sistema Atual

## 1. Objetivo do diagrama

Este documento apresenta o primeiro diagrama formal de casos de uso da frente de modelagem, com foco exclusivo no **ShowTrials atual**.

Seu objetivo é representar, de forma visual e controlada:

- o ator principal do sistema atual
- os casos de uso já sustentados por código e documentação de fases
- uma relação `<<include>>` considerada suficientemente forte para esta primeira versão

## 2. Escopo adotado

Este diagrama trata apenas do sistema atual.

Por isso, ficam fora dele:

- casos de uso da transição arquitetural
- casos de uso do sistema-alvo orientado a pipeline
- cenários especializados da futura engine
- generalização entre atores

## 3. Ator considerado

- `usuario operador`

Este ator foi selecionado por ser o mais aderente ao uso do sistema atual, conforme os insumos anteriores da frente.

## 4. Casos de uso representados

### 4.1 Consulta e navegação

- `ListarDocumentos`
- `ObterDocumento`

### 4.2 Preparação e enriquecimento

- `ClassificarDocumento`

### 4.3 Tradução

- `TraduzirDocumento`
- `ListarTraducoes`

### 4.4 Análise

- `AnalisarDocumento`
- `AnalisarAcervo`
- `ObterEstatisticas`

### 4.5 Saída e consolidação

- `ExportarDocumento`
- `GerarRelatorio`

## 5. Relações representadas

### 5.1 Associações do ator

O `usuario operador` foi associado diretamente a todos os casos de uso representados.

### 5.2 Relação entre casos de uso

Foi adotada, nesta primeira versão, apenas a seguinte relação:

- `GerarRelatorio` `<<include>>` `ObterEstatisticas`

Essa foi considerada a relação mais segura e mais útil para a legibilidade do diagrama nesta etapa.

## 6. Arquivo-fonte do diagrama

O diagrama foi registrado em:

- [08_diagrama_casos_de_uso_sistema_atual.puml](../../diagramas/fontes/08_diagrama_casos_de_uso_sistema_atual.puml)

## 7. Dívidas técnicas registradas

Permanecem como pontos para análise crítica futura:

- avaliar se `ObterDocumento` deve ou não ter relação formal com `ListarTraducoes`
- avaliar se `ExportarDocumento` depende formalmente de `ObterDocumento`
- avaliar se `AnalisarDocumento` deve ter relação formal com recuperação de documento
- decidir em qual diagrama a generalização entre atores deve aparecer
- revisar a granularidade de `ObterEstatisticas` no conjunto dos casos de uso atuais

## 8. Próximos passos

Os próximos passos recomendados são:

- usar este diagrama como base para o diagrama da transição arquitetural
- avançar depois para o diagrama do sistema-alvo
- abrir, em paralelo ou em etapa posterior, as especificações textuais dos casos prioritários
