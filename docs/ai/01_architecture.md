# Arquitetura

## 1. Escopo e regra de evidência

Este documento descreve a arquitetura do projeto com base explícita nas seguintes fontes:

- histórico Git analisado
- mensagens de commit
- análise por diretórios em `src/`, `docs/projeto/` e `docs/flows/`
- issues lidas, incluindo corpo e comentários quando disponíveis
- documentos de projeto e direcionamento arquitetural
- código central já inspecionado diretamente

Regra central de interpretação:

- **implementado** = o que está sustentado principalmente por código e/ou histórico Git
- **em transição** = o que já aparece no código ou no histórico, mas de forma parcial e não dominante
- **planejado / documentado** = o que aparece em documentação e issues, mas não foi confirmado como implementação suficiente no código central inspecionado

Quando a evidência for insuficiente para uma conclusão mais forte, isso será registrado explicitamente como lacuna.

## 2. Leitura arquitetural em três camadas temporais

Para descrever o projeto de forma fiel à sua evolução real, a arquitetura precisa ser separada em três planos:

1. **arquitetura original do ShowTrials**
2. **transição arquitetural efetivamente iniciada**
3. **direção futura associada à engine de pipeline e, de modo ainda não confirmado formalmente, à ideia de CraftText**

Essa separação é necessária porque o repositório atual contém ao mesmo tempo:

- traços claros da arquitetura implementada historicamente
- sinais reais de modularização posterior
- backlog arquitetural futuro formalizado em docs e issues

## 3. Arquitetura original do ShowTrials

## 3.1 Origem arquitetural real do projeto

O histórico Git mostra que o projeto **não** nasceu como engine de pipeline nem como sistema abstrato de processamento documental.

Os primeiros commits mostram:

- aplicação funcional monolítica
- código concentrado na raiz do repositório
- banco SQLite já utilizado
- interface terminal/Rich
- tradução surgindo como funcionalidade concreta

Essa fase inicial é importante porque ela mostra a motivação real do sistema:

- resolver um problema documental concreto
- com forte orientação a fluxo operacional e utilitário

## 3.2 Marco estrutural principal: refatoração para `src/` e arquitetura em camadas

O principal marco arquitetural implementado no histórico ocorre nos commits:

- `6773452` `FASE 1 - Domain Layer concluída`
- `4b7ac57` `FASE 2 - Application Layer concluída`
- `16a3ab0` `FASE 3 - Infrastructure Layer concluída`
- `7f2d782` `FASE 4 - Interface Layer concluída`

Esse conjunto estabelece a base estrutural do sistema atual:

- `domain`
- `application`
- `infrastructure`
- `interface`

Com base no histórico e no código central inspecionado, a arquitetura original consolidada do ShowTrials pode ser descrita como:

- uma variação de **Clean Architecture** aplicada a um sistema documental específico
- fortemente centrada em `Documento`
- organizada por operações de aplicação
- fortemente ligada à persistência
- pensada para um domínio histórico concreto, e não para pipeline configurável genérico

## 3.3 Caracterização da arquitetura original

### 3.3.1 Camada de domínio

O domínio observado no código central é centrado em:

- entidades documentais
- value objects de classificação e metadados
- interfaces de repositório

O núcleo mais forte observado continua sendo a entidade `Documento`.

Isso sugere uma modelagem onde:

- o documento é o agregado dominante
- o restante da arquitetura orbita operações sobre esse agregado

### 3.3.2 Camada de aplicação

O padrão dominante observado é:

- casos de uso orientados a tarefas específicas
- orquestração imperativa
- dependência clara de repositórios e serviços
- acoplamento frequente entre leitura, processamento e persistência

Isso aproxima a aplicação mais de um conjunto de fluxos transacionais especializados do que de uma engine declarativa.

### 3.3.3 Camada de infraestrutura

A infraestrutura observada inclui:

- SQLite como persistência central
- integração com serviços externos para tradução e NLP
- configuração de ambiente e serviços

Aqui o ponto mais importante é que a infraestrutura não aparece apenas como detalhe intercambiável:

- ela influencia diretamente o formato dominante dos fluxos de aplicação

### 3.3.4 Camada de interface

O histórico e o código mostram:

- CLI como interface fortemente presente desde a arquitetura em camadas
- Web entrando depois como expansão funcional relevante

