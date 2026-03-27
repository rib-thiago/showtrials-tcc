# Historico da Fase 2 - Fundacao da Camada de Aplicacao

## Natureza do Documento

Este documento registra historicamente a fundacao da camada de aplicacao do
projeto. Ele deve ser lido como memoria tecnica e arquitetural de uma
intervencao estruturante, nao como guia operacional vigente.

## Objetivo da Intervencao

Estabelecer a camada de aplicacao como responsavel por orquestrar os casos de
uso do sistema, conectar o dominio as interfaces e introduzir DTOs para
separar a representacao interna das entidades da forma como os dados sao
entregues as camadas de apresentacao.

## Contexto

Depois da fundacao da camada de dominio na `FASE 1`, o projeto precisava de um
espaco arquitetural intermediario entre as entidades puras e as interfaces de
entrada e saida. A camada de aplicacao foi introduzida para organizar a logica
de orquestracao do sistema sem deslocar regras de negocio para a interface nem
acoplar o dominio a preocupacoes de exibicao.

Esquema ASCII preservado do fluxo arquitetural alto nivel:

```text
[Interface (CLI/Web)] -> [Caso de Uso] -> [Repositorio (interface)]
         ^                    |                     |
         |                    v                     v
         +-------- [DTO] <- [Entidade] <- [Implementacao]
```

## Componentes Fundadores

Os componentes fundadores registrados nesta fase sao:

- os primeiros casos de uso de aplicacao, como `ClassificarDocumento`,
  `ListarDocumentos`, `ObterDocumento` e `ObterEstatisticas`;
- os DTOs `DocumentoDTO`, `DocumentoListaDTO` e `EstatisticasDTO`;
- os primeiros testes unitarios da camada de aplicacao.

### Sobre os DTOs

Os DTOs foram introduzidos para resolver uma preocupacao arquitetural clara:
evitar que a interface dependesse diretamente da estrutura completa das
entidades de dominio. Historicamente, essa decisao representou:

- separacao entre dados internos do dominio e dados preparados para exibicao;
- reducao de acoplamento entre casos de uso e camadas de apresentacao;
- abertura para listagens resumidas e representacoes completas sem expor toda a
  entidade;
- maior clareza academica sobre a diferenca entre entidade de dominio e objeto
  de transferencia de dados.

### Sobre os casos de uso

Os casos de uso aparecem nesta fase como a primeira formulacao explicita da
camada de aplicacao. O papel deles nao era reimplementar regras de negocio do
dominio, mas coordenar o fluxo entre repositorios, entidades e DTOs, deixando a
regra de negocio central no dominio e a apresentacao nas interfaces.

## Artefatos Afetados

Os artefatos com lastro historico mais forte na intervencao sao:

- [documento_dto.py](/home/thiago/coleta_showtrials/src/application/dtos/documento_dto.py)
- [estatisticas_dto.py](/home/thiago/coleta_showtrials/src/application/dtos/estatisticas_dto.py)
- [classificar_documento.py](/home/thiago/coleta_showtrials/src/application/use_cases/classificar_documento.py)
- [listar_documentos.py](/home/thiago/coleta_showtrials/src/application/use_cases/listar_documentos.py)
- [obter_documento.py](/home/thiago/coleta_showtrials/src/application/use_cases/obter_documento.py)
- [estatisticas.py](/home/thiago/coleta_showtrials/src/application/use_cases/estatisticas.py)
- [test_use_cases.py](/home/thiago/coleta_showtrials/src/tests/test_use_cases.py)

## Rastreabilidade Git e GitHub

- Commit principal identificado com seguranca:
  - `4b7ac57` - `FASE 2 - Application Layer concluida`
- Branch principal:
  - nenhuma branch principal foi confirmada com seguranca para esta fase
- Issues relacionadas:
  - nenhuma issue principal foi confirmada com seguranca
- Pull request relacionada:
  - nenhum PR foi identificado com seguranca

## Impacto Tecnico

O impacto tecnico principal desta fase foi consolidar a camada de aplicacao
como mediadora entre dominio e apresentacao:

- os casos de uso passaram a centralizar a orquestracao do sistema;
- a interface deixou de depender diretamente da entidade completa de dominio;
- a arquitetura ganhou uma separacao mais nitida entre entidade, caso de uso e
  representacao de saida;
- o projeto passou a contar com um primeiro conjunto de testes unitarios da
  camada de aplicacao.

Do ponto de vista academico, esta fase tambem registra uma decisao importante:
o projeto passou a explicitar a diferenca entre regra de negocio, coordenacao
de aplicacao e representacao de dados, o que fortaleceu a leitura arquitetural
geral do sistema.

## Documentos Relacionados

- [FASE01_FUNDACAO_DA_CAMADA_DE_DOMINIO.md](/home/thiago/coleta_showtrials/docs/fases/FASE01_FUNDACAO_DA_CAMADA_DE_DOMINIO.md)
- [FASE03_FUNDACAO_DA_CAMADA_DE_INFRAESTRUTURA.md](/home/thiago/coleta_showtrials/docs/fases/FASE03_FUNDACAO_DA_CAMADA_DE_INFRAESTRUTURA.md)
- [ARCHITECTURE.md](/home/thiago/coleta_showtrials/docs/ARCHITECTURE.md)
- [analise_arquitetural.md](/home/thiago/coleta_showtrials/docs/projeto/analise_arquitetural.md)
- [direcionamento_arquitetural_engine_mvp.md](/home/thiago/coleta_showtrials/docs/projeto/direcionamento_arquitetural_engine_mvp.md)
