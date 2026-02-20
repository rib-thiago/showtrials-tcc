# FASE 11 - Estabilização do Pipeline de Integração Contínua (CI)

<div align="center">

**Diagnóstico completo, análise de soluções e correção das falhas no GitHub Actions**

</div>

## 📅 **Informações da Fase**

| Item | Descrição |
|------|-----------|
| **Status** | ⏳ Em andamento |
| **Data de Início** | 19 de Fevereiro de 2026 |
| **Artefatos** | Script de diagnóstico, Análise de falhas, Workflow CI corrigido, Documentação de decisões |
| **Dependências** | FASE 8 (Análise de Texto), FASE 10 (Service Registry) |
| **Pré-requisitos** | Acesso ao GitHub, Permissão para modificar workflows |

---

## 🎯 **Objetivo Geral**

Estabilizar o pipeline de integração contínua (CI) que atualmente impede todos os merges das branches `type/*` de serem aprovados, garantindo que:

1. **Todos os merges passem automaticamente** no CI
2. **O ambiente do CI replique fielmente** o ambiente de desenvolvimento local
3. **As decisões técnicas fiquem documentadas** para referência futura
4. **Possamos evoluir gradualmente** para uma solução mais elegante

---

## 🔬 **PARTE 1: DIAGNÓSTICO COMPLETO**

### 1.1 Coleta de Evidências

Utilizando o script `diagnostico_ci.sh` (criado especificamente para esta fase), coletamos os seguintes dados:

#### **Métricas Globais do Projeto**
```
📊 COBERTURA DE TESTES: 63% (meta 45% ✓)
🔤 ERROS MYPY: 34
📁 TESTES QUE CRIAM ARQUIVOS: 7
✅ ÚLTIMO COMMIT COM SUCESSO: b8b3242 (18/02/2026 - "test: adiciona testes para telemetria")
```

#### **Histórico de Falhas no CI**
```
STATUS  TITLE                                  BRANCH    EVENT    ID           AGE
X       Merge branch 'type/analisar-texto'     main      push     22207771569  23 minutes ago
X       Merge branch 'type/analisar-acervo'    main      push     22206622629  1 hour ago
X       Merge branch 'type/traduzir-documento' main      push     22205046693  2 hours ago
X       Merge branch 'type/factories'          main      push     22204553138  2 hours ago
X       Merge branch 'type/sqlite-traducao-repo' main   push     22168468450  21 hours ago
...
```

**Padrão observado:** TODOS os merges recentes estão falhando. O último sucesso foi no commit `b8b3242` (18/02).

### 1.2 Análise dos Logs de Falha

Examinando o log da última execução (ID: 22207771569), encontramos a causa raiz:

```python
==================================== ERRORS ====================================
________ ERROR collecting src/tests/test_analisar_acervo.py ________
ImportError while importing test module '.../test_analisar_acervo.py'.
E   ModuleNotFoundError: No module named 'spacy'

________ ERROR collecting src/tests/test_analisar_acervo_telemetry.py ________
E   ModuleNotFoundError: No module named 'spacy'

________ ERROR collecting src/tests/test_analisar_texto.py ________
E   ModuleNotFoundError: No module named 'spacy'

________ ERROR collecting src/tests/test_factories.py ________
E   ModuleNotFoundError: No module named 'spacy'
```

**Cadeia de importação que leva ao erro:**
```
test_analisar_acervo.py
  → from src.application.use_cases.analisar_acervo import AnalisarAcervo
    → from src.infrastructure.analysis.spacy_analyzer import SpacyAnalyzer
      → import spacy  ← ERRO AQUI!
```

### 1.3 Comparação entre Ambiente Local e CI

