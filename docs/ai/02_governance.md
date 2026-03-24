# Governança

## 0. Regra de leitura deste documento

Este documento distingue explicitamente três níveis de afirmação:

- **Norma documentada**: regra descrita em `docs/flows/`
- **Evidência real observada**: ponto sustentado também por Git/GitHub consultado nesta sessão
- **Não confirmado**: ponto normativo ainda não verificado diretamente no estado operacional do repositório

Salvo indicação em contrário, as seções abaixo descrevem primeiro a **norma documentada**. Quando houver evidência operacional real ou ausência de confirmação, isso será indicado explicitamente.

## 1. Princípios de governança

As fontes de governança examinadas definem um modelo orientado a:

- foco arquitetural
- rastreabilidade técnica
- entregáveis estruturais
- redução de dispersão
- evolução incremental controlada

O princípio operacional dominante é que o trabalho técnico não deve avançar como fila livre de tarefas independentes. Ele deve permanecer subordinado a:

- uma milestone estratégica ativa
- issues com escopo objetivo
- priorização explícita
- disciplina de branch e merge

Também é regra central que mudanças estruturais não ocorram de forma implícita. Se uma alteração afeta a arquitetura, ela deve ser tratada como mudança arquitetural explícita.

Classificação desta seção:

- **Norma documentada**: sim
- **Evidência real observada**: parcial, porque o GitHub atual e o caso da issue `#6`/PRs `#18` e `#19` mostram aplicação prática de controle de escopo
- **Não confirmado**: aplicação homogênea dessas regras em todo o histórico do projeto

## 2. Regras sobre milestones e issues

### 2.1 Milestones

As regras observadas para milestones são:

- apenas **uma milestone estratégica pode estar ativa por vez**
- milestone representa **entregável estrutural relevante**
- milestone **não** deve representar janela de tempo, sprint ou período calendárico
- milestones antigas devem ser encerradas, não apagadas

Exemplos de milestone válidos segundo a governança:

- `MVP - Engine de Pipeline`
- `M2 - Migração completa`
- `M3 - Evolução do CLI`

Exemplos explicitamente inválidos:

- `Semanas 1-2`
- `Sprint X`
- `Março 2026`

Classificação desta subseção:

- **Norma documentada**: sim
- **Evidência real observada**: sim, porque foi observada milestone aberta `MVP - Engine de Pipeline` com caráter estrutural
- **Não confirmado**: se existe enforcement técnico para impedir criação de milestones fora desse padrão

### 2.2 Issues

Uma issue só deve existir quando:

- exige mais de uma sessão de trabalho
- possui critério de aceite objetivo
- é rastreável
- é mensurável
- não é mero microajuste trivial

Toda issue deve conter:

1. contexto
2. problema
3. objetivo
4. critérios de aceite
5. fora de escopo
6. tipo
7. prioridade
8. milestone, quando aplicável

Classificação desta subseção:

- **Norma documentada**: sim
- **Evidência real observada**: parcial, porque as issues estratégicas atuais seguem em grande parte esse modelo
- **Não confirmado**: se todo o backlog histórico do repositório segue integralmente esse padrão

### 2.3 Regras de avanço

Durante uma milestone estratégica:

- apenas issues da milestone ativa podem avançar
- apenas `P0` e `P1` podem ir para `Ready`
- `P2` deve permanecer em backlog
- no board, o fluxo oficial é:
  - `Backlog -> Ready -> In Progress -> In Review -> Done`
- no máximo **1 issue pode estar em `In Progress` por vez**

Classificação desta subseção:

- **Norma documentada**: sim
- **Evidência real observada**: parcial, porque labels, milestone e preocupação com escopo foram observadas no GitHub
- **Não confirmado**:
  - estado real e completo do board/Project
  - enforcement operacional de “1 issue em progresso”
  - enforcement operacional de `Ready` apenas para `P0/P1`

## 3. Labels e tipagem de trabalho

O sistema oficial de labels observado em `GOVERNANCA.md` organiza o trabalho por três dimensões principais.

