# Dívidas Técnicas e Documentais da Frente

## 1. Objetivo do documento

Este documento consolida as **dívidas técnicas e documentais** remanescentes da frente.

Seu objetivo é:

- reunir num único lugar os pontos ainda abertos
- separar dívidas de conteúdo, governança, arquitetura e Git
- facilitar a distinção entre dívida controlada da frente e backlog posterior do projeto

## 2. Base de evidência utilizada

- [44_revisao_critica_final_da_frente.md](/home/thiago/coleta_showtrials/docs/modelagem/revisao/44_revisao_critica_final_da_frente.md)
- artefatos anteriores da frente
- rodadas anteriores da frente
- histórico Git da branch

## 3. Dívidas de domínio e modelagem

- estabilização definitiva de `Documento`
- relação entre `Documento`, `Colecao`, acervo e produtos derivados
- posição futura de alguns casos de uso especializados
- refinamento de granularidade entre resultados derivados e revisão

## 4. Dívidas arquiteturais

- momento correto de introdução de background real
- fronteira concreta entre legado, adaptadores e engine
- topologia futura de persistência para pipelines e resultados
- formalização final do validador de pipeline
- decisão sobre plugin system explícito ou solução mais leve

## 5. Dívidas de documentação e estrutura

- normalização fina da estrutura interna de alguns documentos produzidos mais cedo na frente
- revisão de padronização entre artefatos da mesma etapa
- revisão das primeiras rodadas do intervalo que ficaram mais fracas em governança
- revisão exaustiva de rastros históricos de caminhos anteriores de `docs/modelagem/` em artefatos menos centrais

## 6. Dívidas de Git e governança

- reavaliar o histórico de commits desta frente como memória documental
- garantir padrão estável de mensagem documental até o fechamento final da frente

## 7. Classificação preliminar

### 7.1 Atacáveis antes do PR

Tendem a ser atacáveis:

- normalizações documentais
- revisão de coerência e organização interna dos artefatos ainda não consolidados

### 7.2 Melhor tratadas como backlog futuro

Tendem a ser melhor tratadas depois:

- implementação real de background
- plugin system explícito
- reclassificação entre roadmap arquitetural amplo, backlog técnico ativo e blocos prospectivos já modelados

## 8. Inferências adotadas

- boa parte das dívidas remanescentes hoje é mais documental e de governança do que de conceito bruto
- a estabilização já resolveu as dívidas estruturais obrigatórias e reduziu o restante a um conjunto mais controlado

## 9. Suposições operacionais

- esta lista deve funcionar como inventário vivo das dívidas que permanecem conscientes após a estabilização da frente

## 10. Encaminhamento após a estabilização

Após a estabilização da frente:

- as dívidas que não impedem PR permanecem como dívida controlada
- os itens mais estratégicos e expansivos devem ser reavaliados para backlogização posterior
