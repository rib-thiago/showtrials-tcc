# Matriz de Casos de Uso para Diagramas e Insumos

## 1. Objetivo do documento

Este documento consolida a segunda matriz de rastreabilidade da frente de casos de uso, conectando:

- casos de uso
- diagramas
- insumos
- artefatos textuais já produzidos

Seu objetivo é tornar explícito onde cada caso de uso aparece, em que nível foi tratado e quais documentos da frente dão sustentação à sua modelagem atual.

## 2. Base de evidência utilizada

Esta matriz se apoia principalmente em:

- [07_casos_de_uso_iniciais.md](/home/thiago/coleta_showtrials/docs/modelagem/07_casos_de_uso_iniciais.md)
- [08_diagrama_casos_de_uso_sistema_atual.md](/home/thiago/coleta_showtrials/docs/modelagem/08_diagrama_casos_de_uso_sistema_atual.md)
- [09_diagrama_casos_de_uso_transicao_arquitetural.md](/home/thiago/coleta_showtrials/docs/modelagem/09_diagrama_casos_de_uso_transicao_arquitetural.md)
- [10_diagrama_casos_de_uso_sistema_alvo.md](/home/thiago/coleta_showtrials/docs/modelagem/10_diagrama_casos_de_uso_sistema_alvo.md)
- [11_diagrama_casos_de_uso_cenarios_especializados.md](/home/thiago/coleta_showtrials/docs/modelagem/11_diagrama_casos_de_uso_cenarios_especializados.md)
- [13_especificacoes_textuais_de_casos_de_uso_prioritarios.md](/home/thiago/coleta_showtrials/docs/modelagem/13_especificacoes_textuais_de_casos_de_uso_prioritarios.md)
- [14_especificacoes_textuais_de_casos_de_uso_secundarios.md](/home/thiago/coleta_showtrials/docs/modelagem/14_especificacoes_textuais_de_casos_de_uso_secundarios.md)
- insumos `03` a `06` em `docs/modelagem/insumos/`

## 3. Critério de rastreabilidade adotado

Nesta etapa, cada caso de uso é relacionado a:

- o diagrama em que aparece
- os insumos que mais o sustentam
- o artefato textual em que foi especificado, quando aplicável
- observações de cobertura ou maturidade

## 4. Matriz principal

| Caso de uso | Plano | Diagrama(s) | Insumos mais relevantes | Artefato textual | Observação |
|---|---|---|---|---|---|
| `ListarDocumentos` | Sistema atual | `08` | `04`, `05`, `06` | `14` | bem sustentado por fases e código |
| `ObterDocumento` | Sistema atual | `08` | `03`, `04`, `05`, `06` | `13` | caso-hub do sistema atual |
| `ClassificarDocumento` | Sistema atual | `08` | `04`, `06` | `14` | caso de preparação/enriquecimento |
| `TraduzirDocumento` | Sistema atual | `08` | `03`, `04`, `06` | `13` | caso autônomo com forte base factual |
| `ListarTraducoes` | Sistema atual | `08` | `03`, `06` | `14` | autônomo, mas frequentemente acionado a partir de `ObterDocumento` |
| `ObterEstatisticas` | Sistema atual | `08` | `04`, `06` | `14` | permanece com granularidade em aberto |
| `AnalisarDocumento` | Sistema atual | `08` | `03`, `04`, `06` | `13` | caso relevante para a ponte com arquitetura |
| `AnalisarAcervo` | Sistema atual | `08` | `04`, `06` | `14` | complementar à análise pontual de documento |
| `ExportarDocumento` | Sistema atual | `08` | `04`, `06` | `14` | orientado a saída/entrega |
| `GerarRelatorio` | Sistema atual | `08` | `04`, `06` | `14` | caso de consolidação ligado a estatísticas |
| `ConfigurarPipeline` | Transição | `09` | `03`, `04`, `05`, `06` | `13` | caso central da virada arquitetural |
| `ExecutarPipeline` | Transição | `09` | `04`, `05`, `06` | `14` | permanece como caso de transição, não totalmente fundido ao sistema-alvo |
| `CriarPipeline` | Sistema-alvo | `10` | `03`, `04`, `06` | `14` | base inicial distinta de configurar |
| `ListarPipelines` | Sistema-alvo | `10` | `04`, `06` | `14` | bastante estável e factual no roadmap |
| `EditarPipeline` | Sistema-alvo | `10` | `04`, `06` | `14` | ajusta pipeline persistido |
| `ExecutarPipelineDocumental` | Sistema-alvo | `10`, `11` | `03`, `04`, `05`, `06` | `13` | caso geral que sustenta especializações |
| `PersistirProdutosDerivados` | Sistema-alvo | `10` | `03`, `05`, `06` | `14` | relação final com execução ainda em aberto |
| `RevisarTraducao` | Sistema-alvo | `10` | `03`, `04`, `06` | `13` | posição final ainda parcialmente aberta |
| `ProcessarPDFcomOCR` | Especializado | `11` | `03`, `05`, `06` | `14` | especialização de execução documental |
| `ExecutarPipelineDeTraducao` | Especializado | `11` | `03`, `05`, `06` | `14` | especialização orientada a tradução |
| `ExecutarPipelineDeRaspagemEAnalise` | Especializado | `11` | `03`, `05`, `06` | `14` | especialização híbrida de obtenção e análise |
| `ExecutarPipelinePorID` | Especializado | `11` | `05`, `06` | `14` | posição final ainda é dívida técnica |
| `ConsultarResultadosDePipeline` | Especializado | `11` | `05`, `06` | `14` | caso lateral, não tratado como especialização de execução |

