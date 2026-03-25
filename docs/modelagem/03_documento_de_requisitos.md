# Documento de Requisitos — Documento Integrador

## 1. Introdução

Este documento consolida a frente de elicitação e análise de requisitos da nova trilha de **Modelagem, Análise e Padrões de Projeto** do projeto historicamente conhecido como **ShowTrials**.

Seu papel não é substituir os insumos já produzidos sobre o sistema atual e sobre a evolução para engine. Seu papel é integrar, organizar e priorizar esses insumos para sustentar os próximos artefatos da frente, especialmente:

- casos de uso
- visão arquitetural 4+1
- modelo C4
- UML complementar
- rastreabilidade futura com backlog e issues

## 2. Objetivo do documento

Este documento tem como objetivos:

- consolidar a base atual de requisitos da frente
- separar explicitamente sistema atual, transição e sistema-alvo
- registrar stakeholders, atores, problemas, restrições e prioridades
- integrar os requisitos já identificados no sistema atual e na evolução para engine
- preparar a derivação posterior de casos de uso e artefatos arquiteturais

## 3. Escopo e recorte da frente

O recorte adotado neste documento é composto por três planos complementares:

### 3.1 Sistema atual

O sistema atual corresponde ao projeto historicamente conhecido como **ShowTrials**, concebido inicialmente como ferramenta para coletar, armazenar, traduzir, consultar e analisar documentos digitalizados.

### 3.2 Transição arquitetural

A transição corresponde à evolução incremental dessa aplicação documento-cêntrica para uma arquitetura mais configurável, modular e orientada a pipelines, sem reescrever o projeto do zero.

### 3.3 Sistema-alvo

O sistema-alvo corresponde a uma engine ou plataforma configurável de processamento documental, capaz de combinar fontes, processadores e sinks em fluxos de trabalho ajustados ao objetivo do usuário.

## 4. Base de evidência e documentos de apoio

Este documento se apoia explicitamente nos seguintes insumos principais:

- [01_documento_de_requisitos_showtrials_atual.md](/home/thiago/coleta_showtrials/docs/modelagem/insumos/01_documento_de_requisitos_showtrials_atual.md)
- [02_documento_de_requisitos_evolucao_engine.md](/home/thiago/coleta_showtrials/docs/modelagem/insumos/02_documento_de_requisitos_evolucao_engine.md)

Também utiliza como base complementar:

- documentos de contexto em `docs/ai/`
- documentos de fase do projeto
- código central do sistema
- histórico Git consolidado
- issues da trilha de evolução para engine

Função metodológica deste documento:

- o documento do ShowTrials atual consolida a leitura retrospectiva do sistema implementado
- o documento da evolução para engine consolida a leitura prospectiva do sistema-alvo
- este documento integra, compara, organiza e prioriza esses dois planos

## 5. Nomenclatura e glossário inicial

### 5.1 Observação sobre nomenclatura

O nome do sistema ainda não está definitivamente consolidado para esta nova frente.

Situação atual:

- `ShowTrials` é o nome histórico e mais fortemente ligado ao sistema implementado
- `CraftText` foi considerado como nome possível para a fase de engine, mas ainda não está consolidado
- a nomenclatura futura permanece em aberto

Para fins deste documento:

- `ShowTrials` será usado como nome do sistema atual
- `engine futura` será usada como designação provisória da arquitetura-alvo

### 5.2 Glossário inicial

- `ShowTrials`: nome histórico do sistema atual implementado
- `engine futura`: arquitetura-alvo configurável de processamento documental
- `pipeline`: fluxo configurável de execução composto por etapas ordenadas
- `step`: etapa individual de um pipeline
- `source`: componente responsável por obtenção ou entrada de dados documentais
- `processor`: componente responsável por transformação ou análise de dados
- `sink`: componente responsável por persistência, exportação ou saída dos resultados
- `acervo`: conjunto persistido de documentos e produtos derivados
- `colecao tematica`: agrupamento documental definido por critério temático ou analítico
- `usuario pesquisador/historiador`: ator principal do sistema atual, orientado ao trabalho sobre documentos
- `usuario configurador`: ator principal do sistema futuro, orientado à composição de fluxos
- `contexto de pipeline`: estrutura de execução que transporta documentos, artefatos e estado ao longo do pipeline
- `produto derivado`: resultado adicional gerado pelo processamento de um documento, como tradução, análise ou visualização

## 6. Stakeholders e atores

### 6.1 Stakeholders

Os stakeholders iniciais identificados são:

- autor/desenvolvedor do projeto
- usuario pesquisador/historiador
- usuario geral que trabalha com documentos digitalizados
- usuario configurador da engine
- mantenedor futuro do sistema
- banca/professor, como stakeholder academico indireto

### 6.2 Perfis de ator

