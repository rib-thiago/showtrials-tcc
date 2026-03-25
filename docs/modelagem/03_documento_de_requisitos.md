# Documento de Requisitos — Versão Inicial

## 1. Introdução

Este documento inicia a elicitação e análise de requisitos da nova frente de **Modelagem, Análise e Padrões de Projeto** do projeto historicamente conhecido como **ShowTrials**.

O objetivo desta frente não é apenas produzir artefatos acadêmicos isolados. O objetivo é estruturar, com rigor técnico e acadêmico, a evolução do sistema atual em direção a uma arquitetura mais configurável, orientada a pipelines e capaz de combinar diferentes ferramentas de processamento documental.

Este documento não trata apenas do sistema futuro. Ele organiza três dimensões complementares:

- o sistema atual implementado
- a transição arquitetural pretendida
- o sistema-alvo futuro

## 2. Objetivo do documento

Este documento tem como objetivos:

- registrar os requisitos iniciais do sistema
- explicitar stakeholders, objetivos e restrições
- descrever o problema que o sistema resolve hoje
- descrever o problema adicional que a evolução para engine pretende resolver
- criar base para:
  - casos de uso
  - visão arquitetural 4+1
  - modelo C4
  - UML complementar
  - rastreabilidade futura com backlog e issues

## 3. Escopo do sistema

O escopo desta frente não se limita ao ShowTrials atual nem apenas à engine futura.

O recorte adotado neste documento é composto por três planos:

### 3.1 Sistema atual

O sistema atual corresponde ao projeto historicamente conhecido como **ShowTrials**, concebido inicialmente como ferramenta para extrair e manipular conteúdos obtidos a partir do site `showtrials.ru` e de documentos digitalizados.

### 3.2 Evolução do sistema

A evolução do sistema corresponde à transformação progressiva dessa aplicação documento-cêntrica em uma arquitetura mais configurável, flexível e orientada a fluxos de trabalho.

### 3.3 Sistema-alvo

O sistema-alvo corresponde a uma engine ou plataforma configurável de processamento documental, capaz de combinar serviços e ferramentas em pipelines adequados a diferentes tarefas e contextos de uso.

## 4. Observação sobre nomenclatura

O nome do sistema ainda não está definitivamente consolidado para esta nova frente.

Situação atual:

- `ShowTrials` é o nome histórico e mais fortemente ligado ao sistema implementado
- `CraftText` foi considerado como nome possível para a fase de engine, mas ainda não está consolidado
- a nomenclatura futura permanece em aberto

Para fins deste documento:

- `ShowTrials` será usado como nome do sistema atual
- `engine futura` será usada como designação provisória da arquitetura-alvo

## 5. Problema e motivação

### 5.1 Problema resolvido pelo sistema atual

O sistema atual surgiu para apoiar o estudo de documentos digitalizados, em especial documentos em russo, fornecendo ferramentas para:

- coleta de textos a partir de fontes digitais
- persistência dos conteúdos para uso posterior
- tradução
- consulta ao acervo
- análises básicas sobre os documentos

O problema central do ShowTrials atual é a necessidade de **ler, manipular, extrair e analisar informações de documentos digitalizados** com menos trabalho manual e mais apoio computacional.

### 5.2 Motivação da evolução arquitetural

A evolução para engine não nasce apenas de insuficiências técnicas tradicionais, mas sobretudo de:

- necessidade de maior ergonomia dos fluxos de trabalho
- necessidade de compor ferramentas diferentes conforme o objetivo do usuário
- necessidade de suportar novas fontes e novos processos
- necessidade de carregar apenas os recursos necessários
- necessidade de reduzir custo de inicialização e consumo de memória
- necessidade de tornar a arquitetura mais configurável e reutilizável

A introdução de `ServiceRegistry` com lazy loading foi um passo concreto nessa direção e reforçou a percepção de que o projeto pode evoluir para uma arquitetura mais flexível.

## 6. Stakeholders

Os stakeholders iniciais identificados são:

- autor/desenvolvedor do projeto
- usuário pesquisador/historiador
- usuário geral que trabalha com documentos digitalizados
- usuário configurador da engine
- mantenedor futuro do sistema
- banca/professor, como stakeholder acadêmico indireto

## 7. Perfis de ator

### 7.1 Ator principal do sistema atual

No sistema atual, o ator principal é o **usuário pesquisador/historiador**, que utiliza o sistema para coletar, armazenar, consultar, traduzir e analisar documentos.

### 7.2 Ator principal do sistema futuro

No sistema futuro, o ator principal tende a ser o **usuário configurador da engine**, responsável por ajustar ferramentas, fluxos e pipelines conforme o objetivo da tarefa.

Entretanto, essa mudança não elimina o ator anterior. Em vez disso, indica uma evolução do perfil de uso:

- o usuário do sistema passa a precisar também de capacidade de configuração e composição de fluxos

## 8. Objetivos dos usuários

Os objetivos principais identificados são:

### 8.1 No sistema atual

- coletar conteúdos de fontes digitais
- extrair texto de documentos
- persistir conteúdo para uso futuro
- consultar o acervo documental
- traduzir documentos
- consultar traduções
- realizar análises estatísticas e linguísticas básicas

### 8.2 No sistema futuro

