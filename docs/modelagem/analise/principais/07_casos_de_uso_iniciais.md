# Casos de Uso Iniciais

## 1. Objetivo do documento

Este documento consolida o primeiro artefato formal da frente de casos de uso da nova trilha de modelagem do projeto.

Seu papel é organizar, em um único ponto de consulta:

- os casos de uso já sustentados pelo sistema atual
- os casos de uso centrais da transição arquitetural
- os casos de uso centrais e especializados do sistema-alvo

Este documento ainda não constitui a etapa final de especificações textuais completas no estilo Cockburn. Ele funciona como artefato intermediário entre os insumos-base e os futuros artefatos de:

- diagrama de casos de uso
- especificações textuais detalhadas

## 2. Base de evidência e insumos utilizados

Este documento se apoia em:

- [03_documento_de_requisitos.md](/home/thiago/coleta_showtrials/docs/modelagem/requisitos/principais/03_documento_de_requisitos.md)
- [01_documento_de_requisitos_showtrials_atual.md](/home/thiago/coleta_showtrials/docs/modelagem/requisitos/apoio/01_documento_de_requisitos_showtrials_atual.md)
- [02_documento_de_requisitos_evolucao_engine.md](/home/thiago/coleta_showtrials/docs/modelagem/requisitos/apoio/02_documento_de_requisitos_evolucao_engine.md)
- [03_glossario_de_atores_e_termos.md](/home/thiago/coleta_showtrials/docs/modelagem/requisitos/apoio/03_glossario_de_atores_e_termos.md)
- [04_mapa_de_stakeholders_atores_e_objetivos.md](/home/thiago/coleta_showtrials/docs/modelagem/requisitos/apoio/04_mapa_de_stakeholders_atores_e_objetivos.md)
- [05_fronteira_do_sistema_e_recortes_de_modelagem.md](/home/thiago/coleta_showtrials/docs/modelagem/requisitos/apoio/05_fronteira_do_sistema_e_recortes_de_modelagem.md)
- [06_mapa_inicial_de_capacidades_e_casos_de_uso_candidatos.md](/home/thiago/coleta_showtrials/docs/modelagem/requisitos/apoio/06_mapa_inicial_de_capacidades_e_casos_de_uso_candidatos.md)
- documentação de fases do projeto
- código-fonte em `src/application/use_cases/`

## 3. Critério de organização adotado

Os casos de uso foram organizados segundo quatro critérios principais:

- separação entre sistema atual, transição e sistema-alvo
- distinção entre casos de uso centrais e casos especializados
- priorização de objetivos reconhecíveis do ator
- exclusão de atividades puramente internas de evolução arquitetural da lista principal de casos de uso

Por esse critério:

- casos de uso já implementados e documentados no ShowTrials atual aparecem como base factual do sistema atual
- casos da transição expressam a virada arquitetural em direção a pipelines configuráveis
- casos do sistema-alvo expressam a futura lógica da engine
- casos especializados são mantidos como cenários exemplares ou especializações, não como eixo organizador principal

## 4. Atores considerados

Os atores principais considerados neste documento são:

- `usuario operador`
- `usuario configurador`

Esses atores derivam da estrutura conceitual anteriormente consolidada:

- `usuario` funciona como categoria geral
- `usuario operador` é mais aderente ao sistema atual
- `usuario configurador` é mais aderente ao sistema futuro

## 5. Casos de uso do sistema atual

## 5.1 Consulta e navegação documental

### Caso de uso: `ListarDocumentos`

- Ator principal: `usuario operador`
- Objetivo: consultar o acervo por listagem paginada e filtrada
- Base de evidência: FASE 2, FASE 4, FASE 9 e código atual

### Caso de uso: `ObterDocumento`

- Ator principal: `usuario operador`
- Objetivo: acessar um documento completo, incluindo dados enriquecidos e traduções disponíveis
- Base de evidência: FASE 2, FASE 4, FASE 9 e código atual

## 5.2 Preparação e enriquecimento do acervo

### Caso de uso: `ClassificarDocumento`

- Ator principal: `usuario operador`
- Objetivo: enriquecer o documento com classificação tipológica e metadados úteis ao uso posterior
- Base de evidência: FASE 2 e código atual

## 5.3 Tradução

### Caso de uso: `TraduzirDocumento`

- Ator principal: `usuario operador`
- Objetivo: gerar tradução persistida de um documento para idioma de destino
- Base de evidência: FASE 5, FASE 9 e código atual

### Caso de uso: `ListarTraducoes`

- Ator principal: `usuario operador`
- Objetivo: consultar traduções disponíveis de um documento
- Base de evidência: FASE 5, FASE 9 e código atual

## 5.4 Análise e visão agregada

### Caso de uso: `ObterEstatisticas`

- Ator principal: `usuario operador`
- Objetivo: obter visão agregada e estatística do acervo
- Base de evidência: FASE 2 e código atual

### Caso de uso: `AnalisarDocumento`

- Ator principal: `usuario operador`
- Objetivo: analisar linguisticamente um documento específico e gerar artefatos analíticos associados
- Base de evidência: FASE 8 e código atual

### Caso de uso: `AnalisarAcervo`

- Ator principal: `usuario operador`
- Objetivo: realizar análise global do acervo e obter métricas e artefatos agregados
- Base de evidência: FASE 8 e código atual

## 5.5 Saída e consolidação

### Caso de uso: `ExportarDocumento`

- Ator principal: `usuario operador`
- Objetivo: exportar o conteúdo documental e seus resultados para uso posterior
- Base de evidência: FASE 6 e código atual

