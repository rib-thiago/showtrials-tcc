# Especificações Textuais de Casos de Uso Secundários

## 1. Objetivo do documento

Este documento registra a segunda rodada de **especificações textuais** da frente de casos de uso, cobrindo os casos considerados secundários, complementares ou especializados em relação ao conjunto já priorizado no artefato anterior.

Seu papel é ampliar a cobertura da frente sem perder aderência ao que já foi consolidado em:

- requisitos
- catálogo inicial de casos de uso
- diagramas
- revisão integrada
- especificações dos casos prioritários

## 2. Base de evidência utilizada

Este documento se apoia principalmente em:

- [03_documento_de_requisitos.md](/home/thiago/coleta_showtrials/docs/modelagem/requisitos/principais/03_documento_de_requisitos.md)
- [07_casos_de_uso_iniciais.md](/home/thiago/coleta_showtrials/docs/modelagem/analise/principais/07_casos_de_uso_iniciais.md)
- [12_revisao_integrada_dos_casos_de_uso.md](/home/thiago/coleta_showtrials/docs/modelagem/analise/principais/12_revisao_integrada_dos_casos_de_uso.md)
- [13_especificacoes_textuais_de_casos_de_uso_prioritarios.md](/home/thiago/coleta_showtrials/docs/modelagem/analise/principais/13_especificacoes_textuais_de_casos_de_uso_prioritarios.md)
- documentação de fases do projeto
- roadmap arquitetural
- código atual em `src/application/use_cases/`

## 3. Critério de seleção dos casos secundários

Foram tratados neste documento os casos que:

- não entraram no conjunto prioritário do artefato anterior
- já possuem evidência factual ou sustentação documental suficiente
- complementam a cobertura do sistema atual, da transição e do sistema-alvo
- ajudam a fechar o ciclo da frente de casos de uso antes das matrizes de rastreabilidade

## 4. Padrão de especificação adotado

Cada caso de uso foi especificado com a seguinte estrutura, em versão mais sintética que a usada nos casos prioritários:

- nome
- objetivo
- ator principal
- gatilho
- pré-condições
- pós-condições
- fluxo principal
- fluxos alternativos
- observações de modelagem
- base de evidência

## 5. Casos de uso secundários do sistema atual

## 5.1 `ListarDocumentos`

### Objetivo

Consultar o acervo por listagem paginada e filtrada.

### Ator principal

- `usuario operador`

### Gatilho

O usuário solicita a listagem de documentos.

### Pré-condições

- o repositório documental deve estar acessível

### Pós-condições

- uma lista paginada e filtrável de documentos é apresentada

### Fluxo principal

1. o usuário solicita a listagem
2. o usuário informa ou aceita filtros e paginação
3. o sistema consulta o repositório
4. o sistema retorna itens, total, página e filtros aplicados

### Fluxos alternativos

- repositório indisponível
- filtros inválidos
- página sem resultados

### Observações de modelagem

- caso fortemente factual, ancorado em FASE 2
- funciona como porta de entrada frequente para `ObterDocumento`

### Base de evidência

- [FASE02_FUNDACAO_DA_CAMADA_DE_APLICACAO.md](/home/thiago/coleta_showtrials/docs/fases/FASE02_FUNDACAO_DA_CAMADA_DE_APLICACAO.md)
- [FASE04_FUNDACAO_DA_INTERFACE_CLI.md](/home/thiago/coleta_showtrials/docs/fases/FASE04_FUNDACAO_DA_INTERFACE_CLI.md)
- [FASE09_INTRODUCAO_DA_INTERFACE_WEB.md](/home/thiago/coleta_showtrials/docs/fases/FASE09_INTRODUCAO_DA_INTERFACE_WEB.md)

## 5.2 `ClassificarDocumento`

### Objetivo

Enriquecer um documento com classificação tipológica e metadados úteis ao uso posterior.

### Ator principal

- `usuario operador`

### Gatilho

O usuário solicita a classificação de um documento específico ou de um conjunto de documentos.

### Pré-condições

- o documento deve existir no sistema
- regras de classificação devem estar disponíveis

### Pós-condições

- metadados de classificação são atualizados no documento

### Fluxo principal

1. o usuário indica documento ou conjunto de documentos
2. o sistema recupera o material a classificar
3. o sistema aplica regras de classificação
4. o sistema atualiza metadados
5. o sistema salva o resultado

