# Dívidas Técnicas e Documentais da Frente

## 1. Objetivo do documento

Este documento consolida as **dívidas técnicas e documentais** remanescentes da frente.

Seu objetivo é:

- reunir num único lugar os pontos ainda abertos
- separar dívidas de conteúdo, governança, arquitetura e Git
- facilitar decisão posterior sobre o que já pode ser atacado

## 2. Base de evidência utilizada

- [44_revisao_critica_final_da_frente.md](/home/thiago/coleta_showtrials/docs/modelagem/44_revisao_critica_final_da_frente.md)
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
- revisão de organização de diretórios e agrupamentos documentais
- revisão das primeiras rodadas do intervalo que ficaram mais fracas em governança

## 6. Dívidas de Git e governança

- reavaliar o histórico de commits desta frente como memória documental
- decidir se haverá apenas correção por cima ou algum saneamento histórico mais profundo
- garantir padrão estável de mensagem documental até o fechamento final da frente

## 7. Classificação preliminar

### 7.1 Atacáveis antes do PR

Tendem a ser atacáveis:

- normalizações documentais
- padronização de rodadas
- revisão de coerência e organização interna dos artefatos

### 7.2 Melhor tratadas como backlog futuro

Tendem a ser melhor tratadas depois:

- implementação real de background
- plugin system explícito
- separações físicas mais fortes

## 8. Inferências adotadas

- boa parte das dívidas remanescentes hoje é mais documental e de governança do que de conceito bruto
- a decisão sobre o que atacar antes do PR deve ser feita na revisão humana, não automaticamente

## 9. Suposições operacionais

- esta lista será usada como inventário base da fase de saneamento posterior

## 10. Próximos passos

- produzir a síntese executiva da frente
