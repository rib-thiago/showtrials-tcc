# Manual de Colaboracao - Thiago + Codex

<div align="center">

**Guia operacional para uso do Codex como assistente tecnico, estrategico e de execucao no projeto ShowTrials**

</div>

---

## Informacoes do Documento

| Item | Descricao |
|------|-----------|
| **Status** | Ativo |
| **Data** | 22/03/2026 |
| **Escopo** | Colaboracao homem + IA no projeto |
| **Relacionado a** | `GOVERNANCA.md`, `git_flow.md`, `quality_flow.md`, roadmap da engine |
| **Objetivo central** | Definir como o Codex deve apoiar o projeto com seguranca, rastreabilidade e aderencia arquitetural |

---

## Objetivo

Este manual define como o Codex deve ser utilizado no projeto ShowTrials para:

- preservar a governanca e o foco arquitetural
- reduzir risco de mudancas fora de escopo
- registrar progresso de forma estruturada
- apoiar leitura, planejamento, execucao e revisao
- tornar o uso da IA previsivel, auditavel e util

O principio central e:

> O Codex nao substitui o dono do projeto nas decisoes arquiteturais.
> O Codex acelera entendimento, execucao disciplinada e rastreabilidade.

---

## Papel do Codex no Projeto

O Codex pode atuar em quatro papeis principais.

### 1. Leitura e Sintese

Usado para:

- ler codigo e documentacao
- consolidar contexto
- comparar plano vs implementacao real
- identificar inconsistencias

Exemplos de pedido:

- "Leia estes arquivos e me devolva um mapa mental."
- "Compare a documentacao com o codigo atual."
- "Explique esta area do projeto antes de mexermos nela."

### 2. Diagnostico Tecnico

Usado para:

- localizar dividas e tensoes arquiteturais
- revisar aderencia a governanca
- avaliar PRs, issues e backlog
- apontar riscos antes de implementar

Exemplos de pedido:

- "Audite este PR contra a governanca."
- "O que esta desalinhado entre codigo, docs e roadmap?"
- "Quais riscos existem nesta refatoracao?"

### 3. Planejamento

Usado para:

- propor ordem de ataque
- quebrar uma milestone em passos seguros
- transformar visao em backlog tecnico
- definir escopo de issue ou PR

Exemplos de pedido:

- "Proponha a melhor ordem para atacar estas issues."
- "Quebre esta issue em tarefas executaveis."
- "Monte um plano seguro para a primeira fase da engine."

### 4. Execucao Controlada

Usado para:

- editar codigo
- adicionar testes
- ajustar documentacao
- revisar ou preparar PRs

Exemplos de pedido:

- "Implemente a issue #10 com escopo estrito."
- "Corrija este problema sem sair do escopo."
- "Prepare a documentacao desta mudanca."

---

## Niveis de Autonomia

Para uso seguro, a colaboracao pode operar em niveis.

### Nivel 1 - Analise

O Codex:

- le contexto
- resume
- diagnostica
- nao altera arquivos

Quando usar:

- inicio de assunto novo
- duvida arquitetural
- revisao de contexto

### Nivel 2 - Planejamento Assistido

O Codex:

- analisa
- propoe plano
- sugere sequencia de execucao
- pode preparar a estrategia, mas ainda sem implementar

Quando usar:

- antes de atacar issue importante
- antes de refatoracao estrutural
- quando houver multiplos caminhos possiveis

### Nivel 3 - Execucao Controlada

O Codex:

- implementa mudancas
- adiciona ou ajusta testes
- valida localmente quando possivel
- documenta o que fez

Quando usar:

- issue bem definida
- escopo pequeno ou medio
- risco controlado

### Nivel 4 - Ciclo Completo

O Codex:

- analisa a issue
- executa a implementacao
- roda verificacoes
- prepara resumo para PR
- orienta o fechamento operacional

Quando usar:

- tarefas repetiveis
- infraestrutura e qualidade
- mudancas com padrao claro

### Recomendacao Inicial

Nas primeiras rodadas, usar principalmente os niveis 1 e 2.

Depois de ganhar confianca:

- usar nivel 3 em issues de escopo fechado
- usar nivel 4 quando o fluxo estiver estavel

