# Índice Geral da Frente de Modelagem

## 1. Objetivo do documento

Este documento organiza um **índice geral navegável** da frente de modelagem.

Seu objetivo é facilitar:

- revisão humana integral
- navegação por etapa
- localização rápida de artefatos
- preparação futura de saneamento e fechamento operacional

## 2. Como navegar nesta documentação

Esta frente foi reorganizada para refletir um processo de engenharia de software.

Os diretórios principais devem ser lidos assim:

- `fundamentos/`: abre a frente, formaliza sua estratégia operacional e registra os critérios de estabilização
- `requisitos/`: reúne o documento mestre de requisitos em `principais/` e os documentos de apoio em `apoio/`
- `analise/`: concentra catálogo e revisão de casos de uso, matrizes e documentos diagramáticos da análise de casos de uso
- `arquitetura/`: reúne a ponte entre requisitos e arquitetura, o bloco `4+1`, o bloco `C4` e a análise de padrões
- `diagramas/`: separa arquivos-fonte gráficos em `fontes/` e especificações textuais preparatórias em `especificacoes/`
- `revisao/`: concentra revisão crítica, dívidas, síntese executiva, índice geral, conferência de aderência e saneamento da frente

### 2.1 Percursos recomendados

Para diferentes objetivos de leitura, recomenda-se:

- revisão integral da frente:
  - fundamentos
  - requisitos
  - análise
  - arquitetura
  - diagramas
  - revisão
- foco em casos de uso:
  - `requisitos/principais/03`
  - `analise/principais/07`
  - `analise/diagramas/08-11`
  - `analise/principais/12-16`
- foco em arquitetura:
  - `arquitetura/ponte/17-21`
  - `arquitetura/visao_4mais1/22-27`
  - `arquitetura/c4/28-31`
  - `arquitetura/padroes/40-43`
- foco em fechamento crítico:
  - `revisao/44-50`

## 3. Abertura da frente

- [01_estrategia_operacional_da_frente.md](/home/thiago/coleta_showtrials/docs/modelagem/fundamentos/01_estrategia_operacional_da_frente.md)
- [02_formalizacao_da_frente_no_projeto.md](/home/thiago/coleta_showtrials/docs/modelagem/fundamentos/02_formalizacao_da_frente_no_projeto.md)

## 4. Requisitos e insumos iniciais

- [03_documento_de_requisitos.md](/home/thiago/coleta_showtrials/docs/modelagem/requisitos/principais/03_documento_de_requisitos.md)
- [01_documento_de_requisitos_showtrials_atual.md](/home/thiago/coleta_showtrials/docs/modelagem/requisitos/apoio/01_documento_de_requisitos_showtrials_atual.md)
- [02_documento_de_requisitos_evolucao_engine.md](/home/thiago/coleta_showtrials/docs/modelagem/requisitos/apoio/02_documento_de_requisitos_evolucao_engine.md)
- [03_glossario_de_atores_e_termos.md](/home/thiago/coleta_showtrials/docs/modelagem/requisitos/apoio/03_glossario_de_atores_e_termos.md)
- [04_mapa_de_stakeholders_atores_e_objetivos.md](/home/thiago/coleta_showtrials/docs/modelagem/requisitos/apoio/04_mapa_de_stakeholders_atores_e_objetivos.md)
- [05_fronteira_do_sistema_e_recortes_de_modelagem.md](/home/thiago/coleta_showtrials/docs/modelagem/requisitos/apoio/05_fronteira_do_sistema_e_recortes_de_modelagem.md)
- [06_mapa_inicial_de_capacidades_e_casos_de_uso_candidatos.md](/home/thiago/coleta_showtrials/docs/modelagem/requisitos/apoio/06_mapa_inicial_de_capacidades_e_casos_de_uso_candidatos.md)

## 5. Casos de uso

