# Especificações Textuais de Casos de Uso Prioritários

## 1. Objetivo do documento

Este documento registra a primeira rodada de **especificações textuais** dos casos de uso prioritários da frente de modelagem.

Seu papel é aprofundar, em linguagem estruturada, os casos de uso considerados mais maduros e mais centrais para a continuidade da frente, servindo como ponte entre:

- os diagramas de casos de uso
- os requisitos integrados
- os futuros artefatos arquiteturais

Este documento não pretende esgotar todos os casos do sistema. Ele trata apenas do subconjunto mais importante neste estágio.

## 2. Base de evidência utilizada

As especificações aqui registradas se apoiam principalmente em:

- [03_documento_de_requisitos.md](/home/thiago/coleta_showtrials/docs/modelagem/03_documento_de_requisitos.md)
- [07_casos_de_uso_iniciais.md](/home/thiago/coleta_showtrials/docs/modelagem/07_casos_de_uso_iniciais.md)
- [12_revisao_integrada_dos_casos_de_uso.md](/home/thiago/coleta_showtrials/docs/modelagem/12_revisao_integrada_dos_casos_de_uso.md)
- [08_diagrama_casos_de_uso_sistema_atual.md](/home/thiago/coleta_showtrials/docs/modelagem/08_diagrama_casos_de_uso_sistema_atual.md)
- [09_diagrama_casos_de_uso_transicao_arquitetural.md](/home/thiago/coleta_showtrials/docs/modelagem/09_diagrama_casos_de_uso_transicao_arquitetural.md)
- [10_diagrama_casos_de_uso_sistema_alvo.md](/home/thiago/coleta_showtrials/docs/modelagem/10_diagrama_casos_de_uso_sistema_alvo.md)
- [11_diagrama_casos_de_uso_cenarios_especializados.md](/home/thiago/coleta_showtrials/docs/modelagem/11_diagrama_casos_de_uso_cenarios_especializados.md)
- insumos anteriores da frente

## 3. Critério de seleção dos casos prioritários

Foram selecionados os seguintes casos de uso:

- `ObterDocumento`
- `TraduzirDocumento`
- `AnalisarDocumento`
- `ConfigurarPipeline`
- `ExecutarPipelineDocumental`
- `RevisarTraducao`

Eles foram escolhidos por:

- cobrirem sistema atual, transição e sistema-alvo
- já possuírem base conceitual razoavelmente madura
- serem representativos das decisões mais importantes da frente
- ajudarem a testar a coerência entre o que existe hoje e o que está sendo projetado para a futura engine

## 4. Padrão de especificação adotado

Cada caso de uso foi especificado com a seguinte estrutura:

- nome
- objetivo
- ator principal
- stakeholders e interesses
- gatilho
- pré-condições
- pós-condições
- fluxo principal
- fluxos alternativos
- observações de modelagem
- base de evidência

Essa estrutura se inspira em práticas clássicas de especificação textual de casos de uso, mas foi adaptada ao estágio atual da frente.

## 5. Especificações dos casos prioritários

## 5.1 `ObterDocumento`

### Objetivo

Acessar um documento com seu contexto principal de uso, incluindo metadados, resumo e possibilidades imediatas de operação.

### Ator principal

- `usuario operador`

### Stakeholders e interesses

- `usuario operador`: deseja acessar rapidamente o documento, compreender seu contexto e decidir ações posteriores
- `autor/desenvolvedor`: deseja manter coerência com a natureza documento-cêntrica do sistema atual

### Gatilho

O usuário seleciona ou informa um documento que deseja consultar.

### Pré-condições

- o documento deve estar identificado no sistema
- o sistema deve ter acesso ao mecanismo de recuperação documental

### Pós-condições

- o documento é apresentado ao usuário com os dados disponíveis
- o usuário consegue identificar operações posteriores possíveis, como tradução, consulta de tradução e exportação

### Fluxo principal

1. o usuário solicita um documento
2. o sistema recupera os dados principais do documento
3. o sistema apresenta metadados e resumo/preview
4. o sistema informa recursos associados disponíveis
5. o usuário decide eventual ação posterior

### Fluxos alternativos

- documento inexistente
- falha de acesso ao repositório
- documento recuperado com dados parciais
- documento sem traduções disponíveis

### Observações de modelagem

- `ObterDocumento` funciona, no sistema atual, como caso de uso-hub
- a centralidade dos metadados é parte essencial da natureza documento-cêntrica do ShowTrials atual
- consultar detalhadamente traduções não foi absorvido pelo fluxo principal; permanece como ação posterior relacionada
- diferenças entre CLI e Web pertencem principalmente ao plano da interface, não ao núcleo do caso de uso

### Base de evidência

- documentação de fases
- código atual do sistema
- discussões de modelagem da frente

## 5.2 `TraduzirDocumento`

### Objetivo

Produzir uma tradução de um documento para um idioma de destino, vinculando corretamente o resultado ao documento e permitindo seu uso imediato ou posterior.

### Ator principal

- `usuario operador`

### Stakeholders e interesses

