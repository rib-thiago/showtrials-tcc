# Diagrama de Casos de Uso — Transição Arquitetural

## 1. Objetivo do diagrama

Este documento apresenta o diagrama de casos de uso da **transição arquitetural** entre o ShowTrials atual e a futura arquitetura configurável orientada a pipeline.

Seu objetivo é representar:

- a virada conceitual entre operação e configuração
- a relação de generalização entre os atores já consolidados na frente
- os dois casos de uso centrais que estruturam a transição

## 2. Escopo adotado

Este diagrama não representa nem o sistema atual completo nem o sistema-alvo completo.

Ele funciona como um diagrama-ponte entre os dois momentos, focado na emergência da lógica configurável.

Por isso, ficam fora dele:

- os casos de uso detalhados do ShowTrials atual
- os casos de uso completos do sistema-alvo
- casos especializados da futura engine

## 3. Atores considerados

Foram considerados:

- `usuario`
- `usuario operador`
- `usuario configurador`

## 4. Generalização entre atores

Nesta etapa, a generalização entre atores foi considerada madura o suficiente para aparecer formalmente no diagrama:

- `usuario operador` especializa `usuario`
- `usuario configurador` especializa `usuario`

Essa decisão expressa a leitura já consolidada na frente:

- existe uma categoria geral de usuário do sistema
- o sistema atual é mais aderente ao `usuario operador`
- a transição e a futura engine passam a exigir o perfil de `usuario configurador`

## 5. Casos de uso representados

Foram incluídos apenas os dois casos de uso centrais da transição:

- `ConfigurarPipeline`
- `ExecutarPipeline`

Esses dois casos foram considerados suficientes para representar a virada arquitetural nesta etapa.

## 6. Relações representadas

### 6.1 Associações do ator

O `usuario configurador` foi associado diretamente a:

- `ConfigurarPipeline`
- `ExecutarPipeline`

O ator geral `usuario` foi mantido no diagrama para sustentar a generalização, e não como ator operacional direto desta versão.

### 6.2 Relações entre casos de uso

Não foi registrada, nesta etapa, relação formal de `<<include>>` ou `<<extend>>` entre:

- `ConfigurarPipeline`
- `ExecutarPipeline`

Isso foi uma decisão metodológica deliberada.

Embora os dois casos sejam fortemente relacionados, eles ainda representam intenções de uso distintas:

- configurar um fluxo
- executar um fluxo configurado

## 7. Arquivo-fonte do diagrama

O diagrama foi registrado em:

- [09_diagrama_casos_de_uso_transicao_arquitetural.puml](diagramas/09_diagrama_casos_de_uso_transicao_arquitetural.puml)

## 8. Dívidas técnicas registradas

Permanecem como pontos para análise crítica futura:

- decidir se, em iterações futuras, `ExecutarPipeline` deve ser refinado em variantes mais específicas
- decidir quando `CriarPipeline`, `ListarPipelines` e `EditarPipeline` deixam de ser apenas sistema-alvo e passam a aparecer como parte explícita da transição
- avaliar se `usuario operador` deve, em algum momento, manter associação secundária com execução de pipeline
- avaliar se haverá relação `<<include>>` ou `<<extend>>` madura o suficiente entre configuração e execução

## 9. Próximos passos

Os próximos passos recomendados são:

- usar este diagrama como ponte para o diagrama do sistema-alvo
- abrir, em seguida, o diagrama completo da futura engine
- manter o diagrama complementar para os cenários especializados como etapa posterior
