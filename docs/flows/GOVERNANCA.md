A seguir está o documento consolidado para inclusão como `GOVERNANCA.md` no repositório rib-thiago / showtrials-tcc.

---

# GOVERNANCA.md

## 1. Princípios de Governança

Este repositório adota um modelo de governança orientado a:

* Foco arquitetural
* Rastreabilidade técnica
* Entregáveis estruturais
* Redução de dispersão
* Evolução incremental controlada

Toda organização de trabalho deve preservar coerência arquitetural e evitar feature creep.

---

## 2. Modelo de Milestones

### 2.1 Regra Fundamental

* Apenas **1 milestone estratégica pode estar ativa simultaneamente**.

### 2.2 O que é uma Milestone

Milestone representa um **entregável estrutural relevante**, nunca um período temporal.

Exemplos válidos:

* MVP - Engine de Pipeline
* M2 - Migração completa
* M3 - Evolução do CLI

Exemplos inválidos:

* “Semanas 1–2”
* “Sprint X”
* “Março 2026”

### 2.3 Política

* Issues estruturais devem estar vinculadas à milestone ativa.
* Issues não estruturais não devem competir com milestone estratégica.
* Milestones antigas devem ser encerradas, nunca apagadas.

---

## 3. Sistema Oficial de Labels

### 3.1 Dimensão: Tipo

* `type:engine`
* `type:infra`
* `type:feature`
* `type:docs`
* `type:refactor`
* `type:bug`

Toda issue deve possuir exatamente um tipo principal.

---

### 3.2 Dimensão: Prioridade

* `priority:P0` → Bloqueia arquitetura
* `priority:P1` → Necessária para milestone ativa
* `priority:P2` → Melhoria incremental / não urgente

Durante milestone estrutural:

* Apenas P0 e P1 podem ir para Ready.
* P2 permanece em Backlog.

---

### 3.3 Dimensão: Status Estratégico

* `strategic` → Faz parte da milestone ativa.
* `frozen` → Explicitamente congelada até conclusão da milestone ativa.

---

## 4. Fluxo de Status no Project

Backlog
→ Ready
→ In Progress
→ In Review
→ Done

### Regras

* Máximo **1 issue em In Progress por vez**.
* Nenhuma issue vai para Ready sem critérios de aceite claros.
* In Review exige checklist técnico mínimo.
* Apenas issues da milestone ativa podem entrar em In Progress.

---

## 5. Critério de Criação de Issue

Uma issue só deve ser criada se:

* Exige mais de uma sessão de trabalho.
* Possui critério de aceite objetivo.
* É rastreável e mensurável.
* Não é micro ajuste trivial.

Toda issue deve conter:

1. Contexto
2. Problema
3. Objetivo
4. Critérios de aceite
5. Fora de escopo
6. Tipo
7. Prioridade
8. Milestone (se aplicável)

---

## 6. Política de Foco

Durante execução de uma milestone estratégica:

* Features paralelas são marcadas como `frozen`.
* Apenas trabalho relacionado à milestone ativa pode avançar.
* Evitar alternância de contexto.

---

## 7. Política de Branches

Formato obrigatório:

* `engine/<descricao>`
* `infra/<descricao>`
* `feature/<descricao>`
* `docs/<descricao>`
* `refactor/<descricao>`

Exemplos:

* `engine/transformer-contract`
* `infra/mypy-fix`
* `feature/dark-mode`

Nunca trabalhar diretamente na `main`.

---

## 8. Política de Pull Request

Todo PR deve:

* Referenciar a issue correspondente.
* Descrever a solução adotada.
* Explicar impacto arquitetural (se houver).
* Confirmar critérios de aceite.
* Estar vinculado à milestone ativa (se strategic).

---

## 9. Política de Encerramento de Issue

Uma issue só pode ser movida para Done se:

* Critérios de aceite forem cumpridos.
* Código estiver revisado.
* PR estiver mergeado.
* Não houver pendências técnicas ocultas.

---

## 10. Regra de Evolução Arquitetural

Mudanças estruturais:

* Devem ser discutidas antes da implementação.
* Devem ser rastreadas como `type:engine` ou `type:refactor`.
* Nunca devem ocorrer implicitamente dentro de issues de feature.

---

## 11. Estado Atual da Governança

* Milestone ativa: MVP - Engine de Pipeline
* Sistema de labels consolidado
* Features paralelas congeladas
* Modelo de foco unificado

---
