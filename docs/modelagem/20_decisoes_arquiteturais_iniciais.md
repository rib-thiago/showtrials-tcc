# Decisões Arquiteturais Iniciais

## 1. Objetivo do documento

Este documento consolida as **decisões arquiteturais iniciais** já assumidas pela frente até o presente momento.

Seu objetivo não é encerrar toda a arquitetura do projeto, mas registrar aquilo que já pode ser tratado como decisão suficientemente consolidada para orientar os próximos artefatos.

## 2. Base de evidência utilizada

Este documento se apoia principalmente em:

- [17_drivers_arquiteturais.md](/home/thiago/coleta_showtrials/docs/modelagem/17_drivers_arquiteturais.md)
- [18_mapeamento_requisitos_para_drivers.md](/home/thiago/coleta_showtrials/docs/modelagem/18_mapeamento_requisitos_para_drivers.md)
- [19_mapeamento_casos_de_uso_para_blocos_arquiteturais.md](/home/thiago/coleta_showtrials/docs/modelagem/19_mapeamento_casos_de_uso_para_blocos_arquiteturais.md)
- [docs/projeto/direcionamento_arquitetural_engine_mvp.md](/home/thiago/coleta_showtrials/docs/projeto/direcionamento_arquitetural_engine_mvp.md)
- [docs/projeto/analise_arquitetural.md](/home/thiago/coleta_showtrials/docs/projeto/analise_arquitetural.md)
- requisitos e casos de uso da frente

## 3. Critério de decisão adotado

Uma decisão foi considerada consolidada nesta etapa quando:

- aparece repetidamente em mais de um artefato
- é coerente com os requisitos e casos de uso já produzidos
- não depende de hipótese isolada
- já orienta, de fato, o desenho dos próximos artefatos

## 4. Decisões arquiteturais consolidadas

## 4.1 Evolução incremental, sem ruptura total

### Decisão

A evolução para a engine futura será incremental e partirá da base atual, sem reescrita total do projeto.

### Justificativa

- essa diretriz aparece explicitamente nos requisitos e na transição
- ela preserva CLI, Web, base atual e continuidade conceitual do ShowTrials

### Impacto

- impõe presença de adaptadores, convivência de estilos e migração gradual

## 4.2 Manutenção da separação em camadas

### Decisão

A evolução arquitetural deve preservar a força da arquitetura limpa já existente, mantendo separação entre domínio, aplicação, infraestrutura e interfaces.

### Justificativa

- a análise arquitetural prévia valoriza explicitamente essa força do projeto
- a frente não pretende sacrificar esses ganhos na generalização para plataforma

### Impacto

- orienta 4+1, C4, UML e futuras decisões de módulo

## 4.3 Configuração externa e explícita de pipeline

### Decisão

Pipelines devem ser representados de forma explícita e configurável, com tendência forte a configuração externa declarativa.

### Justificativa

- coerente com requisitos de configurabilidade
- coerente com casos `CriarPipeline`, `ConfigurarPipeline`, `EditarPipeline`
- reforçado pelo direcionamento arquitetural do MVP

### Impacto

- exige entidade/configuração de pipeline
- exige validação de configuração

## 4.4 Separação entre configuração e execução

### Decisão

Configuração de pipeline e execução de pipeline devem ser tratadas como responsabilidades arquiteturais distintas.

### Justificativa

- a frente consolidou casos separados para criar, configurar, editar e executar
- os blocos arquiteturais já refletiram essa distinção

### Impacto

- evita colapsar catálogo de pipelines e executor em um único núcleo confuso

## 4.5 Separação entre transformação e persistência

### Decisão

Transformação/processamento e persistência/saída devem ser separados.

### Justificativa

- essa separação aparece como correção do acoplamento forte do sistema atual
- foi explicitamente consolidada no direcionamento arquitetural da engine

### Impacto

- favorece transformadores mais puros
- desloca persistência para sinks, adaptadores ou mecanismos dedicados

## 4.6 Uso de contexto explícito de execução

### Decisão

A execução da engine deve ser orientada por um contexto explícito de pipeline.

### Justificativa

- consolidado no direcionamento arquitetural da engine
- coerente com a necessidade de transportar documentos, artefatos, estado e resultados agregados

### Impacto

- influencia diretamente a modelagem futura de componentes e sequência

## 4.7 Modularidade baseada em sources, processors e sinks

### Decisão

A decomposição funcional futura deve reconhecer explicitamente papéis equivalentes a:

- source
- processor
- sink

### Justificativa

- já consolidado no documento de requisitos e nos drivers
- coerente com a necessidade de múltiplas entradas, processamentos e saídas

### Impacto

- influencia C4, componentes e contratos do domínio

## 4.8 Persistência configurável de produtos derivados

### Decisão

Traduções, análises e outros produtos derivados devem ser tratados como resultados relevantes e potencialmente persistíveis, de forma configurável.

### Justificativa

- aparece repetidamente em requisitos, casos de uso e drivers
- preserva tanto o comportamento atual quanto a flexibilidade futura

### Impacto

- exige modelar resultados derivados com mais cuidado

## 4.9 Distinção entre resultado automático e revisão humana

### Decisão

Resultados produzidos automaticamente e resultados revisados por humano devem permanecer distinguíveis no sistema.

### Justificativa

- essa necessidade emergiu fortemente nas especificações textuais de análise e revisão de tradução
- possui relevância real para uso acadêmico e interpretativo

### Impacto

- exige estados, metadados ou versionamento que preservem a origem do resultado

## 4.10 Preservação de CLI e Web como consumidores legítimos do núcleo

### Decisão

CLI e Web devem ser preservadas como consumidores legítimos do núcleo de aplicação, e não como exceções periféricas.

### Justificativa

- a frente consolidou ambas como interfaces relevantes
- o uso real do projeto depende dessa coexistência

### Impacto

- reforça arquitetura com núcleo reutilizável por múltiplas interfaces

## 5. Decisões ainda não consolidadas

Os pontos abaixo ainda não devem ser tratados como decisão fechada:

- se `RevisarTraducao` permanecerá no núcleo principal do sistema-alvo ou migrará definitivamente para casos especializados
- se `ExecutarPipelinePorID` é especialização real ou apenas detalhe operacional
- se “Resultados derivados” e “Revisão” permanecerão no mesmo bloco arquitetural futuro
- se haverá bloco arquitetural explícito para telemetria, acompanhamento e auditoria de execução

## 6. Inferências adotadas

As principais inferências adotadas neste documento foram:

- decisões repetidas em requisitos, casos de uso e documentos arquiteturais prévios foram tratadas como já consolidadas
- pontos ainda ambíguos foram explicitamente mantidos fora do conjunto de decisões fechadas

## 7. Dívidas técnicas registradas

Permanecem como pontos para aprofundamento futuro:

- eventual transformação dessas decisões em ADRs mais formais
- definição de prioridade e dependência entre decisões
- revisão futura do conjunto à luz do 4+1 e do C4

## 8. Próximos passos

Os próximos passos recomendados são:

- abrir o glossário arquitetural e técnico
- depois iniciar a visão arquitetural formal com 4+1