- `usuario operador`: deseja traduzir o documento para leitura, comparação ou uso futuro
- `autor/desenvolvedor`: deseja preservar a tradução como uma das capacidades mais fortes do sistema atual

### Gatilho

O usuário solicita a tradução de um documento para um idioma de destino.

### Pré-condições

- o documento deve existir no sistema
- o idioma de destino deve estar definido
- o sistema deve ter acesso ao mecanismo de tradução configurado
- o sistema deve ter condição de persistir a tradução no modelo atual

### Pós-condições

- a tradução é gerada
- a tradução é vinculada corretamente ao documento
- a tradução fica disponível para uso posterior

### Fluxo principal

1. o usuário seleciona um documento para tradução
2. o usuário informa o idioma de destino
3. o sistema prepara o conteúdo para tradução
4. o sistema executa a tradução
5. o sistema registra o resultado
6. o sistema vincula a tradução ao documento
7. o sistema informa o sucesso da operação

### Fluxos alternativos

- documento inexistente
- idioma inválido ou não suportado
- falha no serviço de tradução
- erro ao persistir a tradução
- existência de tradução anterior para o mesmo idioma

### Observações de modelagem

- no sistema atual, persistência é parte central do sucesso do caso
- na evolução futura, persistência pode tornar-se opcional/configurável
- o caso é autônomo, ainda que possa ser acionado a partir do contexto de `ObterDocumento`
- a estratégia de segmentação do conteúdo é relevante tanto para limites de API quanto para qualidade da tradução

### Base de evidência

- documentação de fases
- código atual do sistema
- discussões de modelagem da frente

## 5.3 `AnalisarDocumento`

### Objetivo

Analisar um documento para produzir resultados analíticos úteis ao usuário, com possibilidade de exibição e, quando desejado, persistência de produtos derivados.

### Ator principal

- `usuario operador`

### Stakeholders e interesses

- `usuario operador`: deseja obter resultados analíticos relevantes sobre um documento
- `autor/desenvolvedor`: deseja sustentar a evolução futura para um sistema mais forte em análise documental

### Gatilho

O usuário solicita a análise de um documento específico.

### Pré-condições

- o documento deve existir no sistema
- o documento deve possuir conteúdo utilizável para análise
- o sistema deve ter acesso aos recursos analíticos necessários

### Pós-condições

- resultados analíticos são produzidos
- os resultados são apresentados ao usuário
- quando aplicável, os resultados podem ser persistidos como produtos derivados

### Fluxo principal

1. o usuário seleciona um documento para análise
2. o sistema recupera o conteúdo necessário
3. o sistema executa a análise solicitada
4. o sistema produz os resultados analíticos
5. o sistema apresenta os resultados ao usuário
6. quando aplicável, o sistema registra os produtos derivados produzidos

### Fluxos alternativos

- documento inexistente
- documento sem conteúdo útil
- falha em biblioteca ou serviço analítico
- idioma não suportado para determinada análise
- erro ao gerar artefato analítico
- erro ao persistir resultados

### Observações de modelagem

- o caso é autônomo, mas pode ser acionado a partir de `ObterDocumento`
- entidades nomeadas, sumarizações e redes de relacionamento são resultados centrais
- outros resultados podem ser opcionais, conforme escolha do usuário
- todo resultado automático deve ser explicitamente identificado como automático
- a distinção entre resultado automático e resultado validado por humano é importante para o domínio
- a geração de produtos derivados já aparece no sistema atual, mas ainda com maturidade parcial/experimental
- a arquitetura futura deve facilitar a incorporação simples de novos recursos analíticos

### Base de evidência

- documentação de fases
- código atual do sistema
- discussões de modelagem da frente

## 5.4 `ConfigurarPipeline`

### Objetivo

Ajustar um pipeline para que ele atenda ao objetivo de trabalho do usuário.

### Ator principal

- `usuario configurador`

### Stakeholders e interesses

- `usuario configurador`: deseja moldar o pipeline ao contexto e ao objetivo da tarefa
- `autor/desenvolvedor`: deseja consolidar a virada da arquitetura fixa para a lógica configurável

### Gatilho

O usuário decide adaptar um pipeline a uma necessidade documental específica.

### Pré-condições

- deve existir pipeline, preset utilizável ou base mínima configurável
- o sistema deve disponibilizar recursos configuráveis compatíveis

### Pós-condições

- o pipeline fica configurado ou reconfigurado
- a configuração pode ser usada imediatamente ou persistida para uso posterior

### Fluxo principal

1. o usuário seleciona um pipeline, preset ou base inicial
2. o usuário define a fonte de entrada
3. o usuário escolhe steps/processadores
4. o usuário define destino e persistência
5. o usuário ajusta parâmetros
6. o usuário define contexto/domínio do pipeline
7. o usuário escolhe recursos opcionais
8. o sistema valida a configuração
9. o sistema registra a configuração para uso imediato ou posterior

### Fluxos alternativos

- configuração inconsistente
- step incompatível com a entrada
- ausência de recurso obrigatório
- parâmetro inválido
- falha ao salvar configuração

### Observações de modelagem

