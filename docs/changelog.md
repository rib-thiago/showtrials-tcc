# Changelog

Este changelog registra marcos notaveis da evolucao do projeto.

Ele complementa, mas nao substitui, o historico detalhado distribuido entre Git, documentos de fase e documentos de rodada. Na ausencia de um regime rigidamente sustentado de releases versionadas, as entradas abaixo sao organizadas por marcos historicos relevantes do projeto.

## Em andamento

### Documentacao

- consolidacao do saneamento dos blocos `docs/flows/` e `docs/projeto/`;
- conclusao do saneamento dos principais documentos publicos de entrada;
- preparacao para revisao das fases historicas antigas.

## 2026-03-27 - Saneamento documental legado e consolidacao semantica

### Documentacao

- saneamento profundo do bloco `docs/flows/`, com estabilizacao de politicas, protocolos e guias operacionais;
- saneamento e reclassificacao do bloco principal de `docs/projeto/`, separando documentos vivos, documentos historicos e documentos de transicao;
- formalizacao do regime documental entre fases e rodadas em [regime_documental_de_fases_e_rodadas.md](/home/thiago/coleta_showtrials/docs/projeto/regime_documental_de_fases_e_rodadas.md);
- consolidacao de guias transversais como [guia_de_documentacao_do_projeto.md](/home/thiago/coleta_showtrials/docs/flows/guia_de_documentacao_do_projeto.md) e [guia_de_manutencao_do_site_documental.md](/home/thiago/coleta_showtrials/docs/flows/guia_de_manutencao_do_site_documental.md);
- reclassificacao de artefatos historicos e preparatorios, como o plano de issues da documentacao e o questionario de levantamento de requisitos.

### Operacao

- consolidacao do nucleo normativo e operacional de governanca, Git, qualidade, Projects CLI, auto-revisao, debug, dependencias, refatoracao, telemetria e correcao urgente;
- estabilizacao metodologica da frente de saneamento documental legado com criterio explicito de encerramento, matriz semantica e padrao minimo documental.

### Rastreabilidade

- [FASE18_CONSOLIDACAO_DA_GOVERNANCA.md](/home/thiago/coleta_showtrials/docs/fases/FASE18_CONSOLIDACAO_DA_GOVERNANCA.md)
- [FASE19_CONSOLIDACAO_DO_FLUXO_DE_QUALIDADE.md](/home/thiago/coleta_showtrials/docs/fases/FASE19_CONSOLIDACAO_DO_FLUXO_DE_QUALIDADE.md)
- rodadas `32` a `52` em [docs/planejamento/rodadas/](/home/thiago/coleta_showtrials/docs/planejamento/rodadas)

## 2026-03-26 - Frente de modelagem, analise e padroes

### Arquitetura

- consolidacao do documento integrador de requisitos, dos drivers arquiteturais e das decisoes iniciais da evolucao para a engine;
- materializacao dos blocos `4+1`, `C4` e de um subconjunto estrategico do UML complementar;
- consolidacao de um corpo inicial de analise de padroes de projeto, trade-offs e riscos de overengineering.

### Documentacao

- reorganizacao da frente de modelagem por fase de engenharia;
- criacao de indice geral navegavel, sintese executiva, conferencia de aderencia ao projeto real e documento de saneamento da frente;
- formalizacao de [politica_de_diagramas_versionaveis.md](/home/thiago/coleta_showtrials/docs/projeto/politica_de_diagramas_versionaveis.md) e integracao de diagramas renderizados para leitura no GitHub.

### Rastreabilidade

- [47_indice_geral_da_frente_de_modelagem.md](/home/thiago/coleta_showtrials/docs/modelagem/revisao/47_indice_geral_da_frente_de_modelagem.md)
- [46_sintese_executiva_da_frente.md](/home/thiago/coleta_showtrials/docs/modelagem/revisao/46_sintese_executiva_da_frente.md)
- bloco `docs/modelagem/`

