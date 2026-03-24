# Contexto do Projeto

## 1. Regra de leitura deste contexto

Este documento resume o projeto com base em evidência combinada de:

- código inspecionado diretamente
- histórico Git analisado
- mensagens de commit
- issues GitHub
- documentação técnica e arquitetural existente

Para evitar confusão entre implementação e intenção, este contexto separa explicitamente:

- **estado atual**: o que está sustentado principalmente por código e histórico
- **transição**: mudanças reais já iniciadas, mas ainda incompletas
- **visão futura**: direção arquitetural documentada e/ou registrada em issues, ainda não confirmada como implementação suficiente

## 2. Estado atual do projeto

## 2.1 Identidade historicamente confirmada

Com base no histórico Git e no código atual, o projeto deve ser identificado, por enquanto, como **ShowTrials**.

Essa identificação é sustentada por:

- histórico inicial do repositório como aplicação específica
- commits de evolução funcional do sistema ShowTrials
- código centrado no domínio documental atual
- ausência, até esta etapa, de evidência suficiente de renomeação formal para outro nome

## 2.2 O que ShowTrials é hoje, com base em evidência

No estado atual confirmado por código e histórico, ShowTrials é melhor descrito como:

- uma aplicação Python voltada à organização e processamento de documentos históricos
- um sistema especializado, nas origens e no desenho atual, no acervo dos processos de Moscou e Leningrado
- uma base em camadas de `domain`, `application`, `infrastructure` e `interface`
- uma aplicação **documento-cêntrica**
- uma aplicação **orientada a persistência**
- uma aplicação **baseada em casos de uso imperativos**
- um sistema com **SQLite** como infraestrutura central observável
- um sistema com CLI claramente presente no código e aplicação Web também presente no repositório

Formulação importante:

- o projeto atual **não** deve ser descrito, com base no código já observado, como engine de pipeline já implementada

## 2.3 Missão operacional do sistema atual

A documentação, o histórico e o código convergem para um propósito operacional relativamente estável:

- reduzir o trabalho manual de pesquisa documental
- concentrar coleta, estruturação, tradução, análise e exportação em uma base única
- apoiar pesquisadores e historiadores na exploração de um acervo documental específico

Essa missão está alinhada ao que o sistema implementado já tentou resolver historicamente:

- scripts e protótipos iniciais de coleta e navegação
- posterior consolidação em aplicação estruturada
- ampliação para tradução, relatórios, análise textual e Web

## 2.4 Problema central que o projeto aborda

O problema central tratado pelo projeto continua sendo a fragmentação do trabalho de pesquisa documental.

O histórico do repositório sugere que, antes da estrutura atual, o trabalho estava distribuído entre:

- scripts
- código monolítico inicial
- operações manuais de tradução, organização e consulta

O ShowTrials implementado tenta consolidar esse trabalho em um sistema unificado para um caso documental concreto.

## 3. Evolução real do projeto

## 3.1 Fase inicial: protótipo funcional monolítico

O Git mostra que o projeto começou como:

- aplicação funcional incremental
- código concentrado na raiz do repositório
- uso prático de banco SQLite desde cedo
- interface terminal/Rich
- funcionalidade de tradução antes da arquitetura em camadas

Portanto, a origem real do projeto não é a de uma plataforma genérica, mas a de um sistema específico em evolução rápida.

## 3.2 Refatoração estrutural para arquitetura em camadas

Os commits de `FASE 1` a `FASE 4` marcam a transição para:

- domínio
- aplicação
- infraestrutura
- interface

Esse é o principal marco arquitetural já implementado no histórico.

Ele consolida o projeto como:

- sistema documento-cêntrico
- separado por responsabilidades
- com repositório SQLite
- com casos de uso orientados ao domínio atual

## 3.3 Expansão funcional do ShowTrials

Os commits históricos mostram ampliação real para:

- tradução
- exportação
- relatórios
- análise textual
- interface Web

Essa expansão confirma que o sistema atual é mais do que um protótipo inicial, mas continua dentro de uma lógica de:

- recuperar dados persistidos
- operar sobre `Documento`
- persistir resultados ou gerar artefatos

## 3.4 Endurecimento técnico e organizacional

O histórico Git também mostra uma fase real de:

- CI
- cobertura
- testes
- telemetria
- Taskipy
- documentação mais estruturada

Isso indica que o projeto deixou de ser apenas uma base experimental e passou a incorporar disciplina técnica mais explícita.

## 4. Transição em andamento

## 4.1 Transição arquitetural parcial já visível

O código atual e o histórico confirmam uma transição real, mas incompleta, em direção a maior modularidade.

Os sinais concretos mais importantes são:

- introdução de `ServiceRegistry`
- introdução de factories
- configuração por serviços
- lazy loading
- adaptação de alguns casos de uso para consumir serviços de forma menos direta

Esses elementos sustentam uma leitura de **transição em andamento**, não de arquitetura final já estabilizada.

## 4.2 O que essa transição já permite afirmar

Já é possível afirmar, com base em código e histórico, que:

- o projeto saiu de um modelo mais monolítico para uma estrutura em camadas
- o projeto depois começou a reduzir parte do acoplamento de criação de serviços
- existe tentativa real de preparar o sistema para maior modularidade

## 4.3 O que essa transição ainda não permite afirmar

Ainda **não** é possível afirmar, com segurança, que:

- a transição arquitetural terminou
- o sistema já funciona como engine de pipeline
- registry e factories equivalem a um sistema pleno de plugins
- transformação e persistência já foram separadas de forma arquitetural dominante

