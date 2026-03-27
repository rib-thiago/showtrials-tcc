# Historico da Fase 10 - Introducao do Service Registry e do Lazy Loading

## Natureza do Documento

Este documento registra historicamente a introducao do `ServiceRegistry` e do
modelo de lazy loading no ShowTrials. Ele deve ser lido como memoria tecnica e
arquitetural da intervencao, e nao como tutorial de configuracao ou como
descricao definitiva do estado atual do bloco de servicos.

## Objetivo da Intervencao

Introduzir um mecanismo centralizado para registro, inicializacao e acesso a
servicos da aplicacao, reduzindo custo de bootstrap, organizando dependencias
pesadas e preparando o sistema para configuracao mais flexivel de integracoes.

## Contexto

Depois da consolidacao do primeiro ciclo fundador do sistema, o projeto passou
a concentrar mais integracoes externas, servicos de analise e componentes
potencialmente caros de inicializar. Isso gerou a necessidade de separar com
mais clareza:

- registro de servicos;
- configuracao da aplicacao;
- instante de inicializacao real de cada dependencia;
- consumo desses servicos por casos de uso e pela interface web.

Essa fase aparece, por isso, como ponte entre o bloco fundador e o bloco de
estabilizacao tecnica que vem depois.

## Componentes Fundadores

Os componentes historicamente centrais desta fase foram:

- `ServiceRegistry` em `src/infrastructure/registry.py`;
- factories de servicos em `src/infrastructure/factories.py`;
- configuracao declarativa em `config.yaml`;
- `ApplicationConfig` e estruturas associadas em
  `src/infrastructure/config/__init__.py`;
- integracao do registry aos casos de uso que dependiam de servicos de
  traducao, NLP e geracao de wordcloud;
- painel administrativo e pontos de integracao na interface web para leitura de
  status e administracao de servicos.

Do ponto de vista arquitetural, a fase consolidou algumas decisoes importantes:

- servicos pesados nao precisavam ser carregados no bootstrap da aplicacao;
- a configuracao deveria orientar como os servicos seriam registrados;
- a criacao concreta de dependencias deveria ficar encapsulada em factories;
- os casos de uso passariam a depender de um mecanismo de acesso a servicos,
  e nao da instanciacao direta espalhada pelo sistema.

## Esquema ASCII Preservado

```text
[Config YAML] -> [ServiceRegistry] -> [Factory]
      |                 |                |
      v                 v                v
 [ServiceConfig]   [Cache/Stats]   [Translator/Spacy/WordCloud]
                          |
                          v
                 [Casos de Uso / Web App]
```

O esquema preserva a ideia central da fase: configuracao, criacao e consumo de
servicos passaram a ser tratados como preocupacoes explicitas e separadas.

## Artefatos Afetados

Artefatos com lastro forte no commit historico principal:

- [config.yaml](/home/thiago/coleta_showtrials/config.yaml)
- [base.py](/home/thiago/coleta_showtrials/src/application/use_cases/base.py)
- [analisar_acervo.py](/home/thiago/coleta_showtrials/src/application/use_cases/analisar_acervo.py)
- [analisar_texto.py](/home/thiago/coleta_showtrials/src/application/use_cases/analisar_texto.py)
- [traduzir_documento.py](/home/thiago/coleta_showtrials/src/application/use_cases/traduzir_documento.py)
- [spacy_analyzer.py](/home/thiago/coleta_showtrials/src/infrastructure/analysis/spacy_analyzer.py)
- [wordcloud_generator.py](/home/thiago/coleta_showtrials/src/infrastructure/analysis/wordcloud_generator.py)
- [__init__.py](/home/thiago/coleta_showtrials/src/infrastructure/config/__init__.py)
- [factories.py](/home/thiago/coleta_showtrials/src/infrastructure/factories.py)
- [registry.py](/home/thiago/coleta_showtrials/src/infrastructure/registry.py)
- [app.py](/home/thiago/coleta_showtrials/src/interface/web/app.py)
- [admin.py](/home/thiago/coleta_showtrials/src/interface/web/routes/admin.py)
- [main.js](/home/thiago/coleta_showtrials/src/interface/web/static/js/main.js)
- [services.html](/home/thiago/coleta_showtrials/src/interface/web/templates/admin/services.html)
- [test_registry.py](/home/thiago/coleta_showtrials/src/tests/test_registry.py)

## Rastreabilidade Git e GitHub

- Commit principal identificado com seguranca:
  - `b185f0f` - `feat(registry): implementa Service Registry com lazy loading`
- Branch principal identificada com seguranca:
  - `feature/service-registry`
- PR:
  - nenhum PR identificado com seguranca
- Issue principal:
  - nenhuma issue principal numerada confirmada com seguranca

## Impacto Tecnico

Historicamente, a fase teve impacto importante em quatro frentes:

- tornou explicita a gestao de servicos no sistema;
- reduziu a necessidade de inicializacao antecipada de dependencias pesadas;
- organizou a configuracao da aplicacao de forma mais declarativa;
- preparou o terreno para leituras posteriores sobre qualidade, CI,
  telemetria, factories e estabilizacao do bloco NLP.

Tambem vale registrar que esta fase alterou a forma de pensar a aplicacao:
servicos deixaram de ser apenas dependencias concretas espalhadas pelo codigo e
passaram a compor um subsistema proprio de configuracao, inicializacao e
observacao.

## Limites de Leitura no Estado Atual

Esta fase registra a introducao historica do `ServiceRegistry`, do lazy loading
e da configuracao declarativa de servicos. Ela nao deve ser lida, isoladamente,
como descricao completa do estado atual de factories, telemetria, CI, tipagem
ou dependencias NLP.

Para a leitura atual mais forte do projeto, devem ser considerados tambem:

- [FASE11_ESTABILIZACAO_INICIAL_DO_CI.md](/home/thiago/coleta_showtrials/docs/historico/fases/FASE11_ESTABILIZACAO_INICIAL_DO_CI.md)
- [dependencias_nlp_estado_e_transicao.md](/home/thiago/coleta_showtrials/docs/projeto/dependencias_nlp_estado_e_transicao.md)
- [direcionamento_arquitetural_engine_mvp.md](/home/thiago/coleta_showtrials/docs/projeto/direcionamento_arquitetural_engine_mvp.md)
- [analise_arquitetural.md](/home/thiago/coleta_showtrials/docs/projeto/analise_arquitetural.md)

## Documentos Relacionados

- [FASE08_INTRODUCAO_DO_SUBSISTEMA_DE_ANALISE_DE_TEXTO.md](/home/thiago/coleta_showtrials/docs/historico/fases/FASE08_INTRODUCAO_DO_SUBSISTEMA_DE_ANALISE_DE_TEXTO.md)
- [FASE09_INTRODUCAO_DA_INTERFACE_WEB.md](/home/thiago/coleta_showtrials/docs/historico/fases/FASE09_INTRODUCAO_DA_INTERFACE_WEB.md)
- [FASE11_ESTABILIZACAO_INICIAL_DO_CI.md](/home/thiago/coleta_showtrials/docs/historico/fases/FASE11_ESTABILIZACAO_INICIAL_DO_CI.md)
- [dependencias_nlp_estado_e_transicao.md](/home/thiago/coleta_showtrials/docs/projeto/dependencias_nlp_estado_e_transicao.md)