| Componente | Ambiente Local | Ambiente CI | Status |
|------------|----------------|-------------|--------|
| **spacy** | ✅ Instalado (via pip) | ❌ Ausente | 🔴 PROBLEMA |
| **numpy** | ✅ Instalado (1.26.0) | ❌ Ausente | 🔴 PROBLEMA |
| **textblob** | ✅ Instalado | ❌ Ausente | 🔴 PROBLEMA |
| **wordcloud** | ✅ Instalado | ❌ Ausente | 🔴 PROBLEMA |
| **matplotlib** | ✅ Instalado | ❌ Ausente | 🔴 PROBLEMA |
| **Modelos spaCy** | ✅ Baixados | ❌ Ausentes | 🔴 PROBLEMA |
| **Demais dependências** | ✅ Gerenciadas pelo Poetry | ✅ Instaladas via Poetry | 🟢 OK |

### 1.4 Causa Raiz Identificada

Durante a **FASE 8 (Análise de Texto)**, enfrentamos dificuldades com o Poetry devido a incompatibilidades de versões (conforme documentado na época). A solução adotada foi:

```bash
# Instalação manual dentro do ambiente virtual do Poetry
poetry shell
pip install numpy==1.26.0
pip install spacy==3.7.5
pip install textblob nltk wordcloud matplotlib
pip install https://github.com/explosion/spacy-models/releases/download/...
```

**Consequências:**
- ✅ **Localmente:** tudo funciona perfeitamente
- ❌ **No CI:** o comando `poetry install` NÃO instala essas dependências
- ❌ **No cache do GitHub Actions:** as dependências também não estão presentes
- ❌ **Resultado:** todos os testes que importam `spacy` falham no CI

### 1.5 Problemas Secundários

Além do problema principal, identificamos:

| # | Problema | Localização | Impacto |
|---|----------|-------------|---------|
| 1 | **4 testes falhando localmente** | `test_tipo_documento_telemetry.py` | 🟡 Médio (impede merge) |
| 2 | **34 erros de MyPy** | Espalhados pelo código | 🟢 Baixo (ignorado no CI) |
| 3 | **11 arquivos .bak** | Vários diretórios | 🟢 Baixo (limpeza) |

---

## 🧪 **PARTE 2: ANÁLISE DE SOLUÇÕES POSSÍVEIS**

### 2.1 Opção A: Adicionar Dependências ao Poetry

**Descrição:** Adicionar todas as dependências de NLP diretamente no `pyproject.toml` e deixar o Poetry gerenciá-las.

**Comandos necessários:**
```bash
poetry add numpy@^1.26.0
poetry add spacy@^3.7.5
poetry add textblob nltk wordcloud matplotlib
poetry lock
```

**Vantagens:**
- ✅ **Solução canônica:** segue o padrão esperado de gerenciamento
- ✅ **Versionamento:** todas as versões ficam registradas no `poetry.lock`
- ✅ **Reprodutibilidade:** qualquer ambiente com `poetry install` terá as mesmas versões
- ✅ **Manutenibilidade:** um único comando para instalar tudo

**Desvantagens:**
- ❌ **Já tentamos antes e não funcionou:** conforme documentado na FASE 8
- ❌ **Conflitos de versão:** numpy, spacy e outras bibliotecas têm dependências conflitantes
- ❌ **Tempo imprevisível:** pode levar horas de debugging sem garantia de sucesso
- ❌ **Risco de quebrar o ambiente local:** alterações no lock file podem afetar o que já funciona

**Esforço estimado:** 3-5 horas (com risco de não resolver)

---

### 2.2 Opção B: Instalar via pip no CI (Solução Imediata)

**Descrição:** Modificar o workflow do GitHub Actions para instalar as dependências da MESMA forma que você faz localmente (via pip), ANTES de rodar os testes.

**Modificação no CI:**
```yaml
- name: Install Poetry dependencies
  run: poetry install --no-interaction

- name: Install NLP dependencies (pip)
  run: |
    poetry run pip install numpy==1.26.0
    poetry run pip install spacy==3.7.5
    poetry run pip install textblob nltk wordcloud matplotlib
    poetry run python -m spacy download en_core_web_sm
    poetry run python -m spacy download ru_core_news_sm
```