- [07_casos_de_uso_iniciais.md](/home/thiago/coleta_showtrials/docs/modelagem/analise/principais/07_casos_de_uso_iniciais.md)
- [08_diagrama_casos_de_uso_sistema_atual.md](/home/thiago/coleta_showtrials/docs/modelagem/analise/diagramas/08_diagrama_casos_de_uso_sistema_atual.md)
- [09_diagrama_casos_de_uso_transicao_arquitetural.md](/home/thiago/coleta_showtrials/docs/modelagem/analise/diagramas/09_diagrama_casos_de_uso_transicao_arquitetural.md)
- [10_diagrama_casos_de_uso_sistema_alvo.md](/home/thiago/coleta_showtrials/docs/modelagem/analise/diagramas/10_diagrama_casos_de_uso_sistema_alvo.md)
- [11_diagrama_casos_de_uso_cenarios_especializados.md](/home/thiago/coleta_showtrials/docs/modelagem/analise/diagramas/11_diagrama_casos_de_uso_cenarios_especializados.md)
- [12_revisao_integrada_dos_casos_de_uso.md](/home/thiago/coleta_showtrials/docs/modelagem/analise/principais/12_revisao_integrada_dos_casos_de_uso.md)
- [13_especificacoes_textuais_de_casos_de_uso_prioritarios.md](/home/thiago/coleta_showtrials/docs/modelagem/analise/principais/13_especificacoes_textuais_de_casos_de_uso_prioritarios.md)
- [14_especificacoes_textuais_de_casos_de_uso_secundarios.md](/home/thiago/coleta_showtrials/docs/modelagem/analise/principais/14_especificacoes_textuais_de_casos_de_uso_secundarios.md)
- [15_matriz_atores_casos_de_uso_requisitos.md](/home/thiago/coleta_showtrials/docs/modelagem/analise/principais/15_matriz_atores_casos_de_uso_requisitos.md)
- [16_matriz_casos_de_uso_para_diagramas_e_insumos.md](/home/thiago/coleta_showtrials/docs/modelagem/analise/principais/16_matriz_casos_de_uso_para_diagramas_e_insumos.md)

## 6. Ponte para arquitetura

- [17_drivers_arquiteturais.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/ponte/17_drivers_arquiteturais.md)
- [18_mapeamento_requisitos_para_drivers.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/ponte/18_mapeamento_requisitos_para_drivers.md)
- [19_mapeamento_casos_de_uso_para_blocos_arquiteturais.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/ponte/19_mapeamento_casos_de_uso_para_blocos_arquiteturais.md)
- [20_decisoes_arquiteturais_iniciais.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/ponte/20_decisoes_arquiteturais_iniciais.md)
- [21_glossario_arquitetural_e_tecnico.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/ponte/21_glossario_arquitetural_e_tecnico.md)

## 7. Bloco 4+1

- [22_visao_logica_4mais1.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/visao_4mais1/22_visao_logica_4mais1.md)
- [23_visao_de_desenvolvimento_4mais1.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/visao_4mais1/23_visao_de_desenvolvimento_4mais1.md)
- [24_visao_de_processo_4mais1.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/visao_4mais1/24_visao_de_processo_4mais1.md)
- [25_visao_fisica_4mais1.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/visao_4mais1/25_visao_fisica_4mais1.md)
- [26_visao_de_casos_de_uso_4mais1.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/visao_4mais1/26_visao_de_casos_de_uso_4mais1.md)
- [27_sintese_4mais1.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/visao_4mais1/27_sintese_4mais1.md)

## 8. Bloco C4

- [28_c4_modelo_de_contexto.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/c4/28_c4_modelo_de_contexto.md)
- [29_c4_modelo_de_containers.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/c4/29_c4_modelo_de_containers.md)
- [30_c4_modelo_de_componentes.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/c4/30_c4_modelo_de_componentes.md)
- [31_c4_modelo_de_codigo.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/c4/31_c4_modelo_de_codigo.md)

## 9. UML complementar

Nesta estabilização, o bloco UML complementar foi **parcialmente materializado**. Os artefatos abaixo se distribuem em dois grupos:

### 9.1 Diagramas já materializados

- [32_diagrama_de_classes_de_dominio.md](/home/thiago/coleta_showtrials/docs/modelagem/diagramas/especificacoes/32_diagrama_de_classes_de_dominio.md)
- [32_diagrama_de_classes_de_dominio.puml](/home/thiago/coleta_showtrials/docs/modelagem/diagramas/fontes/32_diagrama_de_classes_de_dominio.puml)
- [32_diagrama_de_classes_de_dominio.svg](/home/thiago/coleta_showtrials/docs/modelagem/diagramas/renderizados/32_diagrama_de_classes_de_dominio.svg)
- [34_diagrama_de_componentes.md](/home/thiago/coleta_showtrials/docs/modelagem/diagramas/especificacoes/34_diagrama_de_componentes.md)
- [34_diagrama_de_componentes.puml](/home/thiago/coleta_showtrials/docs/modelagem/diagramas/fontes/34_diagrama_de_componentes.puml)
- [34_diagrama_de_componentes.svg](/home/thiago/coleta_showtrials/docs/modelagem/diagramas/renderizados/34_diagrama_de_componentes.svg)
- [38_diagrama_de_atividades_de_pipelines.md](/home/thiago/coleta_showtrials/docs/modelagem/diagramas/especificacoes/38_diagrama_de_atividades_de_pipelines.md)
- [38_diagrama_de_atividades_de_pipelines.puml](/home/thiago/coleta_showtrials/docs/modelagem/diagramas/fontes/38_diagrama_de_atividades_de_pipelines.puml)
- [38_diagrama_de_atividades_de_pipelines.svg](/home/thiago/coleta_showtrials/docs/modelagem/diagramas/renderizados/38_diagrama_de_atividades_de_pipelines.svg)