#### 6.2.1 Ator principal do sistema atual

No sistema atual, o ator principal é o **usuario pesquisador/historiador**, que utiliza o sistema para coletar, armazenar, consultar, traduzir e analisar documentos.

#### 6.2.2 Ator principal do sistema futuro

No sistema futuro, o ator principal tende a ser o **usuario configurador da engine**, responsavel por ajustar ferramentas, fluxos e pipelines conforme o objetivo da tarefa.

Essa mudanca nao elimina o ator anterior. Em vez disso, indica uma evolucao do perfil de uso:

- o usuario do sistema passa a precisar tambem de capacidade de configuracao e composicao de fluxos

## 7. Problema e motivação

### 7.1 Problema resolvido pelo sistema atual

O sistema atual surgiu para apoiar o estudo de documentos digitalizados, em especial documentos em russo, fornecendo ferramentas para:

- coleta de textos a partir de fontes digitais
- persistencia dos conteudos para uso posterior
- traducao
- consulta ao acervo
- analises basicas sobre os documentos

O problema central do ShowTrials atual e a necessidade de **ler, manipular, extrair e analisar informacoes de documentos digitalizados** com menos trabalho manual e mais apoio computacional.

### 7.2 Motivacao da evolucao arquitetural

A evolucao para engine nao nasce apenas de insuficiencias tecnicas tradicionais, mas sobretudo de:

- necessidade de maior ergonomia dos fluxos de trabalho
- necessidade de compor ferramentas diferentes conforme o objetivo do usuario
- necessidade de suportar novas fontes e novos processos
- necessidade de carregar apenas os recursos necessarios
- necessidade de reduzir custo de inicializacao e consumo de memoria
- necessidade de tornar a arquitetura mais configuravel e reutilizavel

A introducao de `ServiceRegistry` com lazy loading foi um passo concreto nessa direcao e reforcou a percepcao de que o projeto pode evoluir para uma arquitetura mais flexivel.

## 8. Sistema atual: ShowTrials

As capacidades atuais mais relevantes identificadas ate aqui sao:

- coleta de texto de sites
- extracao de texto a partir de documentos txt
- traducao de documentos com API do Google
- persistencia em banco de dados
- suporte a NLP
- consultas ao acervo
- interface CLI
- interface Web com FastAPI

O sistema atual deve ser entendido como uma base funcional e util, mas com maturidade desigual entre suas capacidades. A traducao aparece como area mais satisfatoria, enquanto coleta, extracao, consultas mais amplas, Web e generalizacao arquitetural ainda conservam carater de MVP ou prova de conceito.

## 9. Limitações do sistema atual

As principais limitacoes estruturais observadas sao:

- arquitetura dominante ainda documento-centrica e orientada a persistencia
- pouca generalidade para multiplas fontes e processos
- forte orquestracao imperativa em casos de uso
- dificuldade de compor fluxos diferentes sem reuso ad hoc
- maturidade desigual entre CLI e Web
- ausencia de modelo dominante de pipeline configuravel

Essas limitacoes nao anulam o valor do sistema atual. Elas explicam por que a evolucao para engine se tornou desejavel.

## 10. Transição arquitetural

A transicao arquitetural deve:

- ocorrer de forma incremental, sem reescrita total
- preservar continuidade com a base atual do projeto
- manter CLI e Web como interfaces relevantes
- introduzir separacao mais clara entre transformacao e persistencia
- permitir migracao gradual de fluxos reais do ShowTrials para a nova arquitetura
- usar a base atual como origem de migracao, e nao como descartavel

Essa transicao e um plano proprio dentro da frente de requisitos. Ela nao se reduz ao sistema atual nem coincide integralmente com o sistema-alvo.

## 11. Sistema-alvo: engine futura

A engine futura deve ser capaz de apoiar diferentes tarefas documentais por meio de recursos configuraveis.

Capacidades desejadas mencionadas ate aqui:

- compatibilidade com multiplos bancos de dados
- OCR
- raspagem de sites
- extracao de texto de PDF
- manipulacao de PDF
- tratamento de imagens para apoiar OCR
- traducao robusta com fallbacks
- analises NLP e estatisticas
- criacao de colecoes tematicas
- arvores de relacionamento
- visualizacoes e graficos
- carregamento configuravel e sob demanda
- execucao nao bloqueante
- processos e filas em segundo plano
- distribuicao em versoes distintas, como Web-only ou completa com CLI

No nivel arquitetural, o sistema-alvo ja possui direcao suficientemente clara para modelagem:

- configuracao externa de pipelines
- uso de contexto explicito de execucao
- separacao entre sources, processors e sinks
- deslocamento da persistencia para sinks
- pipeline linear minimo no MVP
- suporte futuro a `Iterable` e evolucoes mais amplas

