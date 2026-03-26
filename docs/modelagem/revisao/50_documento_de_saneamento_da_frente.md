# Documento de Saneamento da Frente

## 1. Objetivo do documento

Este documento consolida o **saneamento da frente de modelagem** a partir das etapas já realizadas de:

- critérios de estabilização
- revisão crítica
- inventário de dívidas
- conferência de aderência ao projeto real

Seu objetivo é transformar diagnóstico em classificação operacional, separando explicitamente:

- o que precisa ser corrigido agora
- o que pode permanecer como dívida controlada
- o que deve ser backlogizado depois
- o que permanece fora do escopo desta estabilização

## 2. Base de evidência utilizada

Este documento se apoia principalmente em:

- [48_criterios_de_estabilizacao_da_frente.md](../fundamentos/48_criterios_de_estabilizacao_da_frente.md)
- [44_revisao_critica_final_da_frente.md](44_revisao_critica_final_da_frente.md)
- [45_dividas_tecnicas_e_documentais_da_frente.md](45_dividas_tecnicas_e_documentais_da_frente.md)
- [49_conferencia_de_aderencia_ao_projeto_real.md](49_conferencia_de_aderencia_ao_projeto_real.md)
- [46_sintese_executiva_da_frente.md](46_sintese_executiva_da_frente.md)
- [47_indice_geral_da_frente_de_modelagem.md](47_indice_geral_da_frente_de_modelagem.md)

## 3. Critério de classificação adotado

Nesta etapa, cada ponto levantado nas fases anteriores foi classificado em uma das seguintes categorias:

- `corrigir agora`
- `manter como dívida controlada`
- `backlogizar depois`
- `fora do escopo desta estabilização`

O critério usado foi:

- corrigir agora tudo o que compromete diretamente os critérios de estabilização da frente
- manter como dívida controlada tudo o que permanece relevante, mas não impede o fechamento disciplinado da frente
- backlogizar depois tudo o que ainda exige formalização futura em issues, revisão de roadmap ou nova frente
- deixar fora do escopo tudo o que extrapola o objetivo desta estabilização

## 4. Itens classificados como `corrigir agora`

Devem ser corrigidos ainda nesta estabilização:

- reorganização estrutural de `docs/modelagem/` para refletir processo de engenharia de software
- ajuste dos links internos e do índice geral após a reorganização
- implantação de mecanismo transversal de captura contínua para:
  - insight bruto
  - dívida em triagem
  - candidato a backlog
- definição explícita da política de diagramas versionáveis do projeto
- normalização final do que ainda restar como incoerência documental crítica para fechamento da frente

### Justificativa

Esses pontos afetam diretamente:

- critério estrutural
- critério de governança
- critério de completude mínima
- capacidade de encerramento disciplinado da frente

## 5. Itens classificados como `manter como dívida controlada`

Devem permanecer como dívida controlada, sem impedir o fechamento desta frente:

- posição final de `RevisarTraducao` no sistema-alvo
- posição final de `ExecutarPipelinePorID`
- refinamento semântico mais fino entre `Documento`, `Colecao`, resultados derivados e artefatos derivados
- parte da modelagem prospectiva da engine ainda não refletida como backlog técnico ativo
- eventual materialização completa dos diagramas remanescentes do bloco UML complementar que não foram produzidos nesta estabilização

### Justificativa

Esses pontos permanecem relevantes, mas hoje:

- não invalidam o núcleo já estabilizado da frente
- não impedem revisão humana integral
- podem ser tratados como dívida consciente e documentada

## 6. Itens classificados como `backlogizar depois`

Devem ser backlogizados apenas depois da estabilização e da revisão final da frente:

- abertura de novas issues da engine para elementos ainda não backlogizados
- reavaliação estruturada do roadmap arquitetural amplo
- decisão mais profunda sobre plugin system explícito versus solução mais leve
- aprofundamento futuro de background, auditoria, telemetria e acompanhamento de execução como blocos mais formais

### Justificativa

Esses pontos:

- exigem decisão posterior mais estratégica
- não precisam ser resolvidos para fechar esta frente de modelagem
- correriam risco de ampliar indevidamente o escopo se fossem tratados agora

## 7. Itens `fora do escopo desta estabilização`

Permanecem fora do escopo desta estabilização:

- implementação da engine futura
- reescrita do backlog técnico inteiro
- fechamento definitivo de toda a arquitetura prospectiva
- busca de perfeição editorial histórica completa do repositório
- revisão exaustiva de todos os commits antigos do projeto fora desta frente

## 8. Plano de execução das correções obrigatórias

As correções obrigatórias devem seguir esta ordem:

1. reorganização estrutural de `docs/modelagem/`
2. ajuste de links, referências e índice geral
3. criação do mecanismo transversal de captura contínua
4. formalização da política de diagramas versionáveis
5. revisão final de coerência documental após essas mudanças

## 9. Questões que permanecem para decisão humana

As questões abaixo permanecem dependentes de decisão humana nas próximas etapas:

- estrutura final exata dos diretórios após a reorganização
- forma concreta do mecanismo transversal de captura contínua
- grau de materialização que o bloco UML complementar ainda terá nesta frente
- momento oportuno para transformar certos elementos prospectivos da engine em novas issues

## 10. Resultado esperado desta classificação

Ao final desta etapa, a frente passa a ter:

- uma fronteira mais clara entre correção obrigatória e dívida aceitável
- um limite mais controlado para o fechamento
- base operacional para executar as correções da próxima etapa sem reabrir análise indefinidamente

## 11. Atualização posterior relevante

Durante a estabilização, foi adotada a decisão de **materializar um subconjunto mínimo e estratégico** do bloco UML complementar:

- diagrama de classes de domínio
- diagrama de componentes
- diagrama de atividades de pipelines

Os demais artefatos do bloco permanecem como especificações textuais preparatórias e continuam enquadrados como dívida controlada ou materialização futura.

## 12. Próximo passo

Consolidar o fechamento controlado da frente e decidir explicitamente o tratamento posterior dos artefatos UML complementares ainda não materializados.
