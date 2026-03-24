# Histórico Git

## 1. Escopo e base de evidência

Este documento reconstrói a evolução do projeto com base prioritária em:

- histórico Git local analisado com:
  - `git log --graph --decorate --oneline --all`
  - `git log --pretty=format:"%h | %ad | %s" --date=short`
  - `git log --reverse`
  - `git log --stat --reverse`
  - `git log -- docs/projeto/`
  - `git log -- docs/flows/`
  - `git log -- src/`
- mensagens de commit
- diffs por diretório
- issues GitHub já existentes, especialmente:
  - `#10` a `#17`
  - `#6`
  - `#1`
  - `#21`

Regra de leitura deste documento:

- commits e diffs são tratados como evidência primária de implementação
- issues são tratadas como evidência primária de intenção arquitetural e governança ativa
- documentação de fases e projeto é tratada como apoio interpretativo, não como prova suficiente por si só

## 2. Fases reais do projeto com base em evidência

## 2.1 Protótipo inicial monolítico

Período confirmado no Git:

- `59c13fd` `Primeira Versão`
- `b1dd806` `Segunda Versão`
- `436c864` `Primeira versão da Interface com Rich`
- `7bff1ee` `Versão do tradutor funcional`
- `06227b5` `primeira versão funcional`

Características observáveis nessa fase:

- aplicação ainda concentrada na raiz do repositório
- arquivos como `app.py`, `db.py`, `extractor.py`, `translator.py`, `nav_ui.py`
- uso prático de SQLite já presente
- interface Rich/CLI e tradutor surgindo antes da arquitetura em camadas

Conclusão:

- o projeto não nasceu em `src/` nem como engine de pipeline
- ele nasceu como aplicação funcional incremental e monolítica voltada ao caso ShowTrials

## 2.2 Refatoração estrutural para arquitetura em camadas

Marco concentrado em 2026-02-15:

- `6773452` `FASE 1 - Domain Layer concluída`
- `4b7ac57` `FASE 2 - Application Layer concluída`
- `16a3ab0` `FASE 3 - Infrastructure Layer concluída`
- `7f2d782` `FASE 4 - Interface Layer concluída`

Evidência concreta em `src/`:

- criação de `src/domain`
- criação de `src/application`
- criação de `src/infrastructure`
- criação de `src/interface`
- entidade `Documento`
- interfaces de repositório
- casos de uso
- repositório SQLite
- CLI refatorada

Conclusão:

- este é o principal marco arquitetural real do histórico
- a identidade técnica de ShowTrials passa a ser a de aplicação documento-cêntrica em camadas

## 2.3 Expansão funcional do ShowTrials documento-cêntrico

Período confirmado entre 2026-02-15 e 2026-02-16:

- `1a67d6c` `FASE 5 - Tradução Avançada concluída`
- `95fadfc` `FASE 6 - Exportação de Documentos concluída`
- `3ad80c9` `FASE 7A - Relatórios Avançados concluída`
- `3def168` `FASE 8 - Análise de Texto concluída`
- `44adbaa` `FASE 9 - Web Interface concluída`

Capacidades que efetivamente surgem no histórico:

- tradução persistida
- exportação em TXT
- geração de relatórios
- análise textual com NLP
- interface Web/FastAPI

Conclusão:

- a expansão real do projeto ocorreu como ampliação de casos de uso sobre o modelo documental existente
- o histórico reforça ShowTrials como sistema especializado, não como engine genérica

## 2.4 Modularização parcial com registry, configuração e remoção do legado

Marcos confirmados:

- `b185f0f` `feat(registry): implementa Service Registry com lazy loading`
- `4e23c10` merge da branch `feature/service-registry`
- `b93f91b` `clean: remove código legado e atualiza .gitignore`
- `c7afe7c` `fix: corrige injeção do registry nos casos de uso`

Mudanças concretas observáveis:

- introdução de `ServiceRegistry`
- introdução de factories
- configuração YAML
- lazy loading de serviços
- adaptação de casos de uso para consumo via registry
- remoção do código legado da raiz e consolidação de `src/`

Conclusão:

- este é um marco arquitetural real de transição
- ele aumenta modularidade, mas não materializa ainda a engine de pipeline descrita depois nas issues

## 2.5 Endurecimento técnico: qualidade, CI, telemetria e testes

Marcos confirmados entre 2026-02-18 e 2026-02-20:

- `f6649f2` ferramentas de qualidade e pre-commit
- `61cc4ff` GitHub Actions
- `5db91e3` pytest-cov
- `54332e7` cobertura com meta inicial de 27%
- `a4e84f3` ajuste da meta para 45%
- `b1f30f8` meta de cobertura no comando de CI
- `f847a71` Taskipy
- `2157a5e` telemetria básica
- sequência de commits entre `3464227` e `31848e4` adicionando telemetria, testes e correções de tipagem em múltiplos módulos

Conclusão:

- qualidade e telemetria aparecem no Git antes da governança formal atual
- esta fase é real e extensa no código, não apenas uma narrativa documental posterior

