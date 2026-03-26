# Criterios de Estabilizacao da Frente

## 1. Objetivo do documento

Este documento formaliza os **criterios de estabilizacao** da frente de modelagem.

Seu objetivo e:

- definir o que significa considerar a frente estabilizada
- limitar a expansao indefinida do escopo de revisao
- registrar o que precisa ser corrigido agora, o que pode permanecer como divida e o que deve virar backlog posterior
- servir como gate formal antes das etapas seguintes do saneamento

## 2. Base de evidencia utilizada

Este documento se apoia em:

- [01_estrategia_operacional_da_frente.md](/home/thiago/coleta_showtrials/docs/modelagem/01_estrategia_operacional_da_frente.md)
- [44_revisao_critica_final_da_frente.md](44_revisao_critica_final_da_frente.md)
- [45_dividas_tecnicas_e_documentais_da_frente.md](45_dividas_tecnicas_e_documentais_da_frente.md)
- [46_sintese_executiva_da_frente.md](46_sintese_executiva_da_frente.md)
- [47_indice_geral_da_frente_de_modelagem.md](47_indice_geral_da_frente_de_modelagem.md)
- `docs/projeto/manual_colaboracao_codex.md` no branch de contexto `docs/ai-context-bootstrap`
- `docs/ai/05_session_handoff.md` no branch de contexto `docs/ai-context-bootstrap`

## 3. Criterios de estabilizacao

Para esta frente, considera-se que ha **estabilizacao suficiente para PR** quando os criterios abaixo forem satisfeitos.

### 3.1 Criterio semantico

Os conceitos centrais da frente devem estar suficientemente estaveis para nao gerar conflito relevante entre os documentos finais.

Esse criterio inclui, no minimo:

- taxonomia de atores consolidada
- terminologia antiga e nova reconciliadas
- conceito de `Documento` suficientemente estabilizado
- separacao coerente entre sistema atual, transicao e sistema-alvo

### 3.2 Criterio de estatuto dos artefatos

Cada artefato principal da frente deve ter natureza claramente identificada, sem ambiguidade relevante entre:

- documento final consolidado
- documento historico de etapa
- recorte preparatorio
- sintese
- indice

Esse criterio exige coerencia entre:

- titulo do artefato
- conteudo do artefato
- papel atribuido no indice geral da frente

### 3.3 Criterio de aderencia factual

A frente deve distinguir com clareza suficiente:

- o que esta implementado no projeto atual
- o que esta apenas em transicao
- o que e modelagem prospectiva legitima
- o que ainda e hipotese nao backlogizada

Codigo e Git devem prevalecer na descricao do que existe; issues e milestone devem prevalecer na descricao da intencao arquitetural futura.

### 3.4 Criterio de completude minima

A frente deve conter todos os artefatos essenciais previstos no plano em forma suficientemente defensavel para:

- revisao humana integral
- saneamento posterior
- submissao futura por PR

Esse criterio nao exige perfeicao total, mas exige que lacunas remanescentes estejam claramente classificadas como:

- correcao obrigatoria agora
- divida tecnica/documental
- backlog futuro

### 3.5 Criterio de governanca

O estado final da frente deve ser suficientemente rastreavel e auditavel segundo a governanca acordada.

Isso implica:

- coerencia minima entre documentos
- coerencia minima entre rodadas e commits
- reconhecimento explicito dos desvios ocorridos
- delimitacao clara do que sera corrigido nesta estabilizacao

### 3.6 Criterio estrutural

A organizacao fisica de `docs/modelagem/` deve refletir um processo de engenharia de software suficientemente claro para:

- releitura humana
- manutencao futura
- evolucao por novas frentes de analise, implementacao e teste

### 3.7 Criterio de encerramento

Tudo o que nao for essencial para estabilizar a frente nesta rodada deve ser explicitamente classificado como:

- divida tecnica ou documental
- ou backlog futuro

Nenhuma descoberta nova, por si so, deve ampliar automaticamente o escopo da frente atual.

## 4. Itens fora do escopo desta estabilizacao

Nao fazem parte obrigatoria desta estabilizacao:

- implementacao da engine futura
- fechamento definitivo de toda divida arquitetural prospectiva
- resolucao completa de background, filas e topologia futura
- abertura imediata de novas issues sem consolidacao previa em documento de saneamento
- busca de perfeicao editorial absoluta em todo o historico da frente

## 5. Regra de encerramento da frente

Esta frente devera ser considerada suficientemente estabilizada quando:

- o nucleo semantico estiver coerente
- o estatuto dos artefatos estiver definido
- as inconsistencias obrigatorias tiverem sido corrigidas
- a estrutura de diretorios estiver reorganizada conforme decisao posterior
- houver mecanismo oficial de captura continua para insights, dividas e candidatos a backlog
- houver politica explicita para diagramas versionaveis
- backlog futuro e dividas remanescentes estiverem classificados

Nesse ponto, o restante do trabalho deixa de pertencer ao escopo da estabilizacao da frente e passa a ser tratado como manutencao, backlog ou nova frente.

## 6. Inferencias adotadas

- a frente ja possui massa critica suficiente para entrar em estabilizacao, e nao em nova fase de expansao
- o principal risco agora nao e falta de conteudo, mas perda de controle de escopo
- um criterio formal de estabilizacao reduz o risco de revisao infinita

## 7. Suposicoes operacionais

- este documento funcionara como gate formal para as proximas etapas do plano operacional de estabilizacao
- novas descobertas durante a revisao serao classificadas, e nao automaticamente incorporadas ao escopo

## 8. Dividas tecnicas registradas

- detalhar, nas proximas etapas, quais inconsistencias sao obrigatorias e quais podem permanecer como divida
- decidir explicitamente o estatuto final do bloco UML `32-39`
- decidir a estrutura final de diretorios apos o saneamento semantico

## 9. Proximos passos

- iniciar a Etapa 2: saneamento semantico do nucleo da frente
