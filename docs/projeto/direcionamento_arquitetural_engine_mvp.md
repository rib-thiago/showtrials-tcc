## Direcionamento Arquitetural para MVP da Engine de Pipeline

---

# 1. Diagnóstico Consolidado do Estado Atual

## 1.1 Natureza do sistema atual

O sistema atual é:

* Documento-cêntrico
* Orientado a persistência
* Baseado em casos de uso imperativos
* Estruturado em busca → mutação → salvar

Fluxo real:

```
Banco → Documento → Mutação → Banco
```

Características:

* `Documento` é entidade rica e mutável
* Use cases dependem de `RepositorioDocumento`
* Processamento e persistência estão acoplados
* Não existe modelo de execução de fluxo

Conclusão:

O sistema atual é uma aplicação CRUD enriquecida, não uma engine de processamento.

---

# 2. Objetivo Arquitetural

Evoluir para:

> Plataforma modular de processamento configurável via YAML/JSON.

Características desejadas:

* Múltiplas fontes (scrape, OCR, PDF, etc.)
* Múltiplos processadores (classificação, NLP, tradução)
* Múltiplos destinos (SQLite, Mongo, relatórios, grafos)
* Execução declarativa
* Persistência opcional
* Análises globais
* Reprodutibilidade e versionamento

Isso caracteriza uma engine de pipeline.

---

# 3. Decisão Arquitetural Final

## Modelo escolhido: Pipeline baseado em Contexto de Execução

### Estrutura conceitual

```
Source → Contexto → Processor → Contexto → Sink
```

### Estrutura refinada do ContextoPipeline

```python
class ContextoPipeline:
    documentos: Iterable[Documento]
    artefatos: Dict[str, Any]
    resultados_agregados: Dict[str, Any]
    estado_execucao: Dict[str, Any]
```

Decisões importantes:

* `Iterable[Documento]` em vez de `List` (suporte futuro a streaming)
* Configuração não pertence ao contexto
* Persistência é responsabilidade exclusiva de sinks
* Contexto representa estado de execução, não intenção

---

# 4. Separação Fundamental Necessária

## 4.1 Transformadores Puros

Devem existir funções ou classes que façam apenas:

```
Documento → Documento
ou
Contexto → Contexto
```

Sem:

* Acesso a repositório
* ID obrigatório
* Persistência
* Efeitos colaterais

## 4.2 Orquestração Externa

Use cases atuais passam a ser adaptadores:

```
buscar → transformar → salvar
```

Isso permite:

* Compatibilidade retroativa
* Reuso no pipeline
* Migração incremental

---

# 5. Versionamento de Pipeline (Pré-MVP Estrutural)

Se pipelines serão:

* Criados
* Salvos
* Reexecutados

Então precisamos de:

## Entidade Pipeline

```python
class Pipeline:
    id: UUID
    nome: str
    versao: int
    configuracao: dict
    criado_em: datetime
```

## Estratégia MVP

* Versionamento numérico incremental
* Configuração imutável por versão
* Reexecução determinística

Modelo git-like não é necessário no MVP.

---

# 6. Escopo Definido do MVP

O MVP deve conter:

1. Estrutura básica de `ContextoPipeline`
2. Executor linear de pipeline
3. Sistema mínimo de plugins:

   * Source
   * Processor
   * Sink
4. YAML loader
5. Separação clara entre transformação e persistência
6. Versionamento simples de pipelines

Não deve conter ainda:

* Sistema complexo de discovery automático
* Execução distribuída
* Execução paralela
* Engine assíncrona
* Versionamento git-like

---

# 7. Próximos Passos Programados

## Fase 1 — Consolidação Estrutural

* Definir estrutura de pacotes da engine
* Definir contrato formal de Plugin
* Definir executor mínimo

## Fase 2 — Refatoração de Base

* Extrair 1 processador puro (ex: classificador)
* Adaptar caso de uso atual para usar transformador puro
* Validar execução manual

## Fase 3 — Motor de Pipeline

* Implementar executor linear
* Implementar carregamento YAML
* Criar primeiro pipeline real

## Fase 4 — Versionamento

* Criar entidade `Pipeline`
* Criar repositório de pipelines
* Salvar configuração com versão incremental

---

# 8. Situação Arquitetural Atual

Estamos em:

> Fase de definição estrutural pré-implementação do MVP.

Decisões já consolidadas:

* Pipeline baseado em Contexto
* Streaming futuro suportado
* Persistência via sink
* YAML declarativo
* Versionamento numérico
* Separação entre execução e configuração

Arquitetura está coerente.

---

# 9. Próximo Movimento

Agora podemos:

1. Discutir formalmente seu fluxo de trabalho.
2. Formalizar um modelo de colaboração estruturado.
3. Em seguida, analisar milestones e issues do repositório.
4. Ajustar roadmap para alinhar com o MVP da engine.

Pode me mostrar seus documentos de fluxo de trabalho.
