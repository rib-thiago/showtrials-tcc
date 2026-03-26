# Diagrama de Classes de Domínio

## 1. Objetivo do documento

Este documento registra o recorte e a leitura do **diagrama de classes de domínio** da frente.

Seu objetivo é identificar:

- classes de domínio já materializadas
- relações principais entre entidades, value objects e contratos
- lacunas entre o domínio atual e o domínio futuro da engine

Nesta estabilização, o diagrama correspondente foi **materializado em PlantUML**, e este documento passa a funcionar como leitura explicativa e delimitadora do seu recorte.

## 2. Base de evidência utilizada

- `src/domain/entities/documento.py`
- `src/domain/entities/traducao.py`
- `src/domain/value_objects/`
- `src/domain/interfaces/`
- [21_glossario_arquitetural_e_tecnico.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/ponte/21_glossario_arquitetural_e_tecnico.md)
- [31_c4_modelo_de_codigo.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/c4/31_c4_modelo_de_codigo.md)
- [32_diagrama_de_classes_de_dominio.puml](../fontes/32_diagrama_de_classes_de_dominio.puml)
- [32_diagrama_de_classes_de_dominio.svg](../renderizados/32_diagrama_de_classes_de_dominio.svg)

## 3. Classes centrais do domínio atual

As classes mais centrais do domínio atual são:

- `Documento`
- `Traducao`
- `TipoDocumento`
- `AnaliseTexto`
- `NomeRusso`
- `RepositorioDocumento`
- `RepositorioTraducao`

## 4. Relações principais do domínio atual

As relações principais são:

- `Traducao` referencia um `Documento` por `documento_id`
- `RepositorioDocumento` persiste e recupera `Documento`
- `RepositorioTraducao` persiste e recupera `Traducao`
- `Documento` concentra metadados enriquecidos e serve de eixo para tradução, análise e exportação

## 5. Classes de domínio futuro já exigidas pela frente

Mesmo ainda não implementadas, a frente já exige como classes de domínio futuro:

- `Pipeline`
- `VersaoPipeline`
- `ContextoPipeline`
- `PipelineStep`

## 6. Leitura recomendada para o diagrama

O diagrama deve ser organizado em dois subconjuntos:

### 6.1 Núcleo factual atual

- `Documento`
- `Traducao`
- contratos de repositório
- value objects já existentes

### 6.2 Núcleo evolutivo futuro

- `Pipeline`
- `VersaoPipeline`
- `ContextoPipeline`
- `PipelineStep`

## 7. Inferências adotadas

- o diagrama foi tratado como ponte entre domínio atual e futuro, e não apenas como retrato do código atual
- `Documento` permanece como centro do domínio atual, ainda que esse centro seja tensionado pela futura engine

## 8. Dívidas técnicas registradas

- estabilização conceitual definitiva de `Documento`
- relação futura entre `Documento`, `Colecao` e produtos derivados
- modelagem concreta de estados e resultados revisados por humano

## 9. Situação do artefato nesta estabilização

- o diagrama de classes de domínio foi materializado em `PlantUML`
- o recorte mantém separação explícita entre núcleo factual atual e núcleo evolutivo futuro
- a materialização do diagrama de classes da engine permanece em etapa posterior
