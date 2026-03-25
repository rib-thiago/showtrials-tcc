# Revisão Integrada dos Casos de Uso

## 1. Objetivo do documento

Este documento registra a revisão integrada da frente de **casos de uso** após a consolidação dos seus principais artefatos:

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
- ajustes recomendados antes da especificação textual dos casos prioritários

## 2. Base de evidência analisada

Esta revisão se apoia principalmente em:

- [07_casos_de_uso_iniciais.md](/home/thiago/coleta_showtrials/docs/modelagem/07_casos_de_uso_iniciais.md)
- [08_diagrama_casos_de_uso_sistema_atual.md](/home/thiago/coleta_showtrials/docs/modelagem/08_diagrama_casos_de_uso_sistema_atual.md)
- [09_diagrama_casos_de_uso_transicao_arquitetural.md](/home/thiago/coleta_showtrials/docs/modelagem/09_diagrama_casos_de_uso_transicao_arquitetural.md)
- [10_diagrama_casos_de_uso_sistema_alvo.md](/home/thiago/coleta_showtrials/docs/modelagem/10_diagrama_casos_de_uso_sistema_alvo.md)
- [11_diagrama_casos_de_uso_cenarios_especializados.md](/home/thiago/coleta_showtrials/docs/modelagem/11_diagrama_casos_de_uso_cenarios_especializados.md)
- [03_documento_de_requisitos.md](/home/thiago/coleta_showtrials/docs/modelagem/03_documento_de_requisitos.md)
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

### 5.1 Ausência de especificações textuais

O conjunto atual já permite boa leitura estrutural, mas ainda não oferece descrição textual completa de:

- fluxo principal
- pré-condições
- pós-condições
- variações
- exceções

Essa é a principal lacuna imediata da frente.

### 5.2 Falta de rastreabilidade mais explícita

Embora a coerência geral exista, ainda não há artefato próprio ligando explicitamente:

- requisitos
- atores
- casos de uso
- diagramas

Essa lacuna justifica a futura criação de matrizes de rastreabilidade.

### 5.3 Falta de revisão cruzada formal entre os diagramas

Até aqui, os diagramas foram construídos incrementalmente e com boa coerência, mas ainda falta um momento mais explícito de verificação conjunta do conjunto como sistema.

Este documento começa esse trabalho, mas ainda não substitui uma futura matriz mais operacional.

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

As principais dívidas técnicas/documentais desta subfrente são:

- revisar a granularidade de `ObterEstatisticas`
- decidir a posição final de `RevisarTraducao`
- decidir a posição final de `ExecutarPipelinePorID`
- reavaliar futuramente relações de `<<include>>` e `<<extend>>` que hoje foram corretamente evitadas
- avaliar a entrada futura de papel colaborativo ou administrativo
- aprofundar o conceito de `documento` antes das etapas arquiteturais mais detalhadas

## 8. Ajustes sugeridos antes das especificações textuais

Antes da abertura do documento de especificações textuais, recomenda-se:

- manter o conjunto atual de diagramas como base estável
- não redesenhar os diagramas sem necessidade forte
- usar a revisão crítica aqui registrada como guia para escolher prioridades
- detalhar primeiro os casos de uso mais maduros e mais centrais

Também se recomenda não tentar resolver, antes do tempo, todas as ambiguidades remanescentes. Algumas delas serão tratadas com mais precisão quando os fluxos textuais forem escritos.

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

Os próximos passos recomendados a partir desta revisão são:

- abrir o artefato de especificações textuais dos casos prioritários
- depois registrar uma segunda rodada com casos secundários, se necessário
- criar matrizes de rastreabilidade entre atores, requisitos e casos de uso
- usar o resultado dessas especificações como ponte para os próximos artefatos arquiteturais
