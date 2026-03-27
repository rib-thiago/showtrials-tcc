# Classificacao Semantica do Legado - Bloco 02

## 1. Objetivo do documento

Este documento registra a classificacao semantica preliminar do segundo bloco da documentacao legada revisada na Etapa 3 da frente de saneamento documental.

Este bloco cobre todos os arquivos de `docs/flows/`.

Seu objetivo e:

- registrar decisao preliminar por arquivo
- distinguir politica, protocolo normativo e guia operacional
- apontar problemas semanticos, formais e de aderencia
- preparar a etapa futura de reorganizacao estrutural

## 2. Escopo do bloco

Arquivos cobertos neste bloco:

- `docs/flows/GOVERNANCA.md`
- `docs/flows/code_review_flow.md`
- `docs/flows/debug_flow.md`
- `docs/flows/dependencies_flow.md`
- `docs/flows/documentation_flow.md`
- `docs/flows/emergency_flow.md`
- `docs/flows/fluxo_projects_github_cli.md`
- `docs/flows/git_flow.md`
- `docs/flows/quality_flow.md`
- `docs/flows/refactoring_flow.md`
- `docs/flows/telemetry_flow.md`

Todos os arquivos do bloco receberam classificacao semantica preliminar nesta etapa.

## 3. Classificacao por arquivo

### 3.1 `docs/flows/GOVERNANCA.md`

**Estatuto preliminar**

- politica de governanca

**Problemas identificados**

- residuo explicito de geracao assistida na abertura do documento
- o nome e o conteudo ja apontam para estatuto de politica, e nao apenas “flow”
- exige alinhamento com demais artefatos normativos do projeto

**Encaminhamento inicial**

- manter no conjunto documental
- promover semanticamente ao grupo de politicas normativas
- candidato forte a correcao obrigatoria

### 3.2 `docs/flows/git_flow.md`

**Estatuto preliminar**

- protocolo normativo de Git e branches

**Problemas identificados**

- nome de “flow” e mais fraco do que o conteudo efetivo
- tom normativo muito forte, mais proximo de procedimento oficial do que guia opcional
- precisa ser comparado com a pratica Git atual desta nova frente e com a governanca consolidada

**Encaminhamento inicial**

- manter no conjunto documental
- candidato a reclassificacao semantica para protocolo normativo
- candidato a saneamento pontual

### 3.3 `docs/flows/quality_flow.md`

**Estatuto preliminar**

- protocolo normativo de qualidade

**Problemas identificados**

- mesmo padrao de alta normatividade observado em `git_flow.md`
- o nome “flow” subestima seu papel de criterio de aceite e controle tecnico
- precisa ser confrontado com o estado atual real do pipeline e das praticas do projeto

**Encaminhamento inicial**

- manter no conjunto documental
- candidato a reclassificacao semantica para protocolo normativo
- candidato a saneamento pontual

### 3.4 `docs/flows/code_review_flow.md`

**Estatuto preliminar**

- guia operacional
- checklist de auto-revisao

**Problemas identificados**

- forte acoplamento a praticas e caminhos especificos que podem estar desatualizados
- mistura checklist tecnico valido com detalhes operacionais historicamente localizados
- tom de “guia completo” com forte marca editorial do periodo legado

**Encaminhamento inicial**

- manter no conjunto documental
- tratar como guia operacional, nao como politica
- candidato a saneamento pontual e atualizacao contextual

### 3.5 `docs/flows/debug_flow.md`

**Estatuto preliminar**

- guia operacional de depuracao

**Problemas identificados**

- conteudo semanticamente coerente como guia
- pode conter tecnicas e exemplos utilmente preservaveis, mas com enquadramento possivelmente inflado como documento oficial
- precisa ser revisto quanto a atualidade de comandos e praticas

**Encaminhamento inicial**

- manter no conjunto documental
- tratar como guia operacional
- candidato a saneamento pontual

### 3.6 `docs/flows/dependencies_flow.md`

**Estatuto preliminar**

- guia operacional de dependencias
- documento de processo historicamente condicionado

**Problemas identificados**

- alto acoplamento a contexto especifico de dependencias NLP e CI de fevereiro de 2026
- carrega suposicoes que podem nao refletir mais o estado atual
- mistura padrao permanente com excecao historica

**Encaminhamento inicial**

