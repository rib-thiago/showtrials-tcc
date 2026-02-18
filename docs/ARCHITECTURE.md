# Arquitetura do Sistema ShowTrials

<div align="center">

**Clean Architecture aplicada a um sistema de gestão de documentos históricos**

</div>

## 📋 **Visão Geral**

O ShowTrials é um sistema para coleta, armazenamento, tradução e análise de documentos históricos dos processos de Moscou e Leningrado (1934-1935). Foi desenvolvido seguindo os princípios da **Clean Architecture** (Arquitetura Limpa), proposta por Robert C. Martin (Uncle Bob).

Esta arquitetura foi escolhida por:

- **Isolar o núcleo do negócio** de detalhes de infraestrutura
- **Facilitar testes** através de injeção de dependência
- **Permitir evolução** com mínimo impacto
- **Separar responsabilidades** de forma clara
- **Garantir que as regras de negócio** sejam independentes de UI, banco de dados ou frameworks

---

## 🏗️ **As Quatro Camadas**

```
┌─────────────────────────────────────────────────────────────┐
│                    INTERFACE LAYER                           │
│  (CLI, Web, API - adaptadores para o mundo externo)        │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   APPLICATION LAYER                          │
│  (Casos de uso, orquestração, DTOs)                         │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      DOMAIN LAYER                            │
│  (Entidades, Value Objects, regras de negócio)              │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                  INFRASTRUCTURE LAYER                        │
│  (Repositórios, serviços externos, implementações)          │
└─────────────────────────────────────────────────────────────┘
```

---

### 1. Domain Layer (Núcleo)

**Localização:** `src/domain/`

**Responsabilidade:** Conter as regras de negócio puras, sem qualquer dependência externa.

**Componentes:**
- **Entities**: Objetos com identidade (Documento, Traducao)
- **Value Objects**: Objetos imutáveis (TipoDocumento, NomeRusso, AnaliseTexto)
- **Interfaces (Ports)**: Contratos para camadas externas (RepositorioDocumento)

**Princípios:**
- Nenhum import de frameworks
- Nenhuma menção a banco de dados
- Totalmente testável com mocks

**Exemplo:**
```python
@dataclass
class Documento:
    id: Optional[int]
    titulo: str
    texto: str

    @property
    def tamanho(self) -> int:
        return len(self.texto)  # Regra de negócio pura
```

---

### 2. Application Layer (Aplicação)

**Localização:** `src/application/`

**Responsabilidade:** Orquestrar os casos de uso do sistema.

**Componentes:**
- **Use Cases**: Cada operação do sistema (ListarDocumentos, TraduzirDocumento)
- **DTOs**: Objetos para transferência de dados (DocumentoDTO)
- **Serviços de aplicação**: Coordenação entre repositórios e serviços

**Princípios:**
- Depende apenas de interfaces do domínio
- Não conhece implementações concretas
- Contém a lógica de aplicação (não confundir com regras de negócio)

**Exemplo:**
```python
class ListarDocumentos:
    def __init__(self, repo: RepositorioDocumento):
        self.repo = repo

    def executar(self, pagina: int) -> List[DocumentoDTO]:
        offset = (pagina - 1) * 15
        documentos = self.repo.listar(offset, 15)
        return [DocumentoDTO.from_domain(d) for d in documentos]
```

---

### 3. Interface Layer (Adaptadores)

**Localização:** `src/interface/`

**Responsabilidade:** Traduzir entre o mundo externo e a aplicação.

**Componentes:**
- **CLI**: Interface de linha de comando com Rich
- **Web**: API FastAPI e templates HTML
- **Presenters**: Formatadores de saída
- **Comandos**: Ações do usuário

**Princípios:**
- Não contém lógica de negócio
- Depende de casos de uso e DTOs
- Pode ter múltiplas implementações (CLI e Web)

**Exemplo:**
```python
class ComandoListar:
    def __init__(self, listar_use_case: ListarDocumentos):
        self.use_case = listar_use_case

    def executar(self):
        resultados = self.use_case.executar(pagina=1)
        self.mostrar_tabela(resultados)  # Formatação específica da CLI
```

---

### 4. Infrastructure Layer (Infraestrutura)

**Localização:** `src/infrastructure/`

**Responsabilidade:** Implementar as interfaces definidas nas camadas internas.

**Componentes:**
- **Repositórios**: Implementações SQLite
- **Serviços externos**: Google Translate, SpaCy
- **Configurações**: Settings, variáveis de ambiente
- **Service Registry**: Gerenciamento de serviços

**Princípios:**
- Contém detalhes técnicos (SQL, HTTP)
- Implementa as interfaces do domínio
- Pode ser substituída sem afetar as camadas internas

**Exemplo:**
```python
class SQLiteDocumentoRepository(RepositorioDocumento):
    def listar(self, offset, limite):
        with self._conexao() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM documentos LIMIT ? OFFSET ?",
                         (limite, offset))
            return [self._row_para_entidade(row) for row in cursor]
```

