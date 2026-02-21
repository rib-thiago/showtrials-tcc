## 📋 **ANÁLISE COMPLETA: O PROBLEMA DOS TESTES DE TELEMETRIA**

Thiago, agora ficou claro! Olhando seus arquivos:

### 🔍 **O QUE ESTÁ ACONTECENDO:**

1. **`tipo_documento.py`** tem um padrão de telemetria **DIFERENTE** dos outros arquivos:
   - Usa `try/except ImportError` com fallback
   - Tem `@monitor` decorator
   - **NÃO TEM** o padrão `_telemetry` e `configure_telemetry`

2. **`test_tipo_documento_telemetry.py`** espera o padrão **QUE VOCÊ USA EM TODOS OS OUTROS ARQUIVOS**:
   - Chama `td_module.configure_telemetry()`
   - Espera que `_telemetry` seja uma variável global

### 📊 **COMPARAÇÃO COM OUTROS ARQUIVOS (ex: analisar_texto.py):**

```python
# Padrão que você consolidou (e os testes esperam)
_telemetry = None

def configure_telemetry(telemetry_instance=None):
    global _telemetry
    _telemetry = telemetry_instance

# No método:
if _telemetry:
    _telemetry.increment("...")
```

```python
# O que está em tipo_documento.py (diferente)
try:
    from src.infrastructure.telemetry import monitor as telemetry_monitor
    TELEMETRY_AVAILABLE = True
    monitor = telemetry_monitor
except ImportError:
    TELEMETRY_AVAILABLE = False
    def monitor(name: Optional[str] = None) -> Callable:
        def decorator(func: Callable) -> Callable:
            return func
        return decorator
```

---

## 🎯 **SOLUÇÃO: PADRONIZAR O ARQUIVO**

Vamos alterar `tipo_documento.py` para seguir EXATAMENTE o mesmo padrão dos outros arquivos que já funcionam.

---

# FASE 12 - Padronização da Telemetria no TipoDocumento

<div align="center">

**Correção dos testes de telemetria e unificação do padrão de instrumentação**

</div>

## 📅 **Informações da Fase**

| Item | Descrição |
|------|-----------|
| **Status** | ⏳ Em andamento |
| **Data de Início** | 19 de Fevereiro de 2026 |
| **Artefatos** | `tipo_documento.py` corrigido, Testes passando |
| **Dependências** | FASE 11 (CI), FASE 8 (Análise de Texto) |

---

## 🎯 **Objetivo**

Padronizar a implementação da telemetria no arquivo `tipo_documento.py` para seguir o mesmo padrão utilizado em todos os outros arquivos do projeto, resolvendo os 4 testes falhando e garantindo consistência na instrumentação.

---

## 🔬 **Diagnóstico**

### 📊 **Estado Atual**

```
📁 ARQUIVO: src/domain/value_objects/tipo_documento.py
🔴 TESTES FALHANDO: 4 (todos de telemetria)
📈 COBERTURA ATUAL: 83%
🎯 META: 45% (já ultrapassada)
```

### 🔍 **Problema Identificado**

O arquivo `tipo_documento.py` implementa um padrão de telemetria diferente do restante do projeto:

| Característica | Padrão do Projeto | `tipo_documento.py` |
|----------------|-------------------|---------------------|
| Variável `_telemetry` | ✅ Sim | ❌ Não |
| Função `configure_telemetry` | ✅ Sim | ❌ Não |
| Uso de decorator `@monitor` | ❌ Não | ✅ Sim |
| `if _telemetry:` nos métodos | ✅ Sim | ❌ Não |

### 📋 **Consequências**

Os testes em `test_tipo_documento_telemetry.py` esperam o padrão do projeto, mas encontram outro, causando:

```python
E   AttributeError: module 'src.domain.value_objects.tipo_documento' has no attribute 'configure_telemetry'
```

---

## 🛠️ **Solução Proposta**

Substituir a implementação atual de telemetria em `tipo_documento.py` pelo padrão consolidado no projeto:

1. Remover o decorator `@monitor`
2. Adicionar variável global `_telemetry`
3. Adicionar função `configure_telemetry`
4. Adicionar verificações `if _telemetry:` nos métodos relevantes