## 2.6 Formalização documental, governança e direção arquitetural futura

Marcos confirmados entre 2026-02-20 e 2026-02-22:

- `e777ff2` `reorganiza: estrutura final da documentação`
- `15d9e4b` `docs: consolida governanca e fluxos oficiais`
- `3669ece` `docs: alinha git_flow e quality_flow à GOVERNANCA.md`
- `3e8f529` merge final da branch `docs/governanca-e-fluxos`

Mudanças concretas observáveis em `docs/projeto/` e `docs/flows/`:

- criação/organização de `docs/flows/`
- criação/organização de `docs/projeto/`
- entrada de `GOVERNANCA.md`
- entrada de `git_flow.md`, `quality_flow.md` e demais flows
- entrada de `direcionamento_arquitetural_engine_mvp.md`

Conclusão:

- aqui surge formalmente a governança ativa atual
- aqui também surge de modo rastreável a direção arquitetural para engine de pipeline
- isso é evidência forte de intenção estratégica, mas não de implementação já concluída em `src/`

## 2.7 Camada operacional recente para colaboração com Codex

Marcos confirmados em 2026-03-23:

- `9d52273` manual e rodadas de colaboração com Codex
- `73fd638` formalização de novas frentes
- `cf64e0d` estrutura inicial de `docs/ai/`

Conclusão:

- trata-se de uma fase documental-operacional recente
- não representa por si só nova fase de arquitetura de produto

## 3. Marcos arquiteturais reais

## 3.1 Nascimento real do projeto: aplicação ShowTrials específica

O histórico inicial mostra:

- foco em documentos históricos
- banco SQLite já presente
- interface de terminal
- tradução como funcionalidade concreta desde cedo

Portanto, o marco inicial confirmado é:

- **ShowTrials como aplicação específica e funcional**, não como plataforma genérica

## 3.2 Replataformização para `src/` e Clean Architecture documento-cêntrica

O conjunto de commits `FASE 1` a `FASE 4` estabelece:

- domínio centrado em `Documento`
- aplicação orientada a casos de uso
- persistência SQLite
- interface CLI

Este é o marco arquitetural implementado mais sólido de todo o histórico.

## 3.3 Crescimento funcional com aumento de acoplamento prático

Tradução, exportação, relatórios, análise e Web ampliam o sistema, mas continuam dentro do padrão:

- buscar dados persistidos
- processar documento/acervo
- persistir ou exportar resultado

Conclusão:

- o crescimento real ocorreu dentro de uma arquitetura documento-cêntrica e orientada a persistência

## 3.4 Introdução de registry/factories como transição parcial

`b185f0f` introduz:

- registry
- factories
- configuração YAML
- lazy loading

Isso confirma:

- tentativa de desacoplar criação de serviços
- transição parcial para maior modularidade

Mas não confirma ainda:

- contratos de `Transformer`
- contratos de `Sink`
- `ContextoPipeline`
- executor de pipeline
- configuração declarativa de execução já implantada

## 3.5 Direção arquitetural futura confirmada por issues, não por implementação em `src/`

As issues abertas `#10` a `#17` confirmam, como intenção estratégica real:

- `Transformer` puro
- `Sink` como plugin de persistência/saída
- `ContextoPipeline`
- executor sequencial mínimo
- uso de `Iterable` para streaming
- configuração externa imutável via YAML/JSON
- versionamento imutável/incremental de pipeline
- migração de um caso de uso real para a nova arquitetura

Conclusão:

- a arquitetura-alvo futura está confirmada por milestone e issues
- ela **não** está confirmada, até esta etapa, como implementada no código central inspecionado

## 4. Marcos de governança reais

## 4.1 Qualidade e disciplina operacional surgem antes da governança formal

Antes de `GOVERNANCA.md`, o histórico já mostra:

- pre-commit
- ruff
- black
- isort
- CI em GitHub Actions
- cobertura
- Taskipy

Logo:

- governança técnica prática começou antes da formalização normativa completa

## 4.2 Formalização inicial de flows e documentos de gestão

`e777ff2` é um marco importante porque coloca no repositório:

- `docs/flows/`
- `docs/projeto/`
- documentos de visão, roadmap e gestão

Ainda assim, neste ponto:

- a governança já está documentada, mas ainda não no formato final consolidado observado depois

## 4.3 Consolidação da governança atual

Os marcos normativos mais fortes são:

- `15d9e4b` criação de `docs/flows/GOVERNANCA.md`
- `3669ece` alinhamento de `git_flow` e `quality_flow` à governança

Pontos confirmados a partir daí:

- milestone estratégica única ativa
- tipagem formal de issues
- prioridades `P0`, `P1`, `P2`
- labels como `strategic` e `frozen`
- branches tipadas
- regra de foco por milestone
- critérios de qualidade explícitos antes de merge

## 4.4 Evidência de governança aplicada nas issues/PRs

