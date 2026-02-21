## 📊 **COBERTURA DE TESTES - SHOWTRIALS**

<div align="center">

**Métricas atualizadas em 21/02/2026 • [Histórico de evolução](#histórico-de-evolução)**

</div>

---

## 📈 **MÉTRICAS ATUAIS**

| Métrica | Valor |
|---------|-------|
| **Cobertura global** | **75%** 🚀 |
| **Testes totais** | ~250 |
| **Meta inicial** | 45% (✅ ultrapassada) |
| **Arquivos monitorados** | 40+ |

---

## 📊 **EVOLUÇÃO DA COBERTURA**

| Data | Cobertura | Δ | Principais Contribuições |
|------|-----------|-----|-------------------------|
| **21/02/2026** | **75%** | +12% | FASE 14-16 (exportar, gerar, listar) |
| 19/02/2026 | 63% | +8% | FASE 12-13 (telemetria + limpeza) |
| 19/02/2026 | 55% | - | Diagnóstico inicial |

*Detalhes das contribuições estão documentados em cada [FASE*.md](fases/)*

---

## 🎯 **TOP PRIORIDADES ATUAIS**

| # | Arquivo | Cobertura | Impacto | Issue | Fase |
|---|---------|-----------|---------|-------|------|
| 1 | `estatisticas.py` | 15% | 🔴 Alto | [#5](https://github.com/rib-thiago/showtrials-tcc/issues/5) | FASE 19 |
| 2 | `classificar_documento.py` | 65% | 🟡 Médio | [#3](https://github.com/rib-thiago/showtrials-tcc/issues/3) | FASE 17 |
| 3 | `obter_documento.py` | 57% | 🟡 Médio | [#4](https://github.com/rib-thiago/showtrials-tcc/issues/4) | FASE 18 |
| 4 | `spacy_analyzer.py` | 23% | 🔴 Alto | - | - |
| 5 | `google_translator.py` | 24% | 🔴 Alto | - | - |

---

## 📊 **COBERTURA POR CAMADA**

| Camada | Cobertura | Status |
|--------|-----------|--------|
| **Domain** | 92% | ✅ Excelente |
| **Application** | 40% | ⚠️ Em progresso |
| **Infrastructure** | 57% | 🟡 Melhorando |
| **Interface** | - | Testes manuais |

---

## 📜 **HISTÓRICO DETALHADO DE MUDANÇAS**

### **FASE 16 - ListarDocumentos (20/02/2026)**
```bash
📁 src/application/use_cases/listar_documentos.py
📈 55% → 80%
✨ Melhorias:
  - Adicionada telemetria
  - Expandidos testes de lógica (12)
  - Criados testes de telemetria (6)
  - Corrigidos 3 erros de MyPy
🔗 [FASE16.md](fases/FASE16.md)
```

### **FASE 15 - GerarRelatorio (20/02/2026)**
```bash
📁 src/application/use_cases/gerar_relatorio.py
📈 0% → 86%
✨ Melhorias:
  - Adicionada telemetria completa
  - Criados 12 testes de lógica
  - Criados 6 testes de telemetria
  - Corrigidos 7 erros de MyPy
🔗 [FASE15.md](fases/FASE15.md)
```

### **FASE 14 - ExportarDocumento (20/02/2026)**
```bash
📁 src/application/use_cases/exportar_documento.py
📈 0% → 81%
✨ Melhorias:
  - Adicionada telemetria
  - Criados 12 testes de lógica
  - Criados 8 testes de telemetria
🔗 [FASE14.md](fases/FASE14.md)
```

### **FASE 12-13 - Fundação (19/02/2026)**
```bash
📈 55% → 63%
✨ Melhorias:
  - Padronização de telemetria em tipo_documento.py
  - Limpeza de arquivos .bak e diagnóstico
  - Organização do repositório
🔗 [FASE12.md](fases/FASE12.md) | [FASE13.md](fases/FASE13.md)
```

---

## 🔍 **COMO INTERPRETAR ESTE DOCUMENTO**

| Seção | Para que serve |
|-------|----------------|
| **Métricas atuais** | Snapshot do momento |
| **Evolução** | Visão histórica do progresso |
| **Top prioridades** | Guia para próximas ações |
| **Cobertura por camada** | Visão arquitetural |
| **Histórico detalhado** | Rastreabilidade das melhorias |

---

## 🔗 **LINKS RÁPIDOS**

- [Issues abertas relacionadas](https://github.com/rib-thiago/showtrials-tcc/issues?q=is%3Aopen+is%3Aissue+label%3Atipo%2Ftestes)
- [Milestone: Qualidade](https://github.com/rib-thiago/showtrials-tcc/milestone/2)
- [Documentação das fases](fases/)
- [Como contribuir com testes](../contributing.md#testes)

---

## 📊 **COMANDO PARA ATUALIZAR ESTE DOCUMENTO**

```bash
# Para gerar métricas atualizadas
poetry run pytest --cov=src --cov-report=term-missing | grep -E "^src/|^TOTAL" | cat

# Após executar, atualize manualmente as seções:
# - Métricas atuais
# - Top prioridades (se mudou)
# - Adicione nova entrada no histórico se houve melhoria
```

---

<div align="center">
  <sub>Documento mantido vivo - última atualização: 21/02/2026</sub>
  <br>
  <sub>✅ Histórico completo • ✅ Métricas atuais • ✅ Próximos passos</sub>
</div>
```

---
