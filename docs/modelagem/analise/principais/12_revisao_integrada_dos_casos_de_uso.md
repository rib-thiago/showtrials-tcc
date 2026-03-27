# Revisão Integrada dos Casos de Uso

## 1. Objetivo do documento

Este documento registra a revisão integrada, em caráter **vivo**, da frente de **casos de uso** após a consolidação dos seus principais artefatos:

- catálogo inicial de casos de uso
- diagrama do sistema atual
- diagrama da transição arquitetural
- diagrama do sistema-alvo
- diagrama complementar de cenários especializados

Seu objetivo é avaliar o conjunto já produzido, identificando:

- coerências já alcançadas
- lacunas ainda abertas
- ambiguidades conceituais
- dívidas técnicas de modelagem
- ajustes recomendados para a estabilização da subfrente de casos de uso

## 2. Base de evidência analisada

Esta revisão se apoia principalmente em:

- [07_casos_de_uso_iniciais.md](/home/thiago/coleta_showtrials/docs/modelagem/analise/principais/07_casos_de_uso_iniciais.md)
- [08_diagrama_casos_de_uso_sistema_atual.md](/home/thiago/coleta_showtrials/docs/modelagem/analise/diagramas/08_diagrama_casos_de_uso_sistema_atual.md)
- [09_diagrama_casos_de_uso_transicao_arquitetural.md](/home/thiago/coleta_showtrials/docs/modelagem/analise/diagramas/09_diagrama_casos_de_uso_transicao_arquitetural.md)
- [10_diagrama_casos_de_uso_sistema_alvo.md](/home/thiago/coleta_showtrials/docs/modelagem/analise/diagramas/10_diagrama_casos_de_uso_sistema_alvo.md)
- [11_diagrama_casos_de_uso_cenarios_especializados.md](/home/thiago/coleta_showtrials/docs/modelagem/analise/diagramas/11_diagrama_casos_de_uso_cenarios_especializados.md)
- [13_especificacoes_textuais_de_casos_de_uso_prioritarios.md](13_especificacoes_textuais_de_casos_de_uso_prioritarios.md)
- [14_especificacoes_textuais_de_casos_de_uso_secundarios.md](14_especificacoes_textuais_de_casos_de_uso_secundarios.md)
- [15_matriz_atores_casos_de_uso_requisitos.md](15_matriz_atores_casos_de_uso_requisitos.md)
- [16_matriz_casos_de_uso_para_diagramas_e_insumos.md](16_matriz_casos_de_uso_para_diagramas_e_insumos.md)
- [03_documento_de_requisitos.md](/home/thiago/coleta_showtrials/docs/modelagem/requisitos/principais/03_documento_de_requisitos.md)
- insumos anteriores de atores, objetivos, fronteira e capacidades

## 3. Síntese do conjunto produzido

O conjunto de artefatos da frente de casos de uso já apresenta uma estrutura coerente e progressiva, organizada em quatro planos complementares:

- sistema atual
- transição arquitetural
- sistema-alvo
- cenários especializados

Essa organização se mostrou adequada ao projeto porque evita misturar, num único artefato, o que pertence:

- ao ShowTrials já implementado
- à virada de arquitetura
- à futura engine configurável

Além disso, o conjunto preserva uma linha metodológica consistente:

- primeiro foram estabilizados os insumos conceituais
- depois foi produzido o catálogo inicial de casos de uso
- por fim, os diagramas foram derivados de forma incremental

## 4. Coerências já alcançadas

As principais coerências já alcançadas pela frente são as seguintes.

### 4.1 Separação clara entre sistema atual, transição e sistema-alvo

Essa separação foi mantida de forma consistente entre:

- o documento de requisitos
- o catálogo inicial de casos de uso
- os diagramas produzidos

Ela constitui, hoje, uma das maiores forças da frente.

### 4.2 Estabilização razoável dos atores

Os atores:

- `usuario`
- `usuario operador`
- `usuario configurador`

foram consolidados com boa coerência conceitual.

Também ficou estável a leitura de:

- `usuario` como categoria geral
- `usuario operador` como especialização mais aderente ao sistema atual
- `usuario configurador` como especialização mais aderente à engine futura

### 4.3 Critério adequado de centralidade e especialização

Foi acertada a decisão de distinguir:

- casos de uso centrais
- casos de uso especializados ou cenários exemplares

Isso evitou inflar os diagramas principais com pipelines muito específicos.

### 4.4 Postura conservadora com `<<include>>` e `<<extend>>`

A frente foi metodologicamente prudente ao evitar relações formais fracas ou artificiais.

Isso fortalece a honestidade dos artefatos já produzidos.

### 4.5 Uso progressivo de generalização

A generalização entre atores foi introduzida apenas no diagrama da transição, onde ela de fato agregou valor.

De forma análoga, a generalização entre casos de uso só apareceu no diagrama complementar, quando já havia base conceitual suficiente.

## 5. Lacunas identificadas

