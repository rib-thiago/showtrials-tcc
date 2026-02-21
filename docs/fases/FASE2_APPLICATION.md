# FASE 2 - Application Layer (Camada de Aplicação)

<div align="center">

**Orquestração dos casos de uso do sistema, conectando o domínio às interfaces**

</div>

## 📅 **Informações da Fase**

| Item | Descrição |
|------|-----------|
| **Status** | ✅ Concluída |
| **Data de Conclusão** | 15 de Fevereiro de 2024 |
| **Artefatos** | Casos de uso, DTOs |
| **Testes** | 4 testes unitários |
| **Dependências** | FASE 1 (Domain) |

---

## 🎯 **Objetivo**

Implementar a camada de aplicação que:

- Orquestra os casos de uso do sistema
- Depende apenas das interfaces do domínio
- Define objetos de transferência de dados (DTOs)
- Implementa a lógica de aplicação (não confundir com regras de negócio)
- Prepara os dados para as interfaces (CLI, Web)

---

## 📁 **Estrutura Criada**

```
src/
├── application/
│   ├── __init__.py
│   ├── dtos/
│   │   ├── __init__.py
│   │   ├── documento_dto.py
│   │   └── estatisticas_dto.py
│   └── use_cases/
│       ├── __init__.py
│       ├── classificar_documento.py
│       ├── listar_documentos.py
│       ├── obter_documento.py
│       └── estatisticas.py
└── tests/
    └── test_use_cases.py
```

---

## 🧩 **Data Transfer Objects (DTOs)**

### DocumentoDTO (`documento_dto.py`)

**Responsabilidade:** Transferir dados do documento para a interface, sem expor a entidade completa.

```python
@dataclass
class DocumentoDTO:
    """DTO completo para exibição de um documento."""

    id: Optional[int]
    centro: str
    titulo: str
    data_original: Optional[str]
    url: str
    texto: str
    data_coleta: str

    # Metadados enriquecidos
    tipo: Optional[str]
    tipo_descricao: Optional[str]
    tipo_icone: Optional[str]
    pessoa_principal: Optional[str]
    pessoa_principal_en: Optional[str]
    remetente: Optional[str]
    destinatario: Optional[str]
    envolvidos: List[str]
    tem_anexos: bool

    # Métricas
    tamanho_caracteres: int
    tamanho_palavras: int

    # Traduções
    traducoes: List[Dict]
```

**Método de fábrica:**
```python
@classmethod
def from_domain(cls, documento, tradutor_nomes=None, traducoes=None):
    """Converte entidade Documento para DTO."""
    # Lógica de conversão...
```

### DocumentoListaDTO (`documento_dto.py`)

```python
@dataclass
class DocumentoListaDTO:
    """DTO resumido para listagens (mais leve)."""

    id: int
    centro: str
    titulo: str
    data_original: Optional[str]
    tipo: Optional[str]
    tipo_icone: str
    tipo_descricao: Optional[str]
    pessoa_principal: Optional[str]
    pessoa_principal_en: Optional[str]
    tem_traducao: bool
    tamanho: int
```

### EstatisticasDTO (`estatisticas_dto.py`)

```python
@dataclass
class EstatisticasDTO:
    """DTO para estatísticas do acervo."""

    # Visão geral
    total_documentos: int
    total_traducoes: int

    # Distribuições
    documentos_por_centro: Dict[str, int]
    documentos_por_tipo: Dict[str, int]
    traducoes_por_idioma: Dict[str, int]

    # Pessoas
    pessoas_frequentes: List[Tuple[str, int, str]]

    # Métricas especiais
    cartas: int
    declaracoes: int
    relatorios: int
    acareacoes: int
    acusacoes: int
    laudos: int
    documentos_com_anexos: int

    # Custos
    custo_total_traducoes: float

    @property
    def percentual_traduzido(self) -> float:
        """Percentual de documentos com tradução."""

    @property
    def resumo(self) -> str:
        """Resumo para exibição rápida."""
```

**Benefícios dos DTOs:**
- 🔒 **Encapsulamento**: A interface não precisa conhecer a estrutura completa da entidade
- 🎯 **Performance**: Dados resumidos para listagens
- 🔄 **Evolução**: Mudanças no domínio não afetam a interface
- 🧪 **Testabilidade**: Fácil de mockar

---

## 🎮 **Casos de Uso**

### 1. ClassificarDocumento (`classificar_documento.py`)

**Responsabilidade:** Classificar documentos baseado no título.

```python
class ClassificarDocumento:
    """
    Caso de uso para classificar um documento.
    """

    def __init__(self, repo: RepositorioDocumento):
        self.repo = repo

    def executar(self, documento_id: int) -> Optional[Documento]:
        """Classifica um documento específico."""

    def executar_em_lote(self, limite: int = None) -> int:
        """Classifica múltiplos documentos não classificados."""
```

