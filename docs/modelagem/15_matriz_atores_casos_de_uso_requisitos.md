# Matriz de Atores, Casos de Uso e Requisitos

## 1. Objetivo do documento

Este documento consolida a primeira **matriz de rastreabilidade** da frente, conectando:

- atores
- casos de uso
- requisitos integrados

Seu objetivo é tornar mais explícita a relação entre:

- quem usa o sistema
- o que esse ator busca realizar
- quais blocos de requisitos sustentam esse comportamento

## 2. Base de evidência utilizada

Esta matriz se apoia principalmente em:

- [03_documento_de_requisitos.md](/home/thiago/coleta_showtrials/docs/modelagem/03_documento_de_requisitos.md)
- [07_casos_de_uso_iniciais.md](/home/thiago/coleta_showtrials/docs/modelagem/07_casos_de_uso_iniciais.md)
- [13_especificacoes_textuais_de_casos_de_uso_prioritarios.md](/home/thiago/coleta_showtrials/docs/modelagem/13_especificacoes_textuais_de_casos_de_uso_prioritarios.md)
- [14_especificacoes_textuais_de_casos_de_uso_secundarios.md](/home/thiago/coleta_showtrials/docs/modelagem/14_especificacoes_textuais_de_casos_de_uso_secundarios.md)
- [04_mapa_de_stakeholders_atores_e_objetivos.md](/home/thiago/coleta_showtrials/docs/modelagem/insumos/04_mapa_de_stakeholders_atores_e_objetivos.md)

## 3. Critério de rastreabilidade adotado

Nesta etapa, a matriz referencia os requisitos integrados por **blocos/seções** do documento principal, e não por identificadores atômicos de requisito.

Essa decisão foi adotada porque o [03_documento_de_requisitos.md](/home/thiago/coleta_showtrials/docs/modelagem/03_documento_de_requisitos.md) está organizado por:

- grupos funcionais (`12.x`)
- grupos não funcionais (`13.x`)

e ainda não por uma taxonomia formal de RF/RNF unitários numerados.

## 4. Matriz principal

| Ator | Caso de uso | Plano | Requisitos relacionados | Justificativa de rastreabilidade |
|---|---|---|---|---|
| `usuario operador` | `ListarDocumentos` | Sistema atual | `12.3`, `12.9`, `13.1` | materializa consulta ao acervo e uso por CLI/Web |
| `usuario operador` | `ObterDocumento` | Sistema atual | `12.3`, `12.2`, `12.9`, `13.1` | acessa documento e seus dados persistidos com foco de uso |
| `usuario operador` | `ClassificarDocumento` | Sistema atual | `12.5`, `12.2`, `13.4` | enriquece o documento com metadados úteis ao acervo |
| `usuario operador` | `TraduzirDocumento` | Sistema atual | `12.4`, `12.2`, `13.1` | produz tradução vinculada ao documento e persistida no modelo atual |
| `usuario operador` | `ListarTraducoes` | Sistema atual | `12.3`, `12.4` | consulta traduções já associadas ao documento |
| `usuario operador` | `ObterEstatisticas` | Sistema atual | `12.5`, `13.1` | fornece visão agregada do acervo e seus dados |
| `usuario operador` | `AnalisarDocumento` | Sistema atual | `12.5`, `12.2`, `13.3` | produz resultados analíticos e pode gerar produtos derivados |
| `usuario operador` | `AnalisarAcervo` | Sistema atual | `12.5`, `12.3`, `13.3` | amplia a análise para o conjunto do acervo |
| `usuario operador` | `ExportarDocumento` | Sistema atual | `12.8`, `12.9`, `13.1` | materializa saída/exportação para uso posterior |
| `usuario operador` | `GerarRelatorio` | Sistema atual | `12.5`, `12.8`, `13.1` | consolida dados documentais e analíticos em artefato de saída |
| `usuario configurador` | `ConfigurarPipeline` | Transição | `12.6`, `12.7`, `13.5`, `13.3` | representa a virada para configuração explícita e reproduzível |
| `usuario configurador` | `ExecutarPipeline` | Transição | `12.7`, `13.6`, `13.2` | expressa a execução do fluxo configurado no plano de transição |
| `usuario configurador` | `CriarPipeline` | Sistema-alvo | `12.6`, `13.5` | cria base inicial de pipeline passível de configuração e reutilização |
| `usuario configurador` | `ListarPipelines` | Sistema-alvo | `12.6`, `12.9`, `13.5` | permite consultar pipelines definidos no sistema |
| `usuario configurador` | `EditarPipeline` | Sistema-alvo | `12.6`, `13.5`, `13.4` | ajusta pipelines persistidos e reforça configurabilidade contínua |
| `usuario configurador` | `ExecutarPipelineDocumental` | Sistema-alvo | `12.7`, `12.1`, `12.5`, `13.2`, `13.3` | núcleo operacional da engine sobre entradas documentais |
| `usuario configurador` | `PersistirProdutosDerivados` | Sistema-alvo | `12.2`, `12.8`, `13.5` | registra resultados gerados de forma configurável no sistema-alvo |
| `usuario configurador` | `RevisarTraducao` | Sistema-alvo | `12.4`, `12.2`, `13.1` | qualifica traduções e distingue revisão humana de resultado automático |
| `usuario configurador` | `ProcessarPDFcomOCR` | Especializado | `12.1`, `12.7`, `13.3` | especializa execução documental para OCR e tratamento de PDF |
| `usuario configurador` | `ExecutarPipelineDeTraducao` | Especializado | `12.4`, `12.7`, `13.5` | especializa a execução para tradução documental configurada |
| `usuario configurador` | `ExecutarPipelineDeRaspagemEAnalise` | Especializado | `12.1`, `12.5`, `12.7`, `13.3` | combina obtenção de conteúdo externo com análise posterior |
| `usuario configurador` | `ExecutarPipelinePorID` | Especializado | `12.6`, `12.7`, `13.5` | especializa a execução sobre pipeline previamente salvo |
| `usuario configurador` | `ConsultarResultadosDePipeline` | Especializado | `12.3`, `12.8`, `13.1` | permite consultar resultados já produzidos e persistidos |