### 9.1.1 Casos de uso com visualizacao renderizada

- [08_diagrama_casos_de_uso_sistema_atual.svg](/home/thiago/coleta_showtrials/docs/modelagem/diagramas/renderizados/08_diagrama_casos_de_uso_sistema_atual.svg)
- [09_diagrama_casos_de_uso_transicao_arquitetural.svg](/home/thiago/coleta_showtrials/docs/modelagem/diagramas/renderizados/09_diagrama_casos_de_uso_transicao_arquitetural.svg)
- [10_diagrama_casos_de_uso_sistema_alvo.svg](/home/thiago/coleta_showtrials/docs/modelagem/diagramas/renderizados/10_diagrama_casos_de_uso_sistema_alvo.svg)
- [11_diagrama_casos_de_uso_cenarios_especializados.svg](/home/thiago/coleta_showtrials/docs/modelagem/diagramas/renderizados/11_diagrama_casos_de_uso_cenarios_especializados.svg)

### 9.2 Artefatos ainda preparatórios

- [33_diagrama_de_classes_da_engine.md](/home/thiago/coleta_showtrials/docs/modelagem/diagramas/especificacoes/33_diagrama_de_classes_da_engine.md)
- [35_diagrama_de_pacotes.md](/home/thiago/coleta_showtrials/docs/modelagem/diagramas/especificacoes/35_diagrama_de_pacotes.md)
- [36_diagrama_de_sequencia_fluxos_atuais.md](/home/thiago/coleta_showtrials/docs/modelagem/diagramas/especificacoes/36_diagrama_de_sequencia_fluxos_atuais.md)
- [37_diagrama_de_sequencia_fluxos_da_engine.md](/home/thiago/coleta_showtrials/docs/modelagem/diagramas/especificacoes/37_diagrama_de_sequencia_fluxos_da_engine.md)
- [39_diagrama_de_estados_da_execucao_de_pipeline.md](/home/thiago/coleta_showtrials/docs/modelagem/diagramas/especificacoes/39_diagrama_de_estados_da_execucao_de_pipeline.md)

## 10. Padrões de projeto

- [40_analise_de_padroes_de_projeto_existentes.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/padroes/40_analise_de_padroes_de_projeto_existentes.md)
- [41_padroes_de_projeto_para_a_evolucao_da_engine.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/padroes/41_padroes_de_projeto_para_a_evolucao_da_engine.md)
- [42_mapa_de_padroes_por_modulo.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/padroes/42_mapa_de_padroes_por_modulo.md)
- [43_riscos_de_overengineering_e_tradeoffs.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/padroes/43_riscos_de_overengineering_e_tradeoffs.md)

## 11. Fechamento crítico da frente

- [44_revisao_critica_final_da_frente.md](/home/thiago/coleta_showtrials/docs/modelagem/revisao/44_revisao_critica_final_da_frente.md)
- [45_dividas_tecnicas_e_documentais_da_frente.md](/home/thiago/coleta_showtrials/docs/modelagem/revisao/45_dividas_tecnicas_e_documentais_da_frente.md)
- [46_sintese_executiva_da_frente.md](/home/thiago/coleta_showtrials/docs/modelagem/revisao/46_sintese_executiva_da_frente.md)
- [47_indice_geral_da_frente_de_modelagem.md](/home/thiago/coleta_showtrials/docs/modelagem/revisao/47_indice_geral_da_frente_de_modelagem.md)

## 12. Uso recomendado deste índice

Para revisão crítica humana, a ordem recomendada é:

1. requisitos e insumos
2. casos de uso
3. ponte para arquitetura
4. `4+1`
5. C4
6. UML complementar
7. padrões
8. fechamento crítico

## 13. Politica transversal relacionada

- [politica_de_diagramas_versionaveis.md](/home/thiago/coleta_showtrials/docs/projeto/politica_de_diagramas_versionaveis.md)
