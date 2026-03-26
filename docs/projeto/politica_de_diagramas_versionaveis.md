# Politica de Diagramas Versionaveis

## 1. Objetivo

Este documento define a politica do projeto para **diagramas versionaveis**, com foco em:

- legibilidade humana
- fonte versionada em codigo sempre que possivel
- escolha disciplinada de ferramenta
- organizacao coerente dos artefatos no repositorio

Seu objetivo nao e impor formalismo maximo em todos os casos, mas garantir que novos diagramas sejam produzidos com criterio, rastreabilidade e utilidade real.

## 2. Principios

Os diagramas do projeto devem seguir os principios abaixo:

- a fonte do diagrama deve ser mantida no repositorio sempre que possivel
- leitura humana tem prioridade pratica
- a ferramenta deve ser escolhida conforme o tipo de diagrama e o objetivo do artefato
- documentos textuais de apoio ou especificacao podem coexistir com diagramas sem serem confundidos com eles
- diagramas nao devem ser produzidos apenas como ornamentacao documental

## 3. Ferramentas adotadas

### 3.1 Padrao default

O projeto adota **Mermaid** como ferramenta default para diagramas versionaveis.

### 3.2 Excecao para UML formal

O projeto adota **PlantUML** como excecao preferencial quando houver necessidade de UML mais formal e Mermaid nao sustentar bem o caso.

## 4. Criterios de uso por tipo de diagrama

### 4.1 Usar Mermaid preferencialmente para

- fluxos
- processos
- diagramas explicativos
- visoes em que a renderizacao nativa no GitHub traga ganho relevante de leitura

### 4.2 Usar PlantUML preferencialmente para

- casos de uso
- diagramas de classes
- diagramas de sequencia
- diagramas de atividades
- diagramas de estados
- cenarios em que a precisao UML seja mais importante que a renderizacao nativa no GitHub

## 5. Organizacao dos artefatos no repositorio

Na frente de modelagem, os diagramas passam a obedecer a organizacao abaixo:

- `docs/modelagem/diagramas/fontes/`
- `docs/modelagem/diagramas/especificacoes/`

### 5.1 Fontes

Devem ficar em `docs/modelagem/diagramas/fontes/`:

- arquivos `.mmd`
- arquivos `.puml`
- outros arquivos-fonte equivalentes adotados pelo projeto

### 5.2 Especificacoes

Devem ficar em `docs/modelagem/diagramas/especificacoes/`:

- documentos de recorte
- documentos de leitura
- especificacoes textuais preparatorias de diagramas
- artefatos que explicam o objetivo e o escopo de um diagrama ainda nao materializado

## 6. Artefatos derivados

O projeto pode versionar artefatos derivados, como `SVG`, quando houver ganho real de leitura humana.

Nesse caso:

- o artefato derivado nao substitui a fonte
- a fonte continua sendo a referencia principal
- o derivado e opcional, e nao obrigatorio

## 7. Regra para o bloco UML complementar atual

Na situacao atual da frente de modelagem:

- os artefatos `32-39` permanecem classificados como especificacoes textuais preparatorias de diagramas
- esta politica nao implica materializacao imediata desses diagramas
- a decisao sobre materializacao futura deve ocorrer apenas em etapa propria do plano de estabilizacao

## 8. Regra para novos diagramas

Antes de criar um novo diagrama, deve-se:

1. confirmar a necessidade do diagrama
2. definir claramente seu objetivo
3. escolher a ferramenta segundo esta politica
4. registrar a fonte no diretorio adequado
5. evitar duplicacao desnecessaria com documentacao textual ja suficiente

## 9. Relacao com a governanca do projeto

Esta politica existe para:

- melhorar a consistencia entre os diagramas do projeto
- evitar escolha ad hoc de ferramenta a cada novo artefato
- preservar a rastreabilidade entre fonte, especificacao e leitura humana
- reduzir o risco de diagramas bonitos, mas pouco uteis

## 10. Proximo uso esperado

Esta politica deve orientar:

- a eventual materializacao futura do bloco UML complementar
- a producao de novos diagramas em frentes de arquitetura, implementacao e revisao
- a manutencao dos diagramas ja existentes no repositorio