**Vantagens:**
- ✅ **JÁ FUNCIONA LOCALMENTE:** a solução é testada e aprovada
- ✅ **Implementação rápida:** 30 minutos no máximo
- ✅ **Baixo risco:** mantém o ambiente de desenvolvimento intacto
- ✅ **Reversível:** fácil voltar atrás se necessário
- ✅ **Desbloqueia o time AGORA:** permite que os merges voltem a acontecer

**Desvantagens:**
- ⚠️ **Foge do padrão "Poetry-only":** mistura duas formas de gerenciamento
- ⚠️ **Manutenção manual:** se novas dependências forem adicionadas via pip, precisamos lembrar de atualizar o CI
- ⚠️ **Duplicação de esforço:** as versões não ficam versionadas no poetry.lock

**Esforço estimado:** 30 minutos

---

### 2.3 Opção C: Dockerizar o Ambiente

**Descrição:** Criar um `Dockerfile` que replica EXATAMENTE o ambiente de desenvolvimento e rodar os testes dentro do container no CI.

**Exemplo de Dockerfile:**
```dockerfile
FROM python:3.12-slim

WORKDIR /app

# Dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Poetry
RUN pip install poetry

# Dependências do projeto
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-interaction --no-ansi

# Instalação via pip (igual ao ambiente local)
RUN poetry run pip install numpy==1.26.0 spacy==3.7.5
RUN poetry run python -m spacy download en_core_web_sm
RUN poetry run python -m spacy download ru_core_news_sm

COPY . .
CMD ["poetry", "run", "pytest"]
```

**Vantagens:**
- ✅ **Reprodutibilidade máxima:** o ambiente é IDÊNTICO ao local
- ✅ **Isolamento completo:** não depende de cache do GitHub
- ✅ **Documentação viva:** o Dockerfile documenta TODO o ambiente

**Desvantagens:**
- ❌ **Complexidade:** curva de aprendizado do Docker
- ❌ **Tempo de build:** maior que a instalação direta
- ❌ **Manutenção:** mais um arquivo para gerenciar

**Esforço estimado:** 4-6 horas

---

### 2.4 Matriz de Decisão

| Critério | Opção A (Poetry) | Opção B (pip no CI) | Opção C (Docker) |
|----------|------------------|---------------------|------------------|
| **Tempo de implementação** | ⭐ (3-5h) | ⭐⭐⭐ (30min) | ⭐⭐ (4-6h) |
| **Risco de falha** | ⭐⭐ (alto) | ⭐⭐⭐ (baixo) | ⭐⭐ (médio) |
| **Manutenibilidade** | ⭐⭐⭐ (excelente) | ⭐⭐ (média) | ⭐⭐ (média) |
| **Reprodutibilidade** | ⭐⭐⭐ (excelente) | ⭐⭐ (boa) | ⭐⭐⭐ (excelente) |
| **Alinhamento com padrões** | ⭐⭐⭐ (perfeito) | ⭐ (baixo) | ⭐⭐ (bom) |
| **Complexidade** | ⭐⭐ (média) | ⭐⭐⭐ (baixa) | ⭐ (alta) |

**Total (prioridade atual):** Opção B vence por ter o melhor custo-benefício para resolver o problema AGORA.

---

## 🎯 **PARTE 3: DECISÃO TÉCNICA E JUSTIFICATIVA**

### 3.1 Decisão

Após análise criteriosa, **optamos pela Opção B (Instalar via pip no CI)** como solução imediata.

### 3.2 Justificativa Detalhada

1. **Urgência do negócio:**
   - 12 merges consecutivos falhando
   - Time impedido de avançar com novas features
   - Precisamos de uma solução HOJE, não daqui uma semana

2. **Baixo risco:**
   - A solução já é testada e aprovada localmente
   - As versões são fixas (numpy 1.26.0, spacy 3.7.5)
   - Fácil de reverter: basta comentar as linhas no workflow

3. **Simplicidade:**
   - Modificação pontual em UM arquivo
   - Não requer mudanças no código fonte
   - Não afeta o ambiente de desenvolvimento

