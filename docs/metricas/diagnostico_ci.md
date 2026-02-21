## 📝 **PASSO 4: CRIAR ARQUIVO DE DIAGNÓSTICO**

### **Novo arquivo: `docs/metricas/diagnostico_ci.md`**

```markdown
# Diagnóstico: Falhas no Pipeline de CI (FASE 11)

<div align="center">

**Análise detalhada das falhas no GitHub Actions que motivaram a FASE 11**

</div>

## 📅 **Informações do Diagnóstico**

| Item | Descrição |
|------|-----------|
| **Data** | 19/02/2026 |
| **Autor** | Thiago Ribeiro |
| **Fase relacionada** | [FASE 11](../fases/FASE11_CI.md) |
| **Commit do diagnóstico** | [`c87fc9e`](https://github.com/rib-thiago/showtrials-tcc/commit/c87fc9eac947b9748c53beaed12de293d173203a) |

---

## 🎯 **Problema Identificado**

Todos os merges das branches `type/*` estavam falhando no GitHub Actions com o erro:

```
ModuleNotFoundError: No module named 'spacy'
```

---

## 📊 **Dados Coletados**

### Histórico de Falhas
```
STATUS  TITLE                                  BRANCH    ID
X       Merge branch 'type/analisar-texto'     main      22207771569
X       Merge branch 'type/analisar-acervo'    main      22206622629
X       Merge branch 'type/traduzir-documento' main      22205046693
X       Merge branch 'type/factories'          main      22204553138
```

**Último commit com sucesso:** `b8b3242` (18/02/2026)

---

## 🔍 **Análise da Causa Raiz**

### Cadeia de Importação
```
test_analisar_acervo.py
  → from src.application.use_cases.analisar_acervo import AnalisarAcervo
    → from src.infrastructure.analysis.spacy_analyzer import SpacyAnalyzer
      → import spacy  ← ERRO!
```

### Comparação de Ambientes

| Componente | Local | CI | Status |
|------------|-------|-----|--------|
| spacy | ✅ (pip) | ❌ | 🔴 PROBLEMA |
| numpy | ✅ (1.26.0) | ❌ | 🔴 PROBLEMA |
| textblob | ✅ | ❌ | 🔴 PROBLEMA |
| Modelos spaCy | ✅ | ❌ | 🔴 PROBLEMA |
| Demais dependências | ✅ (Poetry) | ✅ | 🟢 OK |

---

## 📋 **Causa Raiz**

Durante a **FASE 8**, as dependências NLP foram instaladas manualmente via pip devido a conflitos com Poetry. O CI, porém, executava apenas `poetry install`, não replicando essas dependências.

---

## 📊 **Opções Consideradas**

| Opção | Descrição | Vantagens | Desvantagens |
|-------|-----------|-----------|--------------|
| **A** | Poetry | Solução canônica | Já tentado e falhou |
| **B** | pip no CI | Rápida, testada | Foge do padrão |
| **C** | Docker | Reprodutível | Complexo |

**Decisão:** Opção B (implementada na FASE 11)

---

## 📈 **Impacto**

- 12 merges bloqueados consecutivamente
- Time impedido de avançar por ~24 horas
- Solução implementada em 30 minutos

---

## 🔗 **Links Relacionados**

- [FASE 11 - Solução implementada](../fases/FASE11_CI.md)
- [Issue #1 - Migrar para Poetry](https://github.com/rib-thiago/showtrials-tcc/issues/1)
- [Commit da solução](https://github.com/rib-thiago/showtrials-tcc/commit/c87fc9eac947b9748c53beaed12de293d173203a)

---

<div align="center">
  <sub>Diagnóstico mantido para referência histórica</sub>
  <br>
  <sub>✅ Problema resolvido na FASE 11</sub>
</div>
```

---