---

## 📝 **Passo a Passo da Correção**

### **Passo 1: Criar branch de correção**

```bash
# Certifique-se de estar na main atualizada
git checkout main
git pull origin main

# Criar branch seguindo o padrão
git checkout -b fix/tipo-documento-telemetry
```

### **Passo 2: Editar o arquivo `src/domain/value_objects/tipo_documento.py`**

Substitua TODO o conteúdo pelo código abaixo:

```python
# src/domain/value_objects/tipo_documento.py
"""
Value Object: TipoDocumento
Representa os tipos possíveis de documentos históricos.
"""

from enum import Enum
from typing import Dict, List, Optional

# Telemetria opcional (padrão do projeto)
_telemetry = None


def configure_telemetry(telemetry_instance=None):
    """Configura telemetria para este módulo (usado apenas em testes)."""
    global _telemetry
    _telemetry = telemetry_instance


class TipoDocumento(Enum):
    """
    Enumeração dos tipos de documento identificados no acervo.
    """

    INTERROGATORIO = "interrogatorio"
    ACAREACAO = "acareacao"
    ACUSACAO = "acusacao"
    DECLARACAO = "declaracao"
    CARTA = "carta"
    RELATORIO = "relatorio"
    DEPOIMENTO = "depoimento"
    LAUDO = "laudo"
    DESCONHECIDO = "desconhecido"

    @property
    def descricao_pt(self) -> str:
        """Descrição em português para UI"""
        descricoes: Dict[str, str] = {
            "interrogatorio": "Protocolo de Interrogatório",
            "acareacao": "Protocolo de Acareação",
            "acusacao": "Auto de Acusação",
            "declaracao": "Declaração/Requerimento",
            "carta": "Correspondência",
            "relatorio": "Relatório Especial (NKVD)",
            "depoimento": "Depoimento Espontâneo",
            "laudo": "Laudo Pericial",
            "desconhecido": "Não classificado",
        }
        return descricoes[self.value]

    @property
    def descricao_en(self) -> str:
        """Descrição em inglês para exportação"""
        descricoes: Dict[str, str] = {
            "interrogatorio": "Interrogation Protocol",
            "acareacao": "Confrontation Protocol",
            "acusacao": "Indictment",
            "declaracao": "Statement",
            "carta": "Correspondence",
            "relatorio": "NKVD Special Report",
            "depoimento": "Testimony",
            "laudo": "Forensic Report",
            "desconhecido": "Unclassified",
        }
        return descricoes[self.value]

    @property
    def icone(self) -> str:
        """Ícone para UI"""
        icones: Dict[str, str] = {
            "interrogatorio": "🔍",
            "acareacao": "⚖️",
            "acusacao": "📜",
            "declaracao": "📝",
            "carta": "✉️",
            "relatorio": "📋",
            "depoimento": "🗣️",
            "laudo": "🏥",
            "desconhecido": "📄",
        }
        return icones[self.value]

    @classmethod
    def from_titulo(cls, titulo: str) -> "TipoDocumento":
        """
        Classifica o tipo baseado no título em russo.
        """
        global _telemetry

        if not titulo:
            if _telemetry:
                _telemetry.increment("tipo_documento.titulo_vazio")
            return cls.DESCONHECIDO

        # Mapeamento de padrões para tipos
        padroes: Dict[str, List[str]] = {
            "interrogatorio": ["Протокол допроса"],
            "acareacao": ["Протокол очной ставки"],
            "acusacao": ["Проект обвинительного заключения", "Обвинительное заключение"],
            "declaracao": ["Заявление"],
            "carta": ["Письмо"],
            "relatorio": ["Спецсообщение"],
            "depoimento": ["Показания", "Показание"],
            "laudo": ["Акт судебно-медицинского"],
        }

        for tipo_str, padroes_lista in padroes.items():
            for padrao in padroes_lista:
                if padrao in titulo:
                    if _telemetry:
                        _telemetry.increment(f"tipo_documento.classificado.{tipo_str}")
                    return cls(tipo_str)

        if _telemetry:
            _telemetry.increment("tipo_documento.desconhecido")
        return cls.DESCONHECIDO

    @classmethod
    def listar_todos(cls) -> List["TipoDocumento"]:
        """Retorna todos os tipos válidos (exceto desconhecido)"""
        return [t for t in cls if t != cls.DESCONHECIDO]
```