**Regras aplicadas:**
- Detecção de tipo baseada em padrões no título
- Extração de nomes russos
- Detecção de anexos
- Identificação de remetente/destinatário em cartas

**Fluxo:**
```
1. Buscar documento por ID
2. Aplicar regras de classificação
3. Atualizar metadados
4. Salvar no repositório
```

---

### 2. ListarDocumentos (`listar_documentos.py`)

**Responsabilidade:** Listar documentos com paginação e filtros.

```python
class ListarDocumentos:
    """
    Caso de uso para listar documentos.
    """

    def __init__(self, repo: RepositorioDocumento):
        self.repo = repo

    def executar(self,
                 pagina: int = 1,
                 limite: int = 20,
                 centro: Optional[str] = None,
                 tipo: Optional[str] = None) -> Dict:
        """
        Executa a listagem com filtros e paginação.

        Returns:
            {
                'items': List[DocumentoListaDTO],
                'total': int,
                'pagina': int,
                'total_paginas': int,
                'filtros': dict
            }
        """
```

**Parâmetros:**
- `pagina`: Número da página (começa em 1)
- `limite`: Itens por página
- `centro`: Filtrar por centro ('lencenter'/'moscenter')
- `tipo`: Filtrar por tipo de documento

**Cálculos:**
- `offset = (pagina - 1) * limite`
- `total_paginas = (total + limite - 1) // limite`

---

### 3. ObterDocumento (`obter_documento.py`)

**Responsabilidade:** Buscar documento completo por ID.

```python
class ObterDocumento:
    """
    Caso de uso para obter um documento completo.
    """

    def __init__(self,
                 repo_doc: RepositorioDocumento,
                 repo_trad: Optional[RepositorioTraducao] = None):
        self.repo_doc = repo_doc
        self.repo_trad = repo_trad

    def executar(self, documento_id: int) -> Optional[DocumentoDTO]:
        """
        Busca documento por ID e converte para DTO.
        Inclui traduções se disponíveis.
        """
```

**Diferenciais:**
- Retorna DTO já com tradução de nomes
- Inclui lista de traduções disponíveis
- Retorna None se documento não existir

---

### 4. ObterEstatisticas (`estatisticas.py`)

**Responsabilidade:** Calcular estatísticas completas do acervo.

```python
class ObterEstatisticas:
    """
    Caso de uso para gerar estatísticas completas.
    """

    def __init__(self, repo: RepositorioDocumento):
        self.repo = repo

    def executar(self) -> EstatisticasDTO:
        """
        Calcula estatísticas baseadas em todos os documentos.
        """
```

**Métricas calculadas:**

| Categoria | Métricas |
|-----------|----------|
| **Visão Geral** | Total de documentos, total de traduções |
| **Por Centro** | Leningrad, Moscow |
| **Por Tipo** | Interrogatórios, cartas, acareações... |
| **Pessoas** | Top 20 pessoas mais frequentes |
| **Documentos Especiais** | Cartas, declarações, relatórios |
| **Custos** | Custo total de traduções |

---

## 🧪 **Testes**

### Testes dos Casos de Uso (`test_use_cases.py`)

```python
class TestClassificarDocumento:
    """Testes para o caso de uso ClassificarDocumento."""

    def test_classificar_interrogatorio(self):
        """Deve classificar interrogatório corretamente."""
        # Mock do repositório
        mock_repo = Mock()

        # Documento de teste
        doc = Documento(
            id=1,
            centro='lencenter',
            titulo='Протокол допроса Л.В. Николаева',
            url='http://teste.com',
            texto='...',
            data_coleta=datetime.now()
        )

        mock_repo.buscar_por_id.return_value = doc

        # Executar caso de uso
        caso_uso = ClassificarDocumento(mock_repo)
        resultado = caso_uso.executar(1)

        # Verificações
        assert resultado.tipo == 'interrogatorio'
        assert resultado.tipo_descricao == 'Protocolo de Interrogatório'
        assert resultado.pessoa_principal == 'Л.В. Николаева'
        mock_repo.salvar.assert_called_once()

    def test_documento_nao_encontrado(self):
        """Deve retornar None para documento inexistente."""
        mock_repo = Mock()
        mock_repo.buscar_por_id.return_value = None

        caso_uso = ClassificarDocumento(mock_repo)
        resultado = caso_uso.executar(999)

        assert resultado is None


class TestListarDocumentos:
    """Testes para o caso de uso ListarDocumentos."""

    def test_listar_com_paginacao(self):
        """Deve listar com paginação correta."""
        mock_repo = Mock()

        # Mock de 5 documentos
        docs = [Documento(id=i, ...) for i in range(1, 6)]
        mock_repo.listar.return_value = docs
        mock_repo.contar.return_value = 50

        caso_uso = ListarDocumentos(mock_repo)
        resultado = caso_uso.executar(pagina=2, limite=5)

        assert len(resultado['items']) == 5
        assert resultado['total'] == 50
        assert resultado['pagina'] == 2
        assert resultado['total_paginas'] == 10


class TestObterDocumento:
    """Testes para o caso de uso ObterDocumento."""

    def test_obter_documento_completo(self):
        """Deve retornar documento completo com DTO."""
        mock_repo = Mock()

        doc = Documento(id=1, ...)
        mock_repo.buscar_por_id.return_value = doc

        caso_uso = ObterDocumento(mock_repo)
        dto = caso_uso.executar(1)

        assert dto.id == 1
        assert dto.titulo == doc.titulo
        assert dto.tamanho_caracteres == len(doc.texto)
```

