# Drivers Arquiteturais

## 1. Objetivo do documento

Este documento inaugura formalmente a ponte entre a frente de **casos de uso** e a frente **arquitetural**, consolidando os principais **drivers arquiteturais** do projeto.

Seu objetivo é tornar explícito:

- quais forças empurram a arquitetura
- de onde essas forças vêm
- que consequências elas impõem às decisões arquiteturais futuras

## 2. Base de evidência utilizada

Este documento se apoia principalmente em:

- [03_documento_de_requisitos.md](/home/thiago/coleta_showtrials/docs/modelagem/requisitos/principais/03_documento_de_requisitos.md)
- [12_revisao_integrada_dos_casos_de_uso.md](/home/thiago/coleta_showtrials/docs/modelagem/analise/principais/12_revisao_integrada_dos_casos_de_uso.md)
- [13_especificacoes_textuais_de_casos_de_uso_prioritarios.md](/home/thiago/coleta_showtrials/docs/modelagem/analise/principais/13_especificacoes_textuais_de_casos_de_uso_prioritarios.md)
- [14_especificacoes_textuais_de_casos_de_uso_secundarios.md](/home/thiago/coleta_showtrials/docs/modelagem/analise/principais/14_especificacoes_textuais_de_casos_de_uso_secundarios.md)
- [15_matriz_atores_casos_de_uso_requisitos.md](/home/thiago/coleta_showtrials/docs/modelagem/analise/principais/15_matriz_atores_casos_de_uso_requisitos.md)
- [16_matriz_casos_de_uso_para_diagramas_e_insumos.md](/home/thiago/coleta_showtrials/docs/modelagem/analise/principais/16_matriz_casos_de_uso_para_diagramas_e_insumos.md)
- [docs/projeto/analise_arquitetural.md](/home/thiago/coleta_showtrials/docs/projeto/analise_arquitetural.md)
- [docs/projeto/direcionamento_arquitetural_engine_mvp.md](/home/thiago/coleta_showtrials/docs/projeto/direcionamento_arquitetural_engine_mvp.md)
- [docs/projeto/roadmap_arquitetural.md](/home/thiago/coleta_showtrials/docs/projeto/roadmap_arquitetural.md)

## 3. O que se entende por driver arquitetural nesta frente

Nesta frente, um driver arquitetural é qualquer força relevante que:

- restrinja decisões futuras
- oriente a decomposição da solução
- justifique prioridades de modularidade, execução, persistência ou interface
- ajude a explicar por que a arquitetura precisa assumir determinada forma

Os drivers consolidados aqui não são ainda decisões arquiteturais. Eles são o conjunto de pressões e objetivos que as futuras decisões deverão responder.

## 4. Drivers arquiteturais consolidados

## 4.1 Evolução incremental sem reescrita total

### Formulação do driver

A arquitetura futura deve permitir evolução incremental a partir da base atual, sem reescrever o sistema do zero.

### Origem

- requisitos integrados
- transição arquitetural já consolidada
- governança da frente

### Consequências arquiteturais

- necessidade de compatibilidade evolutiva
- presença de adaptadores e camadas de transição
- convivência entre fluxos antigos e novos
- impossibilidade de ruptura brusca entre ShowTrials atual e engine futura

## 4.2 Preservação de CLI e Web como interfaces relevantes

### Formulação do driver

A arquitetura deve preservar CLI e Web como formas legítimas e relevantes de operação do sistema.

### Origem

- requisitos integrados
- leitura factual do sistema atual
- histórico da frente

### Consequências arquiteturais

- separação clara entre núcleo de aplicação e interfaces
- necessidade de orquestração reutilizável por múltiplas interfaces
- impedimento de soluções excessivamente acopladas a uma interface única

## 4.3 Configurabilidade explícita dos fluxos de trabalho

### Formulação do driver

O sistema-alvo deve permitir configuração explícita, reproduzível e ajustável dos fluxos documentais.

### Origem

- requisitos integrados (`12.6`, `13.5`)
- casos de uso `ConfigurarPipeline`, `CriarPipeline`, `EditarPipeline`
- direcionamento arquitetural da engine

### Consequências arquiteturais

- necessidade de representação formal de pipeline
- necessidade de separação entre criação, configuração e execução
- necessidade de validação de configuração
- tendência a configuração externa declarativa

## 4.4 Separação entre transformação e persistência

### Formulação do driver

A arquitetura deve separar transformação/processamento de persistência/saída.

### Origem

- documento de direcionamento arquitetural
- requisitos integrados
- crítica ao modelo documento-cêntrico e orientado a persistência

### Consequências arquiteturais

- favorecimento de transformadores mais puros
- deslocamento da persistência para sinks ou mecanismos dedicados
- redução de acoplamento entre processamento e banco

## 4.5 Modularidade orientada a sources, processors e sinks

### Formulação do driver

A arquitetura futura deve permitir compor diferentes fontes, processadores e mecanismos de saída.

### Origem

- visão da engine futura
- análise arquitetural
- roadmap arquitetural

### Consequências arquiteturais

- necessidade de contratos/interfaces bem definidos
- possibilidade de pluginização ou composição modular equivalente
- necessidade de encaixe explícito entre entrada, processamento e saída