As interfaces não apenas expõem casos de uso; elas também concentram parte importante do wiring manual da aplicação.

## 3.4 Fluxo arquitetural dominante do ShowTrials

Com base no código e no histórico, o fluxo dominante do sistema implementado é melhor representado como:

`repositório -> entidade Documento -> caso de uso -> mutação/processamento -> persistência/artefato`

Essa formulação é mais fiel ao estado implementado do que descrições de pipeline configurável.

## 4. Componentes centrais do código e seu papel arquitetural real

## 4.1 `Documento` como agregado arquitetural dominante

Em `src/domain/entities/documento.py`, foi observado que `Documento` concentra:

- identidade persistida opcional
- dados textuais e documentais
- metadados enriquecidos
- validações
- serialização
- suporte opcional de telemetria

Arquiteturalmente, isso importa porque:

- o sistema atual gira em torno do agregado documental
- não há evidência equivalente de uma abstração dominante de pipeline ou contexto de execução

## 4.2 Casos de uso como unidade principal de orquestração

Os arquivos inspecionados em `src/application/use_cases/` mostram que a aplicação atual é conduzida principalmente por casos de uso verticais.

Em `traduzir_documento.py`, foi observado:

- leitura por ID
- consulta de tradução existente
- obtenção de serviço de tradução
- produção de `Traducao`
- persistência imediata

Em `analisar_acervo.py`, foi observado:

- listagem de documentos
- agregação de estatísticas
- uso condicional de serviços externos
- produção de artefatos

Isso indica que o caso de uso atual:

- não é apenas coordenador fino
- também absorve parte relevante da composição operacional do fluxo

## 4.3 `SQLiteDocumentoRepository` como peça nuclear, não periférica

Em `src/infrastructure/persistence/sqlite_repository.py`, foi observada uma implementação que:

- materializa `Documento` a partir de rows
- executa operações centrais de persistência
- expõe consulta auxiliar de traduções

Arquiteturalmente, isso sugere:

- persistência muito próxima do modelo dominante
- banco SQLite funcionando como infraestrutura nuclear real
- fronteiras nem sempre rígidas entre agregado documental e consultas auxiliares

## 4.4 CLI e Web como bordas com composição manual relevante

Em `src/interface/cli/app.py` e `src/interface/web/app.py`, foi observada composição explícita de:

- repositórios concretos
- registry
- serviços
- casos de uso

Isso é relevante porque indica que:

- a arquitetura não está organizada em torno de um container mais abstrato de composição
- o wiring ainda vive fortemente na borda
- a modularização existente ainda não eliminou o caráter manual da montagem

## 4.5 `ServiceRegistry` e factories como transição parcial

O histórico Git mostra a introdução do registry como marco arquitetural real em:

- `b185f0f` `feat(registry): implementa Service Registry com lazy loading`
- com ajustes posteriores como `c7afe7c` para corrigir a injeção do registry nos casos de uso

No código central, isso se materializa em:

- `src/infrastructure/registry.py`
- `src/infrastructure/factories.py`
- `src/application/use_cases/base.py`
- uso parcial em alguns casos de uso e na aplicação Web

Arquiteturalmente, o papel real desses componentes parece ser:

- centralizar criação e resolução de serviços
- reduzir parte do custo de inicialização e do acoplamento de instanciação
- preparar o terreno para maior modularidade

O que **não** pode ser concluído a partir dessa evidência:

- que já existe plugin architecture completa
- que registry equivale a executor de pipeline
- que source/processor/sink já são contratos dominantes no sistema

## 5. Acoplamentos estruturais e limitações da arquitetura atual

## 5.1 Acoplamento com persistência

O código central inspecionado mostra um padrão dominante de:

- ler do banco
- operar sobre entidade documental
- persistir resultado ou gerar artefato derivado

Isso implica:

- persistência muito próxima da lógica de aplicação
- ausência de separação arquitetural forte entre transformação e gravação

## 5.2 Acoplamento ao domínio documental atual

A arquitetura observada parece otimizada para:

- um agregado principal
- um acervo específico
- um conjunto relativamente fixo de operações

Consequência:

- a generalização para outras fontes ou outros domínios não aparece como capacidade nativa já consolidada

## 5.3 Acoplamento entre orquestração, transformação e saída

Os casos de uso observados frequentemente misturam:

- leitura do acervo
- decisão de processamento
- chamada de serviços externos
- persistência
- geração de arquivo/artefato

Isso reduz a nitidez entre:

- transformação
- coordenação
- persistência
- exportação

## 5.4 Dependência prática de infraestrutura específica

A introdução histórica de tradução, NLP, Web e CI mostra crescimento de dependências operacionais concretas.

Isso ajuda a explicar:

- por que o projeto precisou endurecer qualidade e CI
- por que surgiram issues específicas para dependências NLP
- por que a arquitetura futura insiste tanto em modularização e separação de responsabilidades

## 5.5 Limitação estrutural mais importante

A limitação estrutural mais importante observada até aqui é:

- o sistema atual é forte como aplicação documental especializada
- mas não expõe ainda, como abstração dominante implementada, um modelo genérico de execução de pipeline

## 6. Transição arquitetural já iniciada

## 6.1 O que o histórico permite afirmar

O histórico Git permite afirmar que houve transição real em pelo menos dois níveis:

- de protótipo monolítico para arquitetura em camadas
- de arquitetura em camadas puramente orientada a operações para uma forma parcialmente mais modular com registry/factories

## 6.2 O que o código permite afirmar

O código central permite afirmar que:

- já existe mecanismo de resolução centralizada de serviços
- já existe alguma separação adicional entre criação de serviço e uso
- a Web usa configuração estruturada para registrar serviços

## 6.3 O que permanece incompleto

Permanece incompleto, com base no código inspecionado:

- adoção sistêmica do `ServiceRegistry`
- remoção do wiring manual da borda
- separação dominante entre transformação e persistência
- reorganização do sistema em torno de contexto de execução genérico

Conclusão:

- há transição arquitetural real
- essa transição é parcial e não autoriza descrever o sistema atual como engine pronta

## 7. Direção futura: pipeline/engine

## 7.1 O que vem da documentação de projeto

Os documentos de projeto e direcionamento arquitetural descrevem uma arquitetura-alvo baseada em:

- pipeline configurável
- configuração declarativa
- contracts claros para etapas
- separação entre transformação e persistência
- versionamento de pipeline

Esses documentos são importantes porque mostram uma mudança conceitual explícita:

- de aplicação específica orientada a documentos
- para plataforma configurável de processamento documental

## 7.2 O que vem das issues

As issues abertas da milestone `MVP - Engine de Pipeline` materializam essa direção em unidades arquiteturais explícitas:

- `#10` contrato de `Transformer`
- `#11` contrato de `Sink`
- `#12` `ContextoPipeline`
- `#13` executor mínimo
- `#14` pipeline configurável via YAML/JSON
- `#15` `Iterable` para streaming
- `#16` versionamento incremental de pipeline
- `#17` migração de um caso de uso real para a nova arquitetura

Isso é relevante porque essas issues tornam a direção futura:

- formal
- rastreável
- priorizada
- vinculada à milestone ativa

## 7.3 O que ainda não foi confirmado como implementação

Apesar da força documental e estratégica dessa direção, até esta etapa **não foram observados no código central inspecionado**:

- entidade `Pipeline`
- `ContextoPipeline`
- executor de pipeline consolidado
- contratos explícitos de `Transformer` e `Sink`
- execução configurada por YAML/JSON como fluxo dominante
- versionamento de pipeline efetivamente implantado

Portanto:

- a engine de pipeline está fortemente confirmada como **plano arquitetural**
- ela **não** está confirmada como arquitetura implementada dominante no código central atual

## 8. ShowTrials, direção futura e CraftText

## 8.1 ShowTrials como arquitetura implementada

O nome e a arquitetura historicamente confirmados continuam sendo os de ShowTrials:

- sistema documental específico
- centrado em `Documento`
- orientado a persistência
- organizado em casos de uso

## 8.2 Engine de pipeline como direção futura formal

A engine de pipeline está confirmada como direção futura por:

- documentos de projeto
- milestone ativa
- issues abertas estratégicas

## 8.3 CraftText como conceito ainda insuficientemente ancorado

Até esta etapa, a relação entre essa direção futura e o nome `CraftText` continua com evidência insuficiente em Git e issues.

O que pode ser dito:

- `CraftText` pode funcionar como rótulo conceitual de uma direção futura de plataforma em alguns materiais