- configurar ferramentas conforme o objetivo da tarefa
- selecionar quais serviços devem ser usados
- compor fluxos de trabalho configuráveis
- executar pipelines diferentes para tarefas diferentes
- reutilizar recursos de processamento documental de forma flexível
- manter o sistema usável, robusto e bem documentado

## 9. Capacidades centrais do sistema atual

As capacidades atuais mais relevantes são:

- coleta de texto de sites
- extração de texto a partir de documentos txt
- tradução de documentos com API do Google
- persistência em banco de dados
- suporte a NLP
- consultas ao acervo
- interface CLI
- interface Web com FastAPI

## 10. Estado percebido das capacidades atuais

### 10.1 Capacidade mais satisfatória

- tradução de textos

### 10.2 Capacidades mais limitadas ou frágeis

- coleta
- extração
- consultas mais amplas ao acervo
- uso da Web
- integração mais madura entre recursos
- generalização arquitetural das funcionalidades

O sistema atual deve ser entendido como MVP ou prova de conceito em várias dessas dimensões.

## 11. Necessidades da engine futura

A engine futura deve ser capaz de apoiar diferentes tarefas documentais por meio de recursos configuráveis.

Capacidades desejadas mencionadas até aqui:

- compatibilidade com múltiplos bancos de dados
- OCR
- raspagem de sites
- extração de texto de PDF
- manipulação de PDF
- tratamento de imagens para apoiar OCR
- tradução robusta com fallbacks
- análises NLP e estatísticas
- criação de coleções temáticas
- árvores de relacionamento
- visualizações e gráficos
- carregamento configurável e sob demanda
- execução não bloqueante
- processos e filas em segundo plano
- distribuição em versões distintas, como Web-only ou completa com CLI

## 12. Requisitos funcionais iniciais

Os requisitos abaixo são iniciais e ainda deverão ser refinados.

### RF01

O sistema deve permitir coletar ou obter conteúdo textual a partir de fontes documentais digitais.

### RF02

O sistema deve permitir persistir conteúdos documentais e produtos derivados em banco de dados.

### RF03

O sistema deve permitir consultar documentos e conteúdos persistidos.

### RF04

O sistema deve permitir traduzir documentos e persistir traduções.

### RF05

O sistema deve permitir aplicar ferramentas de análise textual e estatística aos documentos.

### RF06

O sistema futuro deve permitir configurar diferentes fluxos de trabalho documentais.

### RF07

O sistema futuro deve permitir compor pipelines com ferramentas distintas conforme o objetivo do usuário.

### RF08

O sistema futuro deve permitir carregar apenas os serviços necessários para uma determinada execução.

### RF09

O sistema futuro deve permitir combinar etapas como coleta, OCR, tradução, análise, persistência e exportação.

### RF10

O sistema futuro deve permitir tratar diferentes tipos de entrada documental, como páginas web, PDFs e imagens.

### RF11

O sistema futuro deve permitir persistir não apenas documentos, mas também produtos de processamento e análise.

### RF12

O sistema futuro deve permitir executar tarefas em segundo plano, sem bloquear o uso do sistema.

## 13. Requisitos não funcionais iniciais

### RNF01

O sistema deve manter evolução incremental sem reescrita completa do zero.

### RNF02

O sistema deve preservar, tanto quanto possível, continuidade com a base atual do projeto.

### RNF03

O sistema deve permanecer em Python.

### RNF04

O sistema deve preservar interfaces CLI e Web como partes relevantes da solução.

### RNF05

O sistema futuro deve ser configurável e ergonomicamente utilizável.

### RNF06

O sistema deve buscar facilidade de manutenção.

### RNF07

A arquitetura futura deve favorecer extensibilidade e composição de ferramentas.

### RNF08

A documentação do sistema deve ser forte o suficiente para apoiar desenvolvimento, manutenção e avaliação acadêmica.

### RNF09

O sistema deve permitir uso eficiente de recursos, evitando carregamento desnecessário de serviços pesados.

## 14. Restrições

As restrições identificadas até aqui são:

- esta fase é de modelagem e documentação, não de implementação
- o projeto deve manter aderência à governança já consolidada
- a evolução deve ser incremental
- o projeto não deve ser reescrito do zero
- os artefatos acadêmicos devem ser produzidos com rigor e profundidade
- o prazo final do projeto é novembro de 2026

## 15. Fora de escopo desta fase

Nesta fase específica, ficam fora de escopo:

- implementação imediata da engine
- reescrita do código de produto
- substituição completa da base atual
- decisões finais de branding ou nome do sistema
- refinamento técnico detalhado de todos os diagramas antes da análise de requisitos

## 16. Questões em aberto

Ainda precisam ser definidas ou refinadas:

- nome oficial do sistema ou da arquitetura-alvo
- glossário formal do projeto
- fronteira exata do sistema em cada tipo de artefato
- priorização detalhada dos requisitos da engine
- definição mais precisa do MVP da engine
- relação futura entre requisitos e backlog técnico

## 17. Próximo passo recomendado

O próximo passo recomendado é:

- consolidar esta primeira elicitação
- transformar esta base em uma versão mais estruturada do Documento de Requisitos
- derivar:
  - glossário inicial
  - stakeholders e atores
  - primeiro conjunto organizado de requisitos
- só então avançar para:
  - casos de uso
  - diagrama de casos de uso
  - 4+1
  - C4