## 12. Requisitos funcionais integrados

Os requisitos funcionais abaixo estao organizados por blocos para integrar sistema atual, transicao e sistema-alvo.

### 12.1 Aquisicao documental

- o sistema deve permitir coletar ou obter conteudo textual a partir de fontes documentais digitais
- o sistema deve permitir obter conteudo a partir de paginas web, arquivos textuais, PDFs e imagens, conforme o grau de maturidade da arquitetura
- o sistema futuro deve suportar OCR e novas formas de entrada documental de maneira configuravel

### 12.2 Persistencia e organizacao

- o sistema deve permitir persistir documentos e metadados principais
- o sistema deve permitir persistir traducoes associadas aos documentos
- o sistema deve permitir persistir produtos derivados de processamento e analise
- o sistema futuro deve permitir multiplos destinos de persistencia e saida

### 12.3 Consulta e uso do acervo

- o sistema deve permitir consultar documentos e conteudos persistidos
- o sistema deve permitir listar documentos, traducoes e resultados associados
- o sistema deve permitir evolucao futura para colecoes tematicas e relacoes documentais mais ricas

### 12.4 Traducao

- o sistema deve permitir traduzir documentos
- o sistema deve permitir persistir traducoes
- o sistema futuro deve permitir traducao robusta com fallbacks
- o sistema futuro deve permitir evolucao para traducao segmentada e revisao de traducao

### 12.5 Analise e enriquecimento

- o sistema deve permitir aplicar ferramentas de analise textual e estatistica aos documentos
- o sistema deve permitir extracao de entidades e outros produtos analiticos
- o sistema futuro deve permitir compor etapas de NLP, estatistica, classificacao e enriquecimento no pipeline

### 12.6 Configuracao de pipeline

- o sistema futuro deve permitir configurar diferentes fluxos de trabalho documentais
- o sistema futuro deve permitir representar pipelines por configuracao externa
- o sistema futuro deve permitir salvar, recuperar e versionar configuracoes de pipeline
- o sistema futuro deve permitir carregar apenas os servicos necessarios para uma determinada execucao

### 12.7 Execucao de pipeline

- o sistema futuro deve permitir compor pipelines com ferramentas distintas conforme o objetivo do usuario
- o sistema futuro deve permitir combinar etapas como coleta, OCR, traducao, analise, persistencia e exportacao
- o sistema futuro deve possuir contexto explicito de execucao
- o sistema futuro deve permitir evolucao para tarefas em segundo plano, filas e execucao nao bloqueante

### 12.8 Persistencia e saida no sistema-alvo

- o sistema futuro deve permitir concentrar persistencia e exportacao em sinks
- o sistema futuro deve permitir persistir documentos e produtos derivados sem acoplar essa responsabilidade aos transformadores
- o sistema futuro deve permitir saidas diversas, incluindo banco de dados e artefatos exportaveis

### 12.9 Operacao e interfaces

- o sistema deve preservar CLI como interface relevante
- o sistema deve preservar Web como interface relevante
- o sistema futuro deve permitir diferentes distribuicoes do produto, como versao Web-only e versao completa com CLI

## 13. Requisitos não funcionais integrados

### 13.1 Usabilidade

- o sistema deve buscar facilidade de uso para o trabalho documental
- o sistema futuro deve favorecer ergonomia na configuracao e execucao dos fluxos
- a combinacao de flexibilidade e facilidade de uso deve ser perseguida como diretriz de produto

### 13.2 Desempenho e consumo de recursos

- o sistema deve permitir uso eficiente de recursos
- a arquitetura futura deve evitar carregamento desnecessario de servicos pesados
- o carregamento sob demanda deve ser favorecido quando aplicavel

### 13.3 Modularidade e extensibilidade

- a arquitetura futura deve favorecer extensibilidade e composicao de ferramentas
- o sistema deve favorecer modularidade e reuso de componentes
- a evolucao deve apoiar incorporacao de novas fontes, processadores e sinks

### 13.4 Manutenibilidade

- o sistema deve buscar facilidade de manutencao
- a arquitetura deve preservar separacao de responsabilidades
- a evolucao deve favorecer testabilidade e clareza das responsabilidades

### 13.5 Configurabilidade

- o sistema futuro deve ser configuravel de forma explicita e reproduzivel
- as configuracoes de pipeline devem ser claras o suficiente para reutilizacao e governanca futura

### 13.6 Compatibilidade evolutiva

- o sistema deve manter evolucao incremental sem reescrita completa do zero
- o sistema deve preservar, tanto quanto possivel, continuidade com a base atual do projeto
- a transicao nao deve tornar imediatamente obsoletas as capacidades centrais ja existentes

### 13.7 Documentacao e rastreabilidade

