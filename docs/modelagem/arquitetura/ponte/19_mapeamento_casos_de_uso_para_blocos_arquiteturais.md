# Mapeamento de Casos de Uso para Blocos Arquiteturais

## 1. Objetivo do documento

Este documento consolida o mapeamento entre os **casos de uso** da frente e os **blocos arquiteturais** que deverão dar sustentação à futura solução.

Seu objetivo é preparar a transição da frente de casos de uso para a frente arquitetural, sem ainda entrar formalmente em:

- 4+1
- C4
- UML de componentes detalhada

## 2. Base de evidência utilizada

Este documento se apoia principalmente em:

- [07_casos_de_uso_iniciais.md](/home/thiago/coleta_showtrials/docs/modelagem/analise/principais/07_casos_de_uso_iniciais.md)
- [13_especificacoes_textuais_de_casos_de_uso_prioritarios.md](/home/thiago/coleta_showtrials/docs/modelagem/analise/principais/13_especificacoes_textuais_de_casos_de_uso_prioritarios.md)
- [14_especificacoes_textuais_de_casos_de_uso_secundarios.md](/home/thiago/coleta_showtrials/docs/modelagem/analise/principais/14_especificacoes_textuais_de_casos_de_uso_secundarios.md)
- [17_drivers_arquiteturais.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/ponte/17_drivers_arquiteturais.md)
- [18_mapeamento_requisitos_para_drivers.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/ponte/18_mapeamento_requisitos_para_drivers.md)
- documentos arquiteturais prévios do projeto

## 3. Blocos arquiteturais adotados nesta etapa

Nesta etapa, os casos de uso foram mapeados para os seguintes blocos arquiteturais intermediários:

- **Interfaces de operação**
- **Orquestração de casos de uso**
- **Catálogo/configuração de pipeline**
- **Execução de pipeline**
- **Processamento documental**
- **Persistência e recuperação**
- **Resultados derivados e revisão**
- **Integrações e serviços externos**

Esses blocos ainda não são o C4 formal. Eles funcionam como ponte conceitual entre os casos de uso e os próximos modelos arquiteturais.

## 4. Matriz principal

| Caso de uso | Blocos arquiteturais principais | Justificativa |
|---|---|---|
| `ListarDocumentos` | Interfaces de operação; Orquestração de casos de uso; Persistência e recuperação | depende de consulta paginada ao acervo e apresentação ao usuário |
| `ObterDocumento` | Interfaces de operação; Orquestração de casos de uso; Persistência e recuperação; Resultados derivados e revisão | recupera documento, metadados e contexto de uso associado |
| `ClassificarDocumento` | Orquestração de casos de uso; Processamento documental; Persistência e recuperação | enriquece documento com metadados e persiste resultado |
| `TraduzirDocumento` | Orquestração de casos de uso; Processamento documental; Persistência e recuperação; Integrações e serviços externos | aciona serviço de tradução, trata conteúdo e persiste resultado |
| `ListarTraducoes` | Interfaces de operação; Orquestração de casos de uso; Persistência e recuperação | consulta traduções já vinculadas ao documento |
| `ObterEstatisticas` | Interfaces de operação; Orquestração de casos de uso; Persistência e recuperação | consolida visão agregada do acervo a partir de dados persistidos |
| `AnalisarDocumento` | Orquestração de casos de uso; Processamento documental; Resultados derivados e revisão; Integrações e serviços externos | executa análise, produz artefatos e distingue resultados automáticos |
| `AnalisarAcervo` | Orquestração de casos de uso; Processamento documental; Persistência e recuperação; Resultados derivados e revisão | amplia a análise para escala global do acervo |
| `ExportarDocumento` | Interfaces de operação; Orquestração de casos de uso; Persistência e recuperação | recupera conteúdo e o transforma em artefato de saída |
| `GerarRelatorio` | Interfaces de operação; Orquestração de casos de uso; Persistência e recuperação | consolida dados e métricas em relatório estruturado |
| `ConfigurarPipeline` | Interfaces de operação; Catálogo/configuração de pipeline | ajusta entradas, steps, parâmetros, contexto e persistência do fluxo |
| `ExecutarPipeline` | Interfaces de operação; Execução de pipeline | representa a execução no plano de transição, sem ainda detalhar toda a engine |
| `CriarPipeline` | Interfaces de operação; Catálogo/configuração de pipeline | cria uma base inicial de pipeline reutilizável |
| `ListarPipelines` | Interfaces de operação; Catálogo/configuração de pipeline; Persistência e recuperação | consulta pipelines salvos e disponíveis |
| `EditarPipeline` | Interfaces de operação; Catálogo/configuração de pipeline; Persistência e recuperação | ajusta pipeline persistido e atualiza sua configuração |
| `ExecutarPipelineDocumental` | Interfaces de operação; Execução de pipeline; Processamento documental; Resultados derivados e revisão | núcleo operacional da engine futura |
| `PersistirProdutosDerivados` | Execução de pipeline; Persistência e recuperação; Resultados derivados e revisão | registra resultados produzidos pelo fluxo |
| `RevisarTraducao` | Interfaces de operação; Resultados derivados e revisão; Persistência e recuperação | suporta correção, validação humana e versionamento/revisão |
| `ProcessarPDFcomOCR` | Execução de pipeline; Processamento documental; Integrações e serviços externos | especializa execução para PDF, imagem e OCR |
| `ExecutarPipelineDeTraducao` | Execução de pipeline; Processamento documental; Integrações e serviços externos | especializa execução para tradução documental |
| `ExecutarPipelineDeRaspagemEAnalise` | Execução de pipeline; Processamento documental; Integrações e serviços externos | especializa execução para obtenção externa seguida de análise |
| `ExecutarPipelinePorID` | Interfaces de operação; Catálogo/configuração de pipeline; Execução de pipeline | executa um pipeline previamente salvo e recuperado |
| `ConsultarResultadosDePipeline` | Interfaces de operação; Persistência e recuperação; Resultados derivados e revisão | consulta resultados já produzidos por execuções anteriores |

