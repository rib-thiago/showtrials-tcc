# Cobertura de Testes

## Objetivo

Este documento registra, de forma resumida, o estado atual validado da
cobertura de testes do projeto e uma sintese curta da sua evolucao historica.

Ele deve ser lido como snapshot vivo de acompanhamento, e nao como backlog
completo de qualidade, lista definitiva de prioridades ou substituto do
historico detalhado em Git, fases e rodadas.

## Estado Atual Validado

Validacao mais recente com lastro operacional confirmado:

- cobertura total: `75.51%`
- total de testes executados com sucesso: `235`
- comando validado:

```bash
poetry run task test-cov
```

O resultado operacional que sustentou esse snapshot foi registrado em
[RODADA_20260327_53.md](/home/thiago/coleta_showtrials/docs/planejamento/rodadas/RODADA_20260327_53.md).

## Como Atualizar a Medicao

Fluxo recomendado:

```bash
poetry run task test-cov
```

Depois da execucao:

- atualizar a cobertura total, se o numero tiver mudado;
- atualizar o total de testes executados com sucesso, se necessario;
- registrar, quando houver mudanca relevante, o marco correspondente na secao
  historica abaixo;
- evitar transformar este documento em dump de saida do `pytest`.

## Evolucao Historica Resumida

Marcos historicos principais da evolucao registrada neste bloco:

- `19/02/2026`: diagnostico inicial em torno de `55%`
- `19/02/2026`: avancos para `63%`, associados ao ciclo de telemetria e
  limpeza estrutural
- `20/02/2026` a `21/02/2026`: ampliacao importante da cobertura em casos de
  uso da aplicacao
- `27/03/2026`: validacao recente consolidada em `75.51%`

Fases historicas mais diretamente relacionadas a essa evolucao:

- [FASE12_PADRONIZACAO_DA_TELEMETRIA_EM_TIPODOCUMENTO.md](/home/thiago/coleta_showtrials/docs/fases/FASE12_PADRONIZACAO_DA_TELEMETRIA_EM_TIPODOCUMENTO.md)
- [FASE13_LIMPEZA_E_ORGANIZACAO_DO_REPOSITORIO.md](/home/thiago/coleta_showtrials/docs/fases/FASE13_LIMPEZA_E_ORGANIZACAO_DO_REPOSITORIO.md)
- [FASE14_TELEMETRIA_E_TESTES_EM_EXPORTAR_DOCUMENTO.md](/home/thiago/coleta_showtrials/docs/fases/FASE14_TELEMETRIA_E_TESTES_EM_EXPORTAR_DOCUMENTO.md)
- [FASE15_TELEMETRIA_E_TESTES_EM_GERAR_RELATORIO.md](/home/thiago/coleta_showtrials/docs/fases/FASE15_TELEMETRIA_E_TESTES_EM_GERAR_RELATORIO.md)
- [FASE16_TELEMETRIA_E_EXPANSAO_DE_TESTES_EM_LISTAR_DOCUMENTOS.md](/home/thiago/coleta_showtrials/docs/fases/FASE16_TELEMETRIA_E_EXPANSAO_DE_TESTES_EM_LISTAR_DOCUMENTOS.md)

## Limites de Leitura

Este documento nao substitui:

- o historico fino de mudancas em Git;
- os historicos tecnicos de cada fase;
- os diagnosticos pontuais de CI e telemetria;
- o protocolo de qualidade vigente.

Ele tambem nao deve ser lido como ranking definitivo de prioridades de teste,
porque esse tipo de decisao depende do estado atual do codigo, do backlog e das
frentes tecnicas ativas.

## Documentos Relacionados

- [contributing.md](/home/thiago/coleta_showtrials/docs/contributing.md)
- [protocolo_de_qualidade.md](/home/thiago/coleta_showtrials/docs/flows/protocolo_de_qualidade.md)
- [diagnostico_ci.md](/home/thiago/coleta_showtrials/docs/metricas/diagnostico_ci.md)
- [diagnostico_fase12.md](/home/thiago/coleta_showtrials/docs/metricas/diagnostico_fase12.md)
- [RODADA_20260327_53.md](/home/thiago/coleta_showtrials/docs/planejamento/rodadas/RODADA_20260327_53.md)