A issue `#6` e os comentários ligados ao PR `#18`/`#19` mostram aplicação real do processo:

- identificação de escopo misturado
- reorganização em unidade menor e mais coerente
- reapresentação posterior da solução

Conclusão:

- a governança atual não é apenas decorativa
- ela já está sendo usada para revisar escopo e enquadramento de mudanças

## 5. Transição ShowTrials -> CraftText baseada em evidência

## 5.1 O que está confirmado

Está confirmado por Git, código e issues:

- o sistema implementado historicamente se chama e se comporta como **ShowTrials**
- a direção futura formalizada é uma **engine/plataforma configurável de pipeline**
- a milestone ativa é `MVP - Engine de Pipeline`

## 5.2 O que não está confirmado

Até esta etapa, **não foi encontrada** evidência suficiente em Git ou issues de:

- issue formal de renomeação para `CraftText`
- commit de renomeação do projeto
- milestone com nome `CraftText`
- decisão registrada de substituição oficial do nome `ShowTrials`

Também não apareceu, nas issues consultadas:

- menção explícita a `CraftText`
- plano formal de transição nominal `ShowTrials -> CraftText`

## 5.3 Conclusão operacional

A leitura mais segura é:

- **ShowTrials** = sistema atual implementado e historicamente rastreável
- **engine de pipeline** = direção arquitetural futura formalmente ativa
- **CraftText** = hipótese de nomenclatura futura já sugerida em documentos de projeto, mas **não confirmada por Git e issues como identidade formal consolidada**

## 6. Divergências entre documentação e histórico real

## 6.1 As fases documentais não equivalem integralmente a fases históricas homogêneas

O Git mostra que:

- `FASE1` a `FASE10` correspondem mais diretamente a mudanças reais de código
- `FASE11` a `FASE17` têm parte relevante de reconstrução, reorganização e padronização documental posterior

Conclusão:

- nem toda “fase” documentada representa uma fase histórica autônoma de implementação no mesmo sentido

## 6.2 A governança atual é posterior à maior parte do histórico de produto

A documentação normativa atual fala em:

- squash merge obrigatório
- issue por branch
- milestone única ativa
- labels e fluxo formal de board

Mas o Git anterior mostra:

- múltiplos merge commits tradicionais
- branches com padrões anteriores
- fases de evolução do produto antes da consolidação dessas regras

Conclusão:

- a governança atual não pode ser retroprojetada como se sempre tivesse existido nesse formato

## 6.3 A arquitetura-alvo de pipeline é mais forte nas issues e docs do que no código observado

Issues e documentos afirmam a direção para:

- transformer
- sink
- contexto
- executor
- YAML/JSON
- versionamento

Porém o código inspecionado até aqui ainda mostra majoritariamente:

- entidade `Documento`
- casos de uso imperativos
- persistência SQLite central
- registry/factories como transição parcial

Conclusão:

- há divergência real entre estado implementado e arquitetura-alvo documentada

## 6.4 A narrativa de transição para CraftText está fraca como evidência histórica

Alguns documentos de projeto permitem inferir direção de plataforma.
Mas o histórico Git e as issues analisadas não sustentam, até esta etapa:

- renomeação formal
- coexistência formal estabilizada entre ShowTrials e CraftText

Conclusão:

- qualquer narrativa forte de transição nominal para CraftText deve ser qualificada como hipótese ou direção futura ainda não confirmada

## 7. Lacunas ainda existentes

As seguintes lacunas permanecem mesmo após a análise de Git e issues:

- não foi confirmada implementação concreta dos elementos da engine em `src/`
  - `Transformer`
  - `Sink`
  - `ContextoPipeline`
  - executor mínimo
  - pipeline configurável
- não foi confirmada correlação exata entre cada issue de engine e commits futuros, porque essas issues ainda estão abertas
- não foi confirmada decisão formal de naming para `CraftText`
- não foi feita inspeção de PRs e discussões completas de todas as issues de engine, apenas das issues disponíveis e mais relevantes nesta etapa
- não foi reconstruída ainda uma linha do tempo por arquivo específico usando `git log --follow`
- não foi confirmada implementação do protótipo `coletores/` dentro do fluxo principal; a issue `#21` o trata explicitamente como spike separado

## 8. Síntese final

Com base no histórico Git e nas issues:

- o projeto evoluiu primeiro como **ShowTrials**, aplicação específica de pesquisa documental
- a arquitetura implementada consolidada é **documento-cêntrica, em camadas, orientada a casos de uso e persistência**
- houve uma transição real para maior modularidade com **registry/factories**
- houve endurecimento técnico real com **CI, Taskipy, telemetria, testes e cobertura**
- a governança formal atual é **recente** e nasce principalmente entre 2026-02-20 e 2026-02-22
- a direção para **engine de pipeline configurável** está formalmente confirmada por docs e issues
- a implementação concreta dessa engine ainda **não** está confirmada no código central observado
- a transição nominal **ShowTrials -> CraftText** permanece **não confirmada** por Git e issues