## 5. Leitura interpretativa da matriz

### 5.1 Cobertura plena do conjunto principal

Todos os casos de uso consolidados em [07_casos_de_uso_iniciais.md](/home/thiago/coleta_showtrials/docs/modelagem/07_casos_de_uso_iniciais.md) já estão cobertos por:

- pelo menos um diagrama
- pelo menos um conjunto de insumos
- algum artefato textual de especificação

Isso indica que a subfrente de casos de uso atingiu um bom nível de fechamento interno.

### 5.2 Papel estrutural dos insumos `04`, `05` e `06`

Os insumos mais recorrentes na sustentação dos casos são:

- `04_mapa_de_stakeholders_atores_e_objetivos`
- `05_fronteira_do_sistema_e_recortes_de_modelagem`
- `06_mapa_inicial_de_capacidades_e_casos_de_uso_candidatos`

Isso mostra que eles de fato funcionaram como base estrutural da frente.

### 5.3 Papel do diagrama `11`

O diagrama `11` concentrou corretamente os casos especializados, evitando inflar o diagrama do sistema-alvo.

Essa decisão se mostrou metodologicamente acertada.

## 6. Limitações da matriz nesta etapa

Esta matriz ainda tem algumas limitações:

- ela não expressa níveis de maturidade diferenciados por caso além das observações textuais
- ela não mede força de evidência com uma escala formal
- ela ainda não conecta diretamente os casos de uso ao backlog de issues

## 7. Inferências adotadas

As principais inferências adotadas nesta matriz foram:

- a seleção dos “insumos mais relevantes” foi feita com base na função efetiva que cada insumo desempenhou na consolidação do caso
- os casos especializados foram vinculados prioritariamente aos insumos de fronteira e capacidades, por dependerem menos de histórico factual implementado e mais de projeção controlada

## 8. Dívidas técnicas registradas

Permanecem como pontos futuros:

- eventual gradação formal de maturidade dos casos
- eventual ligação desta matriz ao backlog de issues
- eventual criação de uma matriz mais fina ligando casos de uso a fases e código-fonte

## 9. Próximos passos

Os próximos passos recomendados são:

- considerar a subfrente de casos de uso suficientemente fechada para avançar
- abrir o bloco de ponte formal entre requisitos, casos de uso e arquitetura
- começar por `17_drivers_arquiteturais.md`