- manter no conjunto documental
- tratar como guia operacional com forte componente historico
- candidato a saneamento obrigatorio de aderencia factual

### 3.7 `docs/flows/documentation_flow.md`

**Estatuto preliminar**

- guia operacional de documentacao

**Problemas identificados**

- acoplamento forte ao modelo antigo de `FASE*.md`
- pressupostos documentais anteriores a `docs/ai/` e `docs/modelagem/`
- parte das orientacoes pode perder validade apos a nova frente de saneamento

**Encaminhamento inicial**

- manter no conjunto documental
- tratar como guia operacional sujeito a revisao profunda
- candidato a saneamento obrigatorio por depender da arquitetura documental que esta sendo revista

### 3.8 `docs/flows/emergency_flow.md`

**Estatuto preliminar**

- protocolo operacional de emergencia/hotfix

**Problemas identificados**

- tensao relevante com a governanca ao admitir merge direto ou intervencoes excepcionais em `main`
- precisa de revisao conceitual para compatibilizacao com as regras mais recentes do projeto
- pode estar mais proximo de politica excepcional do que de guia comum

**Encaminhamento inicial**

- manter no conjunto documental
- revisar cuidadosamente contra `GOVERNANCA.md`
- candidato forte a correcao obrigatoria

### 3.9 `docs/flows/fluxo_projects_github_cli.md`

**Estatuto preliminar**

- guia tecnico/procedimental especifico de GitHub Projects via CLI

**Problemas identificados**

- documento fortemente procedural e dependente de detalhes tecnicos de uso da CLI
- pode estar correto como artefato de apoio, mas precisa de enquadramento semantico mais preciso
- menor ambiguidade do que outros arquivos do bloco

**Encaminhamento inicial**

- manter no conjunto documental
- tratar como guia tecnico especifico
- candidato a saneamento formal leve

### 3.10 `docs/flows/refactoring_flow.md`

**Estatuto preliminar**

- guia operacional de refatoracao

**Problemas identificados**

- semanticamente coerente como guia
- tom e estrutura seguem o mesmo molde editorial legado
- pode demandar ajuste de aderencia com governanca e qualidade atuais

**Encaminhamento inicial**

- manter no conjunto documental
- tratar como guia operacional
- candidato a saneamento pontual

### 3.11 `docs/flows/telemetry_flow.md`

**Estatuto preliminar**

- guia tecnico
- padrao operacional de instrumentacao

**Problemas identificados**

- pode combinar partes normativas com partes historicas de implementacao
- depende de verificacao posterior contra o padrao real ainda vigente no codigo
- estatuto e mais forte que simples guia de leitura, mas menos politico que `GOVERNANCA.md`

**Encaminhamento inicial**

- manter no conjunto documental
- tratar como guia/padrao tecnico-operacional
- candidato a saneamento pontual com verificacao factual

## 4. Sintese do bloco

### 4.1 Estatutos predominantes identificados

Neste bloco, os estatutos predominantes foram:

- politica
- protocolo normativo
- guia operacional
- guia tecnico/procedimental

### 4.2 Principais riscos encontrados

- confusao entre politica e “flow”
- excesso de normatividade em arquivos com nome de guia
- residuos de geracao assistida
- tensoes entre documentos do proprio bloco
- acoplamento historico a processos, issues e praticas que podem ter mudado

### 4.3 Classificacao operacional preliminar

Entram como candidatos mais fortes a `corrigir agora`:

- `docs/flows/GOVERNANCA.md`
- `docs/flows/git_flow.md`
- `docs/flows/quality_flow.md`
- `docs/flows/dependencies_flow.md`
- `docs/flows/documentation_flow.md`
- `docs/flows/emergency_flow.md`

Permanecem, por ora, como candidatos a saneamento pontual ou enquadramento semantico:

- `docs/flows/code_review_flow.md`
- `docs/flows/debug_flow.md`
- `docs/flows/fluxo_projects_github_cli.md`
- `docs/flows/refactoring_flow.md`
- `docs/flows/telemetry_flow.md`

## 5. Proximo passo recomendado

Avancar para o bloco `docs/projeto/`, mantendo a mesma disciplina:

- cobrir todos os arquivos do bloco
- registrar classificacao preliminar por arquivo
- distinguir visao, planejamento, politica, analise arquitetural e artefatos historicos de concepcao