## 5. Leitura interpretativa da matriz

### 5.1 Bloco mais transversal: Persistência e recuperação

O bloco mais recorrente é **Persistência e recuperação**.

Isso confirma que, mesmo com a evolução para engine, o projeto continua fortemente dependente de:

- acesso ao acervo
- vínculo entre documento e resultado
- consulta posterior de material persistido

### 5.2 Bloco novo mais importante: Execução de pipeline

O bloco **Execução de pipeline** concentra os casos centrais da transição e do sistema-alvo.

Isso o torna candidato natural a um dos focos principais dos próximos artefatos arquiteturais.

### 5.3 Catálogo/configuração e execução não são o mesmo bloco

O mapeamento reforça que:

- criar/configurar/listar/editar pipeline
- executar pipeline

não são a mesma responsabilidade arquitetural.

Essa distinção será importante tanto no 4+1 quanto no C4.

### 5.4 Resultados derivados e revisão formam um bloco relevante

Traduzir, analisar, persistir produtos derivados, consultar resultados e revisar tradução apontam para a necessidade de um bloco explícito voltado a:

- produtos derivados
- estados de revisão
- diferenciação entre automático e humano

## 6. Inferências adotadas

As principais inferências adotadas nesta matriz foram:

- o bloco **Resultados derivados e revisão** foi tratado como bloco próprio por causa do peso adquirido por traduções, análises e revisão humana na frente
- `ExecutarPipeline` foi mantido como caso da transição e mapeado para execução, sem colapsá-lo artificialmente em `ExecutarPipelineDocumental`
- casos do sistema atual foram mantidos ligados à orquestração de casos de uso, preservando a leitura da arquitetura atual como fortemente centrada em use cases imperativos

## 7. Dívidas técnicas registradas

Permanecem como pontos futuros:

- refinar se “Resultados derivados e revisão” deve permanecer como bloco único ou ser dividido
- decidir o nível de detalhamento em que “Integrações e serviços externos” aparecerá no C4
- decidir se haverá um bloco arquitetural específico para telemetria, logs e acompanhamento de execução

## 8. Próximos passos

Os próximos passos recomendados são:

- abrir o documento de decisões arquiteturais iniciais
- depois consolidar o glossário arquitetural e técnico
- em seguida abrir os artefatos formais de visão arquitetural
