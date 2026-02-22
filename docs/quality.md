# Pipeline de Qualidade

Este projeto adota **Taskipy como fonte única de verdade** para o pipeline de qualidade local e no CI, em conformidade com o **Quality Flow v2.0**.

## Comandos oficiais

### Entrada única (recomendada)

* **Pipeline padrão local (sem coverage XML):**

  ```bash
  poetry run task check
  ```

### Comandos atômicos

* **Lint**

  ```bash
  poetry run task lint
  ```
* **Type-check**

  ```bash
  poetry run task type
  ```
* **Testes**

  ```bash
  poetry run task test
  ```
* **Testes + Coverage (gera `coverage.xml`)**

  ```bash
  poetry run task test-cov
  ```

### Execução “pré-push” (recomendação)

* Pipeline completo incluindo coverage:

  ```bash
  poetry run task pre-push
  ```

## Tasks (fonte de verdade)

As tasks são definidas no `pyproject.toml`. Estado atual (referência):

* `lint`: `ruff check src`
* `type`: `mypy src`
* `test`: `pytest src/tests -v`
* `test-cov`: `pytest src/tests --cov=src --cov-report=term-missing --cov-report=xml:coverage.xml --cov-fail-under=45`
* `check`: `task lint && task type && task test`
* `pre-push`: `task check && task test-cov`

## Lint (Ruff + Black + isort)

### Ruff (linter)

* O Ruff está **consolidado no `pyproject.toml`** (não existe `.ruff.toml`).
* O pre-commit executa Ruff e pode aplicar correções automáticas quando disponível.

Executar manualmente:

```bash
poetry run task lint
```

### Formatação (Black + isort)

* A formatação é aplicada via:

  ```bash
  poetry run task format
  ```
* No fluxo padrão, o pre-commit também assegura consistência quando rodado.

## Testes e Cobertura

### Testes

Executar testes:

```bash
poetry run task test
```

### Cobertura com XML (Codecov)

Executar com cobertura e gerar `coverage.xml`:

```bash
poetry run task test-cov
```

Validação rápida do artefato:

```bash
ls -la coverage.xml
```

Política atual:

* **Threshold mínimo:** `--cov-fail-under=45`
* `coverage.xml` é gerado na raiz do repositório.

## Type-check (MyPy)

Executar:

```bash
poetry run task type
```

Estado atual no CI:

* O step de MyPy **não é gate** (o job não falha por erro de tipo). Isso é intencional enquanto o projeto limpa/estabiliza o baseline de tipagem.

## Pre-commit

Recomenda-se instalar e rodar localmente:

Instalar hooks:

```bash
pre-commit install
pre-commit install --hook-type commit-msg
```

Rodar em todos os arquivos:

```bash
pre-commit run --all-files --show-diff-on-failure
```

Observação:

* Atualizações de hooks podem implicar reformat em massa (ex.: Black), o que é esperado quando se usa `pre-commit autoupdate`.

## CI (GitHub Actions)

### Triggers

O CI roda em:

* `push` para `main`
* `pull_request` para `main`

### Pipeline no CI (espelho das tasks)

O workflow executa, em ordem:

* `poetry run task lint`
* `poetry run task type` (**não-gate**, atualmente)
* `poetry run task test-cov` (gera `coverage.xml`)
* Upload do `coverage.xml` no Codecov

## Dependências NLP no CI (nota técnica)

No workflow atual, há uma etapa que instala dependências NLP via `pip` durante o job (ex.: `spacy`, `numpy`, `textblob`, `nltk`, `wordcloud`, `matplotlib`) e baixa modelos do spaCy.

Isso existe porque, no estado atual do projeto, essas dependências **não estão totalmente resolvidas via Poetry** no pipeline do CI (conflitos/compatibilidade). Se futuramente o lock do Poetry absorver isso de forma estável, a etapa de `pip install ...` pode ser removida.

## Como reproduzir localmente o que o CI faz

Rodar exatamente os mesmos comandos do CI:

```bash
poetry run task lint
poetry run task type
poetry run task test-cov
```

## Encerramento da Issue #6 (checklist de aceite)

* [x] Existe `task check` como entrada única do pipeline local
* [x] `task check` executa lint + type + tests
* [x] CI executa o mesmo pipeline via Taskipy (tasks oficiais)
* [x] Cobertura gera `coverage.xml` e é consumida pelo Codecov
* [ ] MyPy sem erros no target definido (`src/`) **(pendente se a política for “zero erros”)**
* [x] Configurações principais consolidadas (Ruff no `pyproject.toml`; hooks atualizados)
* [x] Documentação mínima dos comandos oficiais (este documento)

---
