# Reanalise da Etapa 4 - Publicacao e Arquitetura Documental

## 1. Objetivo do documento

Este documento registra a reanalise metodologica da Etapa 4 da frente de saneamento documental.

Seu objetivo e:

- corrigir a hipotese inicial de arquitetura documental alvo
- incorporar a funcao publica atual da documentacao publicada via MkDocs
- distinguir estatuto semantico de funcao navegacional
- definir a matriz de decisao que orientara a proposta estrutural da frente

## 2. Motivo da reanalise

A leitura anterior da Etapa 4 partia de uma premissa insuficiente:

- tratar o recorte da frente principalmente como conjunto “legado” a ser reorganizado por natureza semantica

Essa leitura se mostrou metodologicamente incompleta porque:

- `mkdocs.yml` expoe diretamente boa parte desses documentos como paginas publicas do site
- arquivos-raiz como `index.md`, `overview.md`, `ARCHITECTURE.md`, `contributing.md` e `changelog.md` exercem funcao estrutural de entrada e navegacao
- `README.md` tambem cumpre funcao publica e institucional fora do MkDocs
- nem todo documento do recorte deve ser tratado como historico rebaixavel ou apenas interno

Por isso, a Etapa 4 passou a exigir uma camada adicional de analise:

- funcao publica atual e custo de transicao navegacional

## 3. Fontes consideradas nesta reanalise

Foram consideradas nesta reanalise:

- `mkdocs.yml`
- `README.md`
- `docs/index.md`
- `docs/overview.md`
- `docs/ARCHITECTURE.md`
- `docs/contributing.md`
- `docs/changelog.md`
- `docs/flows/GOVERNANCA.md`
- `docs/projeto/politica_de_diagramas_versionaveis.md`
- [05_session_handoff.md](/home/thiago/coleta_showtrials/docs/ai/05_session_handoff.md), via branch `docs/ai-context-bootstrap`
- [10_modelagem_contexto_consolidado.md](/home/thiago/coleta_showtrials/docs/ai/10_modelagem_contexto_consolidado.md), via branch `docs/ai-context-bootstrap`
- [manual_colaboracao_codex.md](/home/thiago/coleta_showtrials/docs/projeto/manual_colaboracao_codex.md), via branch `docs/ai-context-bootstrap`

## 4. Consequencia metodologica principal

A arquitetura documental alvo desta frente nao pode ser definida apenas por natureza semantica abstrata.

Ela precisa considerar simultaneamente:

- estatuto semantico do documento
- funcao publica e navegacional atual
- custo e risco de transicao estrutural
- possibilidade de melhoria incremental no estado atual

Em termos praticos:

- ha documentos que devem ser saneados no lugar
- ha documentos que podem ser reclassificados semanticamente sem mudanca fisica imediata
- ha documentos que podem ser candidatos a reorganizacao futura, mas nao precisam ser movidos ja

## 5. Matriz de decisao da Etapa 4

| Grupo / tipo | Estatuto semantico predominante | Funcao publica atual | Estrategia proposta |
|---|---|---|---|
| `docs/index.md` | pagina de entrada institucional | ancora principal do site | manter caminho e sanear no lugar |
| `docs/overview.md` | visao geral publica | pagina publica de orientacao | manter caminho e sanear no lugar |
| `docs/ARCHITECTURE.md` | visao arquitetural publica de alto nivel | pagina publica central | manter caminho, revisar semantica e aderencia factual |
| `docs/contributing.md` | guia publico de contribuicao | pagina publica de onboarding | manter caminho e atualizar ao fluxo real do projeto |
| `docs/changelog.md` | historico publico de mudancas | pagina publica de referencia | manter caminho e enquadrar como historico formal |
| `docs/metricas/*` | diagnosticos e metricas | paginas publicas de apoio tecnico | manter bloco publicado; sanear conteudo e distinguir “metrica viva” de “diagnostico historico” |
| `docs/flows/GOVERNANCA.md` | politica | pagina publica publicada em bloco inadequado | manter publicado por enquanto; reclassificar semanticamente como politica formal |
| `docs/flows/git_flow.md` | protocolo normativo | pagina publica publicada | manter publicado por enquanto; reclassificar como protocolo |
| `docs/flows/quality_flow.md` | protocolo normativo | pagina publica publicada | manter publicado por enquanto; reclassificar como protocolo |
| demais `docs/flows/*` | guias operacionais e tecnicos | paginas publicas de trabalho | manter publicados; sanear no lugar; avaliar reorganizacao posterior |
| `docs/projeto/politica_de_diagramas_versionaveis.md` | politica formal | artefato estavel fora da nav principal atual | candidato a promocao estrutural futura, sem urgencia fisica |
| demais `docs/projeto/*` | visao, planejamento historico, analise prospectiva, levantamento | parte publicada e parte de referencia | manter no bloco atual por ora; reclassificar semanticamente e separar o que e historico do que e documento ainda util |
| `docs/fases/FASE1` a `FASE10` | historico de entrega e implementacao | bloco publico fortemente exposto | manter publicados por enquanto; enquadrar explicitamente como historico |
| `docs/fases/FASE11` a `FASE17` | historico hibrido de intervencao e revisao | bloco publico exposto | manter publicados por enquanto; saneamento obrigatorio forte; reavaliar permanencia publica posterior |
| `docs/planejamento/*` ligados a frente | documentacao operacional da frente | fora da navegacao principal, salvo excecoes antigas | manter em `planejamento/`; revisar depois o que deve ou nao ficar publicado |
| `README.md` | entrada institucional do repositorio | publico fora do MkDocs | manter na raiz; sincronizar com arquitetura documental real e links validos |

## 6. Regras derivadas da matriz

Da matriz acima, derivam-se as regras abaixo para o restante da frente:

1. Arquivos com funcao publica estrutural nao devem ser movidos sem necessidade clara.
2. A estrategia preferencial inicial e saneamento no lugar.
3. Reclassificacao semantica pode e deve acontecer antes de reorganizacao fisica.
4. Mudancas fisicas devem ser reservadas para casos em que o ganho seja claro e o custo navegacional controlado.
5. A arquitetura alvo da frente deve ser entendida como estrutura de referencia com estrategia de transicao, e nao como arvore a ser aplicada integralmente de uma vez.

## 7. Consequencia para as etapas seguintes

Esta reanalise altera a interpretacao operacional das proximas etapas:

- a Etapa 5 passa a priorizar saneamento semantico, factual e formal no lugar
- a Etapa 6 passa a tratar reorganizacao fisica como consolidacao seletiva, e nao como migracao ampla obrigatoria
- a avaliacao de navegacao MkDocs e de consistencia de `README.md` passa a fazer parte do criterio de consolidacao

## 8. Proximo passo recomendado

Com base nesta reanalise, a frente deve formalizar uma proposta de arquitetura documental alvo que:

- preserve as ancoras publicas principais
- explicite a estrutura semantica de destino
- distinga o que fica onde esta, o que sera apenas reclassificado e o que e candidato real a reorganizacao fisica futura
