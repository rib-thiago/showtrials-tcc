# Padrao Minimo Documental da Etapa 5

## 1. Objetivo do documento

Este documento define o padrao minimo que deve orientar o saneamento obrigatorio da Etapa 5 da frente de saneamento documental.

Seu objetivo e:

- reduzir retrabalho durante o saneamento
- fornecer uma regua minima por tipo documental
- padronizar titulos exibidos
- orientar decisoes de rename de arquivos

Este documento nao pretende estabelecer, neste momento, um sistema final e exaustivo de templates do projeto.

Ele define apenas o minimo necessario para permitir saneamento consistente e controlado nesta frente.

## 2. Principios gerais

Durante a Etapa 5, os documentos saneados devem obedecer aos principios abaixo:

- clareza semantica antes de ornamentacao
- aderencia factual antes de completude aspiracional
- estrutura minima consistente antes de polimento editorial fino
- preservacao de navegacao publica antes de reorganizacao fisica ampla
- titulo legivel e direto antes de titulo “de marketing” ou gerado

## 3. Padrao minimo por tipo documental

### 3.1 Politica

Estrutura minima recomendada:

- `# Titulo`
- objetivo
- escopo
- diretrizes, regras ou principios
- criterios de aplicacao ou conformidade
- relacoes com outros documentos, quando necessario

Observacoes:

- evitar tom tutorial
- evitar exemplos longos se nao forem necessarios para interpretacao da regra
- o documento deve deixar claro que estabelece norma, nao apenas sugestao

### 3.2 Protocolo normativo

Estrutura minima recomendada:

- `# Titulo`
- objetivo
- quando aplicar
- regras operacionais
- criterios minimos de conformidade
- observacoes de governanca, quando couber

Observacoes:

- usar linguagem prescritiva, mas sem inflacao retorica
- o foco deve estar em disciplina operacional, nao em exposicao excessivamente didatica

### 3.3 Guia operacional ou tecnico

Estrutura minima recomendada:

- `# Titulo`
- objetivo
- contexto de uso
- orientacoes, procedimento ou fluxo
- limites, cuidados ou observacoes

Observacoes:

- exemplos praticos sao aceitaveis quando melhoram entendimento
- evitar transformar o guia em politica sem explicitar essa mudanca

### 3.4 Pagina publica de entrada ou visao geral

Estrutura minima recomendada:

- `# Titulo`
- apresentacao curta
- descricao do escopo ou papel da pagina
- links de navegacao ou secoes principais
- observacoes factuais minimas, quando necessario

Observacoes:

- evitar numero ou estatistica sem base confirmada
- evitar promessas arquiteturais ou funcionais acima da evidencia disponivel

### 3.5 Diagnostico ou metrica

Estrutura minima recomendada:

- `# Titulo`
- objetivo
- contexto ou recorte observado
- estado encontrado
- limitacoes, interpretacao ou riscos
- proximo passo, quando fizer sentido

Observacoes:

- deixar claro se o documento registra um estado historico ou um acompanhamento vivo
- nao apresentar estimativa ou medicao como verdade atemporal

### 3.6 Historico de fase ou intervencao

Estrutura minima recomendada:

- `# Titulo`
- natureza historica do documento
- objetivo da fase ou intervencao
- contexto
- acoes realizadas
- artefatos, impactos ou resultados
- observacoes de rastreabilidade, limitacoes ou aprendizagem

Observacoes:

- nao confundir relato historico com norma vigente
- evitar wrappers artificiais, blocos `markdown` literais e tom promocional
- exemplos extensos de shell ou codigo so devem permanecer quando forem realmente parte relevante do registro

### 3.7 Planejamento historico ou prospectivo

Estrutura minima recomendada:

- `# Titulo`
- natureza do documento
- objetivo
- proposta, hipotese ou plano
- limites de validade
- relacao com o estado atual, quando necessario

Observacoes:

- deixar claro quando o documento nao descreve o estado implementado
- evitar leitura ambigua entre visao futura e realidade atual

## 4. Convencao de titulos

### 4.1 Regras gerais de H1

Os titulos principais devem seguir estas regras:

- usar H1 simples e direto
- remover wrappers como `DOCUMENTO:`, `DOCUMENTO 1:` e equivalentes
- remover emojis de H1
- evitar caixa alta integral
- explicitar a natureza do documento quando isso reduzir ambiguidade

### 4.2 Formas preferenciais

Formas de titulo preferenciais:

- `# Politica de Governanca do Projeto`
- `# Protocolo de Git do Projeto`
- `# Protocolo de Qualidade do Projeto`
- `# Guia de Contribuicao`
- `# Visao do Projeto`
- `# Roadmap Arquitetural`
- `# Diagnostico da CI`
- `# Historico da Fase 13 - Limpeza e Organizacao do Repositorio`

### 4.3 Titulos historicos

Nos documentos historicos, o titulo deve sinalizar com clareza seu estatuto sempre que isso for necessario para evitar leitura como documento vivo.

Exemplos aceitaveis:

- `# Historico da Fase 13 - Limpeza e Organizacao do Repositorio`
- `# Registro da Intervencao de CI`

## 5. Politica de nomes de arquivo

### 5.1 Regra geral

Durante a Etapa 5, o nome fisico do arquivo nao deve ser alterado por padrao.

A prioridade da etapa e:

- saneamento semantico
- saneamento formal
- saneamento factual

### 5.2 Quando considerar rename imediato

Rename imediato pode ser considerado quando:

- o nome do arquivo induz erro semantico grave
- o nome quebra fortemente a taxonomia adotada
- o ganho de clareza e alto
- o impacto em navegacao e referencias e controlavel

### 5.3 Quando adiar rename

O rename deve ser adiado quando:

- o arquivo e ancora publica relevante
- o ganho e principalmente estetico
- o conteudo ainda nao foi saneado
- a mudanca depende de revisao maior de `mkdocs.yml`, `README.md` ou navegacao

### 5.4 Titulo exibido versus nome fisico

Nesta frente, o titulo exibido do documento pode e deve ser corrigido antes do nome fisico do arquivo.

Isso permite:

- melhorar leitura e enquadramento semantico imediatamente
- evitar renames em cascata antes do momento adequado
- preservar estabilidade navegacional durante o saneamento

## 6. Consequencia pratica para os primeiros blocos da Etapa 5

Aplicando este padrao aos casos mais sensiveis ja identificados:

- `docs/flows/GOVERNANCA.md`:
  - priorizar titulo de politica formal
- `docs/flows/git_flow.md`:
  - priorizar titulo de protocolo normativo
- `docs/flows/quality_flow.md`:
  - priorizar titulo de protocolo normativo
- `docs/fases/FASE11_ESTABILIZACAO_INICIAL_DO_CI.md`:
  - tratar como historico de intervencao
- `docs/fases/FASE12_PADRONIZACAO_DA_TELEMETRIA_EM_TIPODOCUMENTO.md`:
  - tratar como historico hibrido com reducao de tutorializacao
- `docs/fases/FASE13_LIMPEZA_E_ORGANIZACAO_DO_REPOSITORIO.md` a `docs/fases/FASE16_TELEMETRIA_E_EXPANSAO_DE_TESTES_EM_LISTAR_DOCUMENTOS.md`:
  - remover residuos explicitos de geracao assistida
  - adotar titulo historico direto
- `docs/projeto/visao_do_projeto.md`:
  - manter como visao do projeto, com sinalizacao clara de natureza prospectiva se necessario

## 7. Proximo passo recomendado

Com este padrao minimo formalizado, a frente deve abrir o primeiro bloco real de saneamento da Etapa 5, preferencialmente pelos documentos:

- normativos criticos
- paginas publicas centrais
- documentos com residuos explicitos de geracao assistida e problemas formais severos
