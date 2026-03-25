# Visão de Desenvolvimento — 4+1

## 1. Objetivo do documento

Este documento registra a **visão de desenvolvimento** da arquitetura da frente, no contexto do modelo **4+1**.

Seu objetivo é descrever como a solução se organiza do ponto de vista de:

- módulos e camadas
- responsabilidades de manutenção
- direção das dependências
- evolução incremental do código

## 2. Base de evidência utilizada

Esta visão se apoia principalmente em:

- [20_decisoes_arquiteturais_iniciais.md](/home/thiago/coleta_showtrials/docs/modelagem/20_decisoes_arquiteturais_iniciais.md)
- [21_glossario_arquitetural_e_tecnico.md](/home/thiago/coleta_showtrials/docs/modelagem/21_glossario_arquitetural_e_tecnico.md)
- [22_visao_logica_4mais1.md](/home/thiago/coleta_showtrials/docs/modelagem/22_visao_logica_4mais1.md)
- [docs/projeto/analise_arquitetural.md](/home/thiago/coleta_showtrials/docs/projeto/analise_arquitetural.md)
- [docs/projeto/direcionamento_arquitetural_engine_mvp.md](/home/thiago/coleta_showtrials/docs/projeto/direcionamento_arquitetural_engine_mvp.md)
- estrutura atual do código em `src/`

## 3. Escopo da visão de desenvolvimento

Esta visão trata da organização do sistema para desenvolvimento e manutenção.

Ela não descreve:

- fluxos de execução em runtime
- deployment
- containers C4
- sequência detalhada de mensagens

Ela descreve:

- como o código e os módulos devem se organizar
- como preservar a arquitetura limpa durante a evolução
- onde a engine futura se encaixa na estrutura atual

## 4. Estrutura de desenvolvimento consolidada

Com base no estado atual do projeto e na direção da frente, a visão de desenvolvimento pode ser entendida em seis grandes áreas:

- Interfaces
- Aplicação
- Domínio
- Infraestrutura
- Engine de pipeline
- Documentação e rastreabilidade

## 5. Áreas de organização do desenvolvimento

## 5.1 Interfaces

### Papel

Abrigar os pontos de interação com usuário e canais externos de operação.

### Elementos típicos

- CLI
- Web
- APIs futuras, quando existirem

### Regras de desenvolvimento

- não devem concentrar lógica de negócio
- devem consumir orquestração da camada de aplicação
- devem permanecer intercambiáveis na maior medida possível

## 5.2 Aplicação

### Papel

Abrigar os casos de uso, adaptadores de transição e orquestrações que coordenam domínio, infraestrutura e engine.

### Elementos típicos

- casos de uso atuais
- adaptadores legados
- coordenação entre comandos e operações documentais
- pontos de entrada para criação/configuração/execução de pipeline

### Regras de desenvolvimento

- depende de contratos do domínio, não de implementações concretas
- concentra orquestração, não regras fundamentais do domínio
- deve ser refatorada incrementalmente, e não substituída de uma vez

## 5.3 Domínio

### Papel

Abrigar entidades, value objects, contratos e conceitos estáveis do problema.

### Elementos típicos

- documento
- pipeline
- step
- contratos de source/processor/sink
- value objects e estados relevantes do domínio

### Regras de desenvolvimento

- permanecer livre de framework na maior medida possível
- não depender de infraestrutura
- concentrar semântica estável e invariantes relevantes

## 5.4 Infraestrutura

### Papel

Abrigar persistência, integrações externas, serviços concretos e mecanismos técnicos de suporte.

### Elementos típicos

- repositórios
- SQLite atual e futuros mecanismos de persistência
- tradutor externo
- OCR
- service registry
- integrações com fontes externas

### Regras de desenvolvimento

- implementar contratos da aplicação e do domínio
- permanecer substituível
- evitar invadir a semântica do domínio

## 5.5 Engine de pipeline

### Papel

Abrigar a nova capacidade estrutural de configuração, catálogo e execução de pipelines, articulando contexto de execução, steps e persistência configurável.

### Elementos típicos

- configuração de pipeline
- executor de pipeline
- contexto de execução
- versionamento simples
- validação de configuração

### Regras de desenvolvimento

- nascer de forma incremental ao lado da estrutura atual
- não apagar de imediato os casos de uso existentes
- servir de ponto de convergência para a evolução futura da plataforma

## 5.6 Documentação e rastreabilidade

### Papel

Abrigar a camada documental que sustenta a governança da evolução.

### Elementos típicos

- documentos de modelagem
- rodadas
- rastreabilidade
- artefatos arquiteturais

### Regras de desenvolvimento

- a documentação deve evoluir em paralelo com a modelagem
- decisões e inferências devem permanecer registradas

## 6. Direção das dependências

Com base no que a frente consolidou até aqui, a direção desejada das dependências permanece:

1. interfaces dependem da aplicação
2. aplicação depende do domínio
3. infraestrutura implementa contratos consumidos pela aplicação e pelo domínio
4. engine de pipeline deve se integrar à aplicação e ao domínio sem inverter essa direção

Essa direção é especialmente importante para preservar:

- testabilidade
- modularidade
- evolução incremental sem colapso arquitetural

## 7. Estratégia de evolução do código

A visão de desenvolvimento da frente pressupõe uma estratégia de evolução em três movimentos coexistentes:

### 7.1 Preservação do núcleo atual

O sistema atual não é descartado. Seus módulos continuam válidos como base factual e como ponto de adaptação.

### 7.2 Extração progressiva de responsabilidades

Responsabilidades hoje muito acopladas devem ser gradualmente separadas, especialmente:

- transformação versus persistência
- execução versus configuração
- casos de uso legados versus executor de pipeline

### 7.3 Introdução controlada da engine

A engine deve surgir como nova área de desenvolvimento, sem exigir reestruturação destrutiva imediata do projeto inteiro.

## 8. Leitura da visão de desenvolvimento por estágio do sistema

### 8.1 Sistema atual

Predominância de:

- interfaces
- aplicação baseada em casos de uso imperativos
- infraestrutura acoplada em vários pontos da orquestração

### 8.2 Transição

Introdução de:

- adaptadores
- configuração de pipeline
- executor mínimo
- separação crescente de responsabilidades

### 8.3 Sistema-alvo

Predominância futura de:

- catálogo/configuração de pipeline
- executor de pipeline
- processamento documental modular
- integração explícita entre engine, domínio e infraestrutura

## 9. Inferências adotadas

As principais inferências adotadas nesta visão foram:

- a engine de pipeline foi tratada como área própria de desenvolvimento, e não apenas como detalhe dentro da aplicação atual
- documentação e rastreabilidade foram mantidas como parte da visão de desenvolvimento por causa da governança e da natureza acadêmica do projeto
- a separação em camadas do sistema atual foi preservada como eixo de continuidade, não apenas como herança do passado

## 10. Dívidas técnicas registradas

Permanecem como pontos futuros:

- definir com mais precisão a futura estrutura de pacotes da engine
- decidir quando e como a engine ganhará um espaço explícito no código sem conflitar com o legado
- decidir o papel futuro do service registry diante do crescimento da engine

## 11. Próximos passos

Os próximos passos recomendados são:

- abrir a visão de processo do 4+1
- depois a visão física
- em seguida a visão de casos de uso e a síntese 4+1
