# 📚 **DOCUMENTO: QUALITY FLOW OFICIAL - SHOWTRIALS**

<div align="center">

**Critérios obrigatórios de qualidade técnica em conformidade com a governança do projeto**

</div>

## 📅 **Informações do Documento**

| Item | Descrição |
|------|-----------|
| **Data** | 22 de Fevereiro de 2026 |
| **Autor** | Thiago Ribeiro |
| **Versão** | 2.0 |
| **Relacionado a** | [GOVERNANCA.md](GOVERNANCA.md), [Git Flow Oficial](git_flow.md), Milestone ativa |

---

## 🎯 **OBJETIVO**

Estabelecer critérios **obrigatórios** de qualidade técnica em **total aderência à governança do projeto**, garantindo:

- ✅ Correção funcional antes de otimização
- ✅ Clareza estrutural antes de abstração
- ✅ Arquitetura explícita antes de conveniência
- ✅ Mudanças pequenas e verificáveis
- ✅ Nenhuma mudança estrutural implícita
- ✅ Qualidade como critério de aceite, não melhoria opcional

---

## 📊 **PRINCÍPIOS DE QUALIDADE**

| Princípio | Descrição |
|-----------|-----------|
| **1** | Correção funcional antes de otimização |
| **2** | Clareza estrutural antes de abstração |
| **3** | Arquitetura explícita antes de conveniência |
| **4** | Mudanças pequenas e verificáveis |
| **5** | Nenhuma mudança estrutural implícita |
| **6** | Qualidade é critério de aceite, não opcional |

---

## ✅ **CRITÉRIOS OBRIGATÓRIOS ANTES DE MERGE**

Toda issue só pode ser considerada concluída se:

| Categoria | Critério |
|-----------|----------|
| **Escopo** | ✅ Critérios de aceite definidos na issue foram atendidos |
| **Execução** | ✅ Código compila e executa sem erro |
| **Tipagem** | ✅ Tipagem consistente (sem `Any` não justificado) |
| **Limpeza** | ✅ Sem código morto, prints ou logs temporários |
| **Dívida** | ✅ Sem comentários "TODO" não justificados |
| **Efeitos** | ✅ Sem efeitos colaterais não documentados |
| **Arquitetura** | ✅ Respeita o modelo arquitetural definido |
| **Acoplamento** | ✅ Sem acoplamento indevido com persistência |
| **Pureza** | ✅ Transformadores permanecem puros |
| **Responsabilidade** | ✅ Responsabilidade no módulo correto |

---

## 🔤 **TIPAGEM E CONSISTÊNCIA**

### **Regras Obrigatórias**

```python
# ✅ CORRETO - tipos explícitos
def classificar(documento: Documento) -> Documento:
    return documento

# ✅ CORRETO - Optional quando necessário
def buscar_por_id(id: Optional[int]) -> Optional[Documento]:

# ❌ INCORRETO - Any sem justificativa
def processar(dados: Any) -> Any:

# ❌ INCORRETO - tipos implícitos
def processar(dados):
```

### **Durante Milestone Estrutural (Engine)**

- ✅ Tipagem consistente é **obrigatória**
- ✅ Interfaces devem ser **explícitas**
- ✅ Contratos não podem ser **ambíguos**
- ✅ Módulos devem ter responsabilidades **claras**
- ✅ Dependências entre módulos devem ser **explícitas**

---

## 🏗️ **COERÊNCIA ARQUITETURAL**

### **Checklist Pré-Merge**

Antes de qualquer merge, validar:

```markdown
## 📋 Validação Arquitetural

- [ ] A alteração respeita o modelo arquitetural definido?
- [ ] Não há acoplamento indevido com persistência?
- [ ] Transformadores permanecem puros?
- [ ] Separação entre execução e configuração foi mantida?
- [ ] A responsabilidade está no módulo correto?
- [ ] Dependências externas são injetáveis?
- [ ] Lógica não está acoplada a IO?
```

**Se qualquer resposta for negativa, a issue não deve ser encerrada.**

---

## 📦 **ESCOPO E ISOLAMENTO**

### **Regra Fundamental**

Uma issue deve:

| Deve | Não Deve |
|------|----------|
| ✅ Resolver apenas o problema descrito | ❌ Incluir refatorações oportunistas |
| ✅ Manter-se dentro do escopo definido | ❌ Alterar comportamento não relacionado |
| ✅ Ser verificável isoladamente | ❌ Misturar responsabilidades |

