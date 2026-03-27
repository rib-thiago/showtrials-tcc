# Formalização da Frente de Modelagem, Análise e Padrões no Projeto

## 1. Natureza da frente

Esta frente deve ser tratada como uma frente **documental-arquitetural de análise e modelagem**, com forte impacto futuro sobre a evolução da engine.

Ela não é, neste primeiro momento:

- implementação direta da engine
- refatoração de código de produto
- entrega funcional do backlog técnico principal

Ela é uma frente de:

- análise
- requisitos
- modelagem
- arquitetura
- documentação de apoio à evolução do projeto

## 2. Enquadramento na taxonomia atual

Na taxonomia atual do projeto, o melhor enquadramento inicial para esta frente é:

- `type:docs`

Isso não significa “documentação simples”.
Significa, neste caso:

- documentação estrutural
- modelagem arquitetural
- documentação de requisitos
- apoio formal à governança da evolução da engine

## 3. Relação com a milestone ativa

A milestone aberta no projeto é:

- `MVP - Engine de Pipeline`

Esta nova frente:

- apoia diretamente a evolução da engine
- mas não implementa, por si só, a engine

Por isso, a recomendação inicial desta formalização é:

- abrir a frente **fora da milestone**

Justificativa:

- evitar inflar artificialmente a milestone com entregáveis de modelagem
- preservar a distinção entre análise/modelagem e implementação técnica
- reduzir risco de competição indevida com issues estratégicas da engine

Reavaliação futura:

- se parte desta frente se tornar pré-condição operacional obrigatória para a engine, pode ser válido reavaliar sua relação com a milestone

## 4. Forma recomendada de rastreabilidade

Esta frente deve ser formalizada por:

1. uma issue-mãe da frente
2. issues específicas por bloco de trabalho, quando necessário
3. rodadas documentadas em `docs/planejamento/rodadas/`
4. documentos formais próprios em `docs/modelagem/`

## 5. Issue-mãe recomendada

A issue-mãe desta frente deve:

- definir o escopo
- delimitar entregáveis
- registrar motivação acadêmica e arquitetural
- evitar que a frente pareça um conjunto solto de documentos

Exemplo de escopo da issue-mãe:

- visão da frente
- requisitos
- casos de uso
- 4+1
- C4
- UML complementar
- relação inicial com backlog

## 6. Branches recomendadas

Não se recomenda uma única branch gigante para toda a frente.

O padrão sugerido é:

- uma branch inicial para abrir a frente
- branches específicas para blocos maiores de trabalho

Exemplos:

- `docs/modelagem-analise-projeto`
- `docs/requisitos-engine`
- `docs/casos-de-uso-engine`
- `docs/arquitetura-4mais1`
- `docs/arquitetura-c4`
- `docs/uml-padroes-engine`

## 7. Estrutura documental no repositório

Esta frente deve morar em um espaço próprio, separado de `docs/ai/`.

Estrutura recomendada:

- `docs/modelagem/`

Documentos iniciais recomendados:

- `docs/modelagem/01_estrategia_operacional_da_frente.md`
- `docs/modelagem/02_formalizacao_da_frente_no_projeto.md`

Documentos futuros prováveis:

- `docs/modelagem/03_documento_de_requisitos.md`
- `docs/modelagem/04_casos_de_uso.md`
- `docs/modelagem/05_arquitetura_4mais1.md`
- `docs/modelagem/06_modelo_c4.md`
- `docs/modelagem/07_uml_e_padroes.md`
- `docs/modelagem/diagramas/fontes/`

## 8. Relação com `docs/ai/`

`docs/ai/` deve continuar sendo tratado como:

- memória operacional
- camada de captura de contexto
- base de leitura crítica do estado atual
- apoio para handoff entre sessões com Codex

Já a nova frente de modelagem deve assumir:

- documentação formal de requisitos
- documentação formal de arquitetura
- documentação formal de casos de uso
- artefatos acadêmicos e de projeto

Ou seja:

- `docs/ai/` apoia
- `docs/modelagem/` formaliza a nova frente

## 9. Relação com as rodadas

Cada sessão relevante dessa frente deve continuar gerando documento em:

- `docs/planejamento/rodadas/`

Essa prática é importante porque:

- a frente será longa
- haverá múltiplos artefatos
- a evolução do raciocínio precisa continuar rastreável

## 10. Relação com a governança

Para permanecer aderente à governança do projeto, esta frente deve:

- ter issue própria
- usar branch tipada
- produzir commits atômicos
- não alegar implementação da engine quando ainda estiver em análise/modelagem
- registrar impactos arquiteturais explicitamente
- manter separação entre análise, planejamento e execução

## 11. Relação com PRs já abertos

Como já existem PRs abertos relevantes no projeto, esta frente deve ser introduzida de forma controlada.

Recomendação:

- iniciar com um PR pequeno e claro, abrindo a frente
- evitar abrir múltiplos PRs paralelos de modelagem antes da consolidação inicial

## 12. Padrão de maturação recomendado

Esta frente deve amadurecer em quatro estágios:

### Estágio 1

- issue-mãe
- branch inicial
- visão da frente
- formalização
- primeira rodada

### Estágio 2

- requisitos
- casos de uso

### Estágio 3

- 4+1
- C4

### Estágio 4

- UML complementar
- padrões
- rastreabilidade com backlog e roadmap

## 13. Critério de sucesso desta formalização

Esta frente estará corretamente formalizada quando:

- existir issue própria
- existir branch própria
- existir espaço documental próprio
- a distinção entre contexto operacional e modelagem formal estiver clara
- o trabalho puder avançar sem colidir com a governança da engine

## 14. Decisão inicial recomendada

Com base no estado atual do projeto, a decisão inicial mais aderente é:

- abrir a frente como `type:docs`
- iniciar fora da milestone `MVP - Engine de Pipeline`
- usar `docs/modelagem/` como espaço próprio
- começar por uma branch documental inicial curta
- só depois abrir subfrentes de requisitos, casos de uso e arquitetura