## 5. Leitura interpretativa da matriz

Algumas leituras se destacam a partir da matriz.

### 5.1 Predominância do `usuario operador` no sistema atual

O `usuario operador` concentra casos de uso ligados a:

- consulta
- tradução
- análise
- exportação
- relatório

Essa concentração confirma a natureza documento-cêntrica do ShowTrials atual.

### 5.2 Predominância do `usuario configurador` na transição e no sistema-alvo

O `usuario configurador` concentra casos de uso ligados a:

- configuração
- execução
- persistência configurável
- revisão
- especializações de pipeline

Essa concentração confirma a virada arquitetural que a frente vem modelando.

### 5.3 Centralidade dos blocos `12.5`, `12.6` e `12.7`

Os blocos mais recorrentes na matriz são:

- `12.5` análise e enriquecimento
- `12.6` configuração de pipeline
- `12.7` execução de pipeline

Isso mostra que a frente já se deslocou, corretamente, de uma leitura puramente documento-cêntrica para uma leitura mais rica em:

- análise
- configurabilidade
- orquestração de fluxos

## 6. Limitações da matriz nesta etapa

Esta matriz ainda tem limitações importantes:

- os requisitos ainda não estão numerados em nível atômico
- alguns vínculos são mais fortes que outros, embora a tabela ainda não expresse essa gradação
- certos casos do sistema-alvo e especializados continuam dependentes de amadurecimento arquitetural posterior

## 7. Inferências adotadas

As principais inferências adotadas nesta matriz foram:

- casos de uso especializados foram vinculados aos mesmos blocos funcionais do caso geral mais próximo, acrescidos do recorte específico do cenário
- `RevisarTraducao` foi mantido vinculado aos blocos de tradução e persistência, mesmo permanecendo como ponto parcialmente aberto da frente
- `PersistirProdutosDerivados` foi mantido separado de `ExecutarPipelineDocumental`, em coerência com a modelagem atual

## 8. Dívidas técnicas registradas

Permanecem como pontos para análise futura:

- eventual renumeração de requisitos em nível atômico
- gradação futura entre vínculo forte, médio ou inferido
- posição final de certos casos especializados no sistema-alvo

## 9. Próximos passos

Os próximos passos recomendados são:

- abrir a matriz entre casos de uso, diagramas e insumos
- usar essas duas matrizes como base de rastreabilidade da frente de casos de uso
- em seguida, abrir a ponte formal entre requisitos, casos de uso e arquitetura
