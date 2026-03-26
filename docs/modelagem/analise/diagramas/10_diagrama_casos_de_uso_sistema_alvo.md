# Diagrama de Casos de Uso — Sistema-Alvo

## 1. Objetivo do diagrama

Este documento apresenta o diagrama de casos de uso do **sistema-alvo**, entendido aqui como a futura engine configurável de processamento documental.

Seu objetivo é representar:

- o ator principal da futura engine
- os casos de uso centrais do sistema-alvo
- a organização básica entre configuração, execução e resultados

## 2. Escopo adotado

Este diagrama não busca representar todos os cenários possíveis da futura engine.

Ele se concentra no núcleo de uso já amadurecido na frente:

- criação e manutenção de pipelines
- execução documental configurável
- persistência de produtos derivados
- revisão de tradução

Ficam fora deste diagrama:

- casos de uso especializados de OCR, raspagem e tradução em pipelines específicos
- variantes mais operacionais como execução por identificador
- casos de consulta especializada de resultados

Esses elementos ficam reservados ao diagrama complementar.

## 3. Ator considerado

Foi considerado como ator principal:

- `usuario configurador`

Este ator representa o perfil de uso mais aderente à futura engine, pois o sistema-alvo exige capacidade de configurar, ajustar e operar pipelines conforme o objetivo do trabalho documental.

## 4. Casos de uso representados

Foram incluídos os seguintes casos de uso centrais:

- `CriarPipeline`
- `ListarPipelines`
- `EditarPipeline`
- `ExecutarPipelineDocumental`
- `PersistirProdutosDerivados`
- `RevisarTraducao`

## 5. Relações representadas

### 5.1 Associações do ator

O `usuario configurador` foi associado diretamente a todos os casos de uso representados.

Essa decisão mantém o diagrama simples, legível e coerente com o papel central desse ator no sistema-alvo.

### 5.2 Relações entre casos de uso

Não foi registrada, nesta etapa, relação formal de `<<include>>` ou `<<extend>>` entre os casos de uso centrais do sistema-alvo.

Essa decisão foi deliberada para evitar forçar relações ainda não suficientemente maduras, especialmente em pontos como:

- se `PersistirProdutosDerivados` é sempre obrigatório em toda execução de pipeline
- se `RevisarTraducao` pertence ao núcleo principal ou a um fluxo especializado

## 6. Estratégia visual adotada

O diagrama foi organizado em dois blocos visuais dentro da fronteira do sistema:

- configuração e manutenção de pipelines
- operação e resultados do processamento documental

Essa organização busca preservar legibilidade no PlantUML sem inflar o diagrama com casos especializados nesta etapa.

## 7. Arquivo-fonte do diagrama

O diagrama foi registrado em:

- [10_diagrama_casos_de_uso_sistema_alvo.puml](../../diagramas/fontes/10_diagrama_casos_de_uso_sistema_alvo.puml)

## 8. Dívidas técnicas registradas

Permanecem como pontos para análise crítica futura:

- avaliar se `ExecutarPipelineDocumental` deve se relacionar formalmente com `PersistirProdutosDerivados`
- avaliar se `RevisarTraducao` deve permanecer no diagrama principal ou migrar para o diagrama complementar
- avaliar se `ExecutarPipelinePorID` deve subir do diagrama complementar para o principal
- avaliar futuras relações formais de `<<include>>` ou `<<extend>>` quando a semântica de persistência e revisão estiver mais madura

## 9. Próximos passos

Os próximos passos recomendados são:

- abrir o diagrama complementar com os cenários especializados
- revisar o conjunto dos três diagramas principais em conjunto
- usar esse material como base para especificações textuais de casos de uso prioritários
