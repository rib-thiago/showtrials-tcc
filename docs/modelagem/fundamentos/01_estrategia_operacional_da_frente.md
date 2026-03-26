# Estratégia Operacional da Frente de Modelagem, Análise e Padrões

## 1. Objetivo da frente

Esta frente existe para estruturar, com rigor técnico e acadêmico, a evolução do projeto ShowTrials em direção a uma arquitetura mais geral de engine de pipeline.

O objetivo não é apenas produzir diagramas ou documentação acadêmica isolada. O objetivo correto é:

- transformar a evolução arquitetural em uma frente modelada, analisada e rastreável
- produzir artefatos que expliquem o sistema atual, justifiquem a mudança e orientem a implementação futura
- apoiar decisões de arquitetura, backlog, requisitos, governança e apresentação acadêmica

## 2. Princípio central

Toda a frente deve preservar a separação entre três planos:

1. **estado atual implementado**
2. **transição arquitetural já iniciada**
3. **estado-alvo futuro**

Essa separação é obrigatória para evitar que a modelagem:

- trate como implementado o que ainda é apenas planejado
- apague a história real do ShowTrials
- transforme visão futura em narrativa fictícia de entrega concluída

## 3. Base de evidência

Esta frente deve usar como base prioritária:

- código inspecionado diretamente
- histórico Git
- mensagens de commit
- issues GitHub
- documentação técnica e arquitetural já consolidada
- documentos `docs/ai/` como camada de memória operacional e de leitura crítica

Regra de interpretação:

- **código + Git** têm precedência para descrever estado implementado
- **issues** têm precedência para descrever intenção arquitetural futura e backlog ativo
- **documentação** deve ser usada como apoio interpretativo, não como prova suficiente isolada

## 4. Problema que a frente resolve

O projeto já passou por um esforço forte de racionalização arquitetural e documental. No entanto, a nova etapa do TCC exige uma camada adicional de modelagem e análise que ainda não está formalizada.

Sem esta frente, há riscos claros:

- produzir UML e documentação de análise de forma ornamental ou desconectada do projeto real
- modelar diretamente a engine futura sem consolidar requisitos
- perder alinhamento entre arquitetura, governança, backlog e artefatos acadêmicos
- não capturar, com rigor, a diferença entre ShowTrials atual e engine futura

## 5. Entregáveis principais da frente

Os entregáveis desta frente devem ser organizados em blocos.

### 5.1 Fundamentos da frente

- visão geral da frente
- objetivos
- stakeholders
- problema central
- fronteira do sistema

### 5.2 Requisitos

- levantamento inicial de requisitos
- análise de requisitos
- Documento de Requisitos
- requisitos funcionais
- requisitos não funcionais
- restrições
- requisitos de transição arquitetural

### 5.3 Casos de uso

- identificação de atores
- lista de casos de uso
- diagrama de casos de uso
- especificações textuais de casos de uso

### 5.4 Arquitetura

- Visão Arquitetural no modelo 4+1
- Modelo C4
- descrição da transição arquitetural

### 5.5 UML e padrões

- diagrama de classes conceitual
- diagrama de classes de projeto, quando necessário
- diagramas de sequência
- diagramas de atividades
- diagramas de componentes ou pacotes
- documentação dos padrões de projeto escolhidos

### 5.6 Rastreabilidade

- relação entre requisitos, casos de uso, arquitetura e backlog
- apoio à reorganização futura das issues e do roadmap

## 6. Ordem operacional recomendada

A ordem recomendada desta frente é:

1. abrir formalmente a frente
2. definir escopo, limites e entregáveis
3. identificar stakeholders, problema e objetivos
4. levantar requisitos
5. analisar e organizar requisitos
6. produzir o Documento de Requisitos
7. derivar atores e casos de uso
8. produzir diagrama e especificações de casos de uso
9. produzir 4+1
10. produzir C4
11. produzir UML complementar
12. revisar backlog e governança à luz dos artefatos

Essa ordem deve ser preservada sempre que possível, porque:

- requisitos vêm antes da arquitetura futura
- casos de uso vêm antes dos diagramas comportamentais detalhados
- arquitetura e padrões devem surgir como resposta a problemas e requisitos, não como ponto de partida arbitrário

## 7. Estrutura em rodadas

Esta frente deve avançar por rodadas curtas e explícitas.

### Rodada 1

- abertura formal da frente
- escopo
- objetivos
- entregáveis
- limites

### Rodada 2

- stakeholders
- objetivos do sistema
- problema central
- fronteira do sistema

### Rodada 3

- levantamento inicial de requisitos

### Rodada 4

- análise e consolidação dos requisitos
- primeira versão do Documento de Requisitos

### Rodada 5

- atores
- lista de casos de uso
- diagrama de casos de uso

### Rodada 6

- especificações textuais de casos de uso

### Rodada 7

- visão arquitetural 4+1

### Rodada 8

- modelo C4

### Rodada 9

- UML complementar
- padrões de projeto

### Rodada 10

- rastreabilidade com issues, roadmap e governança

## 8. Critérios de qualidade dos artefatos

Cada artefato desta frente deve responder a pelo menos uma destas funções:

- explicar o sistema atual
- justificar a mudança arquitetural
- orientar a implementação futura
- reduzir ambiguidade de backlog
- apoiar apresentação acadêmica

Se um artefato não cumprir nenhuma dessas funções, ele deve ser reconsiderado.

## 9. Estratégia para requisitos

O trabalho de requisitos deve começar por:

- problema
- stakeholders
- capacidades atuais do ShowTrials
- capacidades futuras da engine
- restrições técnicas e acadêmicas

Os requisitos devem ser separados em:

- funcionais
- não funcionais
- restrições
- requisitos de transição arquitetural
- itens fora de escopo

## 10. Estratégia para casos de uso

Os casos de uso devem seguir, preferencialmente, uma abordagem inspirada em Alistair Cockburn:

- foco no objetivo do ator
- valor entregue
- fluxo principal
- extensões
- pré-condições
- pós-condições

Os casos de uso devem cobrir tanto:

- capacidades atuais do sistema
- quanto capacidades futuras da engine

sempre deixando claro o que é estado atual e o que é evolução futura.

## 11. Estratégia para arquitetura

Os artefatos arquiteturais desta frente devem ser produzidos em dois recortes:

- descrição do ShowTrials atual
- descrição da arquitetura-alvo e da transição

O modelo 4+1 deve ser usado para explicar a arquitetura.
O modelo C4 deve ser usado para comunicar estrutura e relações entre níveis.

## 12. Estratégia para padrões de projeto

Os padrões de projeto não devem ser escolhidos por catálogo.

O processo correto é:

1. identificar o problema de desenho
2. identificar a necessidade arquitetural
3. avaliar qual padrão ajuda a resolver esse problema
4. documentar a justificativa da escolha

## 13. Relação com a implementação futura

Esta frente não é execução direta da engine, mas deve orientar a execução futura.

Portanto, o resultado esperado é que, ao final dela, o projeto tenha:

- base de requisitos mais madura
- casos de uso mais claros
- arquitetura futura mais bem justificada
- melhor rastreabilidade entre modelagem e backlog

## 14. Saída mínima esperada

O mínimo aceitável desta frente deve incluir:

- visão da frente
- Documento de Requisitos
- diagrama de casos de uso
- especificações textuais de casos de uso principais
- visão arquitetural 4+1
- modelo C4
- UML complementar das partes críticas
- relação inicial entre requisitos e backlog