### **Passo 3: Verificar as mudanças**

```bash
# Ver o que foi alterado
git diff src/domain/value_objects/tipo_documento.py
```

### **Passo 4: Testar localmente**

```bash
# Rodar apenas os testes que estavam falhando
poetry run pytest src/tests/test_tipo_documento_telemetry.py -v

# Deve mostrar 5/5 passed (incluindo o novo teste)
```

### **Passo 5: Rodar todos os testes para garantir**

```bash
poetry run pytest src/tests/ -v
```

**Saída esperada:**
```
collected 180 items
... (todos passando)
180 passed in XX.XXs
```

### **Passo 6: Commit com mensagem padronizada**

```bash
git add src/domain/value_objects/tipo_documento.py
git commit -m "fix: padroniza telemetria em tipo_documento.py

- Substitui decorator @monitor pelo padrão _telemetry/configure_telemetry
- Adiciona chamadas a _telemetry.increment() nos pontos relevantes
- Resolve 4 testes falhando em test_tipo_documento_telemetry.py
- Mantém compatibilidade com o padrão do projeto

Esta correção unifica a instrumentação com os demais arquivos
(documento.py, traducao.py, analise_texto.py, etc.)"
```

### **Passo 7: Push para o GitHub**

```bash
git push origin fix/tipo-documento-telemetry
```

### **Passo 8: Verificar CI**

```bash
# Acompanhar a execução
gh run list -L 5
# ou
gh run watch
```

**Resultado esperado:**
```
✅ Todos os 180 testes passando
✅ Cobertura mantida em 63%
✅ CI verde
```

---

## ✅ **Checklist de Verificação**

| Etapa | Descrição | Status |
|-------|-----------|--------|
| 1 | Branch `fix/tipo-documento-telemetry` criada | ⬜ |
| 2 | Arquivo `tipo_documento.py` modificado | ⬜ |
| 3 | Testes locais passando (180/180) | ⬜ |
| 4 | Commit feito com mensagem padrão | ⬜ |
| 5 | Push para o GitHub | ⬜ |
| 6 | CI passando no GitHub | ⬜ |

---

## 🔮 **Próximos Passos (após o merge)**

Com todos os testes passando, podemos:

1. **Fazer o merge** da branch
```bash
git checkout main
git pull origin main
git merge fix/tipo-documento-telemetry
git push origin main
```

2. **Iniciar as próximas fases**:
   - Limpeza dos arquivos `.bak`
   - Correção gradual dos erros de MyPy
   - Implementação de novos casos de uso

---

## 📚 **Referências**

- **FASE 5 - Tradução Avançada**: Primeiro uso do padrão de telemetria
- **FASE 8 - Análise de Texto**: Padronização do padrão
- **FASE 11 - Estabilização do CI**: Contexto do problema

---

## 👤 **Autor**

**Thiago Ribeiro** - Projeto de TCC
**Com assistência de DeepSeek** - Diagnóstico e correção

---

<div align="center">
  <sub>FASE 12 - Padronização da Telemetria no TipoDocumento</sub>
  <br>
  <sub>19 de Fevereiro de 2026</sub>
  <br>
  <sub>✅ Pronto para implementação</sub>
</div>

---

## 🚀 **RESUMO PARA EXECUÇÃO RÁPIDA**

```bash
# 1. Criar branch
git checkout -b fix/tipo-documento-telemetry

# 2. Editar o arquivo (use o código acima)
nano src/domain/value_objects/tipo_documento.py

# 3. Testar
poetry run pytest src/tests/test_tipo_documento_telemetry.py -v

# 4. Commit
git add src/domain/value_objects/tipo_documento.py
git commit -m "fix: padroniza telemetria em tipo_documento.py"

# 5. Push
git push origin fix/tipo-documento-telemetry

# 6. Ver CI
gh run watch
```

**Depois que o CI passar, é só fazer o merge!** 🎉
