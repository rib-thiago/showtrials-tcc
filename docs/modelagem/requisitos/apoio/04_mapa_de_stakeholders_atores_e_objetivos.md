# Mapa de Stakeholders, Atores e Objetivos

## 1. Objetivo do documento

Este documento consolida a leitura atual de stakeholders, atores e objetivos da nova frente de modelagem, com o objetivo de estabilizar a base conceitual que alimentará os próximos insumos e artefatos da frente de casos de uso.

Seu foco não é descrever funcionalidades em detalhe, mas esclarecer:

- quem tem interesse no sistema
- quem interage com o sistema
- o que cada ator quer alcançar
- quais tensões estruturam essas expectativas

## 2. Escopo do mapeamento

O mapeamento considera:

- o sistema atual historicamente conhecido como `ShowTrials`
- a transição arquitetural para uma arquitetura configurável
- o sistema-alvo provisoriamente chamado de `engine futura`

Ele opera no nível de stakeholders e atores humanos, sem ainda detalhar formalmente casos de uso, fluxos ou fronteiras completas do sistema.

## 3. Stakeholders identificados

Os stakeholders principais consolidados nesta etapa são:

- `autor/desenvolvedor`
- `usuario geral do sistema`
- `banca/professor`

### 3.1 Autor/desenvolvedor

Stakeholder diretamente interessado na evolução técnica, acadêmica e documental do projeto.

### 3.2 Usuario geral do sistema

Stakeholder agregador que representa a pessoa que utiliza o sistema para trabalhar com documentos digitalizados.

Nesta etapa, a diferenciação mais útil entre perfis de uso não aparece no nível de stakeholder, mas no nível de ator.

### 3.3 Banca/professor

Stakeholder acadêmico indireto, responsável pela análise e validação final da conclusão do projeto.

## 4. Atores do sistema atual

### 4.1 Ator principal

- `usuario operador`

O `usuario operador` é a especialização de ator mais aderente ao sistema atual. Ele representa o uso direto do sistema para trabalhar com documentos, seus conteúdos e os resultados produzidos a partir deles.

### 4.2 Relação com o stakeholder agregador

O `usuario operador` deve ser entendido como uma especialização do stakeholder agregador `usuario geral do sistema`.

## 5. Atores da transição

Na transição arquitetural, a leitura principal continua temporal:

- o sistema evolui de um uso mais centrado em operação para um uso que passa a exigir configuração

Assim, a transição deve ser lida como o período em que o `usuario operador` começa a acumular, gradualmente, características de `usuario configurador`.

## 6. Atores do sistema-alvo

### 6.1 Ator principal

- `usuario configurador`

O `usuario configurador` é a especialização de ator mais aderente ao sistema-alvo. Ele representa o uso do sistema com capacidade explícita de configurar recursos, ajustar ferramentas e adequar a solução ao fluxo de trabalho desejado.

### 6.2 Coexistência e evolução temporal

Nesta etapa, a leitura principal continua sendo de evolução temporal entre os perfis de uso. Entretanto, admite-se que em cenários colaborativos futuros `usuario operador` e `usuario configurador` possam coexistir no mesmo sistema, em papéis diferenciados.

Essa coexistência, porém, ainda não é pressuposto do MVP da evolução.

## 7. Objetivos principais de cada ator

### 7.1 Objetivos do usuario operador

O `usuario operador` quer:

- trabalhar com um conjunto de documentos de seu interesse
- processar documentos
- realizar as analises desejadas
- decidir o que fazer com os outputs do processamento e da analise

### 7.2 Objetivos do usuario configurador

O `usuario configurador` quer:

- configurar apenas os recursos desejados
- ajustar o sistema ao objetivo do trabalho
- moldar a ferramenta ao fluxo de trabalho pretendido

### 7.3 Objetivo comum do usuario

O objetivo comum mais forte identificado nesta etapa e:

- o usuario da aplicacao deve conseguir ajustar o sistema ao seu objetivo de trabalho para entao usar, processar e analisar documentos de forma eficaz

## 8. Interesses e tensões entre atores

As tensoes mais relevantes identificadas ate aqui sao:

### 8.1 Tensoes de produto

- simplicidade de uso vs configurabilidade
- generalidade da solucao vs preservacao da especializacao historica

### 8.2 Tensoes de projeto

- rigor academico e documentacao completa vs velocidade de evolucao

### 8.3 Posicao adotada nesta etapa

Essas tensoes nao devem ser tratadas como contradicoes insolúveis, mas como polos que precisam ser equilibrados na evolucao do projeto.

## 9. Síntese interpretativa

O mapeamento atual sugere uma leitura coerente em tres camadas:

- no nivel de stakeholder, o `usuario geral do sistema` agrega o interesse de quem utiliza a aplicacao
- no nivel de ator, esse stakeholder se especializa em `usuario operador` e `usuario configurador`
- no nivel historico, a evolucao do sistema desloca progressivamente o centro de uso de operacao para configuracao, sem apagar a historia de uso especializada do ShowTrials

A especializacao historica do projeto nao deve ser apagada pela generalizacao da engine. Ela deve permanecer como referencia de contexto dentro do uso da aplicacao.

## 10. Objetivos dos stakeholders não operacionais

### 10.1 Autor/desenvolvedor

O `autor/desenvolvedor` quer:

- consolidar conhecimentos adquiridos no curso
- obter aprovacao no TCC
- criar uma solucao estruturada para apoiar pesquisas historicas
- manter documentacao completa e abrangente

### 10.2 Banca/professor

A `banca/professor` quer:

- avaliar se foram adotadas boas praticas
- avaliar a presenca de engenharia de software e documentacao adequada
- verificar se a entrega funciona e pode ser avaliada em ambiente de execucao
- verificar aderencia entre o que o projeto propoe fazer e o que ele efetivamente entrega

## 11. Questões em aberto

Ainda precisam ser refinados em rodadas futuras:

- amadurecimento da figura de um futuro `usuario administrador`
- relacao mais precisa entre papeis operacionais, colaborativos e administrativos
- impacto de cenarios colaborativos futuros sobre a taxonomia de atores
- detalhamento de objetivos para artefatos especificos de casos de uso
