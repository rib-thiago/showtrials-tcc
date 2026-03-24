# Qualidade e CI

## 1. Regra de leitura deste documento

Este documento separa explicitamente três níveis de afirmação:

- **confirmado por configuração local**: o que está sustentado por `pyproject.toml` e tooling local observado
- **confirmado pelo workflow real de CI**: o que está sustentado diretamente por `.github/workflows/ci.yml`
- **norma documental ou expectativa de processo**: o que aparece em `docs/flows/` e documentos de fase, mas não deve ser tratado automaticamente como enforcement técnico já verificado

Quando algo ainda não puder ser confirmado nem por configuração local nem pelo workflow real, isso será marcado como incerto.

## 2. Princípios de qualidade

Os documentos de qualidade do repositório, especialmente `docs/flows/quality_flow.md`, estabelecem princípios normativos como:

- correção funcional antes de otimização
- clareza estrutural antes de abstração
- arquitetura explícita antes de conveniência
- mudanças pequenas e verificáveis
- nenhuma mudança estrutural implícita
- qualidade como critério de aceite

Também aparecem como princípios complementares:

- tipagem consistente
- ausência de código morto e artefatos temporários
- respeito ao modelo arquitetural
- evitamento de acoplamento indevido com persistência
- manutenção de transformadores puros, quando aplicável
- testabilidade como requisito de desenho

Esses princípios estão **documentados**.

O que este documento não assume sem evidência adicional:

- que todos esses princípios já estejam homogênea e automaticamente aplicados por tooling em todo o repositório

## 3. Ferramentas identificadas

## 3.1 Ferramentas confirmadas no repositório

Com base em `pyproject.toml` e no workflow real de CI, estão confirmadas as seguintes ferramentas:

- `ruff`
- `mypy`
- `pytest`
- `pytest-cov`
- `black`
- `isort`
- `pre-commit`
- `taskipy`
- GitHub Actions
- Poetry

## 3.2 Ferramentas e dependências adicionais confirmadas no workflow de CI

O arquivo `.github/workflows/ci.yml` confirma que o CI instala explicitamente, via `poetry run pip install`:

- `numpy==1.26.0`
- `spacy==3.7.5`
- `textblob`
- `nltk`
- `wordcloud`
- `matplotlib`

Também confirma download de modelos spaCy:

- `en_core_web_sm`
- `ru_core_news_sm`

## 3.3 Ferramentas e convenções ainda apenas documentadas

Os documentos também mencionam:

- `mkdocs`
- `mkdocs-material`
- `mkdocstrings`
- `mkdocstrings-python`
- `commitizen`

Esses itens aparecem no repositório/documentação, mas não são parte do job de CI observado em `.github/workflows/ci.yml`.

## 4. Fluxo local de qualidade

## 4.1 O que está confirmado em `pyproject.toml`

O papel do Taskipy está confirmado pela seção `[tool.taskipy.tasks]`.

Comandos identificados:

- qualidade:
  - `task lint`
  - `task type`
  - `task quality`
- testes:
  - `task test`
  - `task test-cov`
  - `task test-html`
- telemetria:
  - `task metrics`
  - `task monitor`
- execução:
  - `task run-cli`
  - `task run-web`
- manutenção:
  - `task clean`
  - `task docs`
- agregação:
  - `task check`
  - `task pre-push`
  - `task help`

## 4.2 Pipeline local confirmado

Com base em `pyproject.toml`, o fluxo local confirmado é:

- `task lint` -> `ruff check src`
- `task type` -> `mypy src`
- `task test` -> `pytest src/tests -v`
- `task test-cov` -> `pytest src/tests --cov=src --cov-report=term-missing --cov-fail-under=45`
- `task check` -> lint + type + test
- `task pre-push` -> check + test-cov

## 4.3 O que isso permite afirmar

É seguro afirmar que:

- existe um pipeline local padronizado por Taskipy
- a cobertura mínima local tecnicamente configurada é **45%**
- o fluxo local pretendido combina lint, type-check, testes e cobertura

## 4.4 O que não foi validado nesta sessão

Não foi validado nesta sessão:

