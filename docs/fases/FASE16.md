## 📄 **FASE16.md - Telemetria e Expansão de Testes em ListarDocumentos**

```markdown
# FASE 16 - Telemetria e Expansão de Testes em ListarDocumentos

<div align="center">

**Implementação completa de telemetria, correção de type hints e expansão de testes no caso de uso de listagem de documentos**

</div>

## 📅 **Informações da Fase**

| Item | Descrição |
|------|-----------|
| **Status** | ✅ Concluída |
| **Data de Conclusão** | 20 de Fevereiro de 2026 |
| **Artefatos** | `listar_documentos.py`, `test_listar_documentos.py`, `test_listar_documentos_telemetry.py` |
| **Dependências** | FASE 15 (GerarRelatorio), FASE 14 (ExportarDocumento), FASE 12 (Padronização de Telemetria) |
| **Branch principal** | `type/listar-documentos` |

---

## 🎯 **Objetivo**

Implementar o padrão completo de qualidade no caso de uso `ListarDocumentos`, que já possuía testes parciais (55% cobertura), seguindo a metodologia estabelecida nas fases anteriores:

1. **Adicionar telemetria** com o padrão `_telemetry` e `configure_telemetry`
2. **Expandir testes de lógica** para cobrir métodos não testados (`listar_tipos`, `_verificar_traducoes`)
3. **Criar testes de telemetria** para verificar a instrumentação
4. **Corrigir type hints** (MyPy) no arquivo (3 erros iniciais)
5. **Aumentar cobertura** de 55% para 80%

---

## 🔍 **Estado Inicial**

### 📊 **Métricas Antes da Intervenção**

| Métrica | Valor |
|---------|-------|
| **Cobertura** | 55% |
| **Testes existentes** | 1 (em `test_use_cases.py`) |
| **Telemetria** | ❌ Ausente |
| **MyPy no arquivo** | ⚠️ 3 erros |
| **Linhas de código** | 51 |

### 📋 **Arquivo Alvo**
```python
# src/application/use_cases/listar_documentos.py
"""
Caso de uso: Listar documentos com paginação e filtros.
"""

class ListarDocumentos:
    """
    Caso de uso para listar documentos.
    """
    # ... lógica existente com 55% cobertura ...
```

---

## 🛠️ **Implementação Realizada**

### **1. Adição do Padrão de Telemetria**

```python
# Telemetria opcional
_telemetry = None

def configure_telemetry(telemetry_instance=None):
    """Configura telemetria para este módulo (usado apenas em testes)."""
    global _telemetry
    _telemetry = telemetry_instance
```

### **2. Instrumentação dos Métodos**

Foram adicionados contadores de telemetria em todos os métodos principais:

| Método | Eventos registrados |
|--------|---------------------|
| `executar` | `iniciado`, `pagina.{pagina}`, `concluido`, `resultados` |
| `com_traducao_nomes` | `com_traducao_nomes` |
| `listar_tipos` | `iniciado`, `concluido`, `tipos_encontrados` |
| `_verificar_traducoes` | `iniciado`, `sucesso`, `erro` |

### **3. Correções de Type Hints (MyPy)**

**Problemas iniciais (3 erros):**

| Linha | Erro | Solução |
|-------|------|---------|
| 28 | `Incompatible types in assignment (expression has type "bool", variable has type "None")` | `self._tradutor_nomes: Optional[bool] = None` |
| 53 | `Argument 1 to "_verificar_traducoes" has incompatible type "int | None"` | Adicionar `if doc.id is not None:` |
| 81 | `Need type annotation for "counter"` | `counter: CounterType[str] = Counter()` |

---

## 🧪 **Testes Criados/Expandidos**

### **Testes de Lógica (`test_listar_documentos.py` - 12 testes)**

| # | Teste | Descrição |
|---|-------|-----------|
| 1 | `test_executar_com_paginacao_basica` | Paginação básica |
| 2 | `test_executar_com_filtros` | Filtros por centro/tipo |
| 3 | `test_executar_pagina_2` | Cálculo de offset |
| 4 | `test_executar_sem_resultados` | Lista vazia |
| 5 | `test_com_traducao_nomes_fluent` | Método fluente |
| 6 | `test_listar_tipos_basico` | Listagem de tipos |
| 7 | `test_listar_tipos_com_filtro_centro` | Filtro por centro |
| 8 | `test_listar_tipos_com_tipos_variados` | Múltiplos tipos |
| 9 | `test_listar_tipos_sem_tipos` | Documentos sem tipo |
| 10 | `test_verificar_traducoes_com_sucesso` | Consulta com traduções |
| 11 | `test_verificar_traducoes_sem_traducao` | Consulta sem traduções |
| 12 | `test_verificar_traducoes_com_erro` | Tratamento de exceção |

### **Testes de Telemetria (`test_listar_documentos_telemetry.py` - 6 testes)**

| # | Teste | Descrição |
|---|-------|-----------|
| 1 | `test_telemetria_executar` | Verifica eventos de execução |
| 2 | `test_telemetria_com_traducao_nomes` | Verifica chamada de configuração |
| 3 | `test_telemetria_listar_tipos` | Verifica listagem de tipos |
| 4 | `test_telemetria_verificar_traducoes_sucesso` | Verifica consulta bem-sucedida |
| 5 | `test_telemetria_verificar_traducoes_erro` | Verifica tratamento de erro |
| 6 | `test_sem_telemetria_nao_quebra` | Garante fallback sem telemetria |

---

## 🐛 **Desafios Encontrados e Soluções**

### **Desafio 1: Type Hints e Optional**

**Problema:**
```python
self._tradutor_nomes = ativo  # ativo é bool, mas variável foi declarada como None
```

**Solução:** Declarar corretamente o tipo como `Optional[bool]`.

```python
self._tradutor_nomes: Optional[bool] = None
```

---

### **Desafio 2: ID Opcional do Documento**

**Problema:**
```python
self._verificar_traducoes(doc.id)  # doc.id pode ser None
```

**Solução:** Adicionar verificação antes da chamada.

```python
if doc.id is not None:
    tem_traducao = self._verificar_traducoes(doc.id)
