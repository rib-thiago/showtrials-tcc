# Diagnostico Historico da Divergencia de Telemetria em TipoDocumento

## Natureza do Documento

Este documento registra historicamente o diagnostico da divergencia de
telemetria identificada em `src/domain/value_objects/tipo_documento.py`.

Ele deve ser lido como diagnostico historico de uma incompatibilidade tecnica
de epoca, e nao como descricao viva do estado atual da telemetria no projeto.

## Problema Diagnosticado

O arquivo `tipo_documento.py` seguia, naquele momento, um padrao de
instrumentacao diferente do padrao que se consolidava no restante do projeto.

A divergencia mais visivel era a ausencia de:

- variavel global `_telemetry`
- funcao `configure_telemetry(...)`
- verificacoes condicionais do tipo `if _telemetry:`

Essa diferenca gerava atrito tecnico com os testes e com a uniformidade da
instrumentacao.

## Evidencias Principais

### Divergencia de Padrao

O diagnostico historico identificou a diferenca entre:

- o padrao consolidado da epoca, baseado em `_telemetry` e
  `configure_telemetry(...)`;
- a implementacao de `tipo_documento.py`, que usava abordagem distinta com
  decorator e fallback de importacao.

### Sintoma Observado

O sintoma tecnico mais direto aparecia assim:

```text
AttributeError: module 'src.domain.value_objects.tipo_documento'
has no attribute 'configure_telemetry'
```

Isso indicava incompatibilidade entre o modulo e a expectativa dos testes
relacionados a telemetria.

## Causa Raiz Identificada

A causa raiz identificada no periodo foi que `tipo_documento.py` nao havia sido
atualizado para acompanhar o padrao de telemetria que vinha sendo adotado em
outros modulos do projeto.

O problema, portanto, nao era apenas um teste quebrado, mas uma divergencia de
instrumentacao entre partes semanticamente proximas do codigo.

## Solucao Historica Aplicada

A correcao historica substituiu a abordagem anterior por uma implementacao mais
alinhada ao padrao predominante da epoca:

- introducao de `_telemetry`
- introducao de `configure_telemetry(...)`
- uso de chamadas condicionais de telemetria em pontos relevantes

O lastro tecnico principal dessa correcao esta em:

- [`1b91b23`](https://github.com/rib-thiago/showtrials-tcc/commit/1b91b23660024bef1aa4cb073906db4a70a35d7b) - `fix: padroniza telemetria em tipo_documento.py`
- [FASE12_PADRONIZACAO_DA_TELEMETRIA_EM_TIPODOCUMENTO.md](../../historico/fases/FASE12_PADRONIZACAO_DA_TELEMETRIA_EM_TIPODOCUMENTO.md)

## Impacto Historico

Historicamente, este diagnostico importa por tres motivos:

- mostrou que a consolidacao da telemetria no projeto nao era totalmente
  uniforme;
- justificou a correcao aplicada na fase correspondente;
- registrou um momento de endurecimento tecnico em torno de testes e
  instrumentacao.

## Limites de Leitura no Estado Atual

Este documento nao deve ser lido como fonte viva principal para:

- definicao normativa de telemetria;
- estado atual dos testes do modulo;
- backlog atual de qualidade;
- associacao formal com issue tecnica especifica.

Para isso, a leitura mais forte hoje deve ser feita em:

- [FASE12_PADRONIZACAO_DA_TELEMETRIA_EM_TIPODOCUMENTO.md](../../historico/fases/FASE12_PADRONIZACAO_DA_TELEMETRIA_EM_TIPODOCUMENTO.md)
- [guia_de_telemetria.md](../../guias/guia_de_telemetria.md)
- [protocolo_de_qualidade.md](../../protocolos/protocolo_de_qualidade.md)

## Documentos Relacionados

- [FASE12_PADRONIZACAO_DA_TELEMETRIA_EM_TIPODOCUMENTO.md](../../historico/fases/FASE12_PADRONIZACAO_DA_TELEMETRIA_EM_TIPODOCUMENTO.md)
- [guia_de_telemetria.md](../../guias/guia_de_telemetria.md)
- [protocolo_de_qualidade.md](../../protocolos/protocolo_de_qualidade.md)