**Refatorações adicionais exigem nova issue.**

### **Exemplo Prático**

```python
# Issue #42: Corrigir bug no exportador

# ✅ CORRETO - apenas o bug
def exportar(documento_id: int):
    if documento_id is None:  # ← correção do bug
        return {"erro": "ID inválido"}
    # ... resto do código existente

# ❌ INCORRETO - bug + refatoração
def exportar(documento_id: int):
    # corrigiu bug
    # extraiu método _validar_id
    # renomeou variáveis
    # mudou formatação
```

---

## 🧪 **TESTABILIDADE**

### **Requisitos Mínimos**

Mesmo que o MVP ainda não possua cobertura completa de testes:

```python
# ✅ Código estruturado para ser testável
class Classificador:
    def __init__(self, repo: RepositorioDocumento):  # injetável
        self.repo = repo

    def classificar(self, documento: Documento) -> Documento:  # puro
        # lógica sem IO
        return documento

# ❌ Código não testável
class Classificador:
    def classificar(self, id: int):  # acoplado a banco
        documento = sqlite3.connect().execute(...)  # IO direto
```

### **Padrões Obrigatórios**

- ✅ Transformadores devem ser **isoláveis**
- ✅ Dependências externas devem ser **injetáveis**
- ✅ Lógica não deve estar **acoplada a IO**
- ✅ Efeitos colaterais devem ser **explícitos**

---

## 🔄 **REVISÃO TÉCNICA (CHECKLIST)**

### **Template de Revisão para PRs**

````markdown
## ✅ Checklist de Qualidade

### Escopo e Critérios
- [ ] Critérios de aceite cumpridos
- [ ] Nenhuma alteração fora de escopo

### Arquitetura
- [ ] Respeita o modelo arquitetural definido
- [ ] Sem acoplamento indevido com persistência
- [ ] Transformadores permanecem puros
- [ ] Separação execução/configuração mantida
- [ ] Responsabilidade no módulo correto

### Código
- [ ] Tipagem adequada (sem `Any` não justificado)
- [ ] Sem código morto
- [ ] Sem prints/logs temporários
- [ ] Sem comentários TODO não justificados

### Dependências
- [ ] Dependências externas são injetáveis
- [ ] Lógica não acoplada a IO
- [ ] Sem dependências ocultas

### Documentação
- [ ] Impacto arquitetural documentado (se aplicável)
- [ ] PR referenciando issue (`Closes #N`)
````

---

## 📊 **CONTROLE DE COMPLEXIDADE**

### **O que Evitar**

```python
# ❌ Classe com múltiplas responsabilidades
class ProcessadorTudo:
    def classificar(self): ...
    def traduzir(self): ...
    def exportar(self): ...
    def conectar_banco(self): ...

# ❌ Método excessivamente longo
def processar_tudo():  # 200 linhas
    # faz coisa 1
    # faz coisa 2
    # faz coisa 3
    # ...

# ❌ Estruturas condicionais profundas
if a:
    if b:
        if c:
            if d:
                # ...

# ❌ Lógica de orquestração dentro de transformadores
def transformar(documento):
    self.repo.salvar(documento)  # orquestração, não transformação
```

### **O que Preferir**

```python
# ✅ Funções pequenas e puras
def classificar(documento: Documento) -> Documento:
    """Apenas classificação, sem efeitos colaterais."""
    documento.tipo = regras.classificar(documento.titulo)
    return documento

# ✅ Interfaces explícitas
class Transformer(ABC):
    @abstractmethod
    def transformar(self, contexto: Contexto) -> Contexto:
        pass

# ✅ Separação clara
# engine/transformers.py  → lógica pura
# engine/orquestrador.py   → coordenação
# infrastructure/          → IO, banco, etc.
```

---

## 🎯 **MUDANÇAS ESTRUTURAIS**

### **Regras para Alterações Arquiteturais**

| Requisito | Obrigação |
|-----------|-----------|
| **Tipo de issue** | `type:engine` ou `type:refactor` |
| **Discussão prévia** | Deve ser discutida antes da implementação |
| **Justificativa** | Deve justificar impacto na evolução do MVP |
| **Escopo** | Não pode ocorrer dentro de issue de feature |

### **O que Caracteriza Mudança Estrutural**

- Criação/modificação de contratos fundamentais
- Alteração no modelo de execução
- Mudança na separação de camadas
- Introdução de novas abstrações core
- Refatoração que afeta múltiplos módulos

