# Historico da Fase 12 - Padronizacao da Telemetria em TipoDocumento

## Natureza do Documento

Este documento registra historicamente a intervencao que padronizou a telemetria em `TipoDocumento`.

Ele nao deve ser lido como guia operacional vigente de correcoes, testes ou fluxo Git. Esses assuntos hoje devem ser consultados principalmente em:

- [Guia de Telemetria do Projeto](../guias/guia_de_telemetria.md)
- [Guia de Debug do Projeto](../guias/guia_de_debug.md)
- [Protocolo de Git](../protocolos/protocolo_de_git.md)
- [Protocolo de Qualidade](../protocolos/protocolo_de_qualidade.md)

## Objetivo da Intervencao

Corrigir a implementacao de telemetria em `src/domain/value_objects/tipo_documento.py` para alinhar o arquivo ao padrao predominante do projeto naquele momento e restaurar consistencia nos testes relacionados.

## Contexto

Esta intervencao aconteceu pouco depois da estabilizacao inicial do CI e em continuidade ao endurecimento do uso de telemetria no projeto.

O contexto mais imediato incluia:

- o uso crescente do padrao `_telemetry` com `configure_telemetry`
- necessidade de reduzir divergencias entre modulos semelhantes
- correcoes incrementais em torno de testes e instrumentacao

Hoje esse contexto deve ser lido em conjunto com:

- [FASE 11 - CI: Estabilizacao do Pipeline de Integracao Continua](FASE11_ESTABILIZACAO_INICIAL_DO_CI.md)
- [Guia de Telemetria do Projeto](../guias/guia_de_telemetria.md)

## Problema Enfrentado

O arquivo `tipo_documento.py` seguia uma abordagem diferente da instrumentacao observada em outros pontos do projeto.

Essa divergencia gerava atrito tecnico porque:

- dificultava a uniformidade da instrumentacao
- enfraquecia a coerencia entre modulos semelhantes
- criava friccao nos testes relacionados a telemetria

## Solucao Aplicada

A intervencao historica substituiu a abordagem anterior por uma forma mais alinhada ao padrao predominante da epoca:

- uso de variavel global `_telemetry`
- configuracao explicita via `configure_telemetry`
- chamadas condicionais a `increment(...)` em pontos relevantes

Hoje esse padrao deve ser lido como parte do historico da consolidacao de telemetria do projeto, e nao como especificacao normativa unica e isolada.

## Artefatos Afetados

Com lastro direto no commit principal identificado:

- `src/domain/value_objects/tipo_documento.py`
- `src/tests/test_tipo_documento_telemetry.py`

Artefatos historicamente relacionados:

- [diagnostico_fase12.md](../diagnosticos/diagnostico_fase12.md)
- [FASE11_ESTABILIZACAO_INICIAL_DO_CI.md](FASE11_ESTABILIZACAO_INICIAL_DO_CI.md)

## Rastreabilidade Git e GitHub

### Commit principal

- [`1b91b23`](https://github.com/rib-thiago/showtrials-tcc/commit/1b91b23660024bef1aa4cb073906db4a70a35d7b) - `fix: padroniza telemetria em tipo_documento.py`

### Branch principal

- `fix/tipo-documento-telemetry`

### Branches relacionadas identificadas no mesmo historico

- `type/tipo-documento`
- `fix/tipo-documento-keyerror`

### Issue

O documento antigo apontava a issue [#2](https://github.com/rib-thiago/showtrials-tcc/issues/2) como issue principal, mas a analise historica mostra que essa issue corresponde a uma frente ampla de revisao de documentacao, e nao descreve adequadamente esta intervencao tecnica especifica.

Por isso, nesta fase saneada:

- a issue `#2` nao e tratada como issue principal valida desta intervencao
- nenhuma issue tecnica especifica foi confirmada com seguranca a partir do lastro analisado

### Pull Request

- nenhum pull request foi identificado com seguranca a partir do commit principal analisado

## Impacto Tecnico

Como historico, esta fase registra um momento de consolidacao tecnica em que:

- a instrumentacao de telemetria passou a ser tratada com mais uniformidade
- o projeto reduziu diferencas locais entre modulos com comportamento semelhante
- testes relacionados a telemetria ganharam mais previsibilidade dentro do padrao da epoca

## Documentos Relacionados

- [FASE 11 - CI: Estabilizacao do Pipeline de Integracao Continua](FASE11_ESTABILIZACAO_INICIAL_DO_CI.md)
- [Guia de Telemetria do Projeto](../guias/guia_de_telemetria.md)
- [Protocolo de Qualidade](../protocolos/protocolo_de_qualidade.md)
- [Protocolo de Git](../protocolos/protocolo_de_git.md)
- [diagnostico_fase12.md](../diagnosticos/diagnostico_fase12.md)
