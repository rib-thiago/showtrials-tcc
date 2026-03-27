# Historico da Fase 8 - Introducao do Subsistema de Analise de Texto

## Natureza do Documento

Este documento registra historicamente a introducao do subsistema de analise de
texto do projeto. Ele deve ser lido como memoria tecnica e arquitetural de uma
intervencao estruturante, nao como guia operacional vigente.

## Objetivo da Intervencao

Estabelecer um primeiro fluxo integrado de analise de texto, incluindo extração
de entidades, estatisticas textuais, analise de sentimento, nuvem de palavras e
integracao com a CLI para analise individual e global do acervo.

## Contexto

Depois da introducao dos subsistemas de traducao, exportacao e relatorios, o
projeto avancou para a necessidade de analisar o conteudo textual dos
documentos. Esta fase registra o momento em que NLP e analise textual deixaram
de ser uma possibilidade abstrata e passaram a ter formulacao arquitetural
propria dentro do sistema.

Ela tambem registra uma nuance historica importante: a introducao desse bloco
veio acompanhada de um workaround de dependencias e instalacao que foi valido
para aquele momento, mas que hoje precisa ser lido em conjunto com documentos
mais recentes sobre dependencias, CI e estado de transicao do NLP.

## Componentes Fundadores

Os componentes fundadores registrados nesta fase sao:

- os value objects de analise de texto;
- os casos de uso `AnalisarDocumento` e `AnalisarAcervo`;
- o `SpacyAnalyzer`;
- o `WordCloudGenerator`;
- os comandos e presenters de analise na CLI.

### Sobre o subsistema de analise de texto

Do ponto de vista arquitetural e academico, esta fase foi importante porque
organizou a analise textual como capacidade transversal:

- o dominio passou a ter objetos proprios para representar resultados de
  analise;
- a aplicacao passou a orquestrar analise individual e global;
- a infraestrutura passou a integrar NLP e geracao de wordcloud;
- a interface passou a exibir resultados analiticos e gerar imagens derivadas.

### Sobre o workaround inicial de dependencias NLP

O documento legado descrevia em detalhe a estrategia de instalacao das
dependencias NLP. Historicamente, isso continua relevante como memoria do
momento em que o bloco foi introduzido. No entanto, essa explicacao nao deve
ser lida hoje como regra definitiva do projeto, porque o estado do NLP foi
posteriormente reinterpretado em documentos vivos e em fases posteriores,
especialmente no que diz respeito a CI, Poetry e dependencias de transicao.

## Esquema ASCII Preservado

```text
[Documento/Traducao] -> [AnalisarDocumento] -> [SpacyAnalyzer]
         |                    |                    |
         v                    v                    v
 [Repositorios]         [AnaliseTexto]      [Entidades/Estatisticas]
                                                    |
                                                    v
                                           [WordCloudGenerator]
                                                    |
                                                    v
                                             [analises/*.png]
```

## Artefatos Afetados

Os artefatos com lastro historico mais forte na intervencao sao:

- [analise_texto.py](/home/thiago/coleta_showtrials/src/domain/value_objects/analise_texto.py)
- [analisar_texto.py](/home/thiago/coleta_showtrials/src/application/use_cases/analisar_texto.py)
- [analisar_acervo.py](/home/thiago/coleta_showtrials/src/application/use_cases/analisar_acervo.py)
- [spacy_analyzer.py](/home/thiago/coleta_showtrials/src/infrastructure/analysis/spacy_analyzer.py)
- [wordcloud_generator.py](/home/thiago/coleta_showtrials/src/infrastructure/analysis/wordcloud_generator.py)
- [commands_analise.py](/home/thiago/coleta_showtrials/src/interface/cli/commands_analise.py)
- [presenters_analise.py](/home/thiago/coleta_showtrials/src/interface/cli/presenters_analise.py)
- [pyproject.toml](/home/thiago/coleta_showtrials/pyproject.toml)
- [poetry.lock](/home/thiago/coleta_showtrials/poetry.lock)

## Rastreabilidade Git e GitHub

- Commit principal identificado com seguranca:
  - `3def168` - `FASE 8 - Analise de Texto concluida`
- Branch principal:
  - nenhuma branch principal foi confirmada com seguranca para esta fase
- Issues relacionadas:
  - nenhuma issue principal foi confirmada com seguranca
- Pull request relacionada:
  - nenhum PR foi identificado com seguranca

## Impacto Tecnico

O impacto tecnico principal desta fase foi introduzir a analise textual como
capacidade integrada do sistema:

- documentos passaram a poder ser analisados linguisticamente;
- o acervo passou a admitir analise global de texto;
- a arquitetura ganhou objetos e fluxos proprios para resultados analiticos;
- o projeto passou a gerar nuvens de palavras como artefatos derivados;
- NLP entrou explicitamente como frente tecnica dentro da arquitetura.

Do ponto de vista academico, esta fase reforca a capacidade do projeto de ir
alem da coleta e apresentacao, passando a extrair sinais analiticos do proprio
conteudo documental.

## Limites de Leitura no Estado Atual

Esta fase registra a introducao historica do subsistema de analise de texto,
mas nao deve ser lida isoladamente como descricao completa do estado atual das
dependencias NLP, do CI ou da politica de instalacao desse bloco.

A leitura atual deve considerar em conjunto:

- [guia_de_dependencias.md](/home/thiago/coleta_showtrials/docs/guias/guia_de_dependencias.md)
- [dependencias_nlp_estado_e_transicao.md](/home/thiago/coleta_showtrials/docs/projeto/dependencias_nlp_estado_e_transicao.md)
- [FASE11_ESTABILIZACAO_INICIAL_DO_CI.md](/home/thiago/coleta_showtrials/docs/historico/fases/FASE11_ESTABILIZACAO_INICIAL_DO_CI.md)
- os documentos arquiteturais saneados.

## Documentos Relacionados

- [FASE07_INTRODUCAO_DO_SUBSISTEMA_DE_RELATORIOS.md](/home/thiago/coleta_showtrials/docs/historico/fases/FASE07_INTRODUCAO_DO_SUBSISTEMA_DE_RELATORIOS.md)
- [FASE09_INTRODUCAO_DA_INTERFACE_WEB.md](/home/thiago/coleta_showtrials/docs/historico/fases/FASE09_INTRODUCAO_DA_INTERFACE_WEB.md)
- [ARCHITECTURE.md](/home/thiago/coleta_showtrials/docs/ARCHITECTURE.md)
- [analise_arquitetural.md](/home/thiago/coleta_showtrials/docs/projeto/analise_arquitetural.md)
- [direcionamento_arquitetural_engine_mvp.md](/home/thiago/coleta_showtrials/docs/projeto/direcionamento_arquitetural_engine_mvp.md)
- [guia_de_dependencias.md](/home/thiago/coleta_showtrials/docs/guias/guia_de_dependencias.md)
- [dependencias_nlp_estado_e_transicao.md](/home/thiago/coleta_showtrials/docs/projeto/dependencias_nlp_estado_e_transicao.md)
- [FASE11_ESTABILIZACAO_INICIAL_DO_CI.md](/home/thiago/coleta_showtrials/docs/historico/fases/FASE11_ESTABILIZACAO_INICIAL_DO_CI.md)
