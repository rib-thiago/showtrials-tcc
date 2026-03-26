# Classificacao Semantica do Legado - Bloco 01

## 1. Objetivo do documento

Este documento registra a classificacao semantica preliminar do primeiro bloco da documentacao legada revisada na Etapa 3 da frente de saneamento documental.

Este bloco cobre:

- documentos-raiz de `docs/`
- documentos de `docs/metricas/`

Seu objetivo e:

- registrar decisao preliminar por arquivo
- apontar problemas semanticos, factuais e formais identificados
- indicar encaminhamento inicial para as etapas seguintes

## 2. Escopo do bloco

Arquivos cobertos neste bloco:

- `docs/index.md`
- `docs/overview.md`
- `docs/ARCHITECTURE.md`
- `docs/contributing.md`
- `docs/changelog.md`
- `docs/metricas/cobertura.md`
- `docs/metricas/diagnostico_ci.md`
- `docs/metricas/diagnostico_fase12.md`

Todos os arquivos do bloco receberam classificacao semantica preliminar nesta etapa.

## 3. Classificacao por arquivo

### 3.1 `docs/index.md`

**Estatuto preliminar**

- navegacao institucional
- pagina de entrada da documentacao

**Problemas identificados**

- possivel desatualizacao factual em metricas e estatisticas
- recorte de navegacao pode nao refletir a estrutura documental mais madura do projeto
- linguagem de apresentacao pode estar simplificando em excesso o estado real da arquitetura e do produto

**Encaminhamento inicial**

- manter no conjunto documental
- revisar factualidade e papel na arquitetura documental alvo
- candidato a correcao obrigatoria

### 3.2 `docs/overview.md`

**Estatuto preliminar**

- visao geral introdutoria do projeto

**Problemas identificados**

- possivel desatualizacao factual em metricas e estado do projeto
- uso de narrativa arquitetural mais forte do que a atualmente sustentada por abordagem conservadora posterior
- estrutura de projeto listada pode nao refletir o estado atual integral do repositorio

**Encaminhamento inicial**

- manter no conjunto documental
- revisar aderencia factual e reposicionar como visao geral introdutoria
- candidato a correcao obrigatoria

### 3.3 `docs/ARCHITECTURE.md`

**Estatuto preliminar**

- documento arquitetural explicativo de alto nivel

**Problemas identificados**

- assertividade potencialmente excessiva sobre modelo arquitetural e papel das camadas
- risco de descrever o sistema de forma mais limpa e estabilizada do que o historico real sustenta
- mistura de explicacao geral com formulacoes que podem soar normativas demais frente ao estado implementado

**Encaminhamento inicial**

- manter no conjunto documental
- revisar aderencia factual contra codigo e contexto consolidado
- candidato a correcao obrigatoria

### 3.4 `docs/contributing.md`

**Estatuto preliminar**

- guia de contribuicao
- onboarding tecnico

**Problemas identificados**

- possivel desalinhamento com a governanca mais recente do projeto
- referencias operacionais podem estar simplificadas demais frente aos fluxos e politicas formalizados depois

**Encaminhamento inicial**

- manter no conjunto documental
- revisar alinhamento com governanca e fluxos atuais
- candidato a saneamento pontual, nao necessariamente reclassificacao forte

### 3.5 `docs/changelog.md`

**Estatuto preliminar**

- historico de mudancas
- release notes

**Problemas identificados**

- possivel defasagem temporal
- pode nao refletir a evolucao documental e arquitetural posterior
- ainda assim, seu estatuto semantico e claro

**Encaminhamento inicial**

- manter no conjunto documental
- tratar como historico formal, nao como retrato atual completo
- candidato a atualizacao ou enquadramento historico posterior

### 3.6 `docs/metricas/cobertura.md`

**Estatuto preliminar**

- acompanhamento tecnico de cobertura
- documento de metricas vivas com historico agregado

**Problemas identificados**

- alto risco de desatualizacao factual
- mistura de snapshot atual com historico e priorizacao futura
- fechamento formal de Markdown problemático no final do arquivo

**Encaminhamento inicial**

- manter no conjunto documental
- revisar factualidade e estrutura
- candidato forte a correcao obrigatoria

### 3.7 `docs/metricas/diagnostico_ci.md`

**Estatuto preliminar**

- diagnostico tecnico historico

**Problemas identificados**

- fechamento formal de Markdown problematico ao final
- possivel necessidade de enquadramento mais claro como artefato historico, nao documento vivo

**Encaminhamento inicial**

- manter no conjunto documental
- preservar como diagnostico historico
- candidato a correcao formal e enquadramento semantico

### 3.8 `docs/metricas/diagnostico_fase12.md`

**Estatuto preliminar**

- diagnostico tecnico historico

**Problemas identificados**

- referencia potencialmente inconsistente entre fase e issue
- links e rastros de commit/issue podem exigir verificacao adicional
- texto parece semanticamente coerente como diagnostico, mas depende de checagem fina de rastreabilidade

**Encaminhamento inicial**

- manter no conjunto documental
- preservar como diagnostico historico
- candidato a saneamento pontual de rastreabilidade

## 4. Sintese do bloco

### 4.1 Estatutos predominantes identificados

Neste bloco, os estatutos predominantes foram:

- navegacao institucional
- visao geral introdutoria
- documento arquitetural explicativo
- onboarding/contribuicao
- historico de mudancas
- metricas vivas
- diagnosticos tecnicos historicos

### 4.2 Principais riscos encontrados

- desatualizacao factual
- excesso de assertividade arquitetural
- enquadramento insuficiente entre documento vivo e historico
- problemas formais de Markdown
- rastreabilidade incompleta ou potencialmente inconsistente

### 4.3 Classificacao operacional preliminar

Neste bloco, entram como candidatos mais fortes a `corrigir agora`:

- `docs/index.md`
- `docs/overview.md`
- `docs/ARCHITECTURE.md`
- `docs/metricas/cobertura.md`
- `docs/metricas/diagnostico_ci.md`

Permanecem, por ora, como candidatos a saneamento pontual ou verificacao adicional:

- `docs/contributing.md`
- `docs/changelog.md`
- `docs/metricas/diagnostico_fase12.md`

## 5. Proximo passo recomendado

Avancar para o bloco `docs/flows/`, mantendo a mesma disciplina:

- cobrir todos os arquivos do bloco
- registrar classificacao preliminar por arquivo
- separar politica, protocolo normativo e guia operacional