4. **Experiência anterior:**
   - Já tentamos a Opção A (Poetry) na FASE 8 e não funcionou
   - Documentamos as dificuldades na época
   - Não faz sentido repetir o mesmo erro

### 3.3 Compromisso Técnico

Para não perdermos de vista a solução ideal, estabelecemos o seguinte compromisso:

> **Implementaremos a Opção B como solução IMEDIATA, com um TODO list claro para evoluirmos para a Opção A (Poetry) em momento oportuno, quando tivermos mais tempo para debugging e pesquisa de versões compatíveis.**

Este compromisso fica registrado neste documento e no código (via comentários).

---

## 📋 **PARTE 4: TODO LIST - EVOLUÇÃO FUTURA**

### 4.1 Tarefas para Migração para Poetry

- [ ] **Pesquisar** versões compatíveis de:
  - `numpy` (tentar 1.24.0 ou 1.26.0)
  - `spacy` (3.7.0, 3.7.5)
  - `thinc` (dependência do spacy)
  - `blis` (dependência do spacy)
  - `textblob`, `nltk`, `wordcloud`, `matplotlib`

- [ ] **Criar branch de teste** `test/poetry-nlp`
- [ ] **Testar combinações** no ambiente local (com backup do ambiente atual)
- [ ] **Documentar** sucessos e falhas em um arquivo `docs/experimentos_poetry.md`
- [ ] **Atualizar** `pyproject.toml` com versões que funcionam
- [ ] **Testar no CI** (simulando o ambiente limpo)
- [ ] **Remover** etapas de `pip install` do workflow
- [ ] **Atualizar** este documento com a solução final

### 4.2 Comando para Lembrete

```bash
# Criar issue no GitHub (se usar)
gh issue create \
  --title "Migrar dependências NLP para Poetry" \
  --body "Substituir instalação via pip no CI por dependências gerenciadas pelo Poetry. Ver FASE11.md para detalhes." \
  --label "melhoria"
```

---

## ✅ **PARTE 5: CRITÉRIOS DE SUCESSO**

### 5.1 Métricas de Sucesso Imediato (Opção B)

| Antes | Depois |
|-------|--------|
| ❌ 12 merges falhando consecutivos | ✅ CI verde nos próximos merges |
| ❌ `ModuleNotFoundError: spacy` | ✅ Dependências instaladas corretamente |
| ❌ Impossível avançar com features | ✅ Fluxo de trabalho desbloqueado |
| ❌ Desenvolvedor frustrado | ✅ Desenvolvedor produtivo |

### 5.2 Métricas de Sucesso Futuro (Opção A)

- [ ] `poetry install` instala TODAS as dependências sem erros
- [ ] Nenhum `pip install` necessário no CI
- [ ] `poetry.lock` contém todas as versões
- [ ] Ambiente 100% reproduzível

---

## 📚 **PARTE 6: REFERÊNCIAS**

- **FASE 8 - Análise de Texto:** Documentação original das dificuldades com Poetry
- **FASE 10 - Service Registry:** Última fase antes do problema de CI
- **GitHub Actions Documentation:** https://docs.github.com/actions
- **Poetry Documentation:** https://python-poetry.org/docs/

---

## 👤 **Autor**

**Thiago Ribeiro** - Projeto de TCC
**Com assistência de DeepSeek** - Diagnóstico e documentação

---

## 📜 **HISTÓRICO DE REVISÕES**

| Versão | Data | Autor | Alterações |
|--------|------|-------|------------|
| 1.0 | 19/02/2026 | Thiago Ribeiro | Documento inicial da FASE 11 |

---

<div align="center">
  <sub>FASE 11 - Documento de Diagnóstico do CI e Plano de Ação</sub>
  <br>
  <sub>Versão 1.0 - 19 de Fevereiro de 2026</sub>
  <br>
  <sub>✅ Aguardando aprovação para implementação</sub>
</div>

---
