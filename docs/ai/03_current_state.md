# Estado Atual

## 1. Regra de leitura deste documento

Este documento descreve o estado atual do projeto com a seguinte hierarquia de evidência:

1. código inspecionado diretamente
2. commits e histórico Git
3. issues abertas e fechadas
4. documentação do projeto

Por isso, as classificações abaixo seguem três categorias explícitas:

- **implementado**: há evidência direta no código inspecionado
- **parcialmente implementado / em transição**: há código real, mas com lacunas, uso incompleto ou maturidade não confirmada
- **planejado / documentado**: aparece em docs, commits ou issues, mas não foi confirmado como implementação suficiente no código inspecionado

Quando algo não puder ser confirmado a partir do código lido, isso será dito explicitamente.

## 2. Síntese do estado atual

Com base no código central já inspecionado, o repositório atual deve ser descrito, de forma conservadora, como:

- uma aplicação **ShowTrials** centrada em documentos
- organizada em camadas (`domain`, `application`, `infrastructure`, `interface`)
- fortemente apoiada em persistência SQLite
- baseada em casos de uso imperativos
- com uma CLI cuja composição está explicitamente presente no código inspecionado
- com aplicação Web presente no código, mas ainda não validada ponta a ponta nesta sessão
- com `ServiceRegistry` e factories como sinais reais de transição arquitetural

O projeto **não** deve ser descrito, no estado atual confirmado por código, como engine de pipeline já implementada.

As issues e a milestone ativa confirmam uma direção futura para uma engine de pipeline configurável, mas isso deve ser narrado como **planejamento estratégico ativo**, não como capacidade já materializada no código central observado.

## 3. Implementado no código

## 3.1 Estrutura em camadas

Há evidência direta no repositório da organização em:

- `src/domain`
- `src/application`
- `src/infrastructure`
- `src/interface`

Essa estrutura também é coerente com os commits históricos que introduziram as fases de domínio, aplicação, infraestrutura e interface.

## 3.2 Modelo centrado em `Documento`

Em `src/domain/entities/documento.py`, foi observada implementação de:

- entidade `Documento`
- validações de domínio
- metadados documentais
- serialização
- suporte opcional de telemetria

Isso sustenta a leitura de que o modelo atual é documento-cêntrico.

## 3.3 Casos de uso imperativos do domínio atual

Foram inspecionados diretamente:

- `src/application/use_cases/base.py`
- `src/application/use_cases/traduzir_documento.py`
- `src/application/use_cases/analisar_acervo.py`

Esses arquivos mostram, de forma observável:

- dependência de repositórios
- orquestração imperativa
- uso de serviços externos
- persistência ou geração de artefatos no mesmo fluxo de operação

Isso confirma um estilo arquitetural orientado a casos de uso transacionais do domínio atual, e não a uma engine declarativa genérica.

## 3.4 Persistência SQLite como infraestrutura central

Em `src/infrastructure/persistence/sqlite_repository.py`, foram observados:

- conexão SQLite
- conversão de row para entidade
- operações de persistência como `salvar`, `buscar_por_id`, `listar`, `contar` e `remover`
- consulta auxiliar de traduções

Isso confirma que SQLite é parte central da implementação atual.

## 3.5 Registry e factories

Em:

- `src/infrastructure/registry.py`
- `src/infrastructure/factories.py`

foram observados:

- registro de serviços por nome
- lazy loading
- cache singleton
- factories para tradutor, analisador spaCy, wordcloud e exportador PDF mock
- alguns fallbacks para mocks

Esses componentes existem no código e, portanto, devem ser tratados como implementados.

## 3.6 CLI presente no código e mais diretamente observável

Em `src/interface/cli/app.py`, foi observada composição explícita de:

- repositórios
- registry
- serviços
- casos de uso
- comandos
- loop principal

Isso confirma existência da CLI no código.

O que **não** foi validado nesta etapa:

- execução ponta a ponta da CLI nesta sessão
- completude funcional de todos os comandos expostos

Logo, a formulação mais segura é:

- a CLI está **implementada no código** e é a interface mais diretamente observável entre os arquivos inspecionados

## 3.7 Aplicação Web presente no código

Em `src/interface/web/app.py`, foi observada:

- factory `create_app`
- carregamento de configuração
- registro de serviços no registry
- inicialização de repositórios
- criação de casos de uso
- montagem de rotas FastAPI
- disponibilidade de `/status`

Isso confirma existência de uma aplicação Web no código.

O que **não** foi confirmado nesta etapa:

- comportamento completo de todas as rotas
- consistência entre rotas, templates e dados exibidos
- maturidade funcional geral da interface Web

Portanto:

- a Web está **presente e implementada em parte observável do código**
- sua completude funcional permanece **não confirmada**

## 3.8 Configuração e tooling local

Em `pyproject.toml` e `config.yaml`, foram observados:

- configuração Poetry
- dependências principais e de desenvolvimento
- tarefas Taskipy
- serviços configuráveis como `translator`, `spacy`, `wordcloud` e `pdf_exporter`

Isso confirma existência de base local de configuração e automação.

## 4. Parcialmente implementado ou em transição

## 4.1 Uso sistêmico do `ServiceRegistry`

O registry existe e aparece no código observado, mas o uso ainda parece parcial.

Sinais concretos de parcialidade:

- a CLI ainda concentra composição manual significativa
- parte da montagem continua explícita na borda da interface
- `BaseUseCase` existe, mas a adoção sistêmica em todos os fluxos não foi confirmada

Conclusão:

- `ServiceRegistry` está implementado
- sua adoção como padrão dominante da aplicação ainda parece incompleta

## 4.2 Camada de configuração arquitetural

Há evidência de configuração estruturada por `config.yaml` e por referências a `ApplicationConfig`.

Mas ainda faltam confirmações importantes:

- inspeção detalhada de `ApplicationConfig`
- extensão real do uso da configuração fora dos pontos já lidos
- robustez desse mecanismo em toda a aplicação

Conclusão:

- existe infraestrutura de configuração
- a profundidade de adoção e a robustez global ainda são incertas

## 4.3 Telemetria

O código e o histórico Git mostram telemetria real em múltiplos módulos.

O que está suportado por evidência:

- telemetria foi introduzida por commits reais
- ela aparece em partes centrais do domínio, infraestrutura e casos de uso

O que ainda não foi confirmado nesta sessão:

- cobertura completa da telemetria em todo o repositório
- consistência total do padrão entre todos os módulos
- funcionamento atual ponta a ponta dos pontos de coleta

Conclusão:

- a telemetria não é apenas documental; ela existe no código
- porém sua adoção total e uniforme permanece não confirmada

## 4.4 Qualidade e CI

Commits e arquivos de configuração confirmam:

- uso de lint
- type-check
- testes
- cobertura
- GitHub Actions
- Taskipy como ponto importante do fluxo

Mas ainda faltam, nesta sessão:

- execução local completa do pipeline
- inspeção direta do workflow atual de CI
- confirmação do estado operacional atual dos checks remotos

Conclusão:

- a infraestrutura de qualidade existe
- o estado real de saúde do projeto ainda não foi validado integralmente nesta sessão

## 4.5 Aplicação Web presente, mas não plenamente caracterizada

O código confirma existência da aplicação Web, mas ainda há sinais que impedem descrevê-la de forma mais forte:

- foi observado placeholder no cálculo de `total_trad` da home, conforme análise anterior
- não houve inspeção completa de rotas, templates e acoplamentos

Conclusão:

- a Web não deve ser descrita como inexistente
- também não deve ser descrita como funcionalmente confirmada em todos os aspectos

## 5. Planejado, documentado ou discutido, mas não confirmado como implementado

## 5.1 Engine de pipeline configurável

Docs e issues confirmam forte direção futura para:

- `Transformer`
- `Sink`
- `ContextoPipeline`
- executor mínimo
- streaming via `Iterable`
- configuração via YAML/JSON
- versionamento de pipeline
- migração incremental de caso de uso

Isso aparece especialmente nas issues:

- `#10`
- `#11`
- `#12`
- `#13`
- `#14`
- `#15`
- `#16`
- `#17`

Porém, até esta etapa, **não foram observados no código central inspecionado**:

- entidade `Pipeline`
- `ContextoPipeline`
- executor declarativo de pipeline
- contratos consolidados de source / transformer / sink
- execução versionada por configuração externa

Conclusão:

- a engine de pipeline é **planejamento arquitetural ativo e rastreável**
- ela **não** está confirmada como implementação presente no código central já lido

## 5.2 Arquitetura de plugins ampla

Os documentos e a direção futura falam em plugins e platformização.

O código observado confirma apenas, com segurança:

- registry
- factories

O que não foi confirmado:

- plugin manager completo
- discovery de plugins
- contratos generalizados de plugin já implantados

## 5.3 Generalização para múltiplos domínios documentais

O histórico e as issues indicam interesse em ampliar o projeto.

Exemplo:

- `#21` formaliza protótipo de coletores para fontes externas, mas explicitamente fora da integração imediata com a engine

Mesmo assim, o código central observado ainda permanece fortemente especializado no caso atual de ShowTrials.

Conclusão:

- a generalização existe como direção plausível e parcialmente preparada
- ela não está confirmada como estado atual implementado

## 5.4 Transição ShowTrials -> CraftText

Até esta etapa, o que está confirmado é:

- o sistema implementado é historicamente ShowTrials
- a direção futura é uma engine/plataforma de pipeline

O que **não** está confirmado por código, commits ou issues analisadas:

- renomeação formal para `CraftText`
- coexistência formal consolidada entre os nomes
- decisão rastreável em issues sobre essa transição nominal

Conclusão:

- qualquer menção a `CraftText` deve continuar sendo tratada como hipótese de direção futura ou rótulo conceitual ainda não confirmado como identidade oficial do repositório

## 6. Incertezas relevantes

As seguintes incertezas permanecem abertas:

- completude funcional real da interface Web
- extensão real da adoção de `ServiceRegistry` e `BaseUseCase`
- robustez da camada de configuração em toda a aplicação
- cobertura atual e estado operacional real do pipeline de qualidade
- grau total de adoção da telemetria no repositório
- existência futura ou não de renomeação formal para `CraftText`

## 7. Síntese final

O estado atual mais seguro de descrever é:

- **implementado**: aplicação ShowTrials em camadas, documento-cêntrica, com SQLite, casos de uso imperativos, CLI presente no código, Web presente no código, registry/factories e base local de tooling
- **parcial / em transição**: adoção sistêmica do registry, camada de configuração, telemetria global, caracterização funcional completa da Web e validação operacional do pipeline de qualidade
- **planejado / documentado / discutido**: engine de pipeline configurável, contratos formais de transformação e sinks, execução por contexto de pipeline, versionamento de pipeline, streaming por `Iterable`, generalização mais ampla da plataforma e eventual narrativa ShowTrials -> CraftText