## 2026-02-20 a 2026-02-22 - Reorganizacao documental inicial

### Documentacao

- reorganizacao inicial da arvore de `docs/`, com separacao entre fases, metricas, projeto e flows;
- consolidacao do primeiro grande esforco de padronizacao da documentacao do projeto;
- criacao de template de fases e de script de verificacao para historicos documentais;
- atualizacao inicial de navegacao e referencias internas do conjunto documental.

### Rastreabilidade

- [FASE17.md](/home/thiago/coleta_showtrials/docs/fases/FASE17.md)

## 2026-02-17 a 2026-02-19 - Estabilizacao tecnica inicial

### Arquitetura

- introducao de `Service Registry` com lazy loading para gerenciamento centralizado de servicos;
- consolidacao de uma configuracao mais estruturada para o crescimento tecnico do sistema.

### Qualidade

- implantacao inicial de GitHub Actions, verificacoes de cobertura e ferramentas de automacao do ambiente de desenvolvimento;
- expansao da testabilidade e endurecimento tecnico em torno de telemetria.

### Correcao

- estabilizacao do CI com workaround para dependencias NLP no pipeline;
- correcoes incrementais de telemetria e testes em componentes importantes do sistema.

### Rastreabilidade

- [FASE10_SERVICE_REGISTRY.md](/home/thiago/coleta_showtrials/docs/fases/FASE10_SERVICE_REGISTRY.md)
- [FASE11_CI.md](/home/thiago/coleta_showtrials/docs/fases/FASE11_CI.md)
- [FASE12.md](/home/thiago/coleta_showtrials/docs/fases/FASE12.md)
- [FASE13.md](/home/thiago/coleta_showtrials/docs/fases/FASE13.md)
- [FASE14.md](/home/thiago/coleta_showtrials/docs/fases/FASE14.md)
- [FASE15.md](/home/thiago/coleta_showtrials/docs/fases/FASE15.md)
- [FASE16.md](/home/thiago/coleta_showtrials/docs/fases/FASE16.md)

## 2026-02-15 a 2026-02-16 - Fundacao do sistema atual

### Arquitetura

- implementacao inicial da estrutura em camadas com dominio, aplicacao, infraestrutura e interfaces;
- consolidacao da base arquitetural do sistema atual orientado a coleta, traducao, analise e visualizacao de documentos historicos.

### Funcionalidades

- coleta e armazenamento estruturado de documentos;
- classificacao por tipo, traducao, exportacao e geracao de relatorios;
- analise de texto com foco em entidades e estatisticas;
- disponibilizacao de interface CLI e interface web.

### Qualidade

- introducao do conjunto inicial de testes automatizados que acompanhou as primeiras fases do sistema.

### Rastreabilidade

- [FASE1_DOMAIN.md](/home/thiago/coleta_showtrials/docs/fases/FASE1_DOMAIN.md)
- [FASE2_APPLICATION.md](/home/thiago/coleta_showtrials/docs/fases/FASE2_APPLICATION.md)
- [FASE3_INFRASTRUCTURE.md](/home/thiago/coleta_showtrials/docs/fases/FASE3_INFRASTRUCTURE.md)
- [FASE4_CLI.md](/home/thiago/coleta_showtrials/docs/fases/FASE4_CLI.md)
- [FASE5_TRADUCAO.md](/home/thiago/coleta_showtrials/docs/fases/FASE5_TRADUCAO.md)
- [FASE6_EXPORTACAO.md](/home/thiago/coleta_showtrials/docs/fases/FASE6_EXPORTACAO.md)
- [FASE7_RELATORIOS.md](/home/thiago/coleta_showtrials/docs/fases/FASE7_RELATORIOS.md)
- [FASE8_ANALISE_TEXTO.md](/home/thiago/coleta_showtrials/docs/fases/FASE8_ANALISE_TEXTO.md)
- [FASE9_WEB_INTERFACE.md](/home/thiago/coleta_showtrials/docs/fases/FASE9_WEB_INTERFACE.md)
