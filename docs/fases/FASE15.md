## 📄 **FASE15.md - Telemetria e Testes em GerarRelatorio**

```markdown
# FASE 15 - Telemetria e Testes em GerarRelatorio

<div align="center">

**Implementação completa de telemetria, testes e type hints no caso de uso de geração de relatórios**

</div>

## 📅 **Informações da Fase**

| Item | Descrição |
|------|-----------|
| **Status** | ✅ Concluída |
| **Data de Conclusão** | 20 de Fevereiro de 2026 |
| **Artefatos** | `gerar_relatorio.py`, `test_gerar_relatorio.py`, `test_gerar_relatorio_telemetry.py` |
| **Dependências** | FASE 14 (ExportarDocumento), FASE 12 (Padronização de Telemetria) |
| **Branch principal** | `type/gerar-relatorio` |

---

## 🎯 **Objetivo**

Implementar o padrão completo de qualidade no caso de uso `GerarRelatorio`, seguindo a metodologia estabelecida nas fases anteriores:

1. **Adicionar telemetria** com o padrão `_telemetry` e `configure_telemetry`
2. **Criar testes de lógica** para cobrir todos os fluxos de agregação de dados
3. **Criar testes de telemetria** para verificar a instrumentação
4. **Corrigir type hints** (MyPy) no arquivo (7 erros iniciais)
5. **Aumentar cobertura** de 0% para 86%

---

## 🔍 **Estado Inicial**

### 📊 **Métricas Antes da Intervenção**

| Métrica | Valor |
|---------|-------|
| **Cobertura** | 0% |
| **Testes existentes** | Nenhum |
| **Telemetria** | ❌ Ausente |
| **MyPy no arquivo** | ⚠️ 7 erros |
| **Linhas de código** | 153 |

### 📋 **Arquivo Alvo**
```python
# src/application/use_cases/gerar_relatorio.py
"""
Caso de uso: Gerar relatórios avançados.
"""

class GerarRelatorio:
    """
    Caso de uso para gerar relatórios avançados.
    """
    # ... lógica complexa de agregação ...
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
| `_coletar_dados` | `iniciado`, `concluido`, `documentos_processados` |
| `gerar_relatorio_txt` | `iniciado`, `concluido` |
| `salvar_relatorio` | `iniciado`, `formato.{formato}`, `sucesso_txt`, `html_placeholder`, `formato_invalido` |

### **3. Correções de Type Hints (MyPy)**

**Problema inicial:** 7 erros, principalmente:
- Counters sem anotação de tipo
- Chamada de `listar_por_documento` com `doc.id` podendo ser `None`

**Soluções aplicadas:**

```python
# Antes
centro_counter = Counter()

# Depois
centro_counter: Counter[str] = Counter()
```

```python
# Antes (linha 124)
traducoes = self.repo_trad.listar_por_documento(doc.id)

# Depois
if doc.id is not None:
    traducoes = self.repo_trad.listar_por_documento(doc.id)
```

---

## 🧪 **Testes Criados**

### **Testes de Lógica (`test_gerar_relatorio.py` - 12 testes)**

| # | Teste | Descrição |
|---|-------|-----------|
| 1 | `test_coletar_dados_basico` | Agregação básica por centro |
| 2 | `test_coletar_dados_com_traducoes` | Contagem de traduções |
| 3 | `test_coletar_dados_com_contagens_especificas` | Tipos especiais (cartas, relatórios, etc.) |
| 4 | `test_coletar_dados_com_anexos` | Documentos com anexos |
| 5 | `test_coletar_dados_com_anos` | Extração de anos das datas |
| 6 | `test_gerar_relatorio_txt_formato` | Formatação do relatório |
| 7 | `test_salvar_relatorio_txt` | Salvamento em arquivo |
| 8 | `test_salvar_relatorio_html_placeholder` | Placeholder HTML |
| 9 | `test_salvar_relatorio_formato_invalido` | Formato não suportado |
| 10 | `test_pessoas_frequentes_com_traducao` | Tradução de nomes |
| 11 | `test_sem_repo_trad_nao_quebra` | Fallback sem traduções |
| 12 | `test_documentos_sem_tipo_sao_ignorados` | Robustez com dados incompletos |

### **Testes de Telemetria (`test_gerar_relatorio_telemetry.py` - 6 testes)**

| # | Teste | Descrição |
|---|-------|-----------|
| 1 | `test_telemetria_coletar_dados` | Verifica eventos de coleta |
| 2 | `test_telemetria_gerar_txt` | Verifica geração de relatório |
| 3 | `test_telemetria_salvar_txt` | Verifica salvamento TXT |
| 4 | `test_telemetria_salvar_html` | Verifica placeholder HTML |
| 5 | `test_telemetria_salvar_formato_invalido` | Verifica formato inválido |
| 6 | `test_sem_telemetria_nao_quebra` | Garante fallback sem telemetria |

---

## 🐛 **Desafios Encontrados e Soluções**

### **Desafio 1: Type Hints nos Counters**

**Problema:**
```python
src/application/use_cases/gerar_relatorio.py:36: error: Need type annotation for "centro_counter"
```

**Solução:** Adicionar anotações de tipo em todos os Counters.

