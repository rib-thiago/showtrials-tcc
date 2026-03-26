# C4 — Modelo de Contexto

## 1. Objetivo do documento

Este documento registra o **modelo de contexto** da frente segundo o **C4 Model**.

Seu objetivo é mostrar:

- qual sistema estamos delimitando
- quem interage com ele
- quais sistemas externos o circundam
- quais fronteiras são relevantes para a leitura arquitetural

## 2. Base de evidência utilizada

Esta visão se apoia principalmente em:

- [04_mapa_de_stakeholders_atores_e_objetivos.md](/home/thiago/coleta_showtrials/docs/modelagem/requisitos/apoio/04_mapa_de_stakeholders_atores_e_objetivos.md)
- [05_fronteira_do_sistema_e_recortes_de_modelagem.md](/home/thiago/coleta_showtrials/docs/modelagem/requisitos/apoio/05_fronteira_do_sistema_e_recortes_de_modelagem.md)
- [15_matriz_atores_casos_de_uso_requisitos.md](/home/thiago/coleta_showtrials/docs/modelagem/analise/principais/15_matriz_atores_casos_de_uso_requisitos.md)
- [22_visao_logica_4mais1.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/visao_4mais1/22_visao_logica_4mais1.md)
- [27_sintese_4mais1.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/visao_4mais1/27_sintese_4mais1.md)
- estrutura atual do código em `src/`

## 3. Sistema em foco

O sistema em foco é o **ShowTrials em evolução para uma plataforma configurável de processamento documental**.

Nesta frente, ele é entendido como a solução que permite ao usuário:

- consultar documentos
- processar, traduzir e analisar documentos
- persistir e recuperar artefatos
- configurar e executar pipelines
- revisar resultados derivados quando aplicável

## 4. Pessoas e papéis externos ao sistema

Os papéis humanos mais relevantes no contexto do sistema são:

### 4.1 `usuario operador`

Interage com o sistema atual para:

- consultar documentos
- traduzir
- analisar
- exportar
- gerar relatórios

### 4.2 `usuario configurador`

Interage com a evolução do sistema para:

- criar pipelines
- configurar pipelines
- executar fluxos configurados
- revisar resultados derivados

### 4.3 `autor/desenvolvedor`

É stakeholder relevante da frente, mas não foi tratado como ator principal de operação do sistema nesta modelagem.

## 5. Sistemas externos relevantes

Os sistemas externos mais relevantes no contexto arquitetural são:

### 5.1 Fontes documentais externas

Representam:

- sites
- acervos
- fontes de coleta
- outros provedores de entrada documental

Elas estão fora da fronteira do sistema e são tratadas como origem externa de conteúdo.

### 5.2 Serviços externos de tradução, OCR e análise

Representam:

- APIs de tradução
- OCR
- serviços especializados consumidos pelo sistema

Eles permanecem fora da fronteira do sistema e são consumidos como dependências externas.

### 5.3 Infraestrutura externa de execução

Representa:

- ambiente de deploy
- runtime do host
- recursos de terceiros necessários à operação

Ela também permanece fora da fronteira do sistema no modelo de contexto.

## 6. Relações contextuais principais

As relações contextuais mais importantes são:

1. `usuario operador` usa o sistema para trabalhar com documentos e resultados do sistema atual.
2. `usuario configurador` usa o sistema para configurar e executar fluxos mais flexíveis da engine futura.
3. o sistema consome fontes documentais externas quando necessário.
4. o sistema consome serviços externos especializados, como tradução e OCR.
5. o sistema depende de infraestrutura externa para ser executado, mas essa infraestrutura não é parte da solução modelada aqui.

## 7. Fronteira arquitetural adotada

No modelo de contexto adotado nesta frente:

### Dentro do sistema

- interfaces CLI e Web
- capacidades de consulta, processamento, tradução e análise
- persistência e recuperação
- configuração e execução de pipeline
- revisão de resultados quando suportada

### Fora do sistema

- usuários
- fontes externas
- APIs e serviços externos
- infraestrutura externa

## 8. Leitura contextual do sistema atual, transição e sistema-alvo

## 8.1 Sistema atual

O sistema aparece no contexto como aplicação documento-cêntrica, orientada a persistência, com CLI e Web e consumo pontual de serviços externos.

## 8.2 Transição

O sistema passa a aparecer também como plataforma em configuração, na qual o `usuario configurador` ganha papel explícito.

## 8.3 Sistema-alvo

O sistema passa a aparecer como plataforma configurável de processamento documental, ainda cercada por fontes externas e serviços especializados.

## 9. Inferências adotadas

As principais inferências adotadas neste modelo de contexto foram:

- o `usuario configurador` foi tratado como ator legítimo do contexto, mesmo antes de plena materialização da engine
- serviços externos especializados foram agrupados como sistemas externos relevantes, sem fragmentação excessiva por fornecedor
- o contexto foi mantido aderente ao que já consolidamos na fronteira funcional, sem reabrir a discussão de fronteira-base

## 10. Dívidas técnicas registradas

Permanecem como pontos futuros:

- decidir se algum papel colaborativo ou administrativo precisará aparecer como pessoa explícita no contexto
- decidir o grau futuro de detalhamento entre fontes documentais externas distintas
- decidir se a futura execução em background exigirá explicitação de algum sistema externo adicional no contexto

## 11. Próximos passos

Os próximos passos recomendados são:

- abrir o modelo de containers do C4
- depois detalhar componentes e código
