# Glossário Arquitetural e Técnico

## 1. Objetivo do documento

Este documento consolida o **glossário arquitetural e técnico** da frente de modelagem.

Seu objetivo é estabilizar a linguagem que será reutilizada nos próximos artefatos, especialmente:

- visão 4+1
- C4
- UML complementar
- análises de padrões

## 2. Base de evidência utilizada

Este glossário se apoia principalmente em:

- [03_documento_de_requisitos.md](/home/thiago/coleta_showtrials/docs/modelagem/requisitos/principais/03_documento_de_requisitos.md)
- [17_drivers_arquiteturais.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/ponte/17_drivers_arquiteturais.md)
- [20_decisoes_arquiteturais_iniciais.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/ponte/20_decisoes_arquiteturais_iniciais.md)
- documentos arquiteturais prévios do projeto

## 3. Termos arquiteturais centrais

### Arquitetura limpa

Estrutura arquitetural baseada em separação clara entre camadas, dependência invertida e núcleo de domínio protegido de detalhes de framework.

### Camada de domínio

Camada responsável por entidades, value objects, regras e interfaces centrais do sistema, sem dependência direta de frameworks externos.

### Camada de aplicação

Camada responsável por orquestrar casos de uso e fluxos de trabalho a partir das interfaces do domínio.

### Camada de infraestrutura

Camada responsável por implementações concretas de persistência, serviços externos, integrações e mecanismos técnicos de suporte.

### Camada de interface

Camada responsável por interação com usuários ou sistemas externos, incluindo CLI, Web e eventuais APIs.

## 4. Termos da engine e do processamento configurável

### Pipeline

Fluxo configurável de execução composto por etapas ordenadas, ajustado ao objetivo de trabalho do usuário.

### Step

Etapa individual de um pipeline.

### Configuração de pipeline

Representação explícita dos componentes, parâmetros, entradas, saídas e contexto de um pipeline.

### Catálogo de pipelines

Conjunto de pipelines persistidos, recuperáveis, listáveis e editáveis pelo sistema.

### Execução de pipeline

Processo de orquestrar a passagem de dados e estado pelas etapas configuradas de um pipeline.

### Contexto de execução

Estrutura que transporta documentos, artefatos, resultados agregados e estado ao longo da execução de um pipeline.

### Versionamento de pipeline

Mecanismo de registrar e diferenciar configurações de pipeline ao longo do tempo, com reexecução potencialmente reprodutível.

## 5. Termos de decomposição funcional

### Source

Componente responsável por obtenção ou entrada de dados documentais.

### Processor

Componente responsável por transformação, análise ou enriquecimento de documentos ou contexto de execução.

### Sink

Componente responsável por persistência, exportação ou saída dos resultados.

### Transformador puro

Componente ou função que transforma documento ou contexto sem assumir persistência, acesso a repositório ou efeitos colaterais estruturais.

### Adaptador

Componente responsável por conectar uma interface ou implementação concreta a contratos mais estáveis do domínio ou da aplicação.

## 6. Termos de persistência e resultados

### Documento

Unidade documental central do sistema atual e principal portador de conteúdo, metadados e vínculos persistidos no legado.

Na arquitetura futura, `Documento` continua relevante, mas deixa de ser o único centro semântico do sistema, passando a coexistir com abstrações como `Colecao`, `Contexto de execução` e `Produto derivado`.

### Colecao

Agrupamento documental persistível ou analítico, formado por documentos relacionados por critério temático, operacional ou interpretativo.

### Resultado derivado

Resultado lógico produzido a partir do processamento de documentos ou coleções, independentemente de sua materialização final.

### Persistência configurável

Capacidade de controlar, conforme configuração, se e como resultados serão registrados.

### Produto derivado

Resultado adicional gerado a partir do processamento de documento ou coleção, como tradução, análise, visualização ou artefato exportado.

### Resultado automático

Resultado produzido por processamento automatizado, sem validação humana explícita posterior.

### Resultado revisado por humano

Resultado que passou por intervenção humana e deve permanecer distinguível do resultado automático de origem.

### Estado de revisão

Informação estrutural que indica se um resultado foi apenas gerado automaticamente, revisado, validado ou atualizado manualmente.

## 7. Termos de operação e execução

### Execução síncrona

Execução cujo resultado é esperado no mesmo fluxo de interação do usuário.

### Execução assíncrona

Execução deslocada do fluxo imediato de interação, com possibilidade de acompanhamento posterior.

### Execução não bloqueante

Execução que não impede o prosseguimento de outras interações ou operações do sistema.

### Job

Unidade de execução tratável como tarefa independente, especialmente útil em cenários de background, fila ou agendamento.

### Auditoria de execução

Capacidade de inspecionar etapas, estados intermediários, falhas ou intervenções ocorridas durante a execução.

## 8. Termos de modelagem e visão arquitetural

### Driver arquitetural

Força relevante que restringe ou orienta decisões arquiteturais futuras.

### Bloco arquitetural

Agrupamento intermediário de responsabilidades usado para conectar casos de uso à futura decomposição arquitetural.

### Visão 4+1

Abordagem de descrição arquitetural que organiza a arquitetura em visões lógica, de desenvolvimento, de processo, física e de casos de uso.

### C4

Modelo de descrição arquitetural baseado em níveis progressivos: contexto, contêineres, componentes e código.

### Contêiner

No C4, unidade executável ou implantável de responsabilidade arquitetural, como aplicação Web, CLI, banco ou serviço.

### Componente

No C4, subdivisão relevante dentro de um contêiner, com responsabilidade mais específica.

### Código (nível C4)

Recorte mais próximo da implementação, usado para detalhar internamente componentes específicos quando isso agrega valor real.

## 9. Termos que permanecem parcialmente abertos

### Documento

Termo central do projeto cuja formulação principal já pode ser estabilizada como unidade documental do legado, mas que ainda exige refinamento em sua relação com `Colecao`, `Contexto de execução` e resultados derivados na arquitetura futura.

### Resultado derivado vs artefato derivado

Nesta etapa, os termos podem ser usados de forma próxima. Futuramente, poderá ser útil distinguir:

- resultado lógico
- artefato material/exportado

### Revisão

O termo já é forte o suficiente para os casos de uso, mas ainda pode precisar refinamento quando a modelagem de estados, versionamento e auditoria ficar mais madura.

## 10. Dívidas técnicas registradas

Permanecem como pontos futuros:

- maior refinamento do termo `documento`
- possível distinção mais forte entre resultado, artefato e evidência analítica
- refinamento futuro do vocabulário de execução assíncrona e acompanhamento operacional

## 11. Próximos passos

Os próximos passos recomendados são:

- usar este glossário como referência terminológica para a visão 4+1
- iniciar a próxima etapa com `22_visao_logica_4mais1.md`
