# Classificacao Semantica do Legado - Bloco 03

## 1. Objetivo do documento

Este documento registra a classificacao semantica preliminar do terceiro bloco da documentacao legada revisada na Etapa 3 da frente de saneamento documental.

Este bloco cobre todos os arquivos de `docs/projeto/`.

Seu objetivo e:

- registrar decisao preliminar por arquivo
- distinguir politica, visao estrategica, planejamento historico, analise prospectiva e insumo de levantamento
- apontar problemas semanticos, formais e de aderencia
- preparar a etapa futura de reorganizacao estrutural

## 2. Escopo do bloco

Arquivos cobertos neste bloco:

- `docs/projeto/analise_arquitetural.md`
- `docs/projeto/direcionamento_arquitetural_engine_mvp.md`
- `docs/projeto/manual_gestao.md`
- `docs/projeto/plano_issues_documentacao.md`
- `docs/projeto/politica_de_diagramas_versionaveis.md`
- `docs/projeto/questionario_levantamento_requisitos.md`
- `docs/projeto/roadmap_arquitetural.md`
- `docs/projeto/visao_do_projeto.md`

Todos os arquivos do bloco receberam classificacao semantica preliminar nesta etapa.

## 3. Classificacao por arquivo

### 3.1 `docs/projeto/analise_arquitetural.md`

**Estatuto preliminar**

- analise arquitetural prospectiva
- artefato de reflexao estrategica

**Problemas identificados**

- tom conversacional inadequado para documento consolidado
- mistura de analise com dialogo retorico
- alto grau de prospectividade ainda pouco enquadrada

**Encaminhamento inicial**

- manter no conjunto documental
- rebaixar semanticamente a analise prospectiva/historica, nao tratar como norma viva
- candidato forte a correcao obrigatoria

### 3.2 `docs/projeto/direcionamento_arquitetural_engine_mvp.md`

**Estatuto preliminar**

- direcionamento arquitetural
- documento de decisao/projecao para MVP da engine

**Problemas identificados**

- conteudo fortemente prospectivo
- formulacoes categoricas sobre estado arquitetural alvo podem exigir enquadramento temporal mais explicito
- precisa ser lido em relacao com a modelagem posterior, que amadureceu parte desse tema

**Encaminhamento inicial**

- manter no conjunto documental
- tratar como direcionamento arquitetural historico/prospectivo
- candidato a saneamento semantico e reposicionamento

### 3.3 `docs/projeto/manual_gestao.md`

**Estatuto preliminar**

- guia de gestao operacional

**Problemas identificados**

- tensao com a governanca posterior consolidada
- uso de milestones temporais e praticas que conflitam com `GOVERNANCA.md`
- documento muito operacional, com risco de parcial obsolescencia

**Encaminhamento inicial**

- manter no conjunto documental
- tratar como guia de gestao historicamente contextualizado, sujeito a revisao forte
- candidato forte a correcao obrigatoria

### 3.4 `docs/projeto/plano_issues_documentacao.md`

**Estatuto preliminar**

- planejamento historico de issues e milestones

**Problemas identificados**

- forte dependencia de milestones temporais
- mistura de planejamento executado, hipotetico e ja superado
- nao deve ser tratado como backlog vivo ou norma atual

**Encaminhamento inicial**

- manter no conjunto documental
- reclassificar como artefato historico de planejamento
- candidato a enquadramento semantico, mais do que a reescrita ampla

### 3.5 `docs/projeto/politica_de_diagramas_versionaveis.md`

**Estatuto preliminar**

- politica formal

**Problemas identificados**

- menos ambiguo que os demais documentos do bloco
- ainda depende de verificacao de encaixe na futura arquitetura documental global
- referencia explicitamente a frente de modelagem, o que exige cuidado na sua localizacao final

**Encaminhamento inicial**

- manter no conjunto documental
- preservar como politica formal
- candidato a eventual realocacao estrutural, nao a reclassificacao semantica

### 3.6 `docs/projeto/questionario_levantamento_requisitos.md`

**Estatuto preliminar**

- instrumento de levantamento/elicitacao
- artefato historico preparatorio

**Problemas identificados**

- nao e documento normativo nem retrato factual do projeto
- forte dependencia de contexto conversacional de origem
- precisa ser enquadrado como insumo historico, nao como documento vivo

**Encaminhamento inicial**

- manter no conjunto documental
- reclassificar como artefato historico de levantamento
- candidato a saneamento semantico leve e enquadramento claro

### 3.7 `docs/projeto/roadmap_arquitetural.md`

**Estatuto preliminar**

- roadmap arquitetural prospectivo
- planejamento historico de evolucao

**Problemas identificados**

- alto grau de prospectividade
- milestones e estimativas temporais historicamente situadas e potencialmente superadas
- nao deve ser tratado como plano normativo atual

**Encaminhamento inicial**

- manter no conjunto documental
- reclassificar como roadmap historico/prospectivo
- candidato forte a enquadramento semantico

### 3.8 `docs/projeto/visao_do_projeto.md`

**Estatuto preliminar**

- visao estrategica/prospectiva
- documento de concepcao

**Problemas identificados**

- marcado explicitamente como rascunho inicial
- forte teor prospectivo e de ideacao
- precisa de enquadramento historico claro para nao competir com contexto consolidado posterior

**Encaminhamento inicial**

- manter no conjunto documental
- tratar como documento historico de visao/concepcao
- candidato forte a correcao obrigatoria de estatuto e enquadramento

## 4. Sintese do bloco

### 4.1 Estatutos predominantes identificados

Neste bloco, os estatutos predominantes foram:

- politica formal
- visao estrategica
- planejamento historico
- analise arquitetural prospectiva
- direcionamento arquitetural
- instrumento de levantamento/elicitacao

### 4.2 Principais riscos encontrados

- mistura de documentos vivos e historicos no mesmo diretorio
- excesso de prospectividade sem enquadramento temporal suficientemente claro
- tensao entre gestao antiga e governanca posterior
- tom conversacional ou de rascunho em artefatos que hoje exigem reposicionamento semantico

### 4.3 Classificacao operacional preliminar

Entram como candidatos mais fortes a `corrigir agora`:

- `docs/projeto/analise_arquitetural.md`
- `docs/projeto/manual_gestao.md`
- `docs/projeto/visao_do_projeto.md`
- `docs/projeto/roadmap_arquitetural.md`
- `docs/projeto/direcionamento_arquitetural_engine_mvp.md`

Permanecem, por ora, como candidatos a enquadramento semantico e saneamento pontual:

- `docs/projeto/plano_issues_documentacao.md`
- `docs/projeto/questionario_levantamento_requisitos.md`
- `docs/projeto/politica_de_diagramas_versionaveis.md`

## 5. Proximo passo recomendado

Avancar para o bloco `docs/fases/`, mantendo a mesma disciplina:

- cobrir todos os arquivos do bloco
- registrar classificacao preliminar por arquivo
- distinguir documentos historicos de entrega, documentos de intervencao, tutoriais operacionais embutidos e artefatos com valor apenas rastreavel
