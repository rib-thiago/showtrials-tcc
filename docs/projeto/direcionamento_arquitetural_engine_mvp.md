# Direcionamento Arquitetural do MVP da Engine

## Objetivo

Este documento consolida o direcionamento arquitetural do MVP da engine de pipeline.

Seu papel e:

- sintetizar o diagnostico do sistema atual;
- registrar a decisao arquitetural central do MVP;
- delimitar o escopo minimo da primeira evolucao estrutural da engine;
- orientar backlog e modelagem com um nucleo tecnico mais forte do que a visao ampla e o roadmap geral.

## Diagnostico do Sistema Atual

O sistema atual pode ser lido como:

- documento-centrico;
- orientado a persistencia;
- baseado em casos de uso imperativos;
- estruturado em busca, mutacao e persistencia.

Esquema sintetico:

```text
Banco -> Documento -> Mutacao -> Banco
```

Isso implica:

- `Documento` como entidade rica e mutavel;
- forte dependencia de repositorios documentais;
- acoplamento entre processamento e persistencia;
- ausencia de um modelo explicito de execucao de fluxo.

Em termos arquiteturais, isso caracteriza uma aplicacao CRUD enriquecida, e nao ainda uma engine de pipeline.

## Objetivo Arquitetural do MVP

O objetivo do MVP e abrir uma transicao controlada para uma engine de processamento configuravel, com:

- configuracao externa declarativa;
- multiplas fontes, processadores e destinos;
- execucao orientada por fluxo;
- separacao mais clara entre transformacao e persistencia;
- reprodutibilidade e versionamento simples.

Essa formulacao ainda nao descreve a plataforma completa, mas o nucleo estrutural minimo da engine.

## Decisao Arquitetural Central

A decisao central consolidada para o MVP e:

- adotar um pipeline baseado em contexto de execucao.

Esquema conceitual:

```text
Source -> Contexto -> Processor -> Contexto -> Sink
```

Estrutura refinada de referencia:

```python
class ContextoPipeline:
    documentos: Iterable[Documento]
    artefatos: Dict[str, Any]
    resultados_agregados: Dict[str, Any]
    estado_execucao: Dict[str, Any]
```

Consequencias principais dessa decisao:

- `Iterable[Documento]` e preferivel a `List` para manter abertura futura a streaming;
- configuracao nao pertence ao contexto;
- persistencia deve ser responsabilidade de `Sink`;
- o contexto representa estado de execucao, e nao intencao de configuracao.

## Separacoes Fundamentais

### Transformacao e persistencia

Transformacao e persistencia devem ser separadas.

Isso significa que funcoes ou classes de transformacao devem operar como:

```text
Documento -> Documento
Contexto -> Contexto
```

Sem:

- acesso direto a repositorio;
- persistencia embutida;
- dependencia desnecessaria de identificadores de armazenamento;
- efeitos colaterais que confundam processamento com salvamento.

### Configuracao e execucao

Configuracao de pipeline e execucao de pipeline devem permanecer como responsabilidades distintas.

Essa separacao evita colapsar:

- catalogo e definicao de pipeline;
- estado de execucao;
- armazenamento de configuracao;
- orquestracao operacional.

### Adaptacao incremental dos casos de uso atuais

Os casos de uso atuais devem ser tratados como base de migracao incremental.

Formula resumida:

```text
buscar -> transformar -> salvar
```

Isso permite:

- compatibilidade retroativa;
- reuso de transformadores mais puros;
- migracao gradual para o modelo de pipeline.

## Versionamento de Pipeline no MVP

Se pipelines puderem ser criados, salvos e reexecutados, o MVP precisa de versionamento simples.

Estrutura de referencia:

```python
class Pipeline:
    id: UUID
    nome: str
    versao: int
    configuracao: dict
    criado_em: datetime
```

Estrategia adotada para o MVP:

- versionamento numerico incremental;
- configuracao imutavel por versao;
- reexecucao deterministica;
- sem necessidade de modelo git-like neste primeiro momento.

## Escopo do MVP

O MVP deve conter:

1. estrutura basica de `ContextoPipeline`
2. executor linear de pipeline
3. sistema minimo de `Source`, `Processor` e `Sink`
4. carregamento por YAML
5. separacao clara entre transformacao e persistencia
6. versionamento simples de pipeline

O MVP nao deve conter ainda:

- discovery automatico mais complexo;
- execucao distribuida;
- execucao paralela;
- engine assincrona;
- versionamento git-like.

## Desdobramentos Arquiteturais Imediatos

Os desdobramentos mais imediatos deste direcionamento sao:

### Consolidacao estrutural

- definir estrutura de pacotes da engine;
- definir contratos formais do nucleo de pipeline;
- definir o executor minimo.

### Refatoracao de base

- extrair ao menos um transformador mais puro a partir de um caso atual;
- adaptar um caso de uso existente para usar essa separacao;
- validar a viabilidade da migracao incremental.

### Primeiro motor de pipeline

- implementar executor linear;
- implementar leitura de configuracao YAML;
- criar um primeiro pipeline real e controlado.

### Versionamento minimo

- criar a entidade `Pipeline`;
- definir repositorio de pipelines;
- salvar configuracao com versao incremental.

## Limites do Documento

Este documento deve ser lido como direcionamento arquitetural vivo do MVP.

Ele nao deve ser lido como:

- plataforma completa ja definida em todos os detalhes;
- prova de implementacao material desses componentes;
- substituto do backlog tecnico ativo;
- roteiro exaustivo de todas as evolucoes futuras possiveis.

Para leitura complementar:

- [roadmap_arquitetural.md](/home/thiago/coleta_showtrials/docs/projeto/roadmap_arquitetural.md) preserva o horizonte mais amplo;
- [visao_do_projeto.md](/home/thiago/coleta_showtrials/docs/projeto/visao_do_projeto.md) preserva a formulacao ampla do projeto;
- [49_conferencia_de_aderencia_ao_projeto_real.md](/home/thiago/coleta_showtrials/docs/modelagem/revisao/49_conferencia_de_aderencia_ao_projeto_real.md) ajuda a distinguir o que ja esta sustentado, o que esta backlogizado e o que ainda e hipotese.

## Documentos Relacionados

- [analise_arquitetural.md](/home/thiago/coleta_showtrials/docs/projeto/analise_arquitetural.md)
- [roadmap_arquitetural.md](/home/thiago/coleta_showtrials/docs/projeto/roadmap_arquitetural.md)
- [visao_do_projeto.md](/home/thiago/coleta_showtrials/docs/projeto/visao_do_projeto.md)
- [20_decisoes_arquiteturais_iniciais.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/ponte/20_decisoes_arquiteturais_iniciais.md)
- [49_conferencia_de_aderencia_ao_projeto_real.md](/home/thiago/coleta_showtrials/docs/modelagem/revisao/49_conferencia_de_aderencia_ao_projeto_real.md)
