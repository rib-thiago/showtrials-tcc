# Plano Operacional da Reorganizacao Semantica dos Diretorios

## 1. Objetivo do documento

Este documento formaliza a proxima etapa da frente de saneamento documental: a reorganizacao semantica controlada da arvore `docs/`.

Seu objetivo e:

- consolidar o mapa estrutural `origem -> destino` que emerge do saneamento ja concluido
- distinguir movimentos fisicos necessarios de movimentos apenas desejaveis
- explicitar o impacto esperado em `mkdocs.yml`, navegacao publicada e referencias internas
- reduzir risco de renames em cascata sem criterio editorial claro

## 2. Contexto de partida

Ao final das rodadas anteriores:

- o bloco `docs/projeto/` foi saneado semanticamente
- os documentos publicos de entrada foram saneados
- `docs/fases/` foi saneado, renomeado e reordenado
- `docs/metricas/` foi saneado
- o bloco critico de `docs/planejamento/` foi enquadrado
- `TEMPLATE_FASE.md` foi removido por incompatibilidade com o padrao historico-rastreavel consolidado

Com isso, o principal problema remanescente deixou de ser o conteudo dos arquivos Markdown e passou a ser a relacao entre:

- estrutura fisica dos diretorios
- estatuto semantico real dos documentos
- navegacao configurada em `mkdocs.yml`

## 3. Diagnostico estrutural atual

Hoje, a arvore `docs/` ainda carrega agrupamentos fisicos que ja nao representam bem a natureza dos documentos:

- `docs/flows/` mistura politica, protocolo normativo e guia operacional
- `docs/metricas/` mistura um snapshot vivo e diagnosticos historicos
- `docs/fases/` esta semanticamente correto, mas seu papel e claramente historico
- `docs/projeto/` mistura visoes e diretrizes vivas com artefatos historicos ou preparatorios
- `docs/planejamento/` mistura metodologia viva da frente e arquivo historico da propria frente

Ao mesmo tempo, `mkdocs.yml` permanece fortemente desatualizado:

- referencia nomes antigos de fases
- referencia nomes antigos de `flows`
- ainda aponta para `TEMPLATE_FASE.md`
- nao reflete a arquitetura documental consolidada pela frente

## 4. Principios da reorganizacao

Durante esta etapa, a reorganizacao deve obedecer aos principios abaixo:

- semantica antes de estetica
- navegacao antes de taxonomia aspiracional
- movimentos fisicos em blocos coerentes, nao em renames isolados arbitrarios
- atualizacao coordenada de referencias e `mkdocs.yml`
- preservacao de rastreabilidade historica
- manutencao das ancoras publicas principais em seus caminhos atuais

## 5. Estrutura semantica alvo recomendada

A estrutura alvo recomendada para a proxima consolidacao e a seguinte:

```text
docs/
  index.md
  overview.md
  ARCHITECTURE.md
  contributing.md
  changelog.md

  politicas/
    politica_de_governanca.md

  protocolos/
    protocolo_de_git.md
    protocolo_de_qualidade.md

  guias/
    automacao_operacional_com_taskipy.md
    guia_de_atualizacao_do_changelog.md
    guia_de_auto_revisao.md
    guia_de_correcao_urgente.md
    guia_de_debug.md
    guia_de_dependencias.md
    guia_de_documentacao_do_projeto.md
    guia_de_manutencao_do_site_documental.md
    guia_de_refatoracao.md
    guia_de_telemetria.md
    guia_github_projects_cli.md

  metricas/
    cobertura.md

  historico/
    fases/
      FASE01_FUNDACAO_DA_CAMADA_DE_DOMINIO.md
      ...
      FASE19_CONSOLIDACAO_DO_FLUXO_DE_QUALIDADE.md
    diagnosticos/
      diagnostico_ci.md
      diagnostico_fase12.md
    planejamento/
      plano_issue2_revisao_documentacao.md
      plano_issues_documentacao.md
      questionario_levantamento_requisitos.md

  projeto/
    analise_arquitetural.md
    dependencias_nlp_estado_e_transicao.md
    direcionamento_arquitetural_engine_mvp.md
    manual_gestao.md
    politica_de_diagramas_versionaveis.md
    regime_documental_de_fases_e_rodadas.md
    roadmap_arquitetural.md
    versionamento_e_releases.md
    visao_do_projeto.md

  planejamento/
    classificacao_semantica_legacy_bloco_01_raiz_e_metricas.md
    classificacao_semantica_legacy_bloco_02_flows.md
    classificacao_semantica_legacy_bloco_03_projeto.md
    classificacao_semantica_legacy_bloco_04_fases_1_a_9.md
    classificacao_semantica_legacy_bloco_05_fases_10_a_17.md
    fechamento_etapa_3_classificacao_semantica_legacy.md
    inventario_inicial_documentacao_legacy.md
    padrao_minimo_documental_etapa_5.md
    plano_frente_saneamento_documentacao_legacy.md
    plano_operacional_da_reorganizacao_semantica_dos_diretorios.md
    proposta_arquitetura_documental_alvo.md
    reanalise_etapa_4_publicacao_e_arquitetura_documental.md

  modelagem/
    ...
```

## 6. Mapa `origem -> destino`

### 6.1 Movimentos recomendados com alta prioridade