### Fluxos alternativos

- documento inexistente
- falha nas regras de classificação
- erro ao persistir metadados

### Observações de modelagem

- caso de uso de preparação/enriquecimento, não de análise principal
- inclui detecção de tipo, nomes, anexos e papéis documentais

### Base de evidência

- [FASE02_FUNDACAO_DA_CAMADA_DE_APLICACAO.md](/home/thiago/coleta_showtrials/docs/fases/FASE02_FUNDACAO_DA_CAMADA_DE_APLICACAO.md)

## 5.3 `ListarTraducoes`

### Objetivo

Consultar traduções disponíveis de um documento.

### Ator principal

- `usuario operador`

### Gatilho

O usuário deseja verificar traduções associadas a um documento.

### Pré-condições

- o documento deve estar identificado
- o repositório de traduções deve estar acessível

### Pós-condições

- as traduções disponíveis do documento são apresentadas

### Fluxo principal

1. o usuário informa o documento
2. o sistema consulta o repositório de traduções
3. o sistema retorna a lista de traduções associadas

### Fluxos alternativos

- documento inexistente
- ausência de traduções
- falha no repositório de traduções

### Observações de modelagem

- caso autônomo, embora frequentemente acionado a partir do contexto de `ObterDocumento`

### Base de evidência

- [FASE05_INTRODUCAO_DO_SUBSISTEMA_DE_TRADUCAO.md](/home/thiago/coleta_showtrials/docs/fases/FASE05_INTRODUCAO_DO_SUBSISTEMA_DE_TRADUCAO.md)

## 5.4 `ObterEstatisticas`

### Objetivo

Obter visão agregada e estatística do acervo documental.

### Ator principal

- `usuario operador`

### Gatilho

O usuário solicita estatísticas globais do acervo.

### Pré-condições

- o repositório documental deve estar acessível

### Pós-condições

- métricas agregadas do acervo são produzidas e apresentadas

### Fluxo principal

1. o usuário solicita estatísticas do acervo
2. o sistema consulta os documentos disponíveis
3. o sistema calcula métricas agregadas
4. o sistema apresenta os resultados

### Fluxos alternativos

- falha no repositório
- acervo vazio
- erro ao consolidar métricas

### Observações de modelagem

- caso mantido como autônomo, embora sua granularidade ainda seja dívida técnica
- inclui métricas de distribuição, pessoas frequentes, documentos especiais e custos

### Base de evidência

- [FASE02_FUNDACAO_DA_CAMADA_DE_APLICACAO.md](/home/thiago/coleta_showtrials/docs/fases/FASE02_FUNDACAO_DA_CAMADA_DE_APLICACAO.md)

## 5.5 `AnalisarAcervo`

### Objetivo

Realizar análise global do acervo e obter métricas e artefatos agregados.

### Ator principal

- `usuario operador`

### Gatilho

O usuário solicita análise global do acervo.

### Pré-condições

- o acervo deve estar acessível
- os serviços analíticos necessários devem estar disponíveis

### Pós-condições

- resultados globais de análise são produzidos
- artefatos agregados podem ser apresentados ou persistidos

### Fluxo principal

1. o usuário solicita a análise do acervo
2. o sistema recupera os documentos relevantes
3. o sistema executa análise global e estatísticas agregadas
4. o sistema produz resultados e artefatos
5. o sistema apresenta o resultado ao usuário

### Fluxos alternativos

- acervo indisponível
- amostra insuficiente
- falha em serviço analítico
- erro ao gerar artefatos agregados

### Observações de modelagem

- caso complementar a `AnalisarDocumento`
- reforça a transição conceitual entre análise pontual e exploração global do acervo

### Base de evidência

- [FASE08_INTRODUCAO_DO_SUBSISTEMA_DE_ANALISE_DE_TEXTO.md](/home/thiago/coleta_showtrials/docs/fases/FASE08_INTRODUCAO_DO_SUBSISTEMA_DE_ANALISE_DE_TEXTO.md)

## 5.6 `ExportarDocumento`

### Objetivo

Exportar o conteúdo documental e seus resultados para uso posterior.

### Ator principal

- `usuario operador`

### Gatilho

O usuário solicita a exportação de um documento.

### Pré-condições

- o documento deve existir
- o formato e o idioma desejados devem ser suportados

### Pós-condições

- o conteúdo exportado é gerado no formato solicitado