### 3.1 Tipo

Toda issue deve ter exatamente um tipo principal:

- `type:engine`
- `type:infra`
- `type:feature`
- `type:docs`
- `type:refactor`
- `type:bug`

### 3.2 Prioridade

- `priority:P0` -> bloqueia arquitetura
- `priority:P1` -> necessária para a milestone ativa
- `priority:P2` -> melhoria incremental / não urgente

### 3.3 Status estratégico

- `strategic` -> faz parte da milestone ativa
- `frozen` -> explicitamente congelada até conclusão da milestone ativa

Consequência prática:

- features ou melhorias fora do foco atual podem existir como issue, mas não devem competir com a entrega estrutural ativa

Classificação desta seção:

- **Norma documentada**: sim
- **Evidência real observada**: sim, em parte, porque labels `type:*`, `priority:*`, `strategic` e `frozen` foram observadas no GitHub
- **Não confirmado**: uso perfeitamente consistente dessas labels em todo o repositório

## 4. Fluxo Git e branches tipadas

As regras Git mais recentes observadas estão em `docs/flows/git_flow.md` e são coerentes com `docs/flows/GOVERNANCA.md`.

### 4.1 Regras fundamentais

- nunca trabalhar diretamente na `main`
- toda alteração relevante deve estar vinculada a uma issue
- apenas issues da milestone ativa podem gerar branch
- issues `frozen` não podem gerar branch
- apenas uma issue deve estar em execução ativa por vez

Classificação desta subseção:

- **Norma documentada**: sim
- **Evidência real observada**: parcial
  - foi observado que o trabalho atual não está na `main`
  - foram observadas branches tipadas e uso de issues/milestone
- **Não confirmado**:
  - enforcement técnico para impedir branch fora da milestone
  - enforcement técnico para impedir execução paralela de múltiplas issues

### 4.2 Padrões de branch

Formato obrigatório:

`<tipo>/<descricao-curta>`

Tipos permitidos:

- `engine/`
- `infra/`
- `feature/`
- `docs/`
- `refactor/`
- `bug/`

Exemplos:

- `engine/contexto-pipeline`
- `infra/mypy-fix`
- `docs/governanca-update`
- `refactor/transformadores-puros`
- `bug/exportar-id-none`

Regras adicionais:

- usar hífen, não underscore
- uma branch por issue
- nome curto e sem ambiguidade
- branches estruturais devem corresponder ao tipo de issue apropriado

Classificação desta subseção:

- **Norma documentada**: sim
- **Evidência real observada**: sim, porque o repositório mostra branches recentes coerentes com esse padrão e coexistência com padrões antigos
- **Não confirmado**: aderência total de todas as branches ativas ao padrão novo

### 4.3 Commits

Os commits devem ser:

- atômicos
- descritivos
- de responsabilidade única
- sem mistura de múltiplos tipos de mudança

Também devem manter vínculo explícito com a issue sempre que aplicável.

Classificação desta subseção:

- **Norma documentada**: sim
- **Evidência real observada**: parcial, porque vários commits e PRs recentes já mostram forte preocupação com rastreabilidade
- **Não confirmado**: adesão homogênea de todos os commits a essa regra

## 5. Squash merge e proteção da `main`

### 5.1 Estratégia de merge

O fluxo Git oficial mais recente estabelece que:

- **squash merge é obrigatório**

Justificativa declarada:

- manter histórico limpo
- preservar vínculo de contexto entre branch, issue e entrega

Isso substitui a recomendação mais antiga, encontrada em documentos auxiliares, que ainda admite merge fast-forward. Para fins normativos, a leitura desta sessão privilegia o fluxo Git oficial mais recente.

Classificação desta subseção:

- **Norma documentada**: sim
- **Evidência real observada**: parcial
  - há evidência histórica de merge commits no passado
  - a documentação normativa mais recente passou a exigir squash
- **Não confirmado**:
  - configuração atual do repositório forçando squash merge
  - se administradores e mantenedores já estão obrigatoriamente limitados por essa configuração

