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
- consolidacao de guias transversais como [guia_de_documentacao_do_projeto.md](/home/thiago/coleta_showtrials/docs/guias/guia_de_documentacao_do_projeto.md) e [guia_de_manutencao_do_site_documental.md](/home/thiago/coleta_showtrials/docs/guias/guia_de_manutencao_do_site_documental.md);
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

- [FASE17_PRIMEIRA_REORGANIZACAO_DOCUMENTAL_AMPLA.md](/home/thiago/coleta_showtrials/docs/fases/FASE17_PRIMEIRA_REORGANIZACAO_DOCUMENTAL_AMPLA.md)

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

- [FASE10_INTRODUCAO_DO_SERVICE_REGISTRY_E_DO_LAZY_LOADING.md](/home/thiago/coleta_showtrials/docs/fases/FASE10_INTRODUCAO_DO_SERVICE_REGISTRY_E_DO_LAZY_LOADING.md)
- [FASE11_ESTABILIZACAO_INICIAL_DO_CI.md](/home/thiago/coleta_showtrials/docs/fases/FASE11_ESTABILIZACAO_INICIAL_DO_CI.md)
- [FASE12_PADRONIZACAO_DA_TELEMETRIA_EM_TIPODOCUMENTO.md](/home/thiago/coleta_showtrials/docs/fases/FASE12_PADRONIZACAO_DA_TELEMETRIA_EM_TIPODOCUMENTO.md)
- [FASE13_LIMPEZA_E_ORGANIZACAO_DO_REPOSITORIO.md](/home/thiago/coleta_showtrials/docs/fases/FASE13_LIMPEZA_E_ORGANIZACAO_DO_REPOSITORIO.md)
- [FASE14_TELEMETRIA_E_TESTES_EM_EXPORTAR_DOCUMENTO.md](/home/thiago/coleta_showtrials/docs/fases/FASE14_TELEMETRIA_E_TESTES_EM_EXPORTAR_DOCUMENTO.md)
- [FASE15_TELEMETRIA_E_TESTES_EM_GERAR_RELATORIO.md](/home/thiago/coleta_showtrials/docs/fases/FASE15_TELEMETRIA_E_TESTES_EM_GERAR_RELATORIO.md)
- [FASE16_TELEMETRIA_E_EXPANSAO_DE_TESTES_EM_LISTAR_DOCUMENTOS.md](/home/thiago/coleta_showtrials/docs/fases/FASE16_TELEMETRIA_E_EXPANSAO_DE_TESTES_EM_LISTAR_DOCUMENTOS.md)

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

- [FASE01_FUNDACAO_DA_CAMADA_DE_DOMINIO.md](/home/thiago/coleta_showtrials/docs/fases/FASE01_FUNDACAO_DA_CAMADA_DE_DOMINIO.md)
- [FASE02_FUNDACAO_DA_CAMADA_DE_APLICACAO.md](/home/thiago/coleta_showtrials/docs/fases/FASE02_FUNDACAO_DA_CAMADA_DE_APLICACAO.md)
- [FASE03_FUNDACAO_DA_CAMADA_DE_INFRAESTRUTURA.md](/home/thiago/coleta_showtrials/docs/fases/FASE03_FUNDACAO_DA_CAMADA_DE_INFRAESTRUTURA.md)
- [FASE04_FUNDACAO_DA_INTERFACE_CLI.md](/home/thiago/coleta_showtrials/docs/fases/FASE04_FUNDACAO_DA_INTERFACE_CLI.md)
- [FASE05_INTRODUCAO_DO_SUBSISTEMA_DE_TRADUCAO.md](/home/thiago/coleta_showtrials/docs/fases/FASE05_INTRODUCAO_DO_SUBSISTEMA_DE_TRADUCAO.md)
- [FASE06_INTRODUCAO_DO_SUBSISTEMA_DE_EXPORTACAO.md](/home/thiago/coleta_showtrials/docs/fases/FASE06_INTRODUCAO_DO_SUBSISTEMA_DE_EXPORTACAO.md)
- [FASE07_INTRODUCAO_DO_SUBSISTEMA_DE_RELATORIOS.md](/home/thiago/coleta_showtrials/docs/fases/FASE07_INTRODUCAO_DO_SUBSISTEMA_DE_RELATORIOS.md)
- [FASE08_INTRODUCAO_DO_SUBSISTEMA_DE_ANALISE_DE_TEXTO.md](/home/thiago/coleta_showtrials/docs/fases/FASE08_INTRODUCAO_DO_SUBSISTEMA_DE_ANALISE_DE_TEXTO.md)
- [FASE09_INTRODUCAO_DA_INTERFACE_WEB.md](/home/thiago/coleta_showtrials/docs/fases/FASE09_INTRODUCAO_DA_INTERFACE_WEB.md)