O que não pode ser dito com segurança:

- que houve renomeação formal do repositório
- que `CraftText` já é identidade oficial consolidada
- que existe decisão rastreável em issues formalizando ShowTrials -> CraftText

## 9. Divergências entre implementação, documentação e planejamento

## 9.1 O que está implementado

Com melhor suporte de evidência:

- arquitetura em camadas
- centralidade de `Documento`
- casos de uso imperativos
- persistência SQLite
- CLI e Web presentes no código
- registry/factories como modularização parcial

## 9.2 O que está documentado e parcialmente refletido no código

Com evidência mista:

- transição para maior modularidade
- desacoplamento parcial da criação de serviços
- uso de configuração para registrar serviços

## 9.3 O que está planejado, mas não confirmado como implementado

Com suporte principal em documentação e issues:

- contracts de pipeline
- contexto explícito de execução
- executor mínimo genérico
- streaming via `Iterable`
- pipeline configurável e versionado
- migração de casos de uso para a nova arquitetura
- generalização mais ampla da plataforma

## 9.4 Divergência principal

A divergência principal a registrar é:

- o sistema atual implementado ainda é majoritariamente ShowTrials documento-cêntrico
- a documentação e as issues apontam para uma arquitetura de pipeline mais genérica
- a transição entre esses dois estados ainda não se completou no código central observado

## 10. Restrições arquiteturais para mudanças futuras

As seguintes restrições devem orientar mudanças futuras, com base no que já foi implementado e no que está formalizado em docs/issues.

## 10.1 Não reforçar o acoplamento atual com persistência

Mudanças futuras devem evitar:

- ampliar lógica de transformação diretamente dentro de fluxos acoplados ao banco
- consolidar ainda mais persistência e processamento na mesma unidade

## 10.2 Não tratar registry/factories como solução final por si só

Enquanto não houver novos componentes confirmados, `ServiceRegistry` e factories devem ser tratados como:

- etapa intermediária de modularização

e não como prova de:

- plugin architecture plena
- pipeline engine pronta
- separação completa entre source/processor/sink

## 10.3 Toda mudança estrutural deve ser rastreável como mudança estrutural

Como a arquitetura está em transição e a governança atual é explícita, mudanças arquiteturais devem:

- ter issue apropriada
- explicitar impacto estrutural
- não ser escondidas dentro de feature ou bugfix

## 10.4 Preservar separação clara entre estado atual e arquitetura-alvo

Ao modificar documentação ou código, deve-se evitar:

- descrever o sistema atual com capacidades ainda não implementadas
- introduzir abstrações futuras sem registrar que são futuras
- reescrever a narrativa do histórico como se a engine já tivesse substituído ShowTrials

## 10.5 Favorecer contratos explícitos e migração incremental

As issues de engine sugerem que a evolução futura mais coerente passa por:

- contratos claros
- contexto explícito
- migração de um caso de uso real
- separação gradual entre transformação e persistência

Esses pontos devem ser vistos como restrições positivas:

- a evolução futura precisa ser incremental e verificável
- não deve depender de reinterpretação retroativa da arquitetura já existente

## 11. Lacunas e evidência insuficiente

Permanecem como lacunas relevantes:

- inspeção mais ampla de casos de uso além dos arquivos centrais já lidos
- inspeção completa da Web além de `app.py`
- confirmação de toda a extensão de uso do registry
- verificação do papel de `sqlite_traducao_repository.py`
- inspeção de arquivos adicionais de configuração
- confirmação, por código, de qualquer parte concreta da engine de pipeline
- confirmação histórica ou formal da relação entre a direção futura e o nome `CraftText`

## 12. Síntese arquitetural final

A descrição mais conservadora e tecnicamente fiel do projeto, nesta etapa, é:

- a arquitetura implementada e historicamente confirmada é a do **ShowTrials**: sistema documental específico, em camadas, centrado em `Documento`, orientado a persistência e casos de uso imperativos
- existe **transição arquitetural real**, visível em registry, factories e configuração de serviços, mas ela ainda é parcial
- a **direção futura** para uma engine de pipeline configurável está fortemente sustentada por documentação de projeto e issues estratégicas
- a associação dessa direção futura ao nome **CraftText** permanece, até aqui, com evidência insuficiente para ser tratada como fato consolidado
