# Plano Operacional da Frente de Saneamento da Documentacao Legada

## 1. Objetivo do documento

Este documento formaliza o plano operacional da frente dedicada a revisar, sanear, padronizar e reorganizar a documentacao Markdown legada produzida antes das frentes `docs/ai/` e `docs/modelagem/`.

Seu objetivo e:

- definir o escopo real da frente
- registrar as etapas executaveis
- explicitar criterios de conclusao e encerramento
- separar correcao obrigatoria, divida controlada e backlog posterior
- preservar rastreabilidade metodologica

## 2. Base de evidencia utilizada

Este plano se apoia em:

- `docs/ai/05_session_handoff.md` no branch `docs/ai-context-bootstrap`
- `docs/ai/10_modelagem_contexto_consolidado.md` no branch `docs/ai-context-bootstrap`
- `docs/projeto/manual_colaboracao_codex.md` no branch `docs/ai-context-bootstrap`
- [01_insights_brutos.md](/home/thiago/coleta_showtrials/docs/planejamento/captura/01_insights_brutos.md)
- [48_criterios_de_estabilizacao_da_frente.md](/home/thiago/coleta_showtrials/docs/modelagem/fundamentos/48_criterios_de_estabilizacao_da_frente.md)
- [50_documento_de_saneamento_da_frente.md](/home/thiago/coleta_showtrials/docs/modelagem/revisao/50_documento_de_saneamento_da_frente.md)
- historico Git de `docs/`
- codigo em `src/`, quando necessario para aderencia factual

## 3. Premissas metodologicas

- esta frente deve comecar por analise e planejamento assistido
- nenhuma edicao deve ocorrer sem autorizacao humana previa
- Git, codigo e issues prevalecem sobre documentacao isolada quando houver conflito factual
- o branch `docs/ai-context-bootstrap` deve ser consultado sempre que possivel antes de novas frentes ou recontextualizacoes relevantes
- descobertas novas devem ser classificadas, e nao incorporadas automaticamente ao escopo
- a revisao semantica do legado deve cobrir todos os arquivos do recorte, e nao apenas amostras representativas
- blocos de arquivos sao unidade operacional de execucao e commit, nao mecanismo de reducao de escopo

## 4. Escopo da frente

Entram no escopo:

- documentacao Markdown produzida antes do inicio das frentes `docs/ai/` e `docs/modelagem/`
- principalmente artefatos em `docs/fases/`, `docs/flows/`, `docs/projeto/`, `docs/metricas/` e documentos-raiz de `docs/`
- artefatos de planejamento anteriores relacionados a revisao documental, quando relevantes para rastreabilidade

Ficam fora do escopo direto:

- `docs/modelagem/`, salvo como referencia metodologica e comparativa
- `docs/ai/`, salvo como camada de contexto
- `docs/planejamento/rodadas/`, salvo para registrar a propria frente

## 5. Criterio explicito de encerramento

Esta frente devera ser considerada encerrada quando:

- houver inventario auditavel do legado
- cada documento do recorte legado tiver estatuto semantico claro
- as correcoes estruturais obrigatorias tiverem sido executadas
- a arquitetura documental alvo tiver sido implementada ou mapeada integralmente
- o remanescente estiver classificado entre divida controlada e backlog posterior
- houver documento final de saneamento da frente e documento de rodada correspondente
- nenhum arquivo legado do inventario permanecer sem decisao explicita

## 6. Etapas operacionais

### 6.1 Etapa 1 - Delimitacao formal da frente e baseline de evidencias

**Objetivo**

Definir com rigor o universo documental da frente e as fontes primarias que governarao as decisoes.

**Escopo**

Recorte formal dos documentos legados, fontes de evidencia, premissas metodologicas e criterio de encerramento.

**Entregavel**

- documento de rodada de abertura
- este plano operacional formalizado

**Criterio de conclusao**

O escopo da frente, as fontes primarias e as regras de decisao estao explicitados em artefatos do projeto.

**Justificativa**

Sem enquadramento formal, a frente corre risco de se tornar difusa, reativa e sem criterio de parada.

### 6.2 Etapa 2 - Inventario auditavel do legado

**Objetivo**

Levantar exaustivamente os documentos legados e sua cronologia basica.

**Escopo**

Todos os `.md` relevantes anteriores a 2026-03-24 fora de `docs/ai/` e `docs/modelagem/`.

**Entregavel**

Inventario mestre por arquivo com origem no Git, categoria atual e observacoes iniciais.

**Criterio de conclusao**

Cada documento legado relevante aparece uma unica vez no inventario, com referencia suficiente para futura auditoria.

**Justificativa**

Nao e possivel sanear o conjunto sem saber exatamente qual conjunto esta sendo tratado.

### 6.3 Etapa 3 - Classificacao semantica e estatuto documental

**Objetivo**

Distinguir claramente politica, governanca, flow operacional, diagnostico, planejamento, fase historica, contexto, revisao e artefato de navegacao.

