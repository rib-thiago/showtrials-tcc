# Como Usar a Captura Contínua

## 1. Objetivo

Este conjunto de arquivos define um mecanismo **transversal ao projeto** para registrar itens que surgem durante o trabalho, mas que não devem interromper a tarefa principal em andamento.

Seu objetivo é separar, de forma leve e governada:

- insight bruto
- dívida em triagem
- candidato a backlog

## 2. Princípio de uso

Quando surgir uma ideia, lacuna, oportunidade ou problema fora do foco imediato da tarefa atual, o registro deve ser feito aqui, e não disperso:

- apenas em rodadas
- apenas em conversas
- ou diretamente como issue sem amadurecimento suficiente

As rodadas continuam registrando a execução do trabalho.

A captura contínua passa a registrar o que surgiu e precisa de encaminhamento posterior.

## 3. Estrutura adotada

Este mecanismo usa três estágios:

1. `01_insights_brutos.md`
2. `02_dividas_em_triagem.md`
3. `03_candidatos_a_backlog.md`

## 4. Regra de promoção

### 4.1 Insight bruto

Registrar em `01_insights_brutos.md` quando:

- a ideia ainda está crua
- a observação ainda não foi suficientemente entendida
- interromper a tarefa atual seria contraproducente
- ainda não está claro se se trata de problema, oportunidade ou hipótese

### 4.2 Dívida em triagem

Promover para `02_dividas_em_triagem.md` quando:

- já existir uma lacuna ou limitação reconhecível
- o item já puder ser explicado como dívida documental, técnica, metodológica ou arquitetural
- ainda não houver decisão sobre corrigir agora, manter como dívida ou backlogizar

### 4.3 Candidato a backlog

Promover para `03_candidatos_a_backlog.md` quando:

- o problema ou objetivo estiver claro
- o valor esperado estiver minimamente compreendido
- já houver escopo inicial suficiente para futura abertura de issue

### 4.4 Abertura de issue

Um item só deve virar issue quando houver decisão explícita de backlogização.

## 5. Campos recomendados

### 5.1 Para insights brutos e dívidas em triagem

- `Data`
- `Origem`
- `Tipo`
- `Descrição`
- `Motivo de registro`
- `Próximo encaminhamento`

### 5.2 Para candidatos a backlog

- `Data`
- `Origem`
- `Descrição`
- `Valor esperado`
- `Escopo inicial`
- `Dependências`
- `Sugestão de encaminhamento`

## 6. Relação com a governança do projeto

Este mecanismo existe para:

- reduzir perda de contexto
- evitar expansão indevida de escopo
- melhorar rastreabilidade entre ideia, dívida e backlog
- apoiar decisões futuras sem transformar toda percepção em issue prematuramente

## 7. Uso recomendado

- registrar no mesmo dia em que o item surgir
- manter as entradas curtas e objetivas
- revisar periodicamente os três arquivos em momentos de saneamento, revisão crítica ou planejamento
- não usar este mecanismo para substituir documentação consolidada da frente
