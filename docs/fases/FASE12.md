# FASE 12 - Padronização da Telemetria no TipoDocumento

<div align="center">

**Correção dos testes de telemetria e unificação do padrão de instrumentação**

</div>

## 📅 **Informações da Fase**

| Item | Descrição |
|------|-----------|
| **Status** | ✅ Concluída |
| **Data de Conclusão** | 19/02/2026 |
| **Artefatos** | `src/domain/value_objects/tipo_documento.py` (modificado) |
| **Dependências** | FASE 8 (Análise de Texto), FASE 11 (CI) |
| **Issue principal** | [#3](https://github.com/rib-thiago/showtrials-tcc/issues/3) |
| **Commit principal** | [`1b91b23`](https://github.com/rib-thiago/showtrials-tcc/commit/1b91b23660024bef1aa4cb073906db4a70a35d7b) |

---

## 🎯 **Objetivo**

Padronizar a implementação da telemetria no arquivo `tipo_documento.py` para seguir o mesmo padrão utilizado em todos os outros arquivos do projeto, resolvendo os 4 testes falhando e garantindo consistência na instrumentação.

---

## 📁 **Arquivo Modificado**

```bash
src/
└── domain/
    └── value_objects/
        └── tipo_documento.py  # Modificado para seguir padrão de telemetria
```

---

## 🧩 **Componentes Implementados**

### Padrão de Telemetria Unificado

**Antes:**
```python
# Usava decorator @monitor (padrão diferente dos outros arquivos)
try:
    from src.infrastructure.telemetry import monitor
    TELEMETRY_AVAILABLE = True
except ImportError:
    TELEMETRY_AVAILABLE = False
    def monitor(func): return func
```

**Depois:**
```python
# Padrão consolidado (igual aos outros arquivos)
_telemetry = None

def configure_telemetry(telemetry_instance=None):
    global _telemetry
    _telemetry = telemetry_instance

# Uso nos métodos:
if _telemetry:
    _telemetry.increment("tipo_documento.classificado")
```

### Principais Mudanças:
1. ✅ Substituído decorator `@monitor` por chamadas explícitas
2. ✅ Adicionada variável global `_telemetry`
3. ✅ Adicionada função `configure_telemetry()`
4. ✅ Adicionadas verificações `if _telemetry:` nos métodos

---

## 🧪 **Testes**

### Testes de Lógica (existentes - 9 testes)

Os testes de lógica em `test_tipo_documento.py` continuaram passando:
- `test_classificar_interrogatorio`
- `test_classificar_acareacao`
- `test_classificar_carta`
- `test_classificar_relatorio`
- `test_classificar_depoimento_singular`
- `test_classificar_depoimento_plural`
- `test_titulo_desconhecido`
- `test_listar_todos`

### Testes de Telemetria (corrigidos - 5 testes)

Os testes em `test_tipo_documento_telemetry.py` que estavam falhando agora passam:
- `test_telemetria_chamada_quando_disponivel`
- `test_telemetria_titulo_vazio`
- `test_telemetria_desconhecido`
- `test_com_decorator_mock`
- `test_sem_telemetria_nao_quebra`

**Resultado:**
```bash
pytest src/tests/test_tipo_documento_telemetry.py -v

# Saída:
# test_tipo_documento_telemetry.py::TestTipoDocumentoTelemetry::test_telemetria_chamada_quando_disponivel PASSED
# test_tipo_documento_telemetry.py::TestTipoDocumentoTelemetry::test_telemetria_titulo_vazio PASSED
# test_tipo_documento_telemetry.py::TestTipoDocumentoTelemetry::test_telemetria_desconhecido PASSED
# test_tipo_documento_telemetry.py::TestTipoDocumentoTelemetry::test_com_decorator_mock PASSED
# test_tipo_documento_telemetry.py::TestTipoDocumentoTelemetry::test_sem_telemetria_nao_quebra PASSED
# ========================== 5 passed in 0.15s ==========================
```

---

## 📊 **Métricas da Fase**

| Métrica | Antes | Depois | Evolução |
|---------|-------|--------|----------|
| **Testes de telemetria passando** | 1/5 | 5/5 | ✅ +4 |
| **Cobertura do arquivo** | 83% | 96% | 📈 +13 p.p. |
| **Erros de MyPy** | 0 | 0 | ✅ Mantido |
| **Arquivos com padrão unificado** | ~10 | ~11 | ✅ +1 |

---

## 📚 **Princípios Aplicados**

| Princípio | Aplicação |
|-----------|-----------|
| **Consistência** | Padrão de telemetria unificado com outros arquivos |
| **Testabilidade** | `configure_telemetry()` permite mock nos testes |
| **Fallback seguro** | `if _telemetry:` garante que funciona sem telemetria |
| **DRY** | Mesmo padrão replicado em todos os módulos |

---

## 🔗 **Integração com Fases**

| Fase | Relacionamento |
|------|----------------|
| **FASE 5** | Primeiro uso do padrão de telemetria |
| **FASE 8** | Padronização do padrão em análise de texto |
| **FASE 11** | CI estabilizado permitiu merge |
| **FASE 14-16** | Mesmo padrão aplicado em novos casos de uso |

---

## 🔄 **Evolução do Código**

### Antes (código com padrão diferente)
```python
try:
    from src.infrastructure.telemetry import monitor
    TELEMETRY_AVAILABLE = True
except ImportError:
    TELEMETRY_AVAILABLE = False
    def monitor(func): return func

@monitor
def from_titulo(cls, titulo):
    # ... lógica ...
```

### Depois (padrão unificado)
```python
_telemetry = None

def configure_telemetry(telemetry_instance=None):
    global _telemetry
    _telemetry = telemetry_instance

@classmethod
def from_titulo(cls, titulo):
    if _telemetry:
        _telemetry.increment("tipo_documento.from_titulo.iniciado")
    # ... lógica ...
    if _telemetry:
        _telemetry.increment("tipo_documento.classificado")
```

---

## 🔍 **Lições Aprendidas**

1. **Consistência sobre inovação local** - O padrão único facilitou a manutenção
2. **Testes de telemetria são essenciais** - Pegaram a inconsistência antes do merge
3. **Commits descritivos ajudam** - A mensagem do commit `1b91b23` já documentava a mudança
4. **Padrões evoluem** - O que começou na FASE 5 virou regra para todo o projeto

---

## 📋 **Issues Relacionadas**

- ✅ [#3](https://github.com/rib-thiago/showtrials-tcc/issues/3) - FASE 17 (indiretamente)
- ✅ [#CI](https://github.com/rib-thiago/showtrials-tcc/issues/CI) - CI quebrado (resolvido na FASE 11)

---

## 👤 **Autor**

**Thiago Ribeiro** - Projeto de TCC

---

<div align="center">
  <sub>FASE 12 concluída em 19/02/2026</sub>
  <br>
  <sub>✅ Telemetria padronizada • 🧪 5 testes de telemetria passando</sub>
</div>
```

---