```python
centro_counter: Counter[str] = Counter()
tipo_counter: Counter[str] = Counter()
pessoa_counter: Counter[str] = Counter()
ano_counter: Counter[str] = Counter()
mes_counter: Counter[str] = Counter()
```

---

### **Desafio 2: Optional[int] vs int**

**Problema:**
```python
src/application/use_cases/gerar_relatorio.py:124: error: Argument 1 to "listar_por_documento" has incompatible type "int | None"; expected "int"
```

**Causa:** O campo `id` da entidade `Documento` é opcional, mas o repositório espera um `int` obrigatório.

**Solução:** Adicionar verificação de nulidade antes da chamada.

```python
for doc in documentos[:100]:
    if doc.id is not None:  # ← VERIFICAÇÃO CRÍTICA
        traducoes = self.repo_trad.listar_por_documento(doc.id)
        # ... resto do código
```

---

### **Desafio 3: Complexidade da Lógica de Agregação**

O método `_coletar_dados` tem múltiplos contadores e lógica condicional, exigindo testes abrangentes para garantir que todas as branches sejam cobertas.

**Solução:** Criar mocks específicos para cada cenário:
- Documentos com diferentes centros
- Documentos com diferentes tipos
- Documentos com/sem anexos
- Documentos com datas variadas
- Documentos com/sem traduções

---

### **Desafio 4: Performance vs Cobertura**

O código original limitava a análise de traduções aos primeiros 100 documentos por questão de performance. Isso precisava ser testado sem comprometer a velocidade dos testes.

**Solução:** Nos testes, usar poucos documentos (5-10) mas garantir que a lógica de contagem funciona corretamente.

---

## 📊 **Resultados Finais**

### **Métricas Antes e Depois**

| Métrica | Antes | Depois | Evolução |
|---------|-------|--------|----------|
| **Cobertura do arquivo** | 0% | 86% | 📈 **+86 p.p.** |
| **Testes de lógica** | 0 | 12 | ✅ 12 novos |
| **Testes de telemetria** | 0 | 6 | ✅ 6 novos |
| **Total de testes** | 0 | 18 | ✅ 18 novos |
| **MyPy no arquivo** | 7 erros | 0 erros | ✅ Resolvido |
| **Telemetria** | ❌ Ausente | ✅ Completa | ✅ |

### **Cobertura Detalhada**
```
src/application/use_cases/gerar_relatorio.py
├── Linhas totais: 175
├── Linhas cobertas: 151
└── Cobertura: 86%
```

As linhas não cobertas são principalmente:
- Tratamento de exceções em tradução de nomes (fallback)
- Branches de meses específicos (Dezembro/Novembro)
- Casos de formato HTML (placeholder)

---

## 📝 **Lições Aprendidas**

1. **Type hints em Counters:** Sempre anotar o tipo dos elementos ao usar `Counter()` para evitar erros de MyPy.

2. **IDs opcionais:** Entidades podem ter IDs nulos (novos objetos não persistidos). Sempre verificar antes de usar.

3. **Mocks complexos:** Para testar lógica de agregação, criar fixtures que retornam conjuntos variados de documentos.

4. **Cobertura de branches:** A lógica com múltiplos `if` encadeados (tipos de documento, meses) exige testes específicos para cada condição.

5. **Performance em testes:** Usar amostras pequenas (5-10 documentos) nos testes, mesmo que o código real use limites maiores.

---

## 📚 **Arquivos Modificados/Criados**

```
Modificados:
├── src/application/use_cases/gerar_relatorio.py

Criados:
├── src/tests/test_gerar_relatorio.py
└── src/tests/test_gerar_relatorio_telemetry.py
```

---

## 📈 **Impacto no Projeto**

- **Cobertura global:** Aumento de 68% → ~70% (estimado)
- **Qualidade:** Padrão de telemetria agora presente em mais um caso de uso crítico
- **Manutenibilidade:** Testes garantem que alterações futuras na lógica de relatórios não quebrem funcionalidades
- **Type safety:** Todos os erros de MyPy no arquivo foram eliminados

---

## 🔮 **Próximos Passos**

### **Imediato:**
- [ ] Fazer merge da branch `type/gerar-relatorio` na `main`
- [ ] Escolher próximo arquivo com baixa cobertura

### **Candidatos para próxima fase:**
- `src/application/use_cases/listar_documentos.py` (55% cobertura)
- `src/application/use_cases/classificar_documento.py` (65% cobertura)
- `src/application/use_cases/obter_documento.py` (57% cobertura)

### **Médio prazo:**
- [ ] Corrigir erros de MyPy em outros arquivos (estatisticas.py, config/__init__.py)
- [ ] Instalar stubs para módulos externos (types-PyYAML)

---

## 👤 **Autor**

**Thiago Ribeiro** - Projeto de TCC

---

## 📜 **Histórico de Revisões**

| Versão | Data | Autor | Alterações |
|--------|------|-------|------------|
| 1.0 | 20/02/2026 | Thiago Ribeiro | Documento inicial da FASE 15 |

---

<div align="center">
  <sub>FASE 15 - Telemetria e Testes em GerarRelatorio</sub>
  <br>
  <sub>Versão 1.0 - 20 de Fevereiro de 2026</sub>
  <br>
  <sub>✅ Fase concluída com sucesso</sub>
</div>
```

---