Em outras palavras:

- o repositório mostra sinais concretos de transição
- mas o centro do sistema observado ainda permanece no modelo ShowTrials atual

## 5. Visão futura confirmada por documentação e issues

## 5.1 Direção arquitetural futura

Os documentos de projeto e, principalmente, as issues abertas da milestone `MVP - Engine de Pipeline` confirmam uma visão futura clara:

- contratos de transformação
- contratos de sink
- contexto explícito de pipeline
- executor mínimo sequencial
- suporte a `Iterable` para streaming
- configuração externa via YAML/JSON
- versionamento de pipelines
- migração incremental de casos de uso reais

Essa direção aparece com evidência forte nas issues:

- `#10`
- `#11`
- `#12`
- `#13`
- `#14`
- `#15`
- `#16`
- `#17`

## 5.2 Natureza dessa visão futura

Essa visão futura deve ser tratada como:

- **direção arquitetural ativa**
- **backlog estratégico real**
- **roadmap com ancoragem em issues**

Mas não deve ser tratada, nesta etapa, como:

- implementação já concluída
- capacidade já dominante no código
- substituição já consumada da arquitetura atual

## 5.3 Relação com o sistema atual

A visão futura não surge do nada; ela parte de um sistema já existente.

O histórico e as issues sugerem uma estratégia de evolução:

- preservar a base atual onde necessário
- introduzir contratos mais gerais
- deslocar persistência para sinks
- migrar gradualmente fluxos existentes

Logo, o contexto correto não é “ShowTrials foi substituído”, mas sim:

- **ShowTrials atual como base implementada**
- **transição parcial em andamento**
- **engine de pipeline como alvo futuro formalizado**

## 6. ShowTrials, engine de pipeline e CraftText

## 6.1 ShowTrials

`ShowTrials` é, até aqui, o nome mais fortemente sustentado por:

- histórico Git
- código atual
- trajetória real do projeto

## 6.2 Engine de pipeline

A engine de pipeline é a formulação arquitetural futura mais claramente confirmada por:

- milestone ativa
- issues abertas
- documentação de direcionamento arquitetural

## 6.3 CraftText

`CraftText` não aparece, até esta etapa, com força equivalente de evidência em Git e issues.

O que pode ser dito com segurança:

- há documentação que permite inferir uma direção de plataforma mais ampla
- o nome `CraftText` pode funcionar como rótulo conceitual de direção futura em alguns materiais

O que **não** pode ser dito com segurança:

- que houve renomeação formal do projeto
- que `CraftText` já é identidade oficial consolidada do repositório
- que existe decisão registrada em issues formalizando a transição nominal `ShowTrials -> CraftText`

Conclusão prática:

- **ShowTrials** = sistema atual historicamente confirmado
- **engine de pipeline** = direção futura formalmente ativa
- **CraftText** = hipótese de nomenclatura futura ou conceito em formulação, ainda sem confirmação suficiente como fato consolidado

## 7. Regras de interpretação para futuras sessões

Sessões futuras devem aplicar as seguintes regras:

1. O sistema atual deve ser descrito primeiro pelo que está confirmado em código e histórico.
2. A arquitetura-alvo de pipeline deve ser tratada como visão futura ativa, salvo confirmação direta em código.
3. `ServiceRegistry` e factories devem ser interpretados como sinais de transição, não como prova de engine pronta.
4. Quando documentação e código divergirem, a análise deve separar explicitamente:
   - estado atual confirmado
   - transição parcial
   - visão futura
5. O nome `ShowTrials` deve permanecer como identificador principal até que Git, issues ou commits sustentem outra conclusão.
6. Qualquer menção a `CraftText` deve vir qualificada como hipótese, direção futura ou conceito em formulação, salvo nova evidência forte.

## 8. Cuidados para não confundir narrativa com implementação

Este projeto tem risco alto de mistura entre:

- documentação retrospectiva
- documentação aspiracional
- backlog estratégico
- implementação já existente

Para reduzir esse risco, aplicar sempre os seguintes cuidados:

### 8.1 Não equiparar fase documentada a maturidade comprovada

Uma fase documentada ou concluída no texto não prova automaticamente:

- cobertura funcional completa
- integração operacional plena
- ausência de placeholders
- aderência total à arquitetura descrita

### 8.2 Não equiparar issue aberta a capacidade entregue

Uma issue de engine confirma direção e intenção estratégica, mas não prova:

- presença da capacidade no código
- estabilidade de uso
- adoção dominante no sistema atual

### 8.3 Separar nome atual de nome futuro hipotético

O fato de existir visão de plataforma futura não autoriza concluir, sem mais evidência, que o repositório já deixou de ser ShowTrials.

### 8.4 Registrar incerteza como parte do contexto

Quando a evidência for insuficiente, registrar explicitamente:

- o que está confirmado
- o que está em transição
- o que está apenas planejado

## Estado de referência desta versão

Esta versão já incorpora:

- leitura da documentação base e arquitetural
- inspeção de arquivos centrais de código e configuração
- análise do histórico Git local
- análise por diretórios em `src/`, `docs/projeto/` e `docs/flows/`
- leitura das issues mais relevantes para arquitetura e governança

Ela ainda não incorpora, de forma exaustiva:

- inspeção completa de todo o repositório
- leitura de todos os PRs históricos
- validação por execução completa da aplicação e do pipeline de qualidade nesta sessão
