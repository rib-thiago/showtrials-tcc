# Politica de Diagramas Versionaveis

## Objetivo

Esta politica define como o projeto trata diagramas versionaveis, com foco em:

- legibilidade humana;
- fonte versionada no repositorio sempre que possivel;
- escolha disciplinada de ferramenta;
- organizacao coerente dos artefatos.

Seu objetivo nao e impor formalismo maximo em todos os casos, mas garantir que novos diagramas sejam produzidos com criterio, rastreabilidade e utilidade real.

## Principios

Os diagramas do projeto devem seguir os principios abaixo:

- a fonte do diagrama deve ser mantida no repositorio sempre que possivel;
- leitura humana tem prioridade pratica;
- a ferramenta deve ser escolhida conforme o tipo de diagrama e o objetivo do artefato;
- documentos textuais de apoio ou especificacao podem coexistir com diagramas sem serem confundidos com eles;
- diagramas nao devem ser produzidos apenas como ornamentacao documental.

## Ferramentas Adotadas

### Padrao default

O projeto adota **Mermaid** como ferramenta default para diagramas versionaveis.

### Excecao para UML formal

O projeto adota **PlantUML** como excecao preferencial quando houver necessidade de UML mais formal e Mermaid nao sustentar bem o caso.

## Criterios de Uso

### Usar Mermaid preferencialmente para

- fluxos;
- processos;
- diagramas explicativos;
- visoes em que a renderizacao nativa no GitHub traga ganho relevante de leitura.

### Usar PlantUML preferencialmente para

- casos de uso;
- diagramas de classes;
- diagramas de sequencia;
- diagramas de atividades;
- diagramas de estados;
- cenarios em que a precisao UML seja mais importante que a renderizacao nativa no GitHub.

## Organizacao dos Artefatos

Os diagramas versionaveis do bloco de modelagem obedecem a organizacao abaixo:

- `docs/modelagem/diagramas/fontes/`
- `docs/modelagem/diagramas/especificacoes/`
- `docs/modelagem/diagramas/renderizados/`

### Fontes

Devem ficar em `docs/modelagem/diagramas/fontes/`:

- arquivos `.mmd`;
- arquivos `.puml`;
- outros arquivos-fonte equivalentes adotados pelo projeto.

### Especificacoes

Devem ficar em `docs/modelagem/diagramas/especificacoes/`:

- documentos de recorte;
- documentos de leitura;
- especificacoes textuais preparatorias de diagramas;
- artefatos que explicam o objetivo e o escopo de um diagrama ainda nao materializado.

### Renderizados

Devem ficar em `docs/modelagem/diagramas/renderizados/`:

- artefatos derivados de leitura humana, como `SVG`;
- versoes exportadas destinadas a facilitar consulta no GitHub ou em documentacao navegavel.

## Artefatos Derivados

O projeto pode versionar artefatos derivados, como `SVG`, quando houver ganho real de leitura humana.

Nesse caso:

- o artefato derivado nao substitui a fonte;
- a fonte continua sendo a referencia principal;
- o derivado e opcional, e nao obrigatorio.

## Regras para o Bloco Atual

Na situacao atual da frente de modelagem:

- os artefatos `32-39` permanecem classificados como especificacoes textuais preparatorias de diagramas;
- esta politica nao implica materializacao imediata desses diagramas;
- a decisao sobre materializacao futura deve ocorrer apenas em etapa propria do plano de estabilizacao.

## Regra para Novos Diagramas

Antes de criar um novo diagrama, deve-se:

1. confirmar a necessidade do diagrama;
2. definir claramente seu objetivo;
3. escolher a ferramenta segundo esta politica;
4. registrar a fonte no diretorio adequado;
5. evitar duplicacao desnecessaria com documentacao textual ja suficiente.

## Relacao com a Governanca do Projeto

Esta politica existe para:

- melhorar a consistencia entre os diagramas do projeto;
- evitar escolha ad hoc de ferramenta a cada novo artefato;
- preservar a rastreabilidade entre fonte, especificacao e leitura humana;
- reduzir o risco de diagramas bonitos, mas pouco uteis.
