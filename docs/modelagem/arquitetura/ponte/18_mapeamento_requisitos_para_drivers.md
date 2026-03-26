# Mapeamento de Requisitos para Drivers

## 1. Objetivo do documento

Este documento torna explícita a derivação dos **drivers arquiteturais** a partir da base de requisitos da frente.

Seu objetivo é responder:

- quais blocos de requisitos sustentam cada driver
- quais drivers derivam diretamente dos requisitos
- em que pontos a derivação depende de interpretação complementar

## 2. Base de evidência utilizada

Este documento se apoia principalmente em:

- [03_documento_de_requisitos.md](/home/thiago/coleta_showtrials/docs/modelagem/requisitos/principais/03_documento_de_requisitos.md)
- [17_drivers_arquiteturais.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/ponte/17_drivers_arquiteturais.md)
- matrizes e especificações de casos de uso já produzidas

## 3. Critério de mapeamento adotado

O mapeamento usa como referência:

- blocos funcionais `12.x`
- blocos não funcionais `13.x`
- requisitos de transição `14`
- restrições e priorização quando relevantes

Nesta etapa, os vínculos são classificados de forma qualitativa em:

- `Direto`
- `Forte`
- `Interpretativo`

## 4. Matriz principal

| Driver arquitetural | Requisitos de origem | Força do vínculo | Justificativa |
|---|---|---|---|
| Evolução incremental sem reescrita total | `13.6`, `14`, `15` | Direto | o documento de requisitos explicita incrementalidade, continuidade e não reescrita |
| Preservação de CLI e Web como interfaces relevantes | `12.9`, `13.8`, `14` | Direto | as interfaces são mantidas como partes relevantes da solução e da transição |
| Configurabilidade explícita dos fluxos de trabalho | `12.6`, `13.5`, `17.3` | Direto | configuração reproduzível de pipeline aparece como núcleo funcional e prioridade do MVP |
| Separação entre transformação e persistência | `12.8`, `14`, `17.2` | Forte | requisitos e transição já apontam a separação, embora a formulação arquitetural venha do direcionamento complementar |
| Modularidade orientada a sources, processors e sinks | `12.6`, `12.7`, `12.8`, `13.3` | Forte | a composição configurável e a separação funcional dos blocos indicam a necessidade dessas abstrações |
| Suporte a múltiplos tipos de entrada documental | `12.1`, `11`, `17.4` | Direto | múltiplas formas de entrada são explicitamente esperadas no sistema-alvo |
| Suporte a produtos derivados e resultados persistíveis | `12.2`, `12.4`, `12.5`, `12.8` | Direto | documentos, traduções, análises e produtos derivados aparecem repetidamente como persistíveis |
| Execução não bloqueante e possibilidade de background | `12.7`, `13.2`, `17.4` | Direto | execução não bloqueante aparece como expectativa explícita e desejável posterior |
| Rastreabilidade entre resultados automáticos e intervenção humana | `12.4`, `12.5`, `13.7` | Interpretativo | o requisito não formula isso literalmente, mas a frente consolidou essa necessidade a partir do domínio e dos casos de uso |
| Ergonomia do fluxo de trabalho como força arquitetural | `13.1`, `13.5`, `7.2` | Forte | usabilidade, configurabilidade e motivação arquitetural apontam a ergonomia como força real |
| Generalização sem apagar a especialização histórica | `3`, `7`, `11`, `13.6` | Interpretativo | o requisito integrado sustenta a continuidade e a generalização, e a leitura da frente explicita a tensão entre ambas |
| Documentação forte e rastreabilidade como requisito de arquitetura do projeto | `13.7`, `15` | Direto | documentação e rastreabilidade aparecem como exigências explícitas da frente |

## 5. Leitura interpretativa da matriz

### 5.1 Drivers mais diretamente ancorados em requisitos explícitos

Os drivers mais diretamente sustentados pela base de requisitos são:

- evolução incremental
- preservação de interfaces
- configurabilidade explícita
- múltiplas entradas
- produtos derivados persistíveis
- execução não bloqueante
- documentação e rastreabilidade

Esses drivers já podem ser tratados como base firme para os próximos artefatos arquiteturais.

### 5.2 Drivers que dependem de leitura complementar da frente

Alguns drivers, embora muito relevantes, dependem de interpretação complementar dos artefatos produzidos:

- rastreabilidade entre automático e humano
- ergonomia do fluxo de trabalho como força arquitetural
- generalização sem apagar a especialização histórica

Esses drivers não são arbitrários, mas sua formulação depende mais da leitura integrada da frente do que de uma sentença única do documento de requisitos.

### 5.3 Papel dos requisitos de transição

Os requisitos de transição (`14`) têm papel particularmente importante porque:

- sustentam drivers de compatibilidade evolutiva
- sustentam separação gradual entre transformação e persistência
- impedem que a arquitetura futura seja pensada como ruptura total

## 6. Inferências adotadas

As principais inferências adotadas neste documento foram:

- drivers já formalizados em [17_drivers_arquiteturais.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/ponte/17_drivers_arquiteturais.md) foram reconectados à base de requisitos em nível de bloco, e não de requisito unitário
- alguns drivers foram classificados como `Interpretativo` para evitar declarar como explícito aquilo que, na verdade, emerge da síntese da frente

## 7. Dívidas técnicas registradas

Permanecem como pontos futuros:

- eventual renumeração dos requisitos em nível atômico
- eventual repetição desta matriz com granularidade mais fina
- revisão futura da força relativa dos vínculos quando a arquitetura estiver mais madura

## 8. Próximos passos

Os próximos passos recomendados são:

- abrir o mapeamento de casos de uso para blocos arquiteturais
- usar as duas matrizes de ponte como preparação direta para os artefatos 4+1 e C4