### Fluxo principal

1. o usuário seleciona o documento
2. o usuário escolhe formato e idioma
3. o sistema recupera o conteúdo apropriado
4. o sistema gera o artefato de exportação
5. o sistema entrega o resultado ao usuário

### Fluxos alternativos

- documento inexistente
- tradução inexistente no idioma solicitado
- formato não suportado
- erro ao gerar o arquivo

### Observações de modelagem

- caso orientado a saída/entrega
- no sistema atual, suporta ao menos `txt` e `pdf`

### Base de evidência

- [FASE06_INTRODUCAO_DO_SUBSISTEMA_DE_EXPORTACAO.md](/home/thiago/coleta_showtrials/docs/fases/FASE06_INTRODUCAO_DO_SUBSISTEMA_DE_EXPORTACAO.md)
- [FASE14_TELEMETRIA_E_TESTES_EM_EXPORTAR_DOCUMENTO.md](/home/thiago/coleta_showtrials/docs/fases/FASE14_TELEMETRIA_E_TESTES_EM_EXPORTAR_DOCUMENTO.md)

## 5.7 `GerarRelatorio`

### Objetivo

Consolidar informações documentais e analíticas em relatórios estruturados.

### Ator principal

- `usuario operador`

### Gatilho

O usuário solicita a geração de um relatório.

### Pré-condições

- os dados documentais necessários devem estar acessíveis

### Pós-condições

- um relatório estruturado é produzido

### Fluxo principal

1. o usuário solicita a geração de relatório
2. o sistema coleta os dados necessários
3. o sistema consolida métricas e contagens
4. o sistema estrutura o relatório
5. o sistema entrega o resultado ao usuário

### Fluxos alternativos

- falha ao coletar dados
- acervo insuficiente
- erro ao consolidar relatório

### Observações de modelagem

- permanece ligada a `ObterEstatisticas`, inclusive no diagrama atual
- caso de uso de consolidação, não de exploração interativa

### Base de evidência

- [FASE07_INTRODUCAO_DO_SUBSISTEMA_DE_RELATORIOS.md](/home/thiago/coleta_showtrials/docs/fases/FASE07_INTRODUCAO_DO_SUBSISTEMA_DE_RELATORIOS.md)
- [FASE15_TELEMETRIA_E_TESTES_EM_GERAR_RELATORIO.md](/home/thiago/coleta_showtrials/docs/fases/FASE15_TELEMETRIA_E_TESTES_EM_GERAR_RELATORIO.md)

## 6. Casos de uso secundários da transição e do sistema-alvo

## 6.1 `ExecutarPipeline`

### Objetivo

Executar um fluxo configurado de trabalho documental no plano da transição arquitetural.

### Ator principal

- `usuario configurador`

### Gatilho

O usuário decide executar um fluxo configurado ainda tratado em nível de transição.

### Pré-condições

- deve existir configuração executável

### Pós-condições

- a execução do fluxo é iniciada e produz resultados em conformidade com a configuração disponível

### Fluxo principal

1. o usuário escolhe um fluxo configurado
2. o sistema valida a possibilidade de execução
3. o sistema executa o fluxo
4. o sistema retorna os resultados produzidos

### Fluxos alternativos

- fluxo inexistente
- configuração inválida
- falha em recurso necessário

### Observações de modelagem

- caso mantido para expressar a transição conceitual
- sua relação exata com `ExecutarPipelineDocumental` segue como ponto de refinamento futuro

### Base de evidência

- [09_diagrama_casos_de_uso_transicao_arquitetural.md](/home/thiago/coleta_showtrials/docs/modelagem/analise/diagramas/09_diagrama_casos_de_uso_transicao_arquitetural.md)

## 6.2 `CriarPipeline`

### Objetivo

Criar uma base inicial de pipeline a partir de preset, configuração mínima ou último uso relevante.

### Ator principal

- `usuario configurador`

### Gatilho

O usuário decide criar um novo pipeline.

### Pré-condições

- o sistema deve permitir inicialização de pipeline a partir de base mínima ou preset

### Pós-condições

- uma base inicial de pipeline é criada

### Fluxo principal

1. o usuário solicita a criação de pipeline
2. o sistema oferece base mínima, preset ou reaproveitamento aplicável
3. o usuário escolhe a base desejada
4. o sistema cria o pipeline inicial

### Fluxos alternativos