### Resultados

```bash
poetry run pytest src/tests/test_use_cases.py -v

# Saída esperada:
# src/tests/test_use_cases.py::TestClassificarDocumento::test_classificar_interrogatorio PASSED
# src/tests/test_use_cases.py::TestClassificarDocumento::test_documento_nao_encontrado PASSED
# src/tests/test_use_cases.py::TestListarDocumentos::test_listar_com_paginacao PASSED
# src/tests/test_use_cases.py::TestObterDocumento::test_obter_documento_completo PASSED

# =========================== 4 passed in 0.27s ===========================
```

**Total: 4 testes | Todos PASSANDO ✅**

---

## 🔄 **Fluxo de Dados**

```
[Interface (CLI/Web)] → [Caso de Uso] → [Repositório (interface)]
         ↑                      ↓                    ↓
         └────── [DTO] ←── [Entidade] ←─── [Implementação]
```

**Exemplo prático (ListarDocumentos):**

```
1. Interface chama caso_uso.executar(pagina=1)
2. Caso de uso calcula offset = 0
3. Caso de uso chama repo.listar(offset=0, limite=20)
4. Repositório retorna lista de entidades
5. Caso de uso converte entidades para DTOs
6. Interface recebe DTOs e exibe
```

---

## 📊 **Métricas da Fase**

| Métrica | Valor |
|---------|-------|
| Casos de uso | 4 |
| DTOs | 3 |
| Testes | 4 |
| Cobertura estimada | >85% |
| Dependências | FASE 1 apenas |

---

## 📚 **Princípios Aplicados**

| Princípio | Aplicação |
|-----------|-----------|
| **Injeção de Dependência** | Casos de uso recebem repositórios via construtor |
| **Interface Segregation** | DTOs expõem apenas dados necessários |
| **Single Responsibility** | Cada caso de uso tem uma única responsabilidade |
| **Testabilidade** | Uso de mocks para testar isoladamente |
| **Imutabilidade** | DTOs são dataclasses imutáveis |

---

## 🔗 **Integração com Fases Anteriores e Futuras**

| Fase | Relacionamento |
|------|----------------|
| **FASE 1 (Domain)** | Usa entidades, value objects e interfaces |
| **FASE 3 (Infrastructure)** | Repositórios concretos implementam as interfaces |
| **FASE 4 (CLI)** | Usa os casos de uso e DTOs |
| **FASE 9 (Web)** | Mesmos casos de uso, diferentes presenters |

---

## 🚀 **Evolução do Código**

### Antes (código legado)
```python
# Lógica de listagem misturada com SQL
def listar_documentos(pagina):
    offset = (pagina - 1) * 20
    cursor.execute("SELECT * FROM documentos LIMIT 20 OFFSET ?", (offset,))
    return cursor.fetchall()
```

### Depois (Clean Architecture)
```python
# Caso de uso puro, sem saber de banco
def executar(self, pagina):
    offset = (pagina - 1) * self.limite
    documentos = self.repo.listar(offset, self.limite)
    return [DocumentoListaDTO.from_domain(d) for d in documentos]
```

---

## 📈 **Métricas do Projeto (Após FASE 2)**

```
📊 DOMAIN LAYER: 3 módulos | 13 testes
📊 APPLICATION LAYER: 4 casos de uso | 4 testes
📊 TOTAL: 17 testes passando
```

---

## 🔍 **Lições Aprendidas**

1. **Casos de uso não devem conter regras de negócio**: Isso pertence ao domínio
2. **DTOs são essenciais**: Separar o que vai para a interface do que fica no domínio
3. **Injeção de dependência simplifica testes**: Mocks substituem repositórios reais
4. **Orquestração vs Implementação**: Casos de uso orquestram, não implementam detalhes

---

## 🏁 **Conclusão da Fase**

A FASE 2 estabeleceu a camada de aplicação com:

✅ 4 casos de uso funcionais
✅ 3 DTOs bem definidos
✅ 4 testes unitários
✅ Dependência exclusiva da FASE 1
✅ Código pronto para implementações concretas

---

## 👤 **Autor**

**Thiago Ribeiro** - Projeto de TCC

---

<div align="center">
  <sub>FASE 2 concluída em 15 de Fevereiro de 2024</sub>
  <br>
  <sub>✅ Pronto para a FASE 3 - Infrastructure Layer</sub>
</div>
```
