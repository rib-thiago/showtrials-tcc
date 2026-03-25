# Visão de Processo — 4+1

## 1. Objetivo do documento

Este documento registra a **visão de processo** da arquitetura da frente, no contexto do modelo **4+1**.

Seu objetivo é descrever a solução do ponto de vista de:

- execução
- concorrência
- fluxo de processamento
- estados de execução
- possibilidades de execução síncrona e assíncrona

## 2. Base de evidência utilizada

Esta visão se apoia principalmente em:

- [13_especificacoes_textuais_de_casos_de_uso_prioritarios.md](/home/thiago/coleta_showtrials/docs/modelagem/13_especificacoes_textuais_de_casos_de_uso_prioritarios.md)
- [17_drivers_arquiteturais.md](/home/thiago/coleta_showtrials/docs/modelagem/17_drivers_arquiteturais.md)
- [20_decisoes_arquiteturais_iniciais.md](/home/thiago/coleta_showtrials/docs/modelagem/20_decisoes_arquiteturais_iniciais.md)
- [22_visao_logica_4mais1.md](/home/thiago/coleta_showtrials/docs/modelagem/22_visao_logica_4mais1.md)
- [docs/projeto/direcionamento_arquitetural_engine_mvp.md](/home/thiago/coleta_showtrials/docs/projeto/direcionamento_arquitetural_engine_mvp.md)

## 3. Escopo da visão de processo

Esta visão trata da dinâmica de funcionamento do sistema.

Ela não descreve:

- distribuição física em máquinas
- organização de módulos de código
- detalhe de classes ou interfaces de implementação

Ela descreve:

- como os fluxos principais são executados
- quais partes da solução são potencialmente ativas
- onde aparecem estados, transições, background e pontos de revisão

## 4. Modos principais de execução identificados

Com base na frente já consolidada, a solução precisa acomodar pelo menos três modos principais de execução:

- **execução interativa síncrona**
- **execução configurada de pipeline**
- **execução potencialmente assíncrona/não bloqueante**

## 5. Leitura da visão de processo por estágio

## 5.1 Sistema atual

No sistema atual, predomina um modelo de processo mais simples e linear:

- o usuário aciona um caso de uso
- a aplicação recupera dados
- processa ou transforma o documento
- persiste ou exibe o resultado

Esse modelo é predominantemente:

- síncrono
- orientado à resposta imediata
- documento-cêntrico

## 5.2 Transição arquitetural

Na transição, surge uma nova dinâmica:

- o usuário passa a configurar fluxos
- a execução deixa de ser apenas sequência fixa de casos imperativos
- aparece a necessidade de separar definição do fluxo e execução do fluxo

Aqui, o processo deixa de ser apenas:

- “buscar → transformar → salvar”

e passa a admitir:

- preparação de execução
- validação de configuração
- acompanhamento de estado

## 5.3 Sistema-alvo

No sistema-alvo, a execução passa a ser entendida como:

- um fluxo configurado
- orientado por contexto de execução
- capaz de produzir resultados intermediários e finais
- com possibilidade futura de execução não bloqueante e acompanhamento posterior

## 6. Estrutura de processo consolidada

### 6.1 Fluxo interativo do sistema atual

Padrão predominante:

1. usuário aciona operação
2. aplicação recupera documentos ou dados necessários
3. processamento é realizado
4. resultado é exibido, persistido ou exportado

### 6.2 Fluxo configurado da engine

Padrão desejado:

1. usuário cria ou configura pipeline
2. sistema valida a configuração
3. entrada documental é fornecida ou localizada
4. executor inicia o pipeline
5. steps são executados em ordem
6. contexto de execução é atualizado ao longo do fluxo
7. resultados são exibidos, persistidos ou encaminhados para revisão

### 6.3 Fluxo com acompanhamento posterior

Padrão futuro desejável:

1. usuário inicia execução
2. sistema registra estado de execução
3. a execução segue sem bloquear toda a interação
4. usuário pode consultar andamento, resultados ou pontos de intervenção
5. o sistema registra encerramento, falha parcial ou sucesso

## 7. Estados relevantes da execução

Mesmo sem definir ainda um diagrama formal de estados, a visão de processo já exige reconhecer estados como:

- configurado
- validado
- em execução
- concluído
- concluído com persistência
- falha parcial
- falha total
- aguardando revisão/intervenção

Esses estados são particularmente importantes para:

- execução de pipeline
- persistência configurável
- revisão humana de resultados

## 8. Concorrência e não bloqueio

### 8.1 Situação atual

O sistema atual é predominantemente orientado a execução direta e síncrona.

### 8.2 Direção futura

A frente já consolidou que a arquitetura deve admitir:

- execução não bloqueante
- tarefas em background
- acompanhamento posterior

### 8.3 Consequência arquitetural

Isso implica necessidade futura de:

- separação entre comando de execução e processamento efetivo
- estado explícito de execução
- possibilidade de retomada ou inspeção posterior

## 9. Pontos de intervenção humana no processo

A visão de processo também precisa reconhecer que a futura solução não é apenas automatizada.

Existem pontos em que a intervenção humana pode se tornar parte legítima do fluxo:

- revisão de tradução
- leitura de resultados intermediários
- auditoria de execução
- validação de produtos derivados

Essa característica impede que a arquitetura seja modelada como pipeline cego e totalmente fechado.

## 10. Relação entre processo e resultados derivados

Os resultados derivados não devem ser tratados apenas como subproduto passivo do processamento.

Na visão de processo, eles:

- nascem durante a execução
- podem ser persistidos ou não
- podem permanecer automáticos
- podem ser enviados a revisão
- podem voltar a compor o contexto de trabalho posterior

Isso reforça a importância de estados, versionamento e rastreabilidade de origem.

## 11. Inferências adotadas

As principais inferências adotadas nesta visão foram:

- a arquitetura futura foi tratada como necessariamente capaz de acomodar execução não bloqueante, mesmo que isso não faça parte do MVP estrutural completo imediato
- a possibilidade de pontos de intervenção humana foi elevada a aspecto de processo relevante, e não apenas detalhe de interface
- a noção de estado de execução foi tratada como inevitável para a engine futura

## 12. Dívidas técnicas registradas

Permanecem como pontos futuros:

- decidir se a modelagem futura exigirá bloco próprio para telemetria e acompanhamento
- decidir o nível de detalhamento do ciclo de vida de uma execução
- decidir se haverá diagrama de estados específico para execuções ou para resultados derivados

## 13. Próximos passos

Os próximos passos recomendados são:

- abrir a visão física do 4+1
- depois a visão de casos de uso do 4+1
- consolidar ao final a síntese do 4+1