- preset inválido
- falha ao criar pipeline

### Observações de modelagem

- distinto de `ConfigurarPipeline`
- este caso cria a base; o ajuste fino ocorre em `ConfigurarPipeline`

### Base de evidência

- [docs/projeto/roadmap_arquitetural.md](/home/thiago/coleta_showtrials/docs/projeto/roadmap_arquitetural.md)
- discussões de modelagem da frente

## 6.3 `PersistirProdutosDerivados`

### Objetivo

Persistir resultados gerados por execução de pipeline, como traduções, análises e artefatos derivados.

### Ator principal

- `usuario configurador`

### Gatilho

O usuário ou a configuração do pipeline indica que resultados devem ser persistidos.

### Pré-condições

- deve existir resultado persistível
- o mecanismo de persistência deve estar disponível

### Pós-condições

- produtos derivados são registrados de forma vinculada ao contexto adequado

### Fluxo principal

1. o sistema identifica resultados persistíveis
2. o usuário ou a configuração confirma a persistência
3. o sistema registra os produtos derivados
4. o sistema informa sucesso da operação

### Fluxos alternativos

- resultado não persistível
- persistência desabilitada
- falha no mecanismo de persistência

### Observações de modelagem

- no sistema-alvo, a persistência é configurável
- a relação formal exata com `ExecutarPipelineDocumental` permanece em aberto

### Base de evidência

- [10_diagrama_casos_de_uso_sistema_alvo.md](/home/thiago/coleta_showtrials/docs/modelagem/analise/diagramas/10_diagrama_casos_de_uso_sistema_alvo.md)
- requisitos integrados

## 6.4 `ListarPipelines`

### Objetivo

Consultar pipelines previamente definidos.

### Ator principal

- `usuario configurador`

### Gatilho

O usuário deseja visualizar pipelines disponíveis.

### Pré-condições

- o repositório de pipelines deve estar acessível

### Pós-condições

- uma lista de pipelines é apresentada ao usuário

### Fluxo principal

1. o usuário solicita a listagem
2. o sistema consulta o repositório de pipelines
3. o sistema apresenta os pipelines disponíveis

### Fluxos alternativos

- ausência de pipelines
- falha no repositório

### Observações de modelagem

- caso bastante estável e factual no plano do roadmap

### Base de evidência

- [docs/projeto/roadmap_arquitetural.md](/home/thiago/coleta_showtrials/docs/projeto/roadmap_arquitetural.md)

## 6.5 `EditarPipeline`

### Objetivo

Ajustar e refinar um pipeline já criado.

### Ator principal

- `usuario configurador`

### Gatilho

O usuário decide modificar um pipeline existente.

### Pré-condições

- o pipeline deve existir e estar acessível

### Pós-condições

- o pipeline é atualizado

### Fluxo principal

1. o usuário seleciona um pipeline existente
2. o sistema recupera sua configuração atual
3. o usuário altera parâmetros, steps, entradas ou destinos
4. o sistema valida as mudanças
5. o sistema registra a nova configuração

### Fluxos alternativos

- pipeline inexistente
- alteração inválida
- falha ao salvar

### Observações de modelagem

- fortemente relacionado a `ConfigurarPipeline`, mas mantido como caso distinto por representar ajuste sobre pipeline persistido

### Base de evidência

- inferência de modelagem baseada em persistência e reutilização de pipelines

## 7. Casos de uso especializados da futura engine

## 7.1 `ProcessarPDFcomOCR`

### Objetivo

Executar um fluxo especializado de tratamento de PDF e OCR.

### Ator principal

- `usuario configurador`

### Gatilho

O usuário seleciona um cenário de processamento documental orientado a OCR.

### Pré-condições

- entrada PDF compatível
- recursos de imagem e OCR disponíveis

### Pós-condições

- textos ou artefatos derivados do OCR são produzidos

### Fluxo principal

1. o usuário escolhe o cenário de OCR
2. o sistema recebe ou localiza o PDF
3. o sistema executa tratamento necessário
4. o sistema aplica OCR
5. o sistema retorna ou persiste os resultados conforme configuração

### Fluxos alternativos

- PDF inválido
- falha em recurso de imagem
- falha no OCR

### Observações de modelagem

- especialização de `ExecutarPipelineDocumental`

### Base de evidência

- requisitos integrados
- diagrama complementar de cenários especializados

