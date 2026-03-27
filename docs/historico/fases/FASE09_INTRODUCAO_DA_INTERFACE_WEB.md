# Historico da Fase 9 - Introducao da Interface Web

## Natureza do Documento

Este documento registra historicamente a introducao da interface web do
ShowTrials como parte do primeiro ciclo fundador do sistema. Ele deve ser lido
como memoria tecnica e arquitetural da intervencao, e nao como tutorial de
implementacao ou como descricao definitiva do estado atual da arquitetura.

## Objetivo da Intervencao

Introduzir uma interface web baseada em FastAPI e templates Jinja2 para expor,
via navegador e endpoints HTTP, as capacidades que ja vinham sendo organizadas
nas camadas de dominio, aplicacao, infraestrutura e CLI.

## Contexto

Depois da consolidacao das camadas fundadoras e da incorporacao de capacidades
como traducao, exportacao, relatorios e analise textual, o projeto passou a
precisar de uma segunda interface de acesso ao sistema, complementar a CLI.

Essa fase representou o fechamento do primeiro ciclo de interfaces do produto:

- a CLI permaneceu como interface textual e operacional;
- a web passou a oferecer navegacao, visualizacao e acesso HTTP aos mesmos
  casos de uso centrais;
- a arquitetura em camadas foi reaproveitada sem deslocar a logica de negocio
  para a interface.

## Componentes Fundadores

Os componentes historicamente centrais desta fase foram:

- factory da aplicacao FastAPI em `src/interface/web/app.py`;
- rotas web para documentos, analise, traducoes e estatisticas;
- templates HTML com Jinja2 para navegacao e visualizacao do acervo;
- arquivos estaticos para estilo e comportamento da interface;
- script `web_run.py` para inicializacao da interface web;
- integracao da interface com casos de uso e repositorios ja existentes.

Do ponto de vista arquitetural, a fase tambem consolidou algumas decisoes
importantes:

- a interface web deveria reutilizar os mesmos casos de uso da aplicacao;
- a camada de interface continuaria separada da logica de negocio;
- a web poderia conviver com a CLI sem duplicar regras centrais do sistema;
- a inicializacao da aplicacao poderia aproveitar o `ServiceRegistry` e o
  modelo de lazy loading introduzido no projeto.

## Esquema ASCII Preservado

```text
[Navegador] -> [FastAPI Routes] -> [Casos de Uso]
      |               |                 |
      v               v                 v
 [Templates]    [App/Registry]    [Repositorios/Servicos]
      |                                   |
      v                                   v
 [HTML/CSS/JS]                      [Dados do acervo]
```

O esquema acima preserva a ideia central da fase: a interface web foi
introduzida como camada de acesso e apresentacao, e nao como novo centro da
logica do sistema.

## Artefatos Afetados

Artefatos com lastro forte no commit historico principal:

- [web_run.py](/home/thiago/coleta_showtrials/web_run.py)
- [app.py](/home/thiago/coleta_showtrials/src/interface/web/app.py)
- [documentos.py](/home/thiago/coleta_showtrials/src/interface/web/routes/documentos.py)
- [analise.py](/home/thiago/coleta_showtrials/src/interface/web/routes/analise.py)
- [estatisticas.py](/home/thiago/coleta_showtrials/src/interface/web/routes/estatisticas.py)
- [traducoes.py](/home/thiago/coleta_showtrials/src/interface/web/routes/traducoes.py)
- [base.html](/home/thiago/coleta_showtrials/src/interface/web/templates/base.html)
- [index.html](/home/thiago/coleta_showtrials/src/interface/web/templates/index.html)
- [dashboard.html](/home/thiago/coleta_showtrials/src/interface/web/templates/estatisticas/dashboard.html)
- [lista.html](/home/thiago/coleta_showtrials/src/interface/web/templates/documentos/lista.html)
- [detalhe.html](/home/thiago/coleta_showtrials/src/interface/web/templates/documentos/detalhe.html)
- [style.css](/home/thiago/coleta_showtrials/src/interface/web/static/css/style.css)
- [pyproject.toml](/home/thiago/coleta_showtrials/pyproject.toml)
- [poetry.lock](/home/thiago/coleta_showtrials/poetry.lock)

## Rastreabilidade Git e GitHub

- Commit principal identificado com seguranca:
  - `44adbaa` - `FASE 9 - Web Interface concluida`
- PR:
  - nenhum PR identificado com seguranca
- Issue principal:
  - nenhuma issue principal confirmada com seguranca
- Branch principal:
  - nenhuma branch principal confirmada com seguranca

## Impacto Tecnico

Historicamente, a fase teve impacto importante em quatro frentes:

- ampliou a superficie de acesso ao sistema, adicionando navegacao por browser
  sem abandonar a CLI;
- consolidou a simetria entre interface e casos de uso, reforcando a separacao
  arquitetural ja desenhada nas fases anteriores;
- introduziu uma apresentacao visual mais rica para documentos, estatisticas e
  analises;
- preparou o terreno para leituras posteriores sobre integracao, configuracao
  de servicos e evolucao da arquitetura de interface.

Tambem vale registrar que esta fase combinou API e interface renderizada por
templates no mesmo marco historico, o que a torna um ponto de convergencia
importante no ciclo inicial do projeto.

## Limites de Leitura no Estado Atual

Esta fase registra a introducao historica da interface web baseada em FastAPI,
Jinja2 e arquivos estaticos. Ela nao deve ser lida, isoladamente, como
descricao completa do estado atual da arquitetura, da interface web ou da
evolucao futura do sistema.

Para a leitura atual mais forte do projeto, devem ser considerados tambem:

- [ARCHITECTURE.md](../../ARCHITECTURE.md)
- [direcionamento_arquitetural_engine_mvp.md](../../projeto/direcionamento_arquitetural_engine_mvp.md)
- [analise_arquitetural.md](../../projeto/analise_arquitetural.md)
- [visao_do_projeto.md](../../projeto/visao_do_projeto.md)

## Documentos Relacionados

- [FASE04_FUNDACAO_DA_INTERFACE_CLI.md](../../historico/fases/FASE04_FUNDACAO_DA_INTERFACE_CLI.md)
- [FASE08_INTRODUCAO_DO_SUBSISTEMA_DE_ANALISE_DE_TEXTO.md](../../historico/fases/FASE08_INTRODUCAO_DO_SUBSISTEMA_DE_ANALISE_DE_TEXTO.md)
- [ARCHITECTURE.md](../../ARCHITECTURE.md)
- [direcionamento_arquitetural_engine_mvp.md](../../projeto/direcionamento_arquitetural_engine_mvp.md)
