# C4 — Modelo de Containers

## 1. Objetivo do documento

Este documento registra o **modelo de containers** da frente segundo o **C4 Model**.

Seu objetivo é mostrar:

- os principais containers ou unidades executáveis/persistentes da solução
- como eles se relacionam
- como a arquitetura atual e a evolução futura podem ser lidas nesse nível

## 2. Base de evidência utilizada

Esta visão se apoia principalmente em:

- [22_visao_logica_4mais1.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/visao_4mais1/22_visao_logica_4mais1.md)
- [23_visao_de_desenvolvimento_4mais1.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/visao_4mais1/23_visao_de_desenvolvimento_4mais1.md)
- [24_visao_de_processo_4mais1.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/visao_4mais1/24_visao_de_processo_4mais1.md)
- [25_visao_fisica_4mais1.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/visao_4mais1/25_visao_fisica_4mais1.md)
- [28_c4_modelo_de_contexto.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/c4/28_c4_modelo_de_contexto.md)
- estrutura atual do código em `src/`

## 3. Escopo do modelo de containers

Neste nível, o interesse principal é identificar:

- aplicações executáveis
- armazenamentos relevantes
- unidades principais de processamento

Sem ainda descer ao detalhe interno de componentes.

## 4. Containers identificados

Com base no estado atual do projeto e na direção da frente, os containers mais relevantes são:

- Aplicação CLI
- Aplicação Web
- Núcleo da aplicação ShowTrials
- Banco de dados SQLite
- Executor futuro de pipeline em background, quando aplicável

Além deles, aparecem fora da fronteira:

- serviços externos especializados
- fontes externas documentais

## 5. Descrição dos containers

## 5.1 Aplicação CLI

### Papel

Fornecer operação textual e mais fina do sistema para o usuário.

### Evidência atual

Presente em `src/interface/cli/`.

### Relações principais

- consome o núcleo da aplicação
- acessa os casos de uso do sistema atual
- deve permanecer consumidor legítimo da engine futura

## 5.2 Aplicação Web

### Papel

Fornecer acesso visual e mais leve ao sistema para o usuário.

### Evidência atual

Presente em `src/interface/web/`.

### Relações principais

- consome o núcleo da aplicação
- expõe funcionalidades atuais via rotas e templates
- deve acomodar, progressivamente, operações ligadas à engine

## 5.3 Núcleo da aplicação ShowTrials

### Papel

Concentrar:

- casos de uso
- orquestração
- domínio
- integrações de infraestrutura
- introdução progressiva da engine de pipeline

### Evidência atual

Presente principalmente em:

- `src/application/`
- `src/domain/`
- `src/infrastructure/`

### Relações principais

- atende CLI e Web
- usa o banco SQLite
- consome serviços externos
- pode, no futuro, acionar executor em background

## 5.4 Banco de dados SQLite

### Papel

Persistir documentos, traduções e demais artefatos persistentes do sistema atual, além de servir de base para evolução posterior.

### Evidência atual

Presente em:

- `src/infrastructure/persistence/`

### Relações principais

- é usado pelo núcleo da aplicação
- representa o principal armazenamento persistente já materializado

## 5.5 Executor futuro de pipeline em background

### Papel

Executar pipelines fora do fluxo síncrono principal quando a arquitetura evoluir para isso.

### Evidência atual

Ainda não existe como container materializado, mas é compatível com:

- drivers arquiteturais
- visão de processo
- visão física

### Relações principais

- recebe trabalho do núcleo da aplicação
- executa fluxos configurados
- pode persistir ou devolver resultados ao núcleo

## 6. Relações entre containers

As relações principais deste modelo são:

1. CLI consome o núcleo da aplicação.
2. Web consome o núcleo da aplicação.
3. núcleo da aplicação lê e escreve no SQLite.
4. núcleo da aplicação consome serviços externos especializados.
5. no futuro, núcleo da aplicação pode delegar execuções ao executor em background.

## 7. Leitura por estágio arquitetural

## 7.1 Sistema atual

Predominam:

- CLI
- Web
- núcleo da aplicação
- SQLite

## 7.2 Transição

O núcleo da aplicação começa a acumular responsabilidades de:

- configuração de pipeline
- validação de execução
- separação entre fluxo atual e engine futura

## 7.3 Sistema-alvo

O modelo de containers passa a admitir:

- interfaces de entrada
- núcleo da aplicação com engine consolidada
- armazenamento persistente
- possível executor desacoplado para background

## 8. Inferências adotadas

As principais inferências adotadas neste modelo foram:

- o núcleo da aplicação foi tratado como container único neste estágio, porque a engine ainda não existe como unidade física separada no repositório
- SQLite foi mantido como armazenamento principal explícito por aderência ao estado atual do projeto
- o executor em background foi incluído como container futuro compatível, e não como realidade já implementada

## 9. Dívidas técnicas registradas

Permanecem como pontos futuros:

- decidir quando a engine deixará de ser apenas parte do núcleo da aplicação e passará a justificar container próprio
- decidir a futura topologia de persistência para pipelines e produtos derivados
- decidir se haverá API própria ou outro container de acesso programático mais explícito

## 10. Próximos passos

Os próximos passos recomendados são:

- abrir o modelo de componentes do C4
- depois focalizar o modelo de código em recorte bem escolhido
