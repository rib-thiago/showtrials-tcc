# Visão de Casos de Uso — 4+1

## 1. Objetivo do documento

Este documento registra a **visão de casos de uso** da arquitetura da frente, no contexto do modelo **4+1**.

Seu objetivo é mostrar:

- quais cenários de uso dirigem a arquitetura
- como sistema atual, transição e sistema-alvo se articulam
- como os casos de uso funcionam como eixo integrador das demais visões

## 2. Base de evidência utilizada

Esta visão se apoia principalmente em:

- [07_casos_de_uso_iniciais.md](/home/thiago/coleta_showtrials/docs/modelagem/analise/principais/07_casos_de_uso_iniciais.md)
- [12_revisao_integrada_dos_casos_de_uso.md](/home/thiago/coleta_showtrials/docs/modelagem/analise/principais/12_revisao_integrada_dos_casos_de_uso.md)
- [13_especificacoes_textuais_de_casos_de_uso_prioritarios.md](/home/thiago/coleta_showtrials/docs/modelagem/analise/principais/13_especificacoes_textuais_de_casos_de_uso_prioritarios.md)
- [14_especificacoes_textuais_de_casos_de_uso_secundarios.md](/home/thiago/coleta_showtrials/docs/modelagem/analise/principais/14_especificacoes_textuais_de_casos_de_uso_secundarios.md)
- [15_matriz_atores_casos_de_uso_requisitos.md](/home/thiago/coleta_showtrials/docs/modelagem/analise/principais/15_matriz_atores_casos_de_uso_requisitos.md)
- [16_matriz_casos_de_uso_para_diagramas_e_insumos.md](/home/thiago/coleta_showtrials/docs/modelagem/analise/principais/16_matriz_casos_de_uso_para_diagramas_e_insumos.md)
- [22_visao_logica_4mais1.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/visao_4mais1/22_visao_logica_4mais1.md)
- [24_visao_de_processo_4mais1.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/visao_4mais1/24_visao_de_processo_4mais1.md)

## 3. Escopo da visão de casos de uso

No modelo 4+1, esta é a visão que articula as demais, porque expressa:

- o que o sistema precisa viabilizar
- quais cenários justificam os blocos lógicos
- quais exigências de processo, desenvolvimento e física precisam existir para sustentar esses cenários

## 4. Atores centrais já consolidados

Com base na frente já produzida, os atores centrais desta visão são:

- `usuario operador`
- `usuario configurador`

Como suporte conceitual, permanece a categoria geral:

- `usuario`

## 5. Casos de uso centrais por estágio do sistema

## 5.1 Sistema atual

Os casos mais representativos do sistema atual são:

- `ObterDocumento`
- `TraduzirDocumento`
- `AnalisarDocumento`
- `ExportarDocumento`
- `GerarRelatorio`

Esses casos refletem a natureza:

- documento-cêntrica
- orientada a persistência
- baseada em operações predominantemente síncronas

## 5.2 Transição

Os casos centrais da transição são:

- `ConfigurarPipeline`
- `ExecutarPipeline`

Eles expressam a virada da solução para:

- separação entre definição e execução
- configuração explícita do fluxo
- reinterpretação dos casos de uso imperativos como parte de uma arquitetura mais flexível

## 5.3 Sistema-alvo

Os casos centrais do sistema-alvo são:

- `CriarPipeline`
- `ConfigurarPipeline`
- `ExecutarPipelineDocumental`
- `PersistirProdutosDerivados`
- `EditarPipeline`
- `RevisarTraducao`

Eles expressam a direção arquitetural da engine:

- fluxos configuráveis
- resultados derivados tratáveis como produtos persistíveis
- intervenção humana como parte legítima de certos cenários

## 6. Casos de uso que mais dirigem a arquitetura

Entre os casos já modelados, os que mais dirigem a arquitetura da frente são:

### 6.1 `ObterDocumento`

Porque evidencia:

- centralidade do documento
- relevância da persistência
- papel dos metadados como contexto operacional

### 6.2 `TraduzirDocumento`

Porque evidencia:

- integração externa
- persistência de resultado derivado
- tensão entre uso imediato e uso posterior

### 6.3 `AnalisarDocumento`

Porque evidencia:

- produção de artefatos analíticos
- distinção entre resultado automático e leitura humana
- expansão futura por novos serviços analíticos

### 6.4 `ConfigurarPipeline`

Porque evidencia:

- separação entre criar e ajustar
- importância do contexto/domínio da execução
- necessidade de validação configurável

### 6.5 `ExecutarPipelineDocumental`

Porque evidencia:

- contexto explícito de execução
- persistência opcional/configurável
- possibilidade futura de background, auditoria e intervenção

### 6.6 `RevisarTraducao`

Porque evidencia:

- revisão humana como parte do sistema
- versionamento e rastreabilidade de resultados
- custo e governança de integrações pagas

## 7. Como esta visão dirige as demais

## 7.1 Relação com a visão lógica

Os casos de uso justificam diretamente os blocos lógicos já definidos:

- interfaces de operação
- orquestração de casos de uso
- catálogo e configuração de pipeline
- execução de pipeline
- processamento documental
- persistência e recuperação
- resultados derivados e revisão

## 7.2 Relação com a visão de desenvolvimento

Os casos de uso justificam:

- preservação da aplicação atual
- introdução incremental da engine
- separação progressiva entre legado e nova execução configurável

## 7.3 Relação com a visão de processo

Os casos de uso justificam:

- estados de execução
- compatibilidade com execução síncrona e futura execução não bloqueante
- pontos de intervenção e revisão humana

## 7.4 Relação com a visão física

Os casos de uso justificam:

- múltiplos pontos de entrada
- persistência relevante e consultável
- borda externa clara para tradução, OCR e serviços similares

## 8. Cenários arquiteturalmente mais sensíveis

Os cenários que mais exigem cuidado arquitetural na frente são:

- consulta contextualizada de documentos
- tradução com persistência e versionamento
- análise com produção de resultados derivados
- configuração de pipeline por objetivo de trabalho
- execução configurada com possível persistência opcional
- revisão humana de resultados automatizados

## 9. Inferências adotadas

As principais inferências adotadas nesta visão foram:

- a visão de casos de uso foi tratada como eixo integrador real das demais visões, e não apenas como resumo documental
- os casos da transição foram tratados como arquiteturalmente relevantes, mesmo antes de plena implementação
- `RevisarTraducao` foi mantido como caso relevante para a arquitetura, ainda que não seja o caso mais central do MVP estrutural

## 10. Dívidas técnicas registradas

Permanecem como pontos futuros:

- eventual subida de alguns casos especializados para o conjunto principal, conforme evolução da engine
- necessidade futura de papel colaborativo ou administrativo mais explícito
- estabilização conceitual definitiva de `documento`, `colecao` e resultados derivados em alguns cenários

## 11. Próximos passos

Os próximos passos recomendados são:

- consolidar a síntese do 4+1
- em seguida abrir o bloco C4 da frente