- execução local efetiva desses comandos
- estado atual de sucesso/falha desse pipeline no ambiente local

Portanto, a configuração local está confirmada, mas o estado operacional local nesta sessão continua não executado.

## 5. Workflow real de CI

## 5.1 Gatilhos confirmados no workflow

O arquivo `.github/workflows/ci.yml` confirma que o workflow `CI` é acionado em:

- `push` para branches:
  - `main`
  - `develop`
- `pull_request` para:
  - `main`

## 5.2 Estrutura confirmada do job

O workflow contém um único job visível chamado:

- `test`

Características confirmadas:

- roda em `ubuntu-latest`
- usa matrix com:
  - Python `3.12`

## 5.3 Passos confirmados do CI

O workflow real executa, em ordem:

1. checkout do código
2. setup do Python 3.12
3. instalação do Poetry
4. cache de dependências do Poetry
5. `poetry install --no-interaction`
6. instalação adicional de dependências NLP via `poetry run pip install`
7. download dos modelos spaCy
8. verificação simples das instalações por imports
9. lint com `ruff`
10. type-check com `mypy`
11. testes com `pytest` + cobertura XML + `--cov-fail-under=45`
12. upload de `coverage.xml` para Codecov

## 5.4 Comandos confirmados do CI

Os comandos confirmados no workflow são:

- `poetry install --no-interaction`
- `poetry run pip install numpy==1.26.0`
- `poetry run pip install spacy==3.7.5`
- `poetry run pip install textblob nltk wordcloud matplotlib`
- `poetry run python -m spacy download en_core_web_sm`
- `poetry run python -m spacy download ru_core_news_sm`
- `poetry run ruff check src/`
- `poetry run mypy src/ || echo "⚠️ MyPy warnings (ignorado por enquanto)"`
- `poetry run pytest src/tests/ -v --cov=src --cov-report=xml --cov-fail-under=45`

## 5.5 O que o workflow confirma sobre enforcement real

O workflow confirma, diretamente:

- `ruff` é executado no CI sobre `src/`
- `pytest` é executado no CI sobre `src/tests/`
- a cobertura mínima de **45%** é exigida no CI pelo comando `pytest`
- o arquivo `coverage.xml` é gerado para upload
- Codecov é usado com `continue-on-error: true`

Também confirma algo importante sobre `mypy`:

- `mypy` **é executado**, mas o comando contém `|| echo "⚠️ MyPy warnings (ignorado por enquanto)"`

Interpretação conservadora:

- `mypy` roda no CI
- mas, do modo como o comando está escrito, **erros de mypy não bloqueiam o job da mesma forma que lint e testes/cobertura**

## 5.6 O que o workflow real contradiz ou corrige em relação à leitura anterior

O workflow real corrige a leitura anterior em pontos importantes:

- o CI **já foi inspecionado diretamente**, então ele não deve mais ser descrito apenas por inferência documental
- o CI **não** usa `task pre-push` como entrypoint principal
- o CI executa comandos explícitos de `ruff`, `mypy` e `pytest` diretamente, e não a task agregadora local
- o CI ainda depende de instalação complementar de dependências NLP via `pip`
- o CI ainda baixa modelos spaCy em runtime

## 6. Relação entre fluxo local e fluxo remoto

## 6.1 O que está confirmado

Existe sobreposição real entre local e remoto em vários pontos:

- lint com `ruff`
- type-check com `mypy`
- testes com `pytest`
- cobertura com limiar mínimo de 45%

## 6.2 O que está confirmado como diferença

O fluxo remoto **não replica exatamente** o fluxo local padronizado por Taskipy.

Diferenças confirmadas:

- local tem `task check` e `task pre-push` como agregadores
- CI usa comandos explícitos, não `task pre-push`
- CI instala dependências NLP adicionais e modelos spaCy explicitamente
- CI produz `coverage.xml` e tenta upload ao Codecov
- `mypy` no CI está em modo tolerante a falha, enquanto o fluxo local configurado sugere uso mais forte de `task type`

## 6.3 O que isso implica

É seguro afirmar que:

- existe convergência parcial entre local e remoto
- não existe, no estado atual do workflow inspecionado, identidade perfeita entre os dois pipelines

Portanto, qualquer formulação que diga que “o CI replica exatamente o fluxo local” deve ser evitada.

## 7. Cobertura

## 7.1 O que está confirmado localmente

Em `pyproject.toml`, está confirmado:

- limiar mínimo global de cobertura: **45%**

## 7.2 O que está confirmado no CI

No workflow real, está confirmado:

- `pytest` roda com `--cov=src`
- `--cov-report=xml`
- `--cov-fail-under=45`

Isso confirma que:

- o limiar global de 45% também está ativo no CI

## 7.3 O que permanece apenas documental ou histórico

Percentuais maiores como `48%`, `63%`, `74%` e `75%` aparecem em documentação e histórico de fases, mas:

- não foram confirmados aqui como threshold ativo de tooling
- não devem ser tratados como bloqueio técnico automático atual

## 8. Bloqueios e critérios de aceite

## 8.1 Confirmado por tooling/configuração local

Está confirmado por configuração local:

- existência de pipeline local com lint, type-check, testes e cobertura
- cobertura mínima configurada em 45%

## 8.2 Confirmado pelo CI real

Está confirmado pelo workflow real:

- lint com `ruff` participa do CI
- testes com cobertura participam do CI
- cobertura global mínima de 45% participa do CI
- upload ao Codecov é tentado, mas é best-effort

## 8.3 Confirmado apenas como norma documental

Continuam sendo normas documentadas, mas não automaticamente enforcement técnico já comprovado nesta análise:

- cobertura por arquivo
- metas de 80% ou 85%
- exigência ampla de ausência total de `TODO`
- qualquer checklist de revisão mais amplo do que o que o tooling e o workflow de fato executam

## 8.4 Confirmado como parcialmente enforceado

`mypy` entra nesta categoria.

Ele está:

- presente no fluxo local
- presente no workflow real

Mas, no CI observado:

- está configurado de forma tolerante a falha

Logo, o tipo de enforcement real de `mypy` é mais fraco no remoto do que uma leitura normativa poderia sugerir.

## 9. Incertezas que permanecem

Mesmo após a leitura direta do workflow, ainda permanecem incertos ou não validados nesta sessão:

- o estado atual de sucesso/falha do workflow no GitHub
- se existem outros workflows além de `.github/workflows/ci.yml` com papel relevante
- se as proteções de branch no repositório estão configuradas exatamente como a documentação normativa descreve
- se o pipeline local `task pre-push` passa integralmente no ambiente atual
- se a estratégia de dependências NLP via `pip` continua sendo considerada provisória ou já é política consolidada

## 10. Restrições para futuras sessões

Sessões futuras devem respeitar os seguintes cuidados:

## 10.1 Não afirmar equivalência exata entre local e remoto

Como o workflow real usa comandos explícitos e não `task pre-push`, futuras sessões não devem afirmar que local e CI são idênticos.

## 10.2 Não tratar `mypy` como gate remoto forte sem qualificação

Como o comando do CI tolera falha de `mypy`, futuras sessões devem registrar isso explicitamente.

## 10.3 Tratar dependências NLP como ponto sensível de infraestrutura

O workflow real confirma instalação complementar via `pip` e download de modelos em runtime.

Mudanças nessa área devem ser tratadas com cautela.

## 10.4 Distinguir norma documental de enforcement real

Se um requisito vem de `docs/flows/`, mas não aparece nem no `pyproject.toml` nem em `.github/workflows/ci.yml`, ele deve ser descrito como norma documental, não como bloqueio técnico confirmado.

## Estado desta versão

Este documento foi produzido com base em:

- `.github/workflows/ci.yml`
- `pyproject.toml`
- `docs/flows/quality_flow.md`
- `docs/flows/code_review_flow.md`
- `docs/flows/debug_flow.md`
- `docs/flows/refactoring_flow.md`
- `docs/flows/dependencies_flow.md`
- `docs/fases/FASE11_CI.md`
- `README.md`
- `docs/index.md`
- `docs/overview.md`