- a documentacao do sistema deve ser forte o suficiente para apoiar desenvolvimento, manutencao e avaliacao academica
- a evolucao da frente deve manter rastreabilidade entre rodadas, documentos e proximos artefatos

### 13.8 Tecnologia e plataforma

- o sistema deve permanecer em Python
- CLI e Web devem continuar como partes relevantes da solucao
- a base atual deve ser preservada como origem de migracao para a arquitetura futura

## 14. Requisitos de transição

Os requisitos de transicao abaixo sao centrais no projeto:

- a evolucao deve ocorrer de forma incremental
- a base atual do ShowTrials deve servir como origem de migracao para a nova arquitetura
- pelo menos um fluxo real ja existente deve poder ser migrado para a execucao orientada por pipeline
- CLI e Web devem permanecer validas durante a transicao
- a separacao entre transformacao e persistencia deve ser introduzida sem apagar de imediato os casos de uso atuais
- casos de uso e componentes atuais podem atuar como adaptadores durante a transicao

## 15. Restrições

As restricoes identificadas ate aqui sao:

- esta fase e de modelagem e documentacao, nao de implementacao
- o projeto deve manter aderencia a governanca ja consolidada
- a evolucao deve ser incremental
- o projeto nao deve ser reescrito do zero
- os artefatos academicos devem ser produzidos com rigor e profundidade
- o prazo final do projeto e novembro de 2026

## 16. Fora de escopo

Nesta fase especifica, ficam fora de escopo:

- implementacao imediata da engine
- reescrita do codigo de produto
- substituicao completa da base atual
- decisoes finais de branding ou nome do sistema
- refinamento tecnico detalhado de todos os diagramas antes da analise de requisitos
- execucao distribuida e outras capacidades avancadas antes da consolidacao do MVP estrutural

## 17. Priorização inicial

### 17.1 Essencial para o sistema atual

- persistencia documental
- traducao
- consulta ao acervo
- analise textual e estatistica basica
- preservacao de CLI e Web como interfaces relevantes

### 17.2 Essencial para a transicao

- evolucao incremental sem reescrita total
- preservacao da base atual como origem de migracao
- separacao crescente entre transformacao e persistencia
- introducao de contexto de execucao e composicao mais clara de fluxos

### 17.3 Essencial para o MVP da engine

- pipeline configuravel
- configuracao externa
- composicao de steps
- suporte minimo a sources, processors e sinks
- carregamento sob demanda de servicos
- migracao de pelo menos um fluxo real para a nova arquitetura

### 17.4 Desejavel depois

- multiplos bancos como capacidade mais madura
- visualizacoes e grafos mais ricos
- colecoes tematicas mais sofisticadas
- filas e operacao em background mais robustas
- distribuicoes de produto mais refinadas

### 17.5 Fora do escopo atual

- implementacao imediata de toda a engine
- fechamento definitivo de branding
- exploracao detalhada de todos os diagramas antes de consolidar requisitos

## 18. Relação preliminar com casos de uso

Os requisitos ja permitem antecipar candidatos fortes a casos de uso:

- coletar ou acessar conteudo documental
- consultar acervo documental
- traduzir documento
- analisar documento
- analisar acervo
- configurar pipeline
- executar pipeline
- revisar traducao segmentada
- processar PDF com OCR

Essa relacao ainda e preliminar e sera detalhada em artefato proprio posterior.

## 19. Relação preliminar com arquitetura futura

Os requisitos levantados ja apontam drivers claros para os proximos artefatos arquiteturais:

- a necessidade de separar sistema atual, transicao e sistema-alvo dialoga com a visao 4+1
- a necessidade de explicitar interfaces, containers e componentes dialoga com o modelo C4
- a necessidade de configurar e executar pipelines aponta para modelagem mais detalhada de componentes como contexto, sources, processors e sinks

Este documento, portanto, passa a funcionar como base de requisitos para os proximos documentos de arquitetura.

## 20. Questões em aberto

Ainda precisam ser definidas ou refinadas:

- nome oficial do sistema ou da arquitetura-alvo
- ampliacao e estabilizacao do glossario formal do projeto
- fronteira exata do sistema em cada tipo de artefato
- priorizacao mais detalhada dos requisitos da engine
- definicao mais precisa do MVP da engine
- relacao futura entre requisitos, casos de uso e backlog tecnico

## 21. Próximos passos

Os proximos passos recomendados sao:

- consolidar esta versao integradora do Documento de Requisitos
- usar este documento como base para abrir a frente de casos de uso
- derivar mapa inicial de atores e casos de uso
- preparar, em seguida, os artefatos de arquitetura 4+1 e C4

Este documento nao encerra a frente de requisitos. Ele estabelece uma base mais rigorosa e mais util para a evolucao disciplinada dos proximos artefatos.
