# Proposta de Arquitetura Documental Alvo

## 1. Objetivo do documento

Este documento apresenta a proposta de arquitetura documental alvo da frente de saneamento documental.

Seu objetivo e:

- traduzir a reanalise da Etapa 4 em uma proposta estrutural concreta
- separar arquitetura semantica de destino e estrategia de transicao
- orientar as etapas de saneamento obrigatorio e consolidacao estrutural

## 2. Principio geral da proposta

A estrutura alvo desta frente nao deve ser aplicada como reorganizacao fisica ampla imediata.

Ela deve funcionar como:

- referencia semantica de destino
- criterio para saneamento dos documentos no lugar
- base para movimentos fisicos seletivos apenas quando houver ganho claro

## 3. Estrutura semantica de destino

Em termos semanticos, a documentacao do projeto tende a se organizar melhor segundo os blocos abaixo:

```text
docs/
  index.md
  overview.md
  ARCHITECTURE.md
  contributing.md
  changelog.md

  politicas/
    GOVERNANCA.md
    git_flow.md
    quality_flow.md
    politica_de_diagramas_versionaveis.md

  guias/
    code_review_flow.md
    debug_flow.md
    dependencies_flow.md
    documentation_flow.md
    emergency_flow.md
    fluxo_projects_github_cli.md
    refactoring_flow.md
    telemetry_flow.md

  diagnosticos/
    cobertura.md
    diagnostico_ci.md
    diagnostico_fase12.md

  historico/
    fases/
      FASE1_DOMAIN.md
      ...
      FASE17.md
    planejamento/
      plano_issues_documentacao.md
      roadmap_arquitetural.md
      questionario_levantamento_requisitos.md

  projeto/
    visao_do_projeto.md
    analise_arquitetural.md
    direcionamento_arquitetural_engine_mvp.md

  planejamento/
    ...

  modelagem/
    ...
```

## 4. Interpretacao da proposta

Essa estrutura deve ser lida com cuidado:

- ela representa o destino semantico desejavel
- ela nao implica mover todos os arquivos nesta frente
- ela convive com a necessidade de preservar navegacao publicada e pontos de entrada ja conhecidos

Em especial:

- `index.md`, `overview.md`, `ARCHITECTURE.md`, `contributing.md` e `changelog.md` devem permanecer como ancoras publicas
- `README.md` deve permanecer na raiz do repositorio
- `docs/modelagem/` deve permanecer como frente estabilizada e estrutura propria consolidada

## 5. Estrategia de tratamento por nivel

### 5.1 Nivel A - Manter caminho e sanear agora

Entram preferencialmente neste nivel:

- documentos-raiz de `docs/`
- `docs/metricas/*`
- `docs/flows/*`
- `docs/fases/*`
- boa parte de `docs/projeto/*`

Racional:

- ja estao publicados e navegaveis
- concentram grande ganho possivel sem custo estrutural alto
- o saneamento semantico e editorial pode acontecer no lugar

### 5.2 Nivel B - Reclassificar semanticamente agora, mover depois se ainda fizer sentido

Entram preferencialmente neste nivel:

- `docs/flows/GOVERNANCA.md`
- `docs/flows/git_flow.md`
- `docs/flows/quality_flow.md`
- `docs/projeto/politica_de_diagramas_versionaveis.md`
- `docs/fases/*` como historico publicado, e nao documentacao viva principal

Racional:

- o maior ganho imediato esta no enquadramento correto
- mudanca de caminho pode esperar ate depois do saneamento de conteudo

### 5.3 Nivel C - Candidatos reais a reorganizacao fisica controlada

Entram como candidatos:

- promocao futura de politicas para um bloco fisico proprio
- extracao futura de protocolos normativos hoje mantidos em `docs/flows/`
- separacao futura entre metricas vivas e diagnosticos historicos
- reavaliacao futura da centralidade de `docs/fases/` na navegacao principal

Racional:

- esses movimentos podem fazer sentido
- mas dependem de saneamento previo, validacao de navegacao e criterio editorial mais maduro

## 6. Proposta operacional para a frente atual

Para esta frente, a proposta concreta e:

1. adotar a estrutura acima como referencia semantica de destino
2. nao executar reorganizacao fisica ampla nesta etapa
3. sanear os documentos no lugar, ja respeitando seu estatuto correto
4. reservar para a consolidacao estrutural apenas os movimentos fisicos que permanecerem claramente vantajosos depois do saneamento

## 7. Ganhos esperados com essa abordagem

Essa estrategia busca preservar simultaneamente:

- estabilidade da documentacao publicada
- melhoria semantica e editorial real
- rastreabilidade historica
- controle de escopo

Ela tambem reduz o risco de:

- quebrar navegacao do MkDocs prematuramente
- introduzir renames em cascata antes de sanear o conteudo
- trocar desorganizacao semantica por desorganizacao estrutural nova

## 8. Relacao com as proximas etapas

Esta proposta prepara as proximas etapas da frente da seguinte forma:

- Etapa 5:
  - saneamento obrigatorio do conteudo no lugar, com estatuto semantico correto
- Etapa 6:
  - consolidacao estrutural seletiva, baseada no que ainda fizer sentido mover apos o saneamento
- Etapa 7:
  - fechamento da frente com divisao clara entre o que foi resolvido, o que ficou como divida controlada e o que vai para backlog posterior

## 9. Decisao recomendada

A decisao recomendada para esta frente e:

- aprovar a arquitetura documental alvo como referencia semantica
- adotar postura conservadora para mudancas fisicas
- concentrar esforco imediato em saneamento obrigatorio, correcoes de Markdown, remocao de residuos de geracao assistida, enquadramento semantico e aderencia factual