```

---

### **Desafio 3: Mock de Context Manager**

**Problema:** Ao testar `_verificar_traducoes`, os mocks precisavam simular um context manager (`with repo._conexao() as conn`).

```python
AttributeError: __enter__
```

**Solução:** Usar `MagicMock` para simular corretamente os métodos mágicos `__enter__` e `__exit__`.

```python
mock_context_manager = MagicMock()
mock_repo._conexao.return_value = mock_context_manager
mock_context_manager.__enter__.return_value = mock_conn
```

---

### **Desafio 4: Teste de Exceção com SQLite**

**Problema:** Testar o bloco `except` que captura erros de conexão com o banco.

**Solução:** Configurar o mock para lançar exceção no método `_conexao`.

```python
mock_repo._conexao.side_effect = Exception("Erro simulado")
resultado = use_case._verificar_traducoes(1)
assert resultado is False  # Fallback seguro
```

---

## 📊 **Resultados Finais**

### **Métricas Antes e Depois**

| Métrica | Antes | Depois | Evolução |
|---------|-------|--------|----------|
| **Cobertura do arquivo** | 55% | **80%** | 📈 **+25 p.p.** |
| **Testes de lógica** | 1 | 12 | ✅ +11 novos |
| **Testes de telemetria** | 0 | 6 | ✅ +6 novos |
| **Total de testes** | 1 | 18 | ✅ +17 novos |
| **MyPy no arquivo** | 3 erros | 0 erros | ✅ Resolvido |
| **Telemetria** | ❌ Ausente | ✅ Completa | ✅ |

### **Cobertura Detalhada**
```
src/application/use_cases/listar_documentos.py
├── Linhas totais: 76
├── Linhas cobertas: 61
└── Cobertura: 80%
```

As linhas não cobertas incluem principalmente:
- Tratamento de exceções em `listar_tipos` (fallback de ícones)
- Branches específicas de formatação de tipos desconhecidos

---

## 📝 **Lições Aprendidas**

1. **Mock de context managers:** Ao testar código que usa `with`, é necessário usar `MagicMock` para simular os métodos `__enter__` e `__exit__`.

2. **Optional e type hints:** Sempre declarar variáveis que podem receber `None` com `Optional[Tipo]`.

3. **IDs opcionais:** Entidades podem ter IDs nulos (novos objetos). Sempre verificar antes de usar.

4. **Testes de fallback:** É importante testar não apenas o caminho feliz, mas também os blocos `except` para garantir que o sistema não quebra.

5. **Organização de testes:** Manter todos os testes dentro da classe de teste evita problemas de fixtures e escopo.

---

## 📚 **Arquivos Modificados/Criados**

```
Modificados:
├── src/application/use_cases/listar_documentos.py

Criados/Substituídos:
├── src/tests/test_listar_documentos.py
└── src/tests/test_listar_documentos_telemetry.py
```

---

## 📈 **Impacto no Projeto**

- **Cobertura global:** Aumento de 74% → ~75% (estimado)
- **Qualidade:** Padrão de telemetria agora presente em mais um caso de uso crítico
- **Manutenibilidade:** Testes robustos garantem que alterações futuras não quebrem funcionalidades
- **Type safety:** Todos os erros de MyPy no arquivo foram eliminados

---

## 🔮 **Próximos Passos**

### **Candidatos para próxima fase:**
- `src/application/use_cases/classificar_documento.py` (65% cobertura)
- `src/application/use_cases/obter_documento.py` (57% cobertura)
- `src/application/use_cases/estatisticas.py` (15% cobertura - precisa de atenção)

### **Médio prazo:**
- [ ] Corrigir erros de MyPy em outros arquivos (`estatisticas.py`, `config/__init__.py`)
- [ ] Instalar stubs para módulos externos (`types-PyYAML`)

---

## 👤 **Autor**

**Thiago Ribeiro** - Projeto de TCC

---

## 📜 **Histórico de Revisões**

| Versão | Data | Autor | Alterações |
|--------|------|-------|------------|
| 1.0 | 20/02/2026 | Thiago Ribeiro | Documento inicial da FASE 16 |

---

<div align="center">
  <sub>FASE 16 - Telemetria e Expansão de Testes em ListarDocumentos</sub>
  <br>
  <sub>Versão 1.0 - 20 de Fevereiro de 2026</sub>
  <br>
  <sub>✅ Fase concluída com sucesso</sub>
</div>
```

---
