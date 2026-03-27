# Guia de Correcao Urgente

## Objetivo

Este guia organiza a resposta a correcoes urgentes no projeto quando um problema critico exige tratamento prioritario.

Seu objetivo e:

- manter foco no minimo necessario para restaurar estabilidade
- preservar rastreabilidade tecnica mesmo em situacoes urgentes
- reduzir o risco de que a urgencia suspenda totalmente governanca, Git, qualidade e verificacao

## Quando Este Guia Deve Ser Usado

Este guia deve ser usado quando houver uma falha com impacto alto o suficiente para justificar tratamento prioritario, por exemplo:

- funcionalidade principal quebrada
- erro grave que bloqueia uso essencial
- corrupcao de dados ou comportamento equivalente
- falha critica no CI ou em integracao que bloqueie restauracao do sistema

Nao deve ser usado para:

- melhoria incremental
- refatoracao
- nova funcionalidade
- ajuste menor sem impacto critico real

## Principios para Correcao Urgente

- corrigir apenas o necessario para restaurar estabilidade
- nao misturar correcao urgente com refatoracao ou funcionalidade nova
- manter teste minimo e verificacao tecnica aplicavel
- registrar a urgencia por issue ou mecanismo equivalente de rastreabilidade
- manter o fluxo coerente com governanca e Git, salvo deliberacao explicita em contrario

Urgencia nao deve ser tratada como autorizacao automatica para:

- trabalhar diretamente na `main`
- pular revisao sem justificativa
- ignorar CI
- inventar estrategia de release sem validacao

## Fluxo Minimo de Resposta

Em termos praticos, uma correcao urgente deve seguir no minimo:

1. registrar o problema critico e seu impacto
2. criar branch coerente com o tipo principal da mudanca
3. aplicar a menor correcao necessaria
4. executar verificacao tecnica minima aplicavel
5. abrir ou atualizar pull request com rastreabilidade clara
6. integrar a mudanca conforme o fluxo de Git e a governanca vigente

Exemplos uteis:

```bash
poetry run pytest src/tests/test_arquivo_afetado.py -v
task test
gh run view <ID> --log
```

## Verificacao Antes da Integracao

Antes de considerar a correcao urgente pronta para integracao, verificar no minimo:

- o problema critico foi claramente identificado
- a mudanca permanece minima e focada
- nao houve mistura com refatoracao ou funcionalidade nova
- a verificacao tecnica minima aplicavel foi executada
- a issue, branch e pull request estao rastreaveis
- o impacto no CI foi considerado

## Pendencias e Validacoes Necessarias

- esta frente nao confirmou lastro suficiente para tratar merge direto na `main` como pratica consolidada de correcoes urgentes
- esta frente tambem nao confirmou lastro suficiente para tratar tags patch e releases GitHub como passo obrigatorio em toda correcao urgente
- labels especificas de hotfix, estrategia de release e politica formal de incidentes ainda exigem discussao posterior de processo
- qualquer decisao sobre versionamento, tags e release deve ser lida em conjunto com [Versionamento e Releases](../projeto/versionamento_e_releases.md)

## Documentos Relacionados

- [Politica de Governanca do Projeto](../politicas/politica_de_governanca.md)
- [Protocolo de Git do Projeto](../protocolos/protocolo_de_git.md)
- [Protocolo de Qualidade do Projeto](../protocolos/protocolo_de_qualidade.md)
- [Guia de Debug do Projeto](guia_de_debug.md)
- [Versionamento e Releases](../projeto/versionamento_e_releases.md)
- [Git Flow - Hotfix branches](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow#hotfix-branches)