### 5.2 Condições para merge

Antes do merge, devem estar atendidos:

- PR revisado
- critérios de aceite cumpridos
- testes passando
- CI verde
- branch atualizada com `main`
- ausência de mudanças fora de escopo
- impacto arquitetural documentado, quando houver

Classificação desta subseção:

- **Norma documentada**: sim
- **Evidência real observada**: parcial, porque a issue `#6` e o reenquadramento de PR mostram controle de escopo e revisão real
- **Não confirmado**: enforcement automático de todos esses critérios em GitHub

### 5.3 Proteção da branch principal

Segundo `git_flow.md`, a `main` deve estar protegida com:

- PR obrigatório antes do merge
- status checks obrigatórios
- branch atualizada obrigatoriamente antes do merge
- proteção também aplicável a administradores
- sem force push
- sem deleção da branch

Classificação desta subseção:

- **Norma documentada**: sim
- **Evidência real observada**: não
- **Não confirmado**: sim, porque a configuração real de proteção da `main` não foi inspecionada diretamente nesta sessão

## 6. Relação entre governança, escopo e tipo de mudança

A governança condiciona a execução técnica ao tipo de mudança.

### 6.1 Mudança estrutural

Mudança estrutural:

- deve ser discutida antes da implementação
- deve ser rastreada como `type:engine` ou `type:refactor`
- não pode ser escondida dentro de issue de feature ou bugfix

### 6.2 Mudança de feature

Feature:

- não deve competir com milestone estrutural ativa se estiver fora do foco
- pode ser congelada com label `frozen`
- não deve embutir refatoração ou alteração arquitetural implícita

### 6.3 Bugfix

Bugfix:

- deve resolver apenas o problema descrito
- não deve carregar refatoração oportunista
- pode seguir fluxo emergencial próprio quando for hotfix real

### 6.4 Refatoração

Refatoração:

- deve preservar comportamento externo
- não deve ser misturada com nova funcionalidade
- exige rastreabilidade própria

Em termos práticos, a governança converte o tipo de trabalho em restrição de escopo.

Classificação desta seção:

- **Norma documentada**: sim
- **Evidência real observada**: parcial, sobretudo pelo caso da issue `#6`
- **Não confirmado**: aplicação uniforme desse enquadramento em todos os tipos de trabalho

## 7. Papel de code review, documentation, refactoring, debug, emergency, dependencies, telemetry e Projects CLI

### 7.1 Code Review Flow

Papel:

- checklist de auto-revisão antes de PR/merge
- valida estrutura, testes, cobertura, tipagem, telemetria, documentação, lint e qualidade geral

Função prática:

- impedir fechamento de mudança sem revisão disciplinada, mesmo em trabalho individual

### 7.2 Documentation Flow

Papel:

- padronizar docstrings, README, changelog e documentação de fases
- registrar quando e como documentar entregas

Função prática:

- garantir que documentação acompanhe o código e o histórico do projeto

### 7.3 Refactoring Flow

Papel:

- definir refatoração como mudança sem alteração de comportamento externo
- exigir testes antes da refatoração
- proibir mistura de refatoração com feature no mesmo movimento

Função prática:

- limitar refatoração oportunista e reduzir risco de regressão disfarçada

### 7.4 Debug Flow

Papel:

- estabelecer método de depuração estruturado:
  - reproduzir
  - isolar
  - entender causa
  - corrigir
  - testar
  - prevenir
  - documentar

Função prática:

- reduzir tentativa e erro
- forçar correção mínima e evidência de causa raiz

### 7.5 Emergency Flow

Papel:

- definir exceção controlada para hotfix
- permitir correção urgente sem abandonar rastreabilidade

Regras centrais:

- branch específica de `fix/...`
- correção mínima necessária
- testes rápidos obrigatórios
- documentação do incidente
- tag/release de patch

Função prática:

- acelerar correções críticas sem destruir disciplina operacional

### 7.6 Dependencies Flow

Papel:

- padronizar adição e manutenção de dependências
- distinguir dependências comuns via Poetry e dependências NLP via pip temporariamente
- vincular mudanças de dependência ao CI

Função prática:

- evitar mudanças ad hoc de ambiente
- preservar reprodutibilidade operacional

### 7.7 Telemetry Flow

Papel:

- padronizar telemetria por módulo
- definir nomeação de eventos
- exigir testes de telemetria

Função prática:

- tornar instrumentação consistente, testável e desacoplada

### 7.8 Projects CLI Flow

Papel:

- operacionalizar movimentação de issues no GitHub Projects v2 via `gh`

Função prática:

- permitir que o fluxo estratégico (`Backlog`, `Ready`, `In Progress`, `In Review`, `Done`) seja mantido também por terminal, com uso correto de IDs internos de Project, Item, Field e Option

Classificação desta subseção:

- **Norma documentada**: sim
- **Evidência real observada**: não
- **Não confirmado**: sim, porque os comandos de Projects falharam nesta sessão com `unknown owner type`

## 8. Implicações práticas para futuras sessões do Codex

As regras de governança já examinadas implicam limites concretos para futuras sessões do Codex neste repositório.

### 8.1 O que uma sessão futura deve verificar antes de agir

Antes de implementação relevante, a sessão deve confirmar:

- qual é a milestone ativa
- qual issue está autorizada a avançar
- se a issue é estratégica ou está congelada
- qual tipo de branch corresponde ao trabalho
- se a mudança pretendida é feature, bug, refactor, infra, docs ou engine

### 8.2 O que uma sessão futura não deve fazer

Uma sessão futura não deve:

- trabalhar diretamente na `main`
- abrir trabalho paralelo fora da issue ativa
- implementar item `frozen`
- introduzir mudança estrutural escondida
- misturar bugfix com refatoração ou feature
- tratar documentação de visão como autorização automática para implementar roadmap
- fechar issue sem critérios de aceite, revisão e merge adequados

### 8.3 O que uma sessão futura deve fazer quando o trabalho for autorizado

Quando a execução estiver dentro do escopo correto, a sessão deve:

- manter a mudança estritamente no escopo da issue
- usar branch tipada adequada
- explicitar impacto arquitetural se houver
- seguir o fluxo auxiliar pertinente:
  - debug para correção de falha
  - refactoring para mudança sem alteração comportamental
  - documentation para atualização documental
  - dependencies para alteração de dependências
  - telemetry para instrumentação
  - emergency para hotfix real

### 8.4 Leitura normativa para esta documentação operacional

Houve divergências entre documentos mais antigos e documentos mais recentes, especialmente em:

- nomenclatura de branches
- estratégia de merge

Para efeito desta consolidação, a leitura normativa prioritária é:

1. `docs/flows/GOVERNANCA.md`
2. `docs/flows/git_flow.md`
3. `docs/flows/quality_flow.md`

Documentos auxiliares mais antigos devem ser lidos como complementares, salvo conflito com essas fontes mais recentes.

Classificação desta subseção:

- **Norma documentada**: interpretação editorial desta sessão
- **Evidência real observada**: parcial, porque a formalização recente em Git reforça a prioridade dos documentos mais novos
- **Não confirmado**: se existe documento oficial adicional que altere essa ordem de precedência

## Estado desta versão

Este documento consolida:

- normas documentadas em `docs/flows/`
- evidências reais já observadas em Git/GitHub nesta sessão
- lacunas que continuam sem verificação direta

Os pontos mais fortemente sustentados por evidência operacional nesta etapa são:

- existência de milestone estrutural ativa
- uso real de labels como `type:*`, `priority:*`, `strategic` e `frozen`
- existência de branches tipadas recentes
- uso prático de revisão de escopo e reenquadramento no caso da issue `#6` e PRs relacionados

Os pontos que continuam principalmente normativos e ainda precisam de validação manual ou técnica são:

- proteção real da `main`
- enforcement real do fluxo de Project
- enforcement automático de várias regras de board e merge além do que foi diretamente observado
