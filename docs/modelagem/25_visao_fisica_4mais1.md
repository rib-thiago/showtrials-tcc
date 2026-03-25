# Visão Física — 4+1

## 1. Objetivo do documento

Este documento registra a **visão física** da arquitetura da frente, no contexto do modelo **4+1**.

Seu objetivo é descrever a solução do ponto de vista de:

- distribuição física dos elementos relevantes
- nós ou ambientes de execução
- dependências externas
- evolução provável de deployment entre sistema atual e engine futura

## 2. Base de evidência utilizada

Esta visão se apoia principalmente em:

- [17_drivers_arquiteturais.md](/home/thiago/coleta_showtrials/docs/modelagem/17_drivers_arquiteturais.md)
- [20_decisoes_arquiteturais_iniciais.md](/home/thiago/coleta_showtrials/docs/modelagem/20_decisoes_arquiteturais_iniciais.md)
- [22_visao_logica_4mais1.md](/home/thiago/coleta_showtrials/docs/modelagem/22_visao_logica_4mais1.md)
- [23_visao_de_desenvolvimento_4mais1.md](/home/thiago/coleta_showtrials/docs/modelagem/23_visao_de_desenvolvimento_4mais1.md)
- [24_visao_de_processo_4mais1.md](/home/thiago/coleta_showtrials/docs/modelagem/24_visao_de_processo_4mais1.md)
- [docs/projeto/analise_arquitetural.md](/home/thiago/coleta_showtrials/docs/projeto/analise_arquitetural.md)
- [docs/projeto/direcionamento_arquitetural_engine_mvp.md](/home/thiago/coleta_showtrials/docs/projeto/direcionamento_arquitetural_engine_mvp.md)
- estrutura atual do código em `src/`

## 3. Escopo da visão física

Esta visão trata de:

- onde o sistema executa
- quais recursos físicos ou ambientes ele consome
- como as partes principais tendem a se distribuir

Ela não descreve:

- detalhe de classes e interfaces
- fluxos finos de execução interna
- modelagem C4 formal, que será tratada depois

## 4. Leitura física por estágio do sistema

## 4.1 Sistema atual

O sistema atual pode ser lido, fisicamente, como uma solução predominantemente monolítica e local:

- aplicação CLI
- aplicação Web
- banco SQLite local
- serviços externos consumidos sob demanda

Essa distribuição é compatível com o que o código já mostra:

- interfaces CLI e Web no mesmo repositório
- persistência SQLite como mecanismo principal
- consumo de serviços externos, como tradução, a partir da infraestrutura

## 4.2 Transição arquitetural

Na transição, a leitura física ainda pode permanecer simples, mas passa a exigir uma distinção maior entre:

- interface de operação
- núcleo de execução
- persistência de documentos e pipelines

Mesmo que tudo continue inicialmente no mesmo processo ou host, a visão física já precisa admitir separação conceitual entre:

- frontends ou pontos de entrada
- execução de pipeline
- armazenamento de artefatos

## 4.3 Sistema-alvo

No sistema-alvo, a arquitetura física passa a admitir, ao menos conceitualmente:

- interfaces de operação
- núcleo da aplicação e da engine
- persistência de documentos, pipelines e resultados
- serviços externos consumidos
- eventual processamento em background

Isso não obriga, no MVP, uma distribuição em múltiplas máquinas, mas exige uma modelagem compatível com essa evolução.

## 5. Elementos físicos relevantes

Com base na frente consolidada, os elementos físicos mais relevantes são:

- terminal do usuário
- navegador do usuário
- processo da aplicação
- armazenamento local ou persistente
- serviços externos de tradução, OCR ou coleta
- eventual worker ou executor em background

## 6. Topologia física consolidada

## 6.1 Topologia mínima atual

A topologia mínima atual pode ser entendida assim:

1. usuário acessa CLI ou Web
2. ambas operam sobre a mesma aplicação principal
3. a aplicação acessa SQLite e demais mecanismos locais
4. a aplicação consome serviços externos quando necessário

## 6.2 Topologia de transição

Na transição, a topologia provável passa a admitir:

1. interface de operação
2. aplicação principal
3. executor de pipeline ainda integrado ao processo principal
4. persistência local ou equivalente
5. serviços externos especializados

## 6.3 Topologia futura desejável

No sistema-alvo, a topologia física desejável pode admitir, futuramente:

1. interfaces CLI e Web
2. núcleo da aplicação
3. engine de pipeline
4. armazenamento de documentos, pipelines e produtos derivados
5. executor em background, quando aplicável
6. integrações externas isoladas na borda do sistema

## 7. Consequências físicas dos drivers arquiteturais

Os drivers já consolidados impõem implicações físicas claras:

### 7.1 Preservação de CLI e Web

Exige manter mais de um ponto de entrada legítimo para o sistema.

### 7.2 Persistência configurável

Exige distinguir fisicamente, ao menos em termos de responsabilidade, entre:

- execução
- armazenamento de artefatos

### 7.3 Execução não bloqueante

Abre a necessidade futura de separar:

- comando de execução
- trabalho efetivo em background

### 7.4 Integrações externas

Exige manter serviços externos na borda da solução, sem confundi-los com nós internos.

## 8. Leitura física recomendada para o MVP

Para o MVP estrutural da engine, a leitura física mais aderente é:

- solução ainda predominantemente monolítica
- persistência local ou central simples
- executor de pipeline inicialmente integrado à aplicação
- compatibilidade com futura extração de processamento em background

Essa leitura preserva:

- simplicidade operacional
- aderência ao estado atual do projeto
- possibilidade de evolução incremental

## 9. Inferências adotadas

As principais inferências adotadas nesta visão foram:

- a solução foi tratada como fisicamente simples no presente, sem negar futura separação de responsabilidades
- a existência futura de processamento em background foi tratada como compatível com a direção arquitetural, ainda que não como obrigação imediata do MVP
- a separação física entre aplicação principal e engine foi tratada como possibilidade evolutiva, não como exigência imediata

## 10. Dívidas técnicas registradas

Permanecem como pontos futuros:

- decidir se a engine terá processo próprio ou permanecerá integrada à aplicação principal por mais tempo
- decidir quando a execução em background deixará de ser apenas compatibilidade arquitetural e passará a ser requisito estrutural efetivo
- decidir a futura topologia de persistência para documentos, pipelines e resultados derivados

## 11. Próximos passos

Os próximos passos recomendados são:

- abrir a visão de casos de uso do 4+1
- consolidar depois a síntese do 4+1