### Caso de uso: `GerarRelatorio`

- Ator principal: `usuario operador`
- Objetivo: consolidar informações documentais e analíticas em relatórios estruturados
- Base de evidência: FASE 7 e código atual

## 6. Casos de uso da transição arquitetural

### Caso de uso: `ConfigurarPipeline`

- Ator principal: `usuario configurador`
- Objetivo: definir os recursos, etapas e parâmetros necessários para um fluxo configurável de trabalho documental
- Base de evidência: Documento de Requisitos integrado, roadmap arquitetural e direcionamento da engine

### Caso de uso: `ExecutarPipeline`

- Ator principal: `usuario configurador`
- Objetivo: executar um fluxo configurado de trabalho documental
- Base de evidência: Documento de Requisitos integrado, roadmap arquitetural e direcionamento da engine

### Observação

O item `MigrarFluxoAtualParaPipeline` não entra neste documento como caso de uso principal orientado a ator. Nesta etapa, ele é melhor interpretado como:

- requisito de transição
- atividade interna da evolução
- decisão arquitetural

## 7. Casos de uso do sistema-alvo

### Caso de uso: `CriarPipeline`

- Ator principal: `usuario configurador`
- Objetivo: criar um pipeline persistível a partir de uma configuração explícita
- Base de evidência: roadmap arquitetural e requisitos da engine

### Caso de uso: `ExecutarPipelineDocumental`

- Ator principal: `usuario configurador`
- Objetivo: executar um pipeline documental configurado para produzir resultados úteis ao trabalho do usuário
- Base de evidência: requisitos integrados e documentação da evolução para engine

### Caso de uso: `PersistirProdutosDerivados`

- Ator principal: `usuario configurador`
- Objetivo: persistir resultados gerados pelo pipeline, como traduções, análises e artefatos derivados
- Base de evidência: requisitos integrados e documentação da evolução para engine

### Caso de uso: `ListarPipelines`

- Ator principal: `usuario configurador`
- Objetivo: consultar pipelines previamente definidos
- Base de evidência: roadmap arquitetural e requisitos da engine

### Caso de uso: `EditarPipeline`

- Ator principal: `usuario configurador`
- Objetivo: ajustar e refinar pipelines já criados
- Base de evidência: inferência a partir da persistência e reutilização de pipelines

### Caso de uso: `RevisarTraducao`

- Ator principal: `usuario configurador`
- Objetivo: revisar e ajustar traduções produzidas ou mantidas pelo sistema
- Base de evidência: requisitos integrados e discussões de modelagem da frente

## 8. Casos de uso especializados e cenários exemplares

Os casos abaixo não estruturam este documento como eixo principal. Nesta etapa, devem ser lidos como:

- especializações
- cenários exemplares
- variantes concretas de execução

### Caso especializado: `ProcessarPDFcomOCR`

- Ator principal: `usuario configurador`
- Objetivo: executar fluxo documental voltado a tratamento de PDF e OCR

### Caso especializado: `ExecutarPipelineDeTraducao`

- Ator principal: `usuario configurador`
- Objetivo: executar fluxo configurado voltado à tradução documental

### Caso especializado: `ExecutarPipelineDeRaspagemEAnalise`

- Ator principal: `usuario configurador`
- Objetivo: executar fluxo configurado de obtenção de conteúdo externo seguido de análise

### Caso especializado: `ExecutarPipelinePorID`

- Ator principal: `usuario configurador`
- Objetivo: executar um pipeline já persistido e identificado no sistema

### Caso especializado: `ConsultarResultadosDePipeline`

- Ator principal: `usuario configurador`
- Objetivo: consultar os resultados produzidos por execuções anteriores de pipeline

## 9. Relação preliminar entre atores e casos de uso

### 9.1 `usuario operador`

Relaciona-se mais fortemente com:

- `ListarDocumentos`
- `ObterDocumento`
- `ClassificarDocumento`
- `TraduzirDocumento`
- `ListarTraducoes`
- `ObterEstatisticas`
- `AnalisarDocumento`
- `AnalisarAcervo`
- `ExportarDocumento`
- `GerarRelatorio`

### 9.2 `usuario configurador`

Relaciona-se mais fortemente com:

- `ConfigurarPipeline`
- `ExecutarPipeline`
- `CriarPipeline`
- `ExecutarPipelineDocumental`
- `PersistirProdutosDerivados`
- `ListarPipelines`
- `EditarPipeline`
- `RevisarTraducao`

## 10. Casos prioritários para especificação textual

Os casos abaixo aparecem, nesta etapa, como candidatos prioritários para futura especificação textual mais completa:

- `ObterDocumento`
- `TraduzirDocumento`
- `AnalisarDocumento`
- `ConfigurarPipeline`
- `ExecutarPipelineDocumental`
- `RevisarTraducao`

Esse conjunto foi escolhido por cobrir:

- sistema atual
- transição
- sistema-alvo

## 11. Questões em aberto

Ainda precisam ser refinadas nas próximas rodadas:

- granularidade ideal entre casos centrais e especializados
- relação entre `ExecutarPipeline` e `ExecutarPipelineDocumental`
- detalhamento posterior de `RevisarTraducao`
- eventual inclusão de papéis colaborativos futuros
- critério final de escolha dos casos que entrarão no diagrama

## 12. Próximos passos

Os próximos passos recomendados são:

- transformar este catálogo inicial em base para o primeiro diagrama de casos de uso
- selecionar os casos de uso prioritários para especificação textual
- abrir a etapa de especificações mais detalhadas em documento próprio