Apesar da solidez geral do conjunto, permanecem lacunas importantes.

### 5.1 Consolidação semântica ainda incompleta nas especificações textuais

As especificações textuais prioritárias e secundárias já foram produzidas, o que reduziu uma das principais lacunas da etapa anterior.

Mesmo assim, permanecem pontos que exigem consolidação semântica mais fina, especialmente em torno de:

- `Documento`
- `RevisarTraducao`
- `ExecutarPipelinePorID`
- `ObterEstatisticas`

Ou seja, a lacuna atual já não é mais de ausência de especificações, mas de estabilização conceitual do que elas descrevem.

### 5.2 Rastreabilidade ampliada, mas ainda não completa até backlog e código

As matrizes [15_matriz_atores_casos_de_uso_requisitos.md](15_matriz_atores_casos_de_uso_requisitos.md) e [16_matriz_casos_de_uso_para_diagramas_e_insumos.md](16_matriz_casos_de_uso_para_diagramas_e_insumos.md) ampliaram de forma relevante a rastreabilidade da subfrente.

Mesmo assim, ainda não existe, nesta camada, ligação mais fina e sistemática entre:

- casos de uso e backlog de issues
- casos de uso e trechos mais específicos do código
- grau de força da evidência usada em cada vínculo

### 5.3 Revisão cruzada ampliada, mas com ambiguidades remanescentes

A revisão cruzada do conjunto foi fortalecida pelas especificações textuais e pelas matrizes de rastreabilidade.

Ainda assim, alguns casos mantêm posição semântica em aberto no conjunto, o que impede considerar a subfrente plenamente encerrada sem saneamento adicional.

## 6. Ambiguidades ainda abertas

As ambiguidades mais relevantes hoje são as seguintes.

### 6.1 Granularidade de `ObterEstatisticas`

Ainda existe ambiguidade sobre o papel exato de `ObterEstatisticas`:

- caso de uso autônomo de visão agregada
- apoio a relatórios
- parte de análise mais ampla do acervo

Ele foi mantido como caso autônomo, o que é defensável, mas a granularidade ainda merece revisão futura.

### 6.2 Posição de `RevisarTraducao`

`RevisarTraducao` foi mantido como caso central do sistema-alvo.

Isso é plausível, mas ainda não está totalmente resolvido se ele deve permanecer:

- no diagrama principal do sistema-alvo
- ou migrar para o espaço dos cenários especializados

### 6.3 Posição de `ExecutarPipelinePorID`

Ainda não está completamente estabilizado se esse caso representa:

- uma especialização legítima de execução documental
- ou apenas um detalhe operacional da forma de invocação

### 6.4 Conceito de `documento`

O conceito de `documento` segue em estabilização e isso afeta a precisão futura das especificações textuais.

No estágio atual, essa ambiguidade ainda não inviabiliza os diagramas, mas precisará ser enfrentada antes da modelagem arquitetural mais fina.

## 7. Dívidas técnicas de modelagem

As principais dívidas técnicas/documentais desta subfrente, no estado atual, são:

- revisar a granularidade de `ObterEstatisticas`
- decidir a posição final de `RevisarTraducao`
- decidir a posição final de `ExecutarPipelinePorID`
- reavaliar futuramente relações de `<<include>>` e `<<extend>>` que hoje foram corretamente evitadas
- avaliar a entrada futura de papel colaborativo ou administrativo
- aprofundar o conceito de `documento` antes das etapas arquiteturais mais detalhadas

## 8. Ajustes sugeridos para a estabilização da subfrente

Considerando o estado atual da frente, recomenda-se:

- manter o conjunto de diagramas de casos de uso como base estável
- usar esta revisão como artefato vivo de controle da subfrente
- preservar como dívida o que ainda depende de maior amadurecimento arquitetural
- evitar rediscutir casos já suficientemente estabilizados sem nova evidência forte

Também se recomenda não tentar resolver, nesta camada, toda ambiguidade futura da engine. O foco deve permanecer no saneamento do que é estruturalmente necessário para estabilizar a frente.

## 9. Casos prioritários para detalhamento textual

Com base no conjunto atual, os casos de uso mais maduros e mais valiosos para detalhamento textual inicial são:

- `ObterDocumento`
- `TraduzirDocumento`
- `AnalisarDocumento`
- `ConfigurarPipeline`
- `ExecutarPipelineDocumental`
- `RevisarTraducao`

Esse conjunto é adequado porque cobre:

- sistema atual
- transição
- sistema-alvo

e permite testar, desde já, a consistência entre o que existe hoje e o que está sendo projetado para a engine futura.

## 10. Próximos passos

Os próximos passos recomendados a partir desta revisão viva são:

- usar este documento como base de conferência da subfrente de casos de uso durante o saneamento da frente
- tratar as ambiguidades remanescentes como entrada para a revisão crítica e o documento de saneamento consolidado
- conectar esta revisão ao restante da estabilização documental da frente, sem reabrir desnecessariamente a camada de casos de uso
