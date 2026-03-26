# Fechamento da Etapa 3 - Classificacao Semantica do Legado

## 1. Objetivo do documento

Este documento registra o fechamento formal da Etapa 3 da frente de saneamento documental legado.

Seu objetivo e:

- confirmar a conclusao da classificacao semantica preliminar de todo o recorte legado
- consolidar os principais padroes identificados
- registrar o que ja se mostra como correcao obrigatoria
- preparar a transicao para a Etapa 4, de arquitetura documental alvo

## 2. Escopo coberto

A Etapa 3 cobriu integralmente os arquivos legados do recorte formal da frente, organizados nos seguintes blocos:

- bloco 01:
  - documentos-raiz de `docs/`
  - `docs/metricas/`
- bloco 02:
  - `docs/flows/`
- bloco 03:
  - `docs/projeto/`
- bloco 04:
  - `docs/fases/FASE1` a `FASE9`
- bloco 05:
  - `docs/fases/FASE10` a `FASE17`

## 3. Resultado principal da etapa

Ao final desta etapa:

- todos os arquivos do recorte legado receberam classificacao semantica preliminar
- nenhum item do inventario permaneceu sem decisao inicial
- os blocos documentais ja exibem padroes semanticos suficientemente claros para orientar a arquitetura documental alvo

## 4. Padroes identificados por bloco

### 4.1 Documentos-raiz e metricas

Padroes predominantes:

- navegacao institucional
- visao geral introdutoria
- documento arquitetural explicativo
- onboarding/contribuicao
- historico de mudancas
- metricas vivas
- diagnosticos tecnicos historicos

Principais riscos:

- desatualizacao factual
- excesso de assertividade arquitetural
- enquadramento insuficiente entre documento vivo e historico

### 4.2 Flows

Padroes predominantes:

- politica
- protocolo normativo
- guia operacional
- guia tecnico/procedimental

Principais riscos:

- confusao entre politica e “flow”
- tensoes internas entre documentos
- residuos de geracao assistida
- acoplamento historico a praticas que mudaram

### 4.3 Projeto

Padroes predominantes:

- politica formal
- visao estrategica
- planejamento historico
- analise arquitetural prospectiva
- direcionamento arquitetural
- instrumento de levantamento/elicitacao

Principais riscos:

- mistura de documentos vivos e historicos
- prospectividade mal enquadrada
- tensao entre gestao antiga e governanca posterior

### 4.4 Fases

Padroes predominantes:

- `FASE1` a `FASE10`:
  - historico de entrega/implementacao relativamente homogeneo
- `FASE11` a `FASE17`:
  - historicos hibridos de intervencao tecnica
  - documentos com tutorial operacional embutido
  - residuos explicitos de geracao assistida em parte relevante do conjunto

Principais riscos:

- inconsistencias de datação e rastreabilidade temporal
- mistura de historico de fase com prescricao operacional
- wrappers, blocos `markdown` literais e outros residuos formais de geracao assistida

## 5. Itens que ja se mostram como correcao obrigatoria

Mesmo antes das etapas seguintes, a classificacao semantica ja mostrou como fortemente candidatos a `corrigir agora`:

- documentos com residuos explicitos de geracao assistida
- documentos com fences ou fechamento formal de Markdown problemáticos
- documentos com estatuto semantico gravemente ambiguo
- documentos com datação ou rastreabilidade inconsistente
- documentos vivos ou institucionais com forte risco de desatualizacao factual
- documentos normativos em tensao direta com politicas posteriores do proprio projeto

Casos especialmente sensiveis incluem:

- `docs/flows/GOVERNANCA.md`
- `docs/flows/emergency_flow.md`
- `docs/projeto/analise_arquitetural.md`
- `docs/projeto/manual_gestao.md`
- `docs/projeto/visao_do_projeto.md`
- `docs/fases/FASE11_CI.md`
- `docs/fases/FASE12.md`
- `docs/fases/FASE13.md`
- `docs/fases/FASE14.md`
- `docs/fases/FASE15.md`
- `docs/fases/FASE16.md`

## 6. O que esta etapa ainda nao fez

Esta etapa nao executou ainda:

- definicao da arquitetura documental alvo
- mapa `origem -> destino`
- decisoes finais de fusao, desmembramento ou realocacao
- saneamento de conteudo
- correcao de Markdown, estilo ou aderencia factual item a item

Esses pontos pertencem as etapas seguintes da frente.

## 7. Consequencia metodologica da etapa

Com a Etapa 3 concluida, o trabalho deixa de ser principalmente exploratorio.

O projeto agora ja possui base suficiente para:

- desenhar a estrutura documental alvo
- decidir a hierarquia semantica entre politica, protocolo, guia, historico, diagnostico e navegacao
- executar o saneamento obrigatorio sem reabrir classificacao desde o zero

## 8. Proximo passo recomendado

Iniciar a Etapa 4 da frente:

- definir a arquitetura documental alvo
- propor a estrutura de diretorios final
- mapear `origem -> destino`
- preparar criterios para consolidacao estrutural posterior