**Mudança estrutural implícita é considerada falha de qualidade.**

---

## 🤖 **AUTOMAÇÃO COM TASKIPY**

### **Comandos para Verificação de Qualidade**

```toml
[tool.taskipy.tasks]
# === QUALIDADE (alinhada à governança) ===
check-structural = "python scripts/validar_arquitetura.py"  # futuro
check-scope = "git diff main...HEAD --name-only | grep -v '^docs/' | wc -l"  # mudanças fora de docs?

# === Validação de Issue ===
validate-issue = "gh issue view $(git branch --show-current | cut -d/ -f2-) --json title,labels,milestone"
check-milestone = "gh issue list --milestone 'MVP - Engine de Pipeline' --assignee @me"
```

---

## 📋 **COMANDOS RÁPIDOS**

```bash
# Verificar qualidade geral
task check
task test-cov

# Verificar arquivo específico
task lint-file --path src/engine/transformer.py
task type-file --path src/engine/transformer.py
task test-file --path tests/test_engine.py

# Verificar cobertura
task cov-file --path src/engine/transformer.py

# Validar alinhamento com milestone
task milestone-active
task validate-issue
```

---

## ✅ **CHECKSUM DE QUALIDADE POR ISSUE**

### **Antes de Iniciar**
- [ ] Issue tem critérios de aceite claros?
- [ ] Tipo da issue (`engine/`, `infra/`, etc.) está correto?
- [ ] Issue está na milestone ativa?

### **Durante Desenvolvimento**
- [ ] Código estruturado para ser testável?
- [ ] Transformadores puros e isoláveis?
- [ ] Dependências injetáveis?
- [ ] Nenhuma mudança estrutural implícita?

### **Antes do PR**
- [ ] `task check-file` passa?
- [ ] `task cov-file` >= 85%?
- [ ] Checklist de qualidade preenchido?
- [ ] Impacto arquitetural documentado?

### **Antes do Merge**
- [ ] CI verde?
- [ ] Nenhum desvio arquitetural?
- [ ] Sem código morto?
- [ ] Sem dependências ocultas?
- [ ] Sem alterações fora de escopo?

### **Após Merge**
- [ ] Issue fechou automaticamente?
- [ ] Movida para `Done` no Kanban?
- [ ] (Se estrutural) Documentação atualizada?

---

## 🚨 **O QUE NÃO FAZER**

```bash
# ❌ NÃO ignorar os critérios de aceite
# "funciona na minha máquina" não é suficiente

# ❌ NÃO introduzir mudanças estruturais em issues de feature
# engine/ em feature/dark-mode? NÃO!

# ❌ NÃO deixar TODO sem justificativa
# TODO: otimizar depois  # PRECISA DE ISSUE?

# ❌ NÃO misturar IO com lógica pura
def classificar(documento):
    self.repo.salvar(documento)  # IO no transformador!

# ❌ NÃO pular o checklist de qualidade
# "depois a gente revisa"  # NUNCA!
```

---

## 🏆 **BENEFÍCIOS DESTE FLUXO**

| Antes | Depois |
|-------|--------|
| ❌ Qualidade como opção | ✅ Qualidade como critério de aceite |
| ❌ Mudanças estruturais implícitas | ✅ Issues `type:engine` explícitas |
| ❌ Código não testável | ✅ Estrutura preparada para testes |
| ❌ Acoplamento com persistência | ✅ Transformadores puros |
| ❌ Escopo vazando | ✅ Isolamento por issue |
| ❌ Revisão subjetiva | ✅ Checklist objetivo |

---

## 📚 **REFERÊNCIAS**

- [GOVERNANCA.md](GOVERNANCA.md) - Política de governança do projeto
- [Git Flow Oficial](git_flow.md) - Fluxo de branches e releases
- [Ruff Documentation](https://beta.ruff.rs/docs/)
- [MyPy Documentation](https://mypy.readthedocs.io/)
- [Pytest Documentation](https://docs.pytest.org/)

---

## 👤 **AUTOR**

**Thiago Ribeiro** - Projeto de TCC

---

<div align="center">
  <sub>Quality Flow Oficial - ShowTrials</sub>
  <br>
  <sub>Versão 2.0 - 22 de Fevereiro de 2026</sub>
  <br>
  <sub>✅ Em conformidade com a GOVERNANCA.md</sub>
</div>