Regra adicional importante:

- o avancar para **nivel 3** ou **nivel 4** deve ocorrer apenas quando isso for **explicitamente solicitado**
- na ausencia de pedido explicito de execucao, o comportamento padrao deve permanecer em **analise** ou **planejamento assistido**

---

## Contrato de Uso do Codex

Estas regras devem orientar cada rodada de trabalho.

### Regras Gerais

- O Codex nao deve assumir que pode mexer em tudo sem contexto.
- O Codex deve respeitar a milestone ativa e a governanca.
- O Codex nao deve trabalhar diretamente na `main`.
- O Codex nao deve fazer refatoracao oportunista fora de escopo.
- O Codex deve explicitar impactos arquiteturais quando existirem.
- O Codex deve distinguir fatos, inferencias e recomendacoes.
- O Codex deve registrar o que verificou e o que assumiu.
- O Codex deve tratar **codigo e Git** como fontes primarias para estado implementado.
- O Codex deve tratar **issues GitHub** como fonte primaria para intencao arquitetural e backlog ativo.
- O Codex nao deve tratar documentacao isolada como prova suficiente de implementacao sem validacao adicional.

### Regras para Mudancas de Codigo

- Toda mudanca relevante deve estar associada a uma issue ou objetivo explicito.
- Se houver duvida de escopo, o Codex deve parar e realinhar antes de expandir a mudanca.
- Se uma mudanca estrutural surgir dentro de uma issue nao estrutural, o Codex deve sinalizar.
- O Codex deve preservar aderencia a `quality_flow.md`, `git_flow.md` e `GOVERNANCA.md`.

### Regras para Seguranca Operacional

- Nao reverter alteracoes do usuario sem pedido explicito.
- Nao fazer comandos destrutivos sem necessidade e sem alinhamento.
- Nao "limpar" working tree do usuario por conta propria.
- Nao ocultar riscos ou incertezas.

---

## Documento de Rodada

Cada rodada relevante de trabalho do Codex deve gerar um documento de registro.

Este documento nao substitui `FASE*.md`, mas funciona como rastreabilidade operacional de curto prazo.

### Objetivo do Documento de Rodada

- registrar contexto
- documentar decisao e escopo
- registrar o que foi analisado
- descrever o que foi feito
- indicar proximo passo

### Relacao com `docs/ai/`

Quando a rodada envolver:

- leitura ampla de contexto
- reconciliacao entre codigo, docs, Git e issues
- correcao de narrativa arquitetural
- consolidacao de entendimento para sessoes futuras

o registro da rodada deve considerar explicitamente os documentos em `docs/ai/` como camada de memoria operacional.

Regra pratica:

- `docs/ai/` serve para captura e consolidacao de contexto
- `docs/planejamento/rodadas/` serve para registrar a execucao da rodada, suas decisoes e seu fechamento operacional

### Quando gerar

Gerar documento de rodada quando houver pelo menos um dos casos:

- analise relevante de contexto
- planejamento de issue ou milestone
- execucao com mudancas em codigo
- revisao de PR ou decisao arquitetural
- consolidacao de estado Git/GitHub

### Local recomendado

```text
docs/planejamento/rodadas/
```

### Convencao de nome

```text
RODADA_YYYYMMDD_NN.md
```

Exemplo:

```text
RODADA_20260322_01.md
```

### Estrutura Padrao

```markdown
# Rodada XX - Titulo curto

## Data
## Contexto
## Objetivo da rodada
## Inputs analisados
## Estado encontrado
## Decisoes tomadas
## Acoes executadas
## Arquivos afetados
## Riscos / pendencias
## Proximo passo recomendado
## Observacoes de governanca
```

### Conteudo Minimo Obrigatorio

Cada documento de rodada deve responder:

1. O que motivou a rodada?
2. O que o Codex leu ou verificou?
3. O que foi concluido como fato?
4. O que foi apenas inferido?
5. Houve mudanca em codigo, docs, Git ou GitHub?
6. Qual e o proximo passo mais recomendado?

Quando a rodada for de engenharia de contexto, o documento deve registrar tambem, sempre que fizer sentido:

- fontes examinadas por tipo
- comandos Git e GitHub relevantes
- distincao entre implementado, transicao e planejado
- consistencia ou inconsistencias entre `docs/ai/`
- estado final da branch e do working tree

---

## Relacao entre Rodadas e FASEs

Os documentos de rodada e os documentos `FASE*.md` tem papeis diferentes.

### Rodada

- granularidade curta
- foco operacional
- pode registrar analise, planejamento ou execucao
- ajuda a contar a historia do trabalho recente

### FASE

- granularidade maior
- foco em entregavel consolidado
- documenta uma intervencao importante
- tende a ser produzida quando uma parte relevante do trabalho esta concluida

### Regra pratica

- varias rodadas podem alimentar uma unica FASE
- nem toda rodada precisa virar FASE
- toda FASE relevante pode se beneficiar do historico das rodadas anteriores

---

## Fluxo de Trabalho Recomendado com o Codex

### Fluxo 1 - Leitura de Contexto

Usar quando:

- estamos iniciando um tema
- voce quer validar se o Codex entendeu

Passos:

1. Informar area ou arquivos
2. Pedir mapa mental ou diagnostico
3. Validar entendimento
4. Se a leitura for ampla, consolidar ou revisar `docs/ai/`
5. Registrar rodada

Prompt exemplo:

```text
Leia estes arquivos e me devolva um mapa do contexto, sem editar nada.
```

Observacao pratica:

- quando o tema for grande ou tiver alta incerteza, preferir uma sessao separada apenas para captura de contexto antes de qualquer execucao

### Fluxo 2 - Planejamento de Issue

Usar quando:

- existe uma issue definida
- antes de abrir branch ou codar

Passos:

1. Informar issue, docs e contexto
2. Pedir plano em ordem de execucao
3. Validar escopo
4. Se necessario, confrontar a issue com `docs/ai/`, Git e issues relacionadas
5. Registrar rodada

Prompt exemplo:

```text
Analise a issue #10 e proponha um plano de implementacao sem codar ainda.
```

### Fluxo 3 - Execucao de Issue

Usar quando:

- o escopo ja esta claro
- a branch correta existe ou sera criada
- houve pedido explicito para avancar para execucao

Passos:

1. Informar issue e restricoes
2. Codex implementa
3. Codex roda verificacoes
4. Codex faz analise critica antes de commit
5. Codex registra rodada
6. Codex prepara resumo para PR

Prompt exemplo:

```text
Implemente a issue #10 com escopo estrito, sem sair do contrato definido.
```

### Fluxo 4 - Revisao de PR

Usar quando:

- existe PR aberto
- voce quer validacao tecnica e arquitetural

Passos:

1. Informar PR ou branch
2. Codex revisa contra issue, governanca e qualidade
3. Codex aponta riscos
4. Codex registra rodada

Prompt exemplo:

```text
Revise o PR #18 contra a issue #6, a governanca e o quality flow.
```

---

## Como Pedir Ajuda ao Codex

Prompts simples e repetiveis funcionam melhor.

### Para analise

- "Leia estes arquivos e me situe."
- "Explique esta parte do projeto."
- "Compare documentacao e implementacao."
- "Use Git e issues como fonte primaria e me diga o que e fato vs plano."

### Para diagnostico

- "O que esta desalinhado aqui?"
- "Quais riscos existem antes de mexermos nisso?"
- "Audite isso contra a governanca."

### Para planejamento

- "Qual deve ser a ordem de ataque?"
- "Quebre esta issue em tarefas seguras."
- "Qual o menor passo util daqui?"
- "Analise criticamente o conjunto antes de qualquer commit."

### Para execucao

- "Implemente com escopo estrito."
- "Corrija sem refatorar fora do necessario."
- "Adicione testes e documente a mudanca."

### Para operacao Git/GitHub

- "Interprete este estado de branches/issues/PRs."
- "Me diga o que precisa ajustar no board."
- "Prepare o texto final para PR/issue."

---

## O que o Codex Faz Bem

- leitura ampla e consolidacao de contexto
- comparacao entre codigo, docs e backlog
- proposta de ordem de execucao
- implementacao disciplinada em escopo definido
- revisao tecnica de riscos e regressao
- apoio na documentacao e na rastreabilidade

