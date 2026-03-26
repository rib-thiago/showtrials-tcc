# Conferência de Aderência ao Projeto Real

## 1. Objetivo do documento

Este documento registra a conferência de aderência da frente de modelagem ao **projeto real**, tomando como base:

- backlog e issues do GitHub
- PRs relevantes
- código-fonte atual em `src/`
- documentação arquitetural anterior em `docs/projeto/`
- documentação histórica de fases em `docs/fases/`

Seu objetivo é distinguir, com rigor, entre:

- o que já está sustentado por implementação existente
- o que está sustentado por backlog e direcionamento arquitetural ativo
- o que permanece como hipótese arquitetural ou modelagem ainda não backlogizada

## 2. Base de evidência utilizada

Esta conferência se apoia principalmente em:

- [17_drivers_arquiteturais.md](../arquitetura/ponte/17_drivers_arquiteturais.md)
- [18_mapeamento_requisitos_para_drivers.md](../arquitetura/ponte/18_mapeamento_requisitos_para_drivers.md)
- [19_mapeamento_casos_de_uso_para_blocos_arquiteturais.md](../arquitetura/ponte/19_mapeamento_casos_de_uso_para_blocos_arquiteturais.md)
- [20_decisoes_arquiteturais_iniciais.md](../arquitetura/ponte/20_decisoes_arquiteturais_iniciais.md)
- [03_documento_de_requisitos.md](../requisitos/principais/03_documento_de_requisitos.md)
- [12_revisao_integrada_dos_casos_de_uso.md](../analise/principais/12_revisao_integrada_dos_casos_de_uso.md)
- [13_especificacoes_textuais_de_casos_de_uso_prioritarios.md](../analise/principais/13_especificacoes_textuais_de_casos_de_uso_prioritarios.md)
- [14_especificacoes_textuais_de_casos_de_uso_secundarios.md](../analise/principais/14_especificacoes_textuais_de_casos_de_uso_secundarios.md)
- [15_matriz_atores_casos_de_uso_requisitos.md](../analise/principais/15_matriz_atores_casos_de_uso_requisitos.md)
- [16_matriz_casos_de_uso_para_diagramas_e_insumos.md](../analise/principais/16_matriz_casos_de_uso_para_diagramas_e_insumos.md)
- [docs/projeto/roadmap_arquitetural.md](/home/thiago/coleta_showtrials/docs/projeto/roadmap_arquitetural.md)
- [docs/projeto/direcionamento_arquitetural_engine_mvp.md](/home/thiago/coleta_showtrials/docs/projeto/direcionamento_arquitetural_engine_mvp.md)
- [docs/projeto/analise_arquitetural.md](/home/thiago/coleta_showtrials/docs/projeto/analise_arquitetural.md)
- [FASE2_APPLICATION.md](/home/thiago/coleta_showtrials/docs/fases/FASE2_APPLICATION.md)
- [FASE5_TRADUCAO.md](/home/thiago/coleta_showtrials/docs/fases/FASE5_TRADUCAO.md)
- [FASE8_ANALISE_TEXTO.md](/home/thiago/coleta_showtrials/docs/fases/FASE8_ANALISE_TEXTO.md)
- issue [#25](https://github.com/rib-thiago/showtrials-tcc/issues/25)
- issues [#12](https://github.com/rib-thiago/showtrials-tcc/issues/12) a [#17](https://github.com/rib-thiago/showtrials-tcc/issues/17)
- PRs abertas relevantes do repositório
- estrutura atual do código em `src/`

## 3. Aderência ao backlog do GitHub

### 3.1 Aderência forte à issue-mãe da frente

A frente de modelagem permanece bem aderente à issue [#25](https://github.com/rib-thiago/showtrials-tcc/issues/25), que previa:

- documento de requisitos
- atores e casos de uso
- especificações textuais
- visão arquitetural `4+1`
- modelo C4
- UML complementar
- rastreabilidade inicial entre requisitos, arquitetura e backlog

Em termos de cobertura e variedade de artefatos, a frente entregou adequadamente esse escopo.

### 3.2 Aderência forte ao núcleo ativo do backlog da engine

As issues abertas da milestone `MVP - Engine de Pipeline`, especialmente [#12](https://github.com/rib-thiago/showtrials-tcc/issues/12) a [#17](https://github.com/rib-thiago/showtrials-tcc/issues/17), sustentam bem o núcleo arquitetural mais forte da frente:

- `ContextoPipeline`
- executor mínimo
- pipeline configurável via YAML/JSON
- suporte a `Iterable`
- versionamento incremental
- migração de um caso de uso real

Esses elementos aparecem repetidamente na modelagem e na documentação arquitetural da frente.

### 3.3 Aderência parcial entre modelagem ampliada e backlog técnico ativo

A frente já modela com mais riqueza alguns elementos que ainda não aparecem como issues próprias claramente definidas, por exemplo:

- `PersistirProdutosDerivados`
- `RevisarTraducao`
- `ConsultarResultadosDePipeline`
- bloco arquitetural de resultados derivados e revisão
- distinção explícita entre resultado automático e revisão humana

Esses elementos não contradizem o backlog ativo, mas em vários casos ainda permanecem como:

- hipótese arquitetural legitimamente derivada da frente
- ou projeção controlada ainda não backlogizada

## 4. Aderência ao código atual

### 4.1 Sistema atual fortemente sustentado por implementação

O código atual em `src/` sustenta com boa aderência os principais casos de uso do sistema atual:

- `ListarDocumentos`
- `ObterDocumento`
- `ClassificarDocumento`
- `TraduzirDocumento`
- `ListarTraducoes`
- `ObterEstatisticas`
- `AnalisarDocumento`
- `AnalisarAcervo`
- `ExportarDocumento`
- `GerarRelatorio`

Também sustenta fortemente:

- coexistência de CLI e Web
- arquitetura em camadas
- `ServiceRegistry`
- persistência documental e de traduções
- análise textual e geração de artefatos analíticos

### 4.2 Engine futura ainda não sustentada por implementação material

No código atual, não há implementação factual dos principais elementos centrais da engine futura, tais como:

- `Pipeline`
- `VersaoPipeline`
- `PipelineStep`
- `ContextoPipeline`
- `PipelineExecutor`
- `PipelineValidator`
- `PipelineRepository`
- contratos formais de `Source`, `Processor` e `Sink`

Esses elementos aparecem de forma consistente em documentação e backlog, mas não podem ser tratados como código já existente.

## 5. Aderência a `docs/projeto/` e `docs/fases/`

### 5.1 Aderência forte aos documentos de fases do sistema atual

Os documentos de fase sustentam bem a modelagem do sistema atual, especialmente nos eixos de:

- camada de aplicação
- tradução
- análise textual

Nesse ponto, a frente se mostra aderente e prudente ao distinguir claramente o que já existe do que ainda será evoluído.

### 5.2 Aderência forte ao direcionamento arquitetural do MVP da engine

[direcionamento_arquitetural_engine_mvp.md](/home/thiago/coleta_showtrials/docs/projeto/direcionamento_arquitetural_engine_mvp.md) sustenta fortemente:

- `ContextoPipeline`
- separação entre transformação e persistência
- persistência via `Sink`
- configuração externa declarativa
- versionamento incremental
- executor linear mínimo

Esses pontos aparecem de forma coerente na frente.

### 5.3 Aderência parcial ao roadmap arquitetural amplo

[roadmap_arquitetural.md](/home/thiago/coleta_showtrials/docs/projeto/roadmap_arquitetural.md) descreve uma evolução mais ampla, fortemente orientada a:

- plugin manager
- `SourcePlugin`, `ProcessorPlugin`, `ExporterPlugin`
- múltiplos milestones extensos
- UX visual e API pública

Já a frente atual e o backlog técnico ativo trabalham com uma versão mais concentrada e mais aderente ao MVP estrutural da engine.

Assim, o roadmap funciona melhor, no momento, como:

- fonte histórica e propositiva ampla

enquanto o backlog ativo e o direcionamento arquitetural do MVP funcionam como fontes mais fortes da intenção técnica imediata.

## 6. Pontos de aderência forte

Os pontos de aderência mais fortes identificados nesta etapa são:

- modelagem do sistema atual e código atual
- frente de modelagem e issue-mãe [#25](https://github.com/rib-thiago/showtrials-tcc/issues/25)
- núcleo arquitetural da engine e issues [#12](https://github.com/rib-thiago/showtrials-tcc/issues/12) a [#17](https://github.com/rib-thiago/showtrials-tcc/issues/17)
- manutenção de CLI e Web como interfaces legítimas
- leitura do sistema atual como documento-cêntrico, orientado a persistência e baseado em casos de uso imperativos

## 7. Pontos de aderência parcial

Os pontos de aderência parcial identificados nesta etapa são:

- modelagem mais rica da engine futura do que o backlog técnico ativo hoje explicita
- terminologia da frente em relação à terminologia histórica do roadmap e de documentos arquiteturais prévios
- distinção entre blocos já implementados, blocos apenas projetados e blocos ainda só implícitos no backlog

## 8. Hipóteses arquiteturais ainda não backlogizadas de forma explícita

Permanecem como hipóteses arquiteturais ou itens ainda não claramente backlogizados:

- posição final de `RevisarTraducao` na arquitetura futura
- tratamento explícito de `PersistirProdutosDerivados` como responsabilidade separada
- formalização arquitetural de `ConsultarResultadosDePipeline`
- bloco próprio para resultados derivados e revisão
- necessidade de telemetria, auditoria e acompanhamento de execução como bloco explícito

## 9. Dívidas e riscos de interpretação

Os principais riscos desta etapa são:

- ler como implementado aquilo que hoje está apenas documentado ou backlogizado
- tomar o roadmap arquitetural amplo como expressão da prioridade técnica imediata
- ignorar a deriva terminológica entre `Transformer`/`ExporterPlugin` e `Processor`/`Sink`
- deixar implícito o que ainda depende de futura transformação em issue ou backlog

## 10. Questões para decisão na etapa de saneamento

Na etapa de saneamento, será necessário decidir explicitamente:

- quais elementos da modelagem arquitetural da engine precisam ser rebaixados a hipótese/documentação prospectiva mais explícita
- quais elementos já merecem issue própria no backlog
- qual terminologia passa a ser normativa no projeto daqui em diante
- como tratar o roadmap arquitetural amplo em relação ao backlog técnico ativo atual
- se certos blocos arquiteturais da frente já devem ser refinados agora ou mantidos como dívida controlada

## 11. Próximo passo

Usar esta conferência como entrada direta da etapa de saneamento consolidado da frente, distinguindo:

- correções obrigatórias ainda nesta frente
- dívidas aceitáveis para fechamento
- itens a backlogizar depois da revisão crítica integral