## 7.2 `ExecutarPipelineDeTraducao`

### Objetivo

Executar um fluxo especializado de tradução documental.

### Ator principal

- `usuario configurador`

### Gatilho

O usuário seleciona um cenário de pipeline voltado à tradução.

### Pré-condições

- entrada documental válida
- recursos de tradução disponíveis

### Pós-condições

- resultados de tradução são produzidos e tratados conforme configuração

### Fluxo principal

1. o usuário escolhe o pipeline de tradução
2. o sistema valida entrada e recursos
3. o sistema executa o fluxo de tradução
4. o sistema retorna ou persiste resultados

### Fluxos alternativos

- documento inválido
- falha no serviço de tradução
- erro ao persistir resultados, quando configurado

### Observações de modelagem

- especialização de `ExecutarPipelineDocumental`

### Base de evidência

- requisitos integrados
- diagrama complementar de cenários especializados

## 7.3 `ExecutarPipelineDeRaspagemEAnalise`

### Objetivo

Executar fluxo especializado de obtenção de conteúdo externo seguido de análise.

### Ator principal

- `usuario configurador`

### Gatilho

O usuário seleciona um cenário de raspagem e análise.

### Pré-condições

- fonte externa acessível
- recursos de obtenção e análise disponíveis

### Pós-condições

- conteúdo obtido e resultados analíticos são produzidos

### Fluxo principal

1. o usuário escolhe o cenário
2. o sistema acessa a fonte externa
3. o sistema obtém o conteúdo
4. o sistema executa análise sobre o material
5. o sistema apresenta ou persiste resultados

### Fluxos alternativos

- fonte externa inacessível
- falha na raspagem
- falha analítica

### Observações de modelagem

- especialização de `ExecutarPipelineDocumental`

### Base de evidência

- requisitos integrados
- diagrama complementar de cenários especializados

## 7.4 `ExecutarPipelinePorID`

### Objetivo

Executar um pipeline já persistido e identificado no sistema.

### Ator principal

- `usuario configurador`

### Gatilho

O usuário solicita a execução de um pipeline salvo por identificador.

### Pré-condições

- o pipeline deve existir no repositório

### Pós-condições

- a execução do pipeline salvo é iniciada e processada

### Fluxo principal

1. o usuário informa o identificador do pipeline
2. o sistema recupera a configuração salva
3. o sistema valida a possibilidade de execução
4. o sistema executa o pipeline
5. o sistema retorna os resultados

### Fluxos alternativos

- pipeline inexistente
- configuração corrompida
- falha durante a execução

### Observações de modelagem

- mantido como caso especializado, mas sua posição final segue como dívida técnica

### Base de evidência

- [docs/projeto/roadmap_arquitetural.md](/home/thiago/coleta_showtrials/docs/projeto/roadmap_arquitetural.md)
- diagrama complementar de cenários especializados

## 7.5 `ConsultarResultadosDePipeline`

### Objetivo

Consultar resultados produzidos por execuções anteriores de pipeline.

### Ator principal

- `usuario configurador`

### Gatilho

O usuário deseja revisar ou reaproveitar resultados já produzidos.

### Pré-condições

- deve existir resultado consultável

### Pós-condições

- os resultados disponíveis são apresentados ao usuário

### Fluxo principal

1. o usuário solicita resultados de pipeline
2. o sistema localiza execuções e resultados disponíveis
3. o sistema apresenta o material consultável

### Fluxos alternativos

- ausência de resultados
- falha ao recuperar histórico

### Observações de modelagem

- caso lateral, não tratado como especialização de execução
- sua posição futura entre complementar e principal permanece em aberto

### Base de evidência

- diagrama complementar de cenários especializados
- revisão integrada dos casos de uso

## 8. Questões em aberto

Permanecem como pontos ainda não totalmente resolvidos:

- a posição final de `ExecutarPipeline`
- a granularidade definitiva de `ObterEstatisticas`
- a posição final de `ExecutarPipelinePorID`
- o refinamento futuro de `PersistirProdutosDerivados`
- a eventual necessidade de detalhar melhor casos colaborativos ou administrativos

## 9. Próximos passos

Os próximos passos recomendados são:

- abrir a matriz de rastreabilidade entre atores, casos de uso e requisitos
- consolidar depois a matriz entre casos de uso, diagramas e insumos
- usar esse conjunto completo de casos de uso como base para a ponte com a arquitetura