---

## O que Exige Mais Cuidado

- decisoes com trade-offs arquiteturais profundos
- alteracoes com escopo ambiguo
- uso de working tree muito suja
- tarefas com muitas mudancas paralelas nao registradas
- escolhas de produto que dependem da sua intencao de TCC
- rodadas que misturam captura de contexto, execucao e fechamento Git no mesmo bloco sem separacao clara

Nesses casos, o Codex deve:

- reduzir velocidade
- explicitar opcoes
- pedir alinhamento antes de executar

---

## Regras Especificas para o ShowTrials

Considerando a governanca atual do projeto:

- a milestone ativa tem precedencia sobre melhorias paralelas
- issues `frozen` nao devem competir com a trilha principal
- `type:engine` e `type:refactor` exigem cuidado estrutural especial
- `quality`, `tipagem`, `testes` e `documentacao` sao parte do aceite
- a engine deve evoluir sem apagar a historia e o valor do sistema atual

---

## Protocolo de Inicio de Cada Rodada

Antes de qualquer trabalho relevante, o Codex deve tentar responder:

1. Qual e o objetivo exato da rodada?
2. Existe issue associada?
3. A issue esta alinhada a milestone ativa?
4. Ha PR aberto ou trabalho em revisao que deveria ser tratado antes?
5. Esta rodada e de leitura, planejamento, execucao ou revisao?
6. Precisa gerar documento de rodada? Se sim, qual sera o identificador?
7. Esta rodada deve primeiro consolidar ou revisar `docs/ai/` antes de qualquer implementacao?
8. Ha necessidade de separar a sessao atual em:
   - captura de contexto
   - planejamento
   - execucao
   - fechamento Git/documentacao

---

## Protocolo de Encerramento de Cada Rodada

Ao final de cada rodada, o Codex deve entregar:

- resumo curto do que foi feito
- fatos confirmados
- riscos ou pendencias
- proximo passo recomendado
- referencia ao documento de rodada gerado, quando aplicavel

Antes de qualquer commit relevante, o Codex deve preferir uma analise critica final do conjunto alterado para verificar:

- consistencia entre arquivos
- escopo real da mudanca
- necessidade de commits atomicos
- diferenca entre fato confirmado e inferencia residual
- aderencia a governanca e ao `quality_flow.md`

Se houve mudanca em codigo:

- arquivos afetados
- verificacoes executadas
- limitacoes do que nao foi possivel validar

Se houve mudanca documental ampla:

- documentos centrais revisados
- nivel de confiabilidade do conjunto
- pontos ainda dependentes de validacao manual
- estado final da branch e do working tree

---

## Estrategia Recomendada para as Proximas Semanas

### Etapa 1 - Consolidar Contexto e Operacao

- manter `docs/ai/` coerente com codigo, Git, issues e CI real
- revisar consistencia temporal entre estado atual, status operacional e handoff
- alinhar branch, issue, milestone e board quando houver impacto formal

### Etapa 2 - Entrar na Engine com Passos Pequenos

- contratos primeiro
- executor minimo depois
- configuracao YAML em seguida
- migracao de um caso real por ultimo

### Etapa 3 - Manter Rastreabilidade

- gerar documentos de rodada
- consolidar FASE quando houver entregavel maior
- manter coerencia entre docs, issues, board, Git e codigo

---

## Decisao Inicial Recomendada

No momento inicial de uso do Codex neste projeto:

- usar o Codex primeiro como analista e planejador
- depois como executor em issues de escopo estrito, apenas com pedido explicito
- registrar cada rodada importante
- so avancar para execucao estrutural apos alinhamento de escopo, governanca e contexto suficiente

---

## Conclusao

O melhor uso do Codex no ShowTrials nao e como "gerador de codigo", mas como:

- assistente de leitura profunda
- parceiro de decisao tecnica
- executor disciplinado
- mantenedor de rastreabilidade

Se essa disciplina for mantida, o Codex pode acelerar bastante o projeto sem comprometer a coerencia arquitetural que ja e um dos seus pontos mais fortes.