## 4.6 Suporte a múltiplos tipos de entrada documental

### Formulação do driver

A solução futura deve acomodar múltiplas formas de entrada documental, e não apenas o recorte histórico atual.

### Origem

- requisitos integrados (`12.1`)
- visão da engine futura
- cenários especializados já modelados

### Consequências arquiteturais

- generalização das entradas
- necessidade de abstrações de aquisição/coleta
- redução do acoplamento a uma única fonte ou formato

## 4.7 Suporte a produtos derivados e resultados persistíveis

### Formulação do driver

O sistema deve tratar traduções, análises e outros resultados como produtos derivados relevantes e potencialmente persistíveis.

### Origem

- requisitos integrados (`12.2`, `12.8`)
- casos de uso `TraduzirDocumento`, `AnalisarDocumento`, `PersistirProdutosDerivados`, `ConsultarResultadosDePipeline`

### Consequências arquiteturais

- necessidade de modelar resultados derivados de modo explícito
- necessidade de rastrear vínculo entre documento, execução e resultado
- necessidade de suportar persistência configurável

## 4.8 Execução não bloqueante e possibilidade de background

### Formulação do driver

A arquitetura deve admitir evolução para execução não bloqueante, em segundo plano e potencialmente auditável.

### Origem

- requisitos integrados (`12.7`, `13.2`)
- modelagem de `ExecutarPipelineDocumental`
- necessidades de auditoria e revisão intermediária já apontadas na frente

### Consequências arquiteturais

- separação entre definição de execução e acompanhamento da execução
- necessidade de estado explícito de execução
- compatibilidade futura com filas, jobs e retomadas

## 4.9 Rastreabilidade entre resultados automáticos e intervenção humana

### Formulação do driver

Resultados automáticos e resultados revisados por humano devem ser distinguíveis no sistema.

### Origem

- especificações textuais de `AnalisarDocumento`
- especificações textuais de `RevisarTraducao`
- preocupação explícita do domínio com uso acadêmico e interpretativo

### Consequências arquiteturais

- necessidade de metadados de origem do resultado
- necessidade de versionamento ou estados de validação
- necessidade de suportar revisão humana sem apagar a origem automática

## 4.10 Ergonomia do fluxo de trabalho como força arquitetural

### Formulação do driver

A arquitetura deve responder à ergonomia dos fluxos de trabalho, e não apenas à expansão funcional.

### Origem

- motivação arquitetural consolidada no documento de requisitos
- falas do usuário na elicitação
- crítica ao fluxo imperativo fixo do sistema atual

### Consequências arquiteturais

- arquitetura orientada ao uso real do sistema
- necessidade de configuração ajustável ao objetivo de trabalho
- necessidade de equilibrar poder de configuração e usabilidade

## 4.11 Generalização sem apagar a especialização histórica

### Formulação do driver

A arquitetura deve se generalizar para múltiplos domínios sem apagar a história de uso especializada que deu origem ao projeto.

### Origem

- mapa de stakeholders, atores e objetivos
- requisitos integrados
- discussões da frente

### Consequências arquiteturais

- necessidade de modelo de contexto/domínio explícito
- necessidade de evitar abstrações tão genéricas que percam aderência ao uso real
- preservação de compatibilidade conceitual com o ShowTrials atual

## 4.12 Documentação forte e rastreabilidade como requisito de arquitetura do projeto

### Formulação do driver

A evolução arquitetural deve ser acompanhada de documentação forte, suficiente para desenvolvimento, manutenção e avaliação acadêmica.

### Origem

- requisitos não funcionais
- governança
- objetivo acadêmico do projeto

### Consequências arquiteturais

- necessidade de decisões mais explícitas
- necessidade de artefatos de visão, rastreabilidade e justificativa
- impossibilidade de conduzir a evolução apenas por implementação ad hoc

## 5. Síntese interpretativa

Os drivers consolidados nesta etapa mostram que a arquitetura futura precisa responder simultaneamente a quatro grandes eixos:

- continuidade evolutiva
- configurabilidade e composição
- tratamento rico de documentos e produtos derivados
- rastreabilidade técnica e acadêmica

Isso confirma que a engine futura não pode ser tratada apenas como uma refatoração técnica. Ela precisa ser modelada como resposta coordenada a pressões de produto, uso, manutenção e governança.

## 6. Inferências adotadas

As principais inferências adotadas neste documento foram:

- a ergonomia do fluxo de trabalho foi tratada como driver arquitetural formal, e não apenas como motivação de produto
- a distinção entre resultado automático e revisão humana foi elevada a driver por seu impacto estrutural em persistência, versionamento e modelagem de estado
- a preservação da especialização histórica foi tratada como força arquitetural e não apenas como nota contextual

## 7. Dívidas técnicas registradas

Permanecem como pontos para aprofundamento futuro:

- medir a prioridade relativa de cada driver
- decidir quais drivers são mandatórios para o MVP estrutural e quais são de expansão
- detalhar melhor o impacto do contexto/domínio na futura modelagem arquitetural

## 8. Próximos passos

Os próximos passos recomendados são:

- abrir o mapeamento de requisitos para drivers
- depois abrir o mapeamento de casos de uso para blocos arquiteturais
- usar esse conjunto como base imediata para a visão 4+1 e o C4