**Escopo**

Leitura integral e classificacao individual de todos os documentos inventariados, organizada por blocos operacionais e comparada com a estrutura disciplinada consolidada em `docs/modelagem/`.

**Entregavel**

Matriz de classificacao documental por arquivo, com proposta de manutencao, promocao, rebaixamento, fusao, desmembramento ou arquivamento.

**Criterio de conclusao**

Todo documento legado do inventario possui natureza documental explicitada e decisao preliminar registrada.

**Justificativa**

A ambiguidade de natureza dos artefatos e uma das principais causas de desorganizacao do legado.

### 6.4 Etapa 4 - Arquitetura documental alvo

**Objetivo**

Definir a estrutura de diretorios e convencoes semanticas que absorverao o legado saneado.

**Escopo**

Mapa estrutural de `docs/` para os artefatos legados, preservando rastreabilidade historica.

**Entregavel**

Mapa `origem -> destino`, convencoes de nome e regras para documentos de fase, politicas, diagnosticos, planejamento, revisao e contexto.

**Criterio de conclusao**

Existe uma proposta unica, coerente e executavel de reorganizacao estrutural.

**Justificativa**

Mover arquivos sem arquitetura documental definida apenas desloca a desordem.

### 6.5 Etapa 5 - Saneamento obrigatorio do conteudo

**Objetivo**

Corrigir tudo o que compromete legibilidade, confiabilidade, rastreabilidade e coerencia semantica.

**Escopo**

Formatacao Markdown, links, titulos, blocos semanticos, residuos de prompt, marcas de geracao assistida e inconsistencias factuais demonstraveis.

**Entregavel**

Conjunto de documentos saneados segundo o estatuto definido.

**Criterio de conclusao**

Os documentos classificados como correcao obrigatoria ficam estruturalmente coerentes e aderentes as fontes primarias.

**Justificativa**

Esta e a etapa que efetivamente estabiliza o legado em vez de apenas descreve-lo.

### 6.6 Etapa 6 - Consolidacao estrutural

**Objetivo**

Executar fusoes, desmembramentos, promocoes de estatuto e reorganizacao fisica dos arquivos.

**Escopo**

Movimentos de arquivos, consolidacao de redundancias e ajuste de referencias internas.

**Entregavel**

Arvore documental reorganizada e coerente com a matriz semantica.

**Criterio de conclusao**

Nao ha arquivos orfaos no escopo da frente, e a navegacao principal reflete a nova arquitetura documental.

**Justificativa**

Saneamento sem consolidacao estrutural deixa a documentacao parcialmente contraditoria.

### 6.7 Etapa 7 - Fechamento governado da frente

**Objetivo**

Registrar o que foi resolvido, o que ficou pendente e impedir reabertura informal de escopo.

**Escopo**

Documento final de saneamento, documento de rodada final, classificacao do remanescente e ciclo Git completo.

**Entregavel**

Artefatos finais de fechamento e base para PR ou revisao humana.

**Criterio de conclusao**

A frente fica auditavel, com fronteira clara de encerramento e sem pendencias implicitas.

**Justificativa**

Fechamento disciplinado e parte da propria governanca da frente.

## 7. Classificacao operacional inicial

### 7.1 Corrigir agora

- Markdown invalido ou malformado
- residuos evidentes de prompt, instrucao ao modelo ou marcas de geracao assistida
- ambiguidade grave de estatuto documental
- redundancias que geram contradicao ou dispersao
- links e estruturas que prejudiquem leitura confiavel
- desalinhamentos factuais demonstraveis com Git, codigo ou issues

### 7.2 Divida controlada

- reescrita estilistica ampla sem impacto semantico
- uniformizacao editorial fina de todo o acervo
- recuperacao historica exaustiva por arquivo quando nao for necessaria para decisao estrutural
- polimento de apresentacao alem do necessario para estabilizacao

### 7.3 Backlog posterior

- formalizacao ampla de politica de consulta obrigatoria ao branch de contexto
- discussao madura sobre processo de desenvolvimento de software
- reflexao estruturada sobre RUP e alternativas
- revisao estrategica completa de governanca alem do necessario para saneamento do legado
- revisao do site de documentacao como frente separada

## 8. Observacao metodologica importante

`docs/planejamento/captura/01_insights_brutos.md` nao existia ainda no branch `docs/ai-context-bootstrap`.

Isso nao invalida seu uso atual como referencia. Ao contrario, confirma a cronologia:

- primeiro houve consolidacao de contexto em `docs/ai/`
- depois estabilizacao da frente de modelagem
- e, em seguida, formalizacao do mecanismo de captura continua

Por isso, esta frente deve operar apoiando-se nas tres camadas:

- branch de contexto para memoria operacional
- branch atual para estrutura consolidada mais recente
- Git, codigo e issues para validacao factual

## 9. Proximo passo

Executar a Etapa 3 em blocos completos, classificando semanticamente todos os arquivos do legado inventariado.
