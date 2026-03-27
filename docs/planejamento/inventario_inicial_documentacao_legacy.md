# Inventario Inicial da Documentacao Legada

## 1. Objetivo do documento

Este documento registra o inventario inicial da documentacao Markdown legada abrangida pela frente de saneamento documental.

Seu objetivo e:

- consolidar o recorte auditavel do legado
- registrar a cronologia basica observada no Git
- classificar preliminarmente os grupos documentais
- apontar achados iniciais de saneamento obrigatorio
- servir de base para a etapa seguinte de classificacao semantica por arquivo

Este inventario inicial nao encerra a analise semantica da frente.

Ele registra uma primeira consolidacao do universo legado a partir de leitura dirigida por amostragem, realizada apenas para construir a base auditavel da etapa seguinte.

A classificacao semantica definitiva desta frente devera cobrir todos os arquivos do recorte legado, arquivo a arquivo, ainda que a execucao ocorra em blocos operacionais.

## 2. Recorte formal utilizado

Para esta etapa, foi considerado como documentacao legada o conjunto de arquivos Markdown:

- produzidos antes do inicio das frentes `docs/ai/` e `docs/modelagem/`
- atualmente localizados principalmente em:
  - `docs/`
  - `docs/fases/`
  - `docs/flows/`
  - `docs/projeto/`
  - `docs/metricas/`
  - `docs/planejamento/`, apenas quando diretamente relacionados a revisao documental legada

Foram excluidos do inventario direto desta etapa:

- `docs/modelagem/`
- `docs/ai/`
- `docs/planejamento/rodadas/`, exceto como apoio metodologico e historico

## 3. Base de evidencia utilizada

Este inventario inicial foi construído a partir de:

- historico Git de `docs/` em ordem cronologica
- listagem atual de arquivos Markdown em `docs/`
- leitura inicial de documentos-raiz
- leitura dirigida de amostras representativas dos grupos `fases`, `flows`, `projeto` e `metricas`
- confronto metodologico com o branch `docs/ai-context-bootstrap`

Observacao metodologica:

- a amostragem usada nesta etapa teve funcao exploratoria e inventariante
- ela nao substitui a revisao semantica integral que sera realizada na Etapa 3

## 4. Cronologia basica do legado

Pelo historico Git, o nucleo principal da documentacao legada foi produzido nesta sequencia macro:

- `2026-02-15`:
  - abertura das `FASE1` a `FASE7`
- `2026-02-16`:
  - abertura das `FASE8` e `FASE9`
- `2026-02-18`:
  - criacao de `ARCHITECTURE.md`
  - atualizacao de fases anteriores
  - abertura de `index.md`, `overview.md`, `contributing.md` e `changelog.md`
- `2026-02-20`:
  - abertura inicial de documentos de projeto
  - abertura inicial de `flows/`
  - abertura de planejamento ligado a revisao documental
- `2026-02-21`:
  - reorganizacao fisica em `docs/fases/` e `docs/metricas/`
  - criacao de `TEMPLATE_FASE.md`
  - separacao de diagnosticos em `metricas/`
- `2026-02-22`:
  - abertura de `FASE17_PRIMEIRA_REORGANIZACAO_DOCUMENTAL_AMPLA.md`
  - consolidacao adicional de governanca e fluxos

Conclusao preliminar:

- o legado nao e um bloco homogeneo
- ele combina documentos historicos de entrega, guias operacionais, material estrategico/prospectivo, diagnosticos tecnicos e navegacao institucional

## 5. Grupos documentais inventariados

### 5.1 Documentos-raiz de `docs/`

Arquivos principais observados:

- `docs/index.md`
- `docs/overview.md`
- `docs/ARCHITECTURE.md`
- `docs/contributing.md`
- `docs/changelog.md`

**Estatuto preliminar**

- navegacao institucional
- apresentacao do projeto
- referencia introdutoria

**Observacoes iniciais**

- parecem concentrar narrativa de entrada no projeto
- alguns dados e estatisticas podem estar desatualizados
- ha indicios de excesso de assertividade arquitetural frente ao padrao mais conservador consolidado depois

### 5.2 Bloco `docs/fases/`

Arquivos observados:

- `FASE01_FUNDACAO_DA_CAMADA_DE_DOMINIO.md` a `FASE17_PRIMEIRA_REORGANIZACAO_DOCUMENTAL_AMPLA.md`

**Estatuto preliminar**

- documentacao historica de entregas e intervencoes

**Observacoes iniciais**

- o grupo nao parece ser documentacao normativa viva
- ha mistura entre registro de fase, tutorial operacional, reproducoes extensas de codigo e rastros de execucao
- parte do valor do grupo parece historico e rastreavel, nao necessariamente como referencia principal de estado atual

### 5.3 Bloco `docs/flows/`

Arquivos observados:

- `GOVERNANCA.md`
- `git_flow.md`
- `quality_flow.md`
- `code_review_flow.md`
- `debug_flow.md`
- `dependencies_flow.md`
- `documentation_flow.md`
- `emergency_flow.md`
- `refactoring_flow.md`
- `telemetry_flow.md`
- `fluxo_projects_github_cli.md`

**Estatuto preliminar**

- mistura de politica, governanca operacional e protocolos/flows de trabalho

**Observacoes iniciais**

- `GOVERNANCA.md`, `git_flow.md` e `quality_flow.md` parecem mais proximos de politica ou protocolo normativo do que de “flow” leve
- ha forte possibilidade de reclassificacao semantica interna deste bloco
- ja foi identificado residuo explicito de geracao assistida em `GOVERNANCA.md`

### 5.4 Bloco `docs/projeto/`

Arquivos observados:

- `analise_arquitetural.md`
- `direcionamento_arquitetural_engine_mvp.md`
- `manual_gestao.md`
- `plano_issues_documentacao.md`
- `politica_de_diagramas_versionaveis.md`
- `questionario_levantamento_requisitos.md`
- `roadmap_arquitetural.md`
- `visao_do_projeto.md`

**Estatuto preliminar**

- mistura de visao estrategica, analise arquitetural, governanca, planejamento e politica

**Observacoes iniciais**

- este grupo parece ser o mais heterogeneo semanticamente
- alguns documentos sao fortemente prospectivos
- alguns documentos carregam sinais de rascunho, conversa ou geracao assistida
- a relacao entre documentos vivos, documentos historicos de concepcao e documentos normativos ainda precisa ser refinada

### 5.5 Bloco `docs/metricas/`

Arquivos observados:

- `cobertura.md`
- `diagnostico_ci.md`
- `diagnostico_fase12.md`

**Estatuto preliminar**

- diagnostico tecnico e acompanhamento historico

**Observacoes iniciais**

- o grupo parece semanticamente mais coeso do que `flows/` e `projeto/`
- ainda assim, ha risco de desatualizacao factual e problemas formais de fechamento de Markdown

### 5.6 Bloco `docs/planejamento/` relacionado ao legado

Arquivos observados:

- `plano_issue2_revisao_documentacao.md`
- `TEMPLATE_FASE.md`

**Estatuto preliminar**

- artefatos de planejamento e padronizacao historica

**Observacoes iniciais**

- `plano_issue2_revisao_documentacao.md` parece importante como rastreabilidade da tentativa anterior de organizar a documentacao
- `TEMPLATE_FASE.md` pode influenciar a decisao sobre preservar, padronizar ou rebaixar o bloco `fases/`

## 6. Achados iniciais de saneamento obrigatorio

Os itens abaixo ja podem ser classificados, desde esta etapa, como candidatos fortes a `corrigir agora`:

- residuos explicitos de geracao assistida em `docs/flows/GOVERNANCA.md`
- tom conversacional inadequado para documento consolidado em `docs/projeto/analise_arquitetural.md`
- sinais de rascunho/prospectividade nao suficientemente enquadrados em `docs/projeto/visao_do_projeto.md`
- possivel tensao normativa entre `docs/projeto/manual_gestao.md` e `docs/flows/GOVERNANCA.md`
- fences e fechamento formal problematico em:
  - `docs/fases/FASE11_ESTABILIZACAO_INICIAL_DO_CI.md`
  - `docs/metricas/diagnostico_ci.md`
  - `docs/metricas/cobertura.md`
- possivel desatualizacao factual em documentos-raiz como `docs/index.md` e `docs/overview.md`

## 7. Hipoteses de classificacao semantica para a etapa seguinte

Para a Etapa 3, as hipoteses iniciais de classificacao sao:

- `docs/fases/`:
  - historico de entregas/intervencoes
- `docs/flows/`:
  - subconjunto de politicas/protocolos normativos
  - subconjunto de guias operacionais
- `docs/projeto/`:
  - subconjunto de visao/estrategia
  - subconjunto de planejamento
  - subconjunto de politica/governanca
  - subconjunto de analise historica ou prospectiva
- `docs/metricas/`:
  - diagnostico e acompanhamento tecnico
- `docs/` raiz:
  - navegacao institucional e documentos de entrada

Essas hipoteses ainda precisam ser refinadas por arquivo, mas ja sao suficientes para orientar a etapa seguinte.

## 8. Limites deste inventario inicial

Este documento ainda nao entrega:

- classificacao semantica individual por arquivo
- decisao de estrutura documental alvo
- proposta final de fusao, desmembramento ou movimentacao
- verificacao exaustiva de aderencia factual item a item contra `src/`

Esses pontos pertencem as etapas seguintes da frente.

## 9. Proximo passo recomendado

Executar a Etapa 3 da frente:

- classificar semanticamente cada arquivo legado do recorte, sem excecao
- distinguir o que e politica, flow, historico, diagnostico, planejamento, contexto ou navegacao
- organizar essa classificacao em blocos operacionais para manter controle de execucao e commits atomicos
- preparar a futura arquitetura documental alvo com base nessa classificacao