- `CriarPipeline` e `ConfigurarPipeline` não são o mesmo caso
- `CriarPipeline` cria uma base inicial; `ConfigurarPipeline` pode ser acionado a qualquer momento para ajuste
- o pipeline pode ser temporário ou persistido
- o contexto/domínio do pipeline deve aparecer explicitamente

### Base de evidência

- documento de requisitos integrado
- catálogo inicial de casos de uso
- discussões de modelagem da frente

## 5.5 `ExecutarPipelineDocumental`

### Objetivo

Executar um pipeline configurado para processar documentos conforme o objetivo de trabalho do usuário.

### Ator principal

- `usuario configurador`

### Stakeholders e interesses

- `usuario configurador`: deseja operar um fluxo configurado e obter resultados úteis
- `autor/desenvolvedor`: deseja consolidar o núcleo operacional da engine futura

### Gatilho

O usuário solicita a execução de um pipeline sobre uma entrada documental.

### Pré-condições

- um pipeline válido deve estar disponível
- a entrada documental deve ser compatível
- os recursos necessários devem estar acessíveis

### Pós-condições

- os outputs do pipeline são produzidos
- os resultados podem ser exibidos, retornados, persistidos ou encaminhados para revisão/intervenção
- quando configurado, produtos derivados são persistidos

### Fluxo principal

1. o usuário seleciona um pipeline
2. o usuário fornece ou confirma a entrada documental
3. o sistema valida a configuração e a compatibilidade da entrada
4. o sistema executa os steps do pipeline
5. o sistema gera outputs e resultados intermediários ou finais
6. o sistema exibe ou retorna os resultados
7. quando configurado, o sistema persiste os produtos derivados
8. o usuário pode continuar o trabalho a partir dos resultados produzidos

### Fluxos alternativos

- pipeline inexistente
- entrada inválida
- falha em step/processador
- falha em serviço externo
- falha de persistência
- execução parcial com erro

### Observações de modelagem

- persistir produtos derivados é opcional/configurável
- a especificação deve admitir execução síncrona e assíncrona/background
- a execução pode admitir pontos de leitura, revisão, auditoria ou intervenção humana
- o caso funciona como caso geral do qual derivam cenários especializados
- ainda há dívida técnica sobre como modelar intervenções no meio da execução sem poluir a semântica do caso

### Base de evidência

- documento de requisitos integrado
- catálogo inicial de casos de uso
- diagramas do sistema-alvo e dos cenários especializados
- discussões de modelagem da frente

## 5.6 `RevisarTraducao`

### Objetivo

Corrigir e validar uma tradução existente para uso posterior, produzindo uma versão revisada e explicitamente marcada quanto à intervenção humana.

### Ator principal

- `usuario configurador`

### Stakeholders e interesses

- `usuario configurador`: deseja validar, corrigir e tornar confiável uma tradução existente
- `autor/desenvolvedor`: deseja sustentar a distinção entre resultados automáticos e resultados revisados por humano

### Gatilho

O usuário decide revisar uma tradução existente.

### Pré-condições

- deve existir tradução recuperável no sistema
- o conteúdo original e a tradução devem estar disponíveis para comparação
- o sistema deve permitir registrar revisão e nova versão

### Pós-condições

- a tradução é corrigida quando necessário
- a tradução revisada é marcada como revisada por humano
- uma nova versão ou novo estado persistido da tradução é registrado

### Fluxo principal

1. o usuário seleciona uma tradução existente
2. o sistema recupera original e tradução
3. o sistema apresenta o conteúdo para comparação
4. o usuário revisa segmentos ou trechos
5. o sistema pode prever ou informar custo associado, quando aplicável
6. o usuário confirma as alterações
7. o sistema salva a nova versão ou o novo estado da tradução
8. o sistema marca a tradução como revisada por humano

### Fluxos alternativos

- tradução inexistente
- erro ao recuperar original ou tradução
- conflito de versão
- falha ao salvar revisão

### Observações de modelagem

- o caso deve aceitar qualquer tradução existente, com ênfase prática nas traduções automáticas
- a distinção entre tradução revisada e não revisada por humano é central
- o caso envolve edição, validação e versionamento
- previsão e cálculo de custo devem ser considerados quando houver consumo de API paga
- o caso permanece importante, mas ainda pode futuramente migrar entre o diagrama principal e o espaço dos especializados

### Base de evidência

- documento de requisitos integrado
- revisão integrada dos casos de uso
- diagramas do sistema-alvo e dos cenários especializados
- discussões de modelagem da frente

## 6. Questões em aberto

Permanecem como pontos ainda não totalmente resolvidos:

- a granularidade final de `ObterEstatisticas`
- a posição definitiva de `RevisarTraducao`
- a modelagem futura de execução com intervenções humanas em fluxo não bloqueante
- a estabilização conceitual completa de `documento`
- a relação exata entre persistência obrigatória e persistência configurável na transição para a engine

## 7. Próximos passos

Os próximos passos recomendados são:

- abrir o documento de especificações textuais dos casos secundários, se necessário
- criar matrizes de rastreabilidade entre atores, requisitos e casos de uso
- usar estas especificações como base para os próximos artefatos arquiteturais