---

## 🔄 **Fluxo de Dados**

```
[Usuário] → [Interface] → [Caso de Uso] → [Repositório (interface)]
    ↑          ↓              ↓                    ↓
    └──── [Presenter] ← [DTO] ← [Entidade] ← [Implementação concreta]
```

**Exemplo com Listar Documentos:**

1. Usuário digita '1' no menu CLI
2. `ComandoListar` chama `listar_use_case.executar()`
3. Caso de uso calcula offset e chama `repo.listar()`
4. Repositório SQLite busca dados no banco
5. Dados são convertidos para entidades do domínio
6. Caso de uso converte entidades para DTOs
7. Presenter formata DTOs em tabela colorida
8. Usuário vê o resultado

---

## 📦 **Service Registry e Injeção de Dependência**

```
[ServiceRegistry] ← [Config YAML]
        ↓
    [Factories]
        ↓
    [Serviços]
        ↓
    [Casos de Uso]
```

**Vantagens:**
- Lazy loading: serviços só carregam quando usados
- Configurável via YAML
- Estatísticas de uso
- Fácil adicionar novos serviços

---

## 🧪 **Estratégia de Testes**

```
┌─────────────────┐
│   Unit Tests    │ → Domain (18 testes)
│   (isolados)    │ → Application (10 testes)
└─────────────────┘
        ↓
┌─────────────────┐
│ Integration     │ → Infrastructure (20 testes)
│ Tests           │ → Repositórios, APIs
└─────────────────┘
        ↓
┌─────────────────┐
│   Manual Tests  │ → CLI (36 cenários)
│   (end-to-end)  │ → Web (36 cenários)
└─────────────────┘
```

**Total:** 48 testes automatizados + validação manual

---

## 📊 **Diagrama de Camadas com Componentes**

```
┌─────────────────────────────────────────────────────────────────┐
│                        INTERFACE LAYER                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │     CLI      │  │   Web App    │  │     API      │          │
│  │   (Rich)     │  │  (FastAPI)   │  │   (REST)     │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │  Presenters  │  │   Commands   │  │   Templates   │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      APPLICATION LAYER                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │ ListarDocs   │  │ TraduzirDoc  │  │ AnalisarDoc  │          │
│  ├──────────────┤  ├──────────────┤  ├──────────────┤          │
│  │ ExportarDoc  │  │ GerarRelat   │  │ ObterStats   │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
│  ┌─────────────────────────────────────────────────────┐        │
│  │                     DTOs                             │        │
│  │  (DocumentoDTO, TraducaoDTO, EstatisticasDTO)       │        │
│  └─────────────────────────────────────────────────────┘        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                         DOMAIN LAYER                              │
│  ┌──────────────┐  ┌──────────────────┐  ┌──────────────┐      │
│  │   Entidades  │  │   Value Objects  │  │  Interfaces  │      │
│  │  • Documento │  │  • TipoDocumento │  │ • RepoDoc    │      │
│  │  • Traducao  │  │  • NomeRusso     │  │ • RepoTrad   │      │
│  │              │  │  • AnaliseTexto  │  │              │      │
│  └──────────────┘  └──────────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     INFRASTRUCTURE LAYER                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │   SQLite     │  │   Google     │  │    SpaCy     │          │
│  │  Repositórios│  │  Translate   │  │   Analyzer   │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │   WordCloud  │  │   Service    │  │  Configuração│          │
│  │   Generator  │  │   Registry   │  │    (YAML)    │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📈 **Métricas da Arquitetura**

| Camada | Arquivos | Testes | Dependências Externas |
|--------|----------|--------|----------------------|
| **Domain** | 8 | 18 | Nenhuma |
| **Application** | 12 | 10 | Domain apenas |
| **Interface** | 25+ | Manual | Application |
| **Infrastructure** | 15 | 20 | Application + externas |

**Total:** 60+ arquivos, 48 testes automatizados

---

## 🎯 **Benefícios da Arquitetura**

1. **Manutenibilidade**: Mudanças em uma camada não afetam as outras
2. **Testabilidade**: Cada camada pode ser testada isoladamente
3. **Flexibilidade**: Trocar banco de dados não afeta o domínio
4. **Clareza**: Responsabilidades bem definidas
5. **Evolução**: Novas funcionalidades são casos de uso adicionais

---

## 📚 **Referências**

- Martin, R. C. (2017). *Clean Architecture: A Craftsman's Guide to Software Structure and Design*
- Martin, R. C. (2003). *Agile Software Development: Principles, Patterns, and Practices*

---

## 👤 **Autor**

**Thiago Ribeiro** - Projeto de TCC

---

<div align="center">
  <sub>Documento de Arquitetura - Versão 1.0</sub>
  <br>
  <sub>Fevereiro de 2026</sub>
</div>
```

---
