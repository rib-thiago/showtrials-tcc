## 📊 **ANÁLISE COMPLETA DE COBERTURA - SHOWTRIALS**

<div align="center">

**Documento de planejamento baseado em dados reais (19/02/2026)**

</div>

---

## 📈 **MÉTRICAS GLOBAIS ATUAIS**

| Métrica | Valor |
|---------|-------|
| **Total de arquivos** | 40 |
| **Linhas de código** | 1.726 |
| **Cobertura global** | **55%** |
| **Testes totais** | 116 |
| **Testes passando** | 114 (98%) |
| **Testes falhando** | 2 |

**Meta atual:** 45% (já ultrapassada! ✅)

---

## 🎯 **TOP 10 ARQUIVOS POR PRIORIDADE (MENOR COBERTURA)**

| # | Arquivo | Cobertura | Linhas | Impacto | Prioridade |
|---|---------|-----------|--------|---------|------------|
| 1 | `sqlite_traducao_repository.py` | **0%** | 53 | Alto | 🔴 **URGENTE** |
| 2 | `factories.py` | **0%** | 63 | Alto | 🔴 **URGENTE** |
| 3 | `traduzir_documento.py` | **0%** | 42 | Alto | 🔴 **URGENTE** |
| 4 | `analisar_acervo.py` | **0%** | 52 | Médio | 🔴 **URGENTE** |
| 5 | `analisar_texto.py` | **0%** | 38 | Médio | 🔴 **URGENTE** |
| 6 | `exportar_documento.py` | **0%** | 89 | Médio | 🟡 MÉDIA |
| 7 | `gerar_relatorio.py` | **0%** | 153 | Médio | 🟡 MÉDIA |
| 8 | `listar_traducoes.py` | **0%** | 11 | Baixo | 🟢 BAIXA |
| 9 | `txt_exporter.py` | **0%** | 38 | Baixo | 🟢 BAIXA |
| 10 | `estatisticas.py` | **15%** | 48 | Médio | 🟡 MÉDIA |

---

## 📊 **COBERTURA POR CAMADA (DADOS REAIS)**

| Camada | Cobertura | Cálculo |
|--------|-----------|---------|
| **Domain** | 92% | (89 + 91 + 88 + 95 + 96) / 5 |
| **Application** | 24% | (41 + 15 + 55 + 57 + 0*5) / 9 |
| **Infrastructure** | 41% | (54 + 92 + 0 + 88 + 95 + 85 + 0 + 90 + 89) / 9 |
| **GLOBAL** | **55%** | - |

---

## 🗺️ **PLANO DE AÇÃO POR FASES (COM DADOS REAIS)**

### **FASE 1: ARQUIVOS CRÍTICOS (0%) - 5 ARQUIVOS**

| # | Arquivo | Linhas | Esforço | Impacto |
|---|---------|--------|---------|---------|
| 1 | `sqlite_traducao_repository.py` | 53 | 2h | 🔴 Alto |
| 2 | `factories.py` | 63 | 2h | 🔴 Alto |
| 3 | `traduzir_documento.py` | 42 | 1.5h | 🔴 Alto |
| 4 | `analisar_acervo.py` | 52 | 2h | 🟡 Médio |
| 5 | `analisar_texto.py` | 38 | 1.5h | 🟡 Médio |

**Ganho estimado:** +15% na cobertura global

---

### **FASE 2: ARQUIVOS BAIXA COBERTURA (15-41%) - 3 ARQUIVOS**

| # | Arquivo | Cobertura | Linhas | Esforço |
|---|---------|-----------|--------|---------|
| 6 | `estatisticas.py` | 15% | 48 | 1.5h |
| 7 | `classificar_documento.py` | 41% | 51 | 1.5h |
| 8 | `config/__init__.py` | 54% | 70 | 1h |

**Ganho estimado:** +5% na cobertura global

---

### **FASE 3: ARQUIVOS MÉDIA COBERTURA (55-85%) - 5 ARQUIVOS**

| # | Arquivo | Cobertura | Linhas | Esforço |
|---|---------|-----------|--------|---------|
| 9 | `listar_documentos.py` | 55% | 51 | 1h |
| 10 | `obter_documento.py` | 57% | 35 | 0.5h |
| 11 | `repositories.py` | 74% | 19 | 0.5h |
| 12 | `sqlite_repository.py` | 85% | 82 | 1h |
| 13 | `estatisticas_dto.py` | 85% | 26 | 0.5h |

**Ganho estimado:** +3% na cobertura global

---

## ⚡ **ARQUIVOS QUE PODEMOS IGNORAR (JÁ > 85%)**

| Arquivo | Cobertura | Motivo |
|---------|-----------|--------|
| `documento.py` | 89% | Já excelente |
| `traducao.py` | 91% | Já excelente |
| `analise_texto.py` | 88% | Já excelente |
| `nome_russo.py` | 95% | Já excelente |
| `tipo_documento.py` | 96% | Já excelente |
| `registry.py` | 90% | Já excelente |
| `telemetry/__init__.py` | 89% | Já excelente |

---

## 🔧 **CORREÇÕES URGENTES (2 TESTES FALHANDO)**

Os dois testes que estão falhando são no mesmo arquivo: **`tipo_documento.py`** (linhas 60 e 92)

```python
# Problema: KeyError nos dicionários descricoes e icones
return descricoes[self]  # ← KeyError
return icones[self]      # ← KeyError
```

**Solução:** Corrigir o dicionário para usar `self.value` em vez de `self`

---

## ✅ **PRÓXIMO PASSO CONCRETO (BASEADO EM DADOS)**

### **Prioridade #1: Corrigir os 2 testes falhando**

```bash
git checkout -b fix/tipo-documento-keyerror
# Corrigir linhas 60 e 92
git add src/domain/value_objects/tipo_documento.py
git commit -m "fix: corrige KeyError em tipo_documento.py

- Substitui self por self.value nos dicionários
- Resolve 2 testes falhando
- Mantém cobertura em 96%"
```

### **Prioridade #2: Arquivo com 0% mais crítico**

```bash
git checkout -b feat/sqlite-traducao-repo
# Implementar testes para sqlite_traducao_repository.py
```

---

## 📋 **COMANDO PARA REAVALIAR APÓS CORREÇÕES**

```bash
poetry run pytest --cov=src --cov-report=term-missing | grep -E "^src/|^TOTAL" | cat
```