- `docs/flows/politica_de_governanca.md` -> `docs/politicas/politica_de_governanca.md`
- `docs/flows/protocolo_de_git.md` -> `docs/protocolos/protocolo_de_git.md`
- `docs/flows/protocolo_de_qualidade.md` -> `docs/protocolos/protocolo_de_qualidade.md`
- `docs/flows/*.md` restantes de natureza operacional -> `docs/guias/`
- `docs/fases/*.md` -> `docs/historico/fases/`
- `docs/metricas/diagnostico_ci.md` -> `docs/historico/diagnosticos/diagnostico_ci.md`
- `docs/metricas/diagnostico_fase12.md` -> `docs/historico/diagnosticos/diagnostico_fase12.md`

### 6.2 Movimentos recomendados com prioridade media

- `docs/projeto/plano_issues_documentacao.md` -> `docs/historico/planejamento/plano_issues_documentacao.md`
- `docs/projeto/questionario_levantamento_requisitos.md` -> `docs/historico/planejamento/questionario_levantamento_requisitos.md`
- `docs/planejamento/plano_issue2_revisao_documentacao.md` -> `docs/historico/planejamento/plano_issue2_revisao_documentacao.md`

### 6.3 Itens que devem permanecer onde estao, por enquanto

- `docs/index.md`
- `docs/overview.md`
- `docs/ARCHITECTURE.md`
- `docs/contributing.md`
- `docs/changelog.md`
- `docs/metricas/cobertura.md`
- `docs/projeto/visao_do_projeto.md`
- `docs/projeto/analise_arquitetural.md`
- `docs/projeto/direcionamento_arquitetural_engine_mvp.md`
- `docs/projeto/regime_documental_de_fases_e_rodadas.md`
- `docs/modelagem/`
- o bloco metodologico principal de `docs/planejamento/`

## 7. Ordem recomendada de execucao

### 7.1 Rodada A - Reorganizacao institucional e operacional

Escopo:

- criar `docs/politicas/`
- criar `docs/protocolos/`
- criar `docs/guias/`
- mover o atual bloco `docs/flows/` para esses tres destinos
- atualizar referencias internas e `mkdocs.yml`

Racional:

- este e o bloco hoje mais semanticamente incoerente no filesystem
- o ganho de legibilidade e imediato
- a atualizacao da navegacao do site fica mais inteligivel

### 7.2 Rodada B - Reorganizacao historica

Escopo:

- criar `docs/historico/`
- criar `docs/historico/fases/`
- criar `docs/historico/diagnosticos/`
- mover `docs/fases/`
- mover os diagnosticos historicos hoje em `docs/metricas/`
- atualizar referencias internas e `mkdocs.yml`

Racional:

- o estatuto historico destes documentos ja foi consolidado
- o ganho semantico e alto e pouco controverso

### 7.3 Rodada C - Separacao entre projeto vivo e planejamento historico

Escopo:

- criar `docs/historico/planejamento/`
- mover artefatos historicos/preparatorios hoje espalhados entre `docs/projeto/` e `docs/planejamento/`
- atualizar referencias internas e `mkdocs.yml`

Racional:

- este bloco exige um pouco mais de cuidado conceitual
- parte dele ainda dialoga fortemente com a historia da propria frente

## 8. Impacto em `mkdocs.yml`

Esta reorganizacao exige revisao coordenada de `mkdocs.yml`.

Os problemas mais evidentes hoje sao:

- referencias a nomes antigos de fases
- referencias a nomes antigos de `flows`
- referencia a `TEMPLATE_FASE.md`, ja removido
- ausencia da nova classificacao entre politica, protocolo, guia e historico

Consequencia pratica:

- nao faz sentido mover arquivos sem revisar `mkdocs.yml` na mesma rodada
- toda rodada de reorganizacao fisica deve incluir atualizacao completa da navegacao correspondente

## 9. Riscos e mitigacoes

### 9.1 Risco de quebra de links internos

Mitigacao:

- atualizar referencias por bloco na mesma rodada do movimento
- revisar links em documentos publicos e no bloco `docs/projeto/`

### 9.2 Risco de quebra da navegacao do site

Mitigacao:

- revisar `mkdocs.yml` por secao
- validar a correspondencia entre arvore real e caminhos declarados

### 9.3 Risco de supermovimentacao

Mitigacao:

- executar a reorganizacao em tres rodadas estruturais
- evitar mover documentos publicos de entrada
- manter `docs/modelagem/` fora desta etapa

## 10. Decisao recomendada

A decisao recomendada a partir deste ponto e:

1. aprovar a reorganizacao semantica controlada da arvore `docs/`
2. iniciar pela reorganizacao de `docs/flows/` em `politicas/`, `protocolos/` e `guias/`
3. executar em seguida a migracao de `docs/fases/` e dos diagnosticos historicos para `docs/historico/`
4. deixar para uma terceira rodada a separacao entre projeto vivo e planejamento historico

## 11. Documentos relacionados

- [proposta_arquitetura_documental_alvo.md](../planejamento/proposta_arquitetura_documental_alvo.md)
- [reanalise_etapa_4_publicacao_e_arquitetura_documental.md](../planejamento/reanalise_etapa_4_publicacao_e_arquitetura_documental.md)
- [plano_frente_saneamento_documentacao_legacy.md](../planejamento/plano_frente_saneamento_documentacao_legacy.md)
- [regime_documental_de_fases_e_rodadas.md](../projeto/regime_documental_de_fases_e_rodadas.md)
