# Mapa Inicial de Capacidades e Casos de Uso Candidatos

## 1. Objetivo do documento

Este documento consolida um primeiro mapa entre capacidades do sistema e casos de uso candidatos, com o objetivo de preparar a abertura dos futuros artefatos específicos da frente de casos de uso.

Seu foco não é ainda formalizar um documento completo de casos de uso nem detalhar fluxos principais, extensões ou diagramas. Seu papel é organizar:

- casos de uso já existentes no sistema atual
- candidatos derivados da transição arquitetural
- candidatos derivados do sistema-alvo

## 2. Base de evidência utilizada

Este insumo foi construído com base em:

- `docs/fases/FASE2_APPLICATION.md`
- `docs/fases/FASE5_TRADUCAO.md`
- `docs/fases/FASE6_EXPORTACAO.md`
- `docs/fases/FASE7_RELATORIOS.md`
- `docs/fases/FASE8_ANALISE_TEXTO.md`
- `docs/modelagem/03_documento_de_requisitos.md`
- `docs/modelagem/requisitos/apoio/03_glossario_de_atores_e_termos.md`
- `docs/modelagem/requisitos/apoio/04_mapa_de_stakeholders_atores_e_objetivos.md`
- `docs/modelagem/requisitos/apoio/05_fronteira_do_sistema_e_recortes_de_modelagem.md`
- `src/application/use_cases/`
- documentos de projeto que já nomeiam casos de uso futuros para a engine

## 3. Capacidades do ShowTrials atual

As capacidades já sustentadas por documentação e código no sistema atual podem ser resumidas em:

- listar documentos
- obter documento completo
- classificar documento
- obter estatísticas do acervo
- traduzir documento
- listar traduções
- analisar documento
- analisar acervo
- exportar documento
- gerar relatório

## 4. Capacidades da transição arquitetural

Na camada de transição, as capacidades mais fortes identificadas são:

- configurar pipeline
- executar pipeline
- separar configuração de execução
- preparar fluxos atuais para migração gradual à nova arquitetura

Nem todas essas capacidades devem ser elevadas imediatamente a casos de uso principais orientados ao ator. Algumas pertencem mais ao plano de transição e à evolução arquitetural do que ao nível de uso direto do sistema.

## 5. Capacidades do sistema-alvo

No sistema-alvo, as capacidades mais fortes identificadas até aqui são:

- criar pipeline
- executar pipeline documental
- persistir produtos derivados
- listar pipelines
- editar pipeline
- revisar tradução
- operar pipelines especializados, como:
  - OCR sobre PDF
  - tradução documental
  - raspagem e análise
- consultar resultados produzidos por pipelines

## 6. Critério adotado para transformar capacidade em caso de uso candidato

Para esta etapa, uma capacidade é promovida a caso de uso candidato quando:

- representa um objetivo reconhecível do ator
- possui identidade funcional própria
- pode ser distinguida de decisões puramente internas de arquitetura
- contribui para a futura modelagem de interação entre ator e sistema

Por isso:

- `ConfigurarPipeline` e `ExecutarPipeline` foram mantidos como candidatos fortes da transição
- `MigrarFluxoAtualParaPipeline` nao foi promovido a caso de uso principal, por se aproximar mais de requisito de transição e atividade interna da evolução

## 7. Casos de uso existentes do sistema atual

### 7.1 Consulta e navegação documental

- `ListarDocumentos`
- `ObterDocumento`

### 7.2 Preparação e enriquecimento do acervo

- `ClassificarDocumento`

### 7.3 Tradução

- `TraduzirDocumento`
- `ListarTraducoes`

### 7.4 Análise e visão agregada

- `ObterEstatisticas`
- `AnalisarDocumento`
- `AnalisarAcervo`

### 7.5 Saída e consolidação

- `ExportarDocumento`
- `GerarRelatorio`

## 8. Leitura interpretativa dos casos de uso atuais

As leituras consolidadas nesta etapa foram:

- `ClassificarDocumento` funciona melhor como caso de uso de preparação e enriquecimento do acervo, com forte relação com metadados
- `ObterEstatisticas` funciona melhor como caso de uso de análise agregada ou visão do acervo, e não como enriquecimento documental
- `ListarTraducoes` permanece como caso de uso autônomo
- `GerarRelatorio` permanece bem agrupado com `ExportarDocumento` como saída e consolidação

## 9. Casos de uso candidatos da transição

Os casos de uso candidatos centrais da transição ficam consolidados assim:

- `ConfigurarPipeline`
- `ExecutarPipeline`

### 9.1 Elemento deliberadamente não promovido

- `MigrarFluxoAtualParaPipeline`

Esse item foi mantido fora da lista principal de casos de uso candidatos porque, nesta etapa, ele é melhor compreendido como:

- requisito de transição
- atividade interna da evolução
- decisão arquitetural

e não como objetivo principal do ator do sistema.

## 10. Casos de uso candidatos centrais do sistema-alvo

Os candidatos centrais do sistema-alvo ficam consolidados assim:

- `CriarPipeline`
- `ExecutarPipelineDocumental`
- `PersistirProdutosDerivados`
- `ListarPipelines`
- `EditarPipeline`
- `RevisarTraducao`

## 11. Casos de uso candidatos especializados do sistema-alvo

Os candidatos abaixo devem ser lidos, por enquanto, como especializações, cenários exemplares ou variantes concretas de execução:

- `ProcessarPDFcomOCR`
- `ExecutarPipelineDeTraducao`
- `ExecutarPipelineDeRaspagemEAnalise`
- `ExecutarPipelinePorID`
- `ConsultarResultadosDePipeline`

## 12. Relação preliminar entre atores e casos de uso

### 12.1 Usuario operador

Mais fortemente associado a:

- `ListarDocumentos`
- `ObterDocumento`
- `TraduzirDocumento`
- `ListarTraducoes`
- `AnalisarDocumento`
- `AnalisarAcervo`
- `ExportarDocumento`
- `GerarRelatorio`

### 12.2 Usuario configurador

Mais fortemente associado a:

- `ConfigurarPipeline`
- `ExecutarPipeline`
- `CriarPipeline`
- `ExecutarPipelineDocumental`
- `PersistirProdutosDerivados`
- `ListarPipelines`
- `EditarPipeline`
- `RevisarTraducao`

## 13. Síntese interpretativa

O mapa atual sugere uma progressão coerente:

- o sistema atual já possui um conjunto sólido de casos de uso imperativos e documentados
- a transição é estruturada por `ConfigurarPipeline` e `ExecutarPipeline`
- o sistema-alvo expande essa lógica em torno de criação, edição, execução e persistência de pipelines e seus resultados
- casos específicos de OCR, tradução e raspagem devem ser tratados, por ora, como especializações de um caso mais geral de execução documental

## 14. Questões em aberto

Ainda precisam ser refinadas em rodadas futuras:

- granularidade ideal entre casos de uso centrais e especializados
- relação entre `ExecutarPipeline` e `ExecutarPipelineDocumental`
- detalhamento posterior de `RevisarTraducao`
- eventual inclusão futura de casos de uso ligados a cenários colaborativos
- passagem deste mapa preliminar para artefatos formais de casos de uso
