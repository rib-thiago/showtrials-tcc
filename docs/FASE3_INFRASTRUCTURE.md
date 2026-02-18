# FASE 3 - Infrastructure Layer (Camada de Infraestrutura)

<div align="center">

**Implementações concretas dos contratos definidos no domínio**

</div>

## 📅 **Informações da Fase**

| Item | Descrição |
|------|-----------|
| **Status** | ✅ Concluída |
| **Data de Conclusão** | 15 de Fevereiro de 2024 |
| **Artefatos** | Repositórios SQLite, Modelos, Migrações |
| **Testes** | 13 testes de integração |
| **Dependências** | FASE 1 (Domain), FASE 2 (Application) |

---

## 🎯 **Objetivo**

Implementar a camada de infraestrutura que:

- Conecta o sistema ao mundo externo (banco de dados, APIs, serviços)
- Implementa as interfaces definidas no domínio
- Gerencia persistência e recuperação de dados
- Fornece serviços concretos (tradução, análise, etc)
- Isola detalhes técnicos das camadas superiores

---

## 📁 **Estrutura Criada**

```
src/
├── infrastructure/
│   ├── __init__.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── persistence/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── migrations.py
│   │   ├── sqlite_repository.py
│   │   └── sqlite_traducao_repository.py
│   └── translation/
│       └── google_translator.py
└── tests/
    └── test_infrastructure/
        ├── __init__.py
        ├── test_migrations.py
        └── test_sqlite_repository.py
```

---

## 🧩 **Componentes Implementados**

### 1. Configurações (`config/settings.py`)

**Responsabilidade:** Centralizar todas as configurações da aplicação.

```python
@dataclass
class Settings:
    """Configurações centralizadas da aplicação."""

    # Diretórios
    BASE_DIR: Path
    DB_PATH: Path
    EXPORT_DIR: Path
    REPORTS_DIR: Path
    ANALYSIS_DIR: Path

    # URLs
    LENCENTER_URL: str
    MOSCENTER_URL: str

    # API Keys
    GOOGLE_TRANSLATE_API_KEY: Optional[str]

    # Configurações de scraping
    REQUEST_TIMEOUT: int = 30
    REQUEST_DELAY: int = 1

    # Configurações de UI
    ITENS_POR_PAGINA: int = 15
    MAX_TEXTO_PREVIEW: int = 2000

    @property
    def modo_desenvolvimento(self) -> bool:
        """Verifica se está em modo desenvolvimento."""

    @property
    def db_url(self) -> str:
        """URL do banco para SQLAlchemy (futuro)."""
```

**Carregamento de variáveis de ambiente:**
```python
# .env
GOOGLE_TRANSLATE_API_KEY=AIzaSy...
ENV=development
DEBUG=true
```

**Benefícios:**
- 🔒 **Segurança**: Chaves de API fora do código
- 🔧 **Flexibilidade**: Configurações por ambiente
- 📍 **Centralização**: Tudo em um lugar

---

### 2. Modelos (`persistence/models.py`)

**Responsabilidade:** Mapeamento objeto-relacional para SQLite.

#### DocumentoModel

```python
@dataclass
class DocumentoModel:
    """Modelo de documento para o banco SQLite."""

    id: Optional[int]
    centro: str
    titulo: str
    data_original: Optional[str]
    url: str
    texto: str
    data_coleta: str

    # Colunas adicionadas nas migrações
    tipo_documento: Optional[str] = None
    tipo_descricao: Optional[str] = None
    pessoa_principal: Optional[str] = None
    remetente: Optional[str] = None
    destinatario: Optional[str] = None
    envolvidos: Optional[str] = None
    tem_anexos: int = 0
```

**Métodos de conversão:**
```python
def para_entidade(self) -> Documento:
    """Converte modelo para entidade do domínio."""

@classmethod
def de_entidade(cls, documento: Documento) -> 'DocumentoModel':
    """Converte entidade para modelo."""
```

#### TraducaoModel

```python
@dataclass
class TraducaoModel:
    """Modelo para tabela de traduções."""

    id: Optional[int]
    documento_id: int
    idioma: str
    texto_traduzido: str
    modelo: Optional[str]
    custo: float
    data_traducao: str
```

**Schema SQL:**
```sql
CREATE TABLE IF NOT EXISTS documentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    centro TEXT NOT NULL,
    titulo TEXT NOT NULL,
    data_original TEXT,
    url TEXT UNIQUE NOT NULL,
    texto TEXT NOT NULL,
    data_coleta TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS traducoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    documento_id INTEGER NOT NULL,
    idioma TEXT NOT NULL,
    texto_traduzido TEXT NOT NULL,
    modelo TEXT,
    custo REAL,
    data_traducao TEXT NOT NULL,
    FOREIGN KEY (documento_id) REFERENCES documentos (id) ON DELETE CASCADE
);
```

---

### 3. Migrações (`persistence/migrations.py`)

**Responsabilidade:** Gerenciar a evolução do schema do banco.

```python
def criar_tabelas():
    """Cria todas as tabelas se não existirem."""

def migrar_banco_existente():
    """
    Adiciona colunas de metadados ao banco existente.
    Usado após a FASE 1 para enriquecer dados antigos.
    """

def verificar_integridade() -> List[str]:
    """
    Verifica integridade do banco.
    Retorna lista de problemas encontrados.
    """

def estatisticas_banco() -> dict:
    """Retorna estatísticas do banco de dados."""
```

**Exemplo de migração:**
```python
def adicionar_colunas_metadados(cursor):
    colunas = [
        ("tipo_documento", "TEXT"),
        ("tipo_descricao", "TEXT"),
        ("pessoa_principal", "TEXT"),
        ("remetente", "TEXT"),
        ("destinatario", "TEXT"),
        ("envolvidos", "TEXT"),
        ("tem_anexos", "INTEGER DEFAULT 0"),
    ]

    for coluna, tipo in colunas:
        try:
            cursor.execute(f"ALTER TABLE documentos ADD COLUMN {coluna} {tipo}")
        except sqlite3.OperationalError:
            pass  # Coluna já existe
```

**Estatísticas do banco:**
```python
def estatisticas_banco():
    return {
        'total_docs': 519,
        'total_traducoes': 16,
        'docs_por_centro': {'lencenter': 152, 'moscenter': 367},
        'docs_classificados': 519,
    }
```

---

### 4. Repositório SQLite (`persistence/sqlite_repository.py`)

**Responsabilidade:** Implementação concreta do `RepositorioDocumento`.

```python
class SQLiteDocumentoRepository(RepositorioDocumento):
    """
    Repositório SQLite para documentos.
    Implementa a interface definida no domínio.
    """

    def __init__(self, db_path: Optional[str] = None):
        self.db_path = db_path or str(settings.DB_PATH)

    @contextmanager
    def _conexao(self):
        """Gerenciador de contexto para conexões SQLite."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

    def salvar(self, documento: Documento) -> int:
        """Insere ou atualiza um documento."""
        with self._conexao() as conn:
            cursor = conn.cursor()
            modelo = DocumentoModel.de_entidade(documento)

            if documento.id:
                # Update
                cursor.execute("""
                    UPDATE documentos SET
                        centro = ?, titulo = ?, data_original = ?, url = ?,
                        texto = ?, data_coleta = ?, tipo_documento = ?,
                        tipo_descricao = ?, pessoa_principal = ?, remetente = ?,
                        destinatario = ?, envolvidos = ?, tem_anexos = ?
                    WHERE id = ?
                """, (...))
                return documento.id
            else:
                # Insert
                cursor.execute("""
                    INSERT INTO documentos (...)
                    VALUES (...)
                """, (...))
                return cursor.lastrowid

    def buscar_por_id(self, id: int) -> Optional[Documento]:
        """Busca documento pelo ID."""
        with self._conexao() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM documentos WHERE id = ?", (id,))
            row = cursor.fetchone()
            return self._row_para_entidade(row) if row else None

    def listar(self,
               offset: int = 0,
               limite: int = 20,
               centro: Optional[str] = None,
               tipo: Optional[str] = None) -> List[Documento]:
        """Lista documentos com filtros."""
        with self._conexao() as conn:
            cursor = conn.cursor()

            query = "SELECT * FROM documentos WHERE 1=1"
            params = []

            if centro:
                query += " AND centro = ?"
                params.append(centro)
            if tipo:
                query += " AND tipo_documento = ?"
                params.append(tipo)

            query += " ORDER BY id LIMIT ? OFFSET ?"
            params.extend([limite, offset])

            cursor.execute(query, params)
            return [self._row_para_entidade(row) for row in cursor.fetchall()]

    def contar(self, centro: Optional[str] = None, tipo: Optional[str] = None) -> int:
        """Conta documentos com filtros."""
        # ... similar ao listar, mas com COUNT(*)
```

### 5. Repositório de Traduções (`persistence/sqlite_traducao_repository.py`)

```python
class SQLiteTraducaoRepository(RepositorioTraducao):
    """Repositório SQLite para traduções."""

    def buscar_por_documento(self, documento_id: int, idioma: str) -> Optional[Traducao]:
        """Busca tradução específica de um documento."""

    def listar_por_documento(self, documento_id: int) -> List[Traducao]:
        """Lista todas as traduções de um documento."""

    def contar_por_documento(self, documento_id: int) -> int:
        """Conta traduções de um documento."""
```

---

### 6. Adaptador Google Translate (`translation/google_translator.py`)

**Responsabilidade:** Integrar com a API do Google Translate.

```python
class GoogleTranslator:
    """
    Cliente para Google Cloud Translation API.
    """

    def traduzir(self, texto: str, destino: str = 'en') -> str:
        """Traduz texto para o idioma destino."""

    def traduzir_documento_completo(self, texto: str, destino: str = 'en') -> str:
        """Traduz documentos grandes dividindo em chunks."""

    def testar_conexao(self) -> bool:
        """Testa se a API está respondendo."""
```

**Chunking para documentos grandes:**
```python
def traduzir_documento_completo(self, texto, destino='en', chunk_size=3000):
    # Dividir em parágrafos
    paragrafos = texto.split('\n')
    chunks = []

    for para in paragrafos:
        if tamanho_atual + len(para) < chunk_size:
            chunk_atual.append(para)
        else:
            chunks.append('\n'.join(chunk_atual))
            chunk_atual = [para]

    # Traduzir cada chunk
    traducoes = []
    for chunk in chunks:
        traducoes.append(self.traduzir(chunk, destino))

    return '\n'.join(traducoes)
```

---

## 🧪 **Testes de Infraestrutura**

### Testes do Repositório (`test_sqlite_repository.py`)

```python
class TestSQLiteDocumentoRepository:
    """Testes para o repositório SQLite."""

    @pytest.fixture
    def repo_memoria(self):
        """Fixture que cria um repositório com banco em memória."""
        with tempfile.NamedTemporaryFile(suffix='.db') as tmp:
            repo = SQLiteDocumentoRepository(db_path=tmp.name)
            with repo._conexao() as conn:
                cursor = conn.cursor()
                DocumentoModel.criar_tabela(cursor)
                TraducaoModel.criar_tabela(cursor)
            yield repo

    def test_salvar_novo_documento(self, repo_memoria):
        """Deve inserir novo documento."""
        doc = Documento(
            centro='lencenter',
            titulo='Teste',
            url='http://teste.com/1',
            texto='Conteúdo',
            data_coleta=datetime.now()
        )

        doc_id = repo_memoria.salvar(doc)
        assert doc_id > 0

        salvo = repo_memoria.buscar_por_id(doc_id)
        assert salvo.titulo == 'Teste'

    def test_listar_com_filtro_centro(self, repo_memoria):
        """Deve filtrar por centro."""
        # Inserir documentos de teste
        for i in range(3):
            doc = Documento(centro='lencenter', ...)
            repo_memoria.salvar(doc)
        for i in range(2):
            doc = Documento(centro='moscenter', ...)
            repo_memoria.salvar(doc)

        docs_len = repo_memoria.listar(centro='lencenter')
        docs_mos = repo_memoria.listar(centro='moscenter')

        assert len(docs_len) == 3
        assert len(docs_mos) == 2

    def test_remover_documento(self, repo_memoria):
        """Deve remover documento por ID."""
        doc = Documento(...)
        doc_id = repo_memoria.salvar(doc)

        resultado = repo_memoria.remover(doc_id)
        assert resultado is True

        removido = repo_memoria.buscar_por_id(doc_id)
        assert removido is None
```

### Testes de Migrações (`test_migrations.py`)

```python
class TestMigrations:
    """Testes para scripts de migração."""

    def test_criar_tabelas(self, db_temporario):
        """Deve criar tabelas sem erros."""
        criar_tabelas()

        conn = sqlite3.connect(db_temporario)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tabelas = [row[0] for row in cursor.fetchall()]

        assert 'documentos' in tabelas
        assert 'traducoes' in tabelas

    def test_migrar_banco_existente(self, db_temporario):
        """Deve adicionar colunas de metadados."""
        # Criar tabela sem metadados
        conn = sqlite3.connect(db_temporario)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE documentos (id INTEGER PRIMARY KEY, ...)")
        conn.close()

        migrar_banco_existente()

        conn = sqlite3.connect(db_temporario)
        cursor = conn.cursor()
        cursor.execute("PRAGMA table_info(documentos)")
        colunas = [row[1] for row in cursor.fetchall()]

        assert 'tipo_documento' in colunas
        assert 'pessoa_principal' in colunas
```

### Resultados

```bash
poetry run pytest src/tests/test_infrastructure/ -v

# Saída esperada (13 testes):
# test_sqlite_repository.py::TestSQLiteDocumentoRepository::test_salvar_novo_documento PASSED
# test_sqlite_repository.py::TestSQLiteDocumentoRepository::test_salvar_documento_existente PASSED
# test_sqlite_repository.py::TestSQLiteDocumentoRepository::test_buscar_por_id_inexistente PASSED
# test_sqlite_repository.py::TestSQLiteDocumentoRepository::test_listar_sem_filtros PASSED
# test_sqlite_repository.py::TestSQLiteDocumentoRepository::test_listar_com_filtro_centro PASSED
# test_sqlite_repository.py::TestSQLiteDocumentoRepository::test_contar_documentos PASSED
# test_sqlite_repository.py::TestSQLiteDocumentoRepository::test_remover_documento PASSED
# test_sqlite_repository.py::TestSQLiteDocumentoRepository::test_remover_inexistente PASSED
# test_migrations.py::TestMigrations::test_criar_tabelas PASSED
# test_migrations.py::TestMigrations::test_migrar_banco_existente PASSED
# test_migrations.py::TestMigrations::test_verificar_integridade_banco_ok PASSED
# test_migrations.py::TestMigrations::test_verificar_integridade_banco_incompleto PASSED
# test_migrations.py::TestMigrations::test_estatisticas_banco PASSED

# =========================== 13 passed in 1.66s ===========================
```

**Total: 13 testes | Todos PASSANDO ✅**

---

## 🔄 **Fluxo de Dados na Infraestrutura**

```
[Domínio] → [Interface] ← [SQLiteRepository]
                ↑
        [DocumentoModel]
                ↑
        [SQLite (banco real)]
```

**Exemplo prático (salvar documento):**

```
1. Caso de uso chama repo.salvar(documento)
2. Repositório converte entidade para modelo
3. Executa INSERT/UPDATE no SQLite
4. Retorna ID do documento salvo
5. Caso de uso continua
```

---

## 📊 **Métricas da Fase**

| Métrica | Valor |
|---------|-------|
| Repositórios | 2 |
| Modelos | 2 |
| Migrações | 2 |
| Testes de integração | 13 |
| Cobertura estimada | >80% |
| Dependências externas | SQLite |

---

## 📚 **Princípios Aplicados**

| Princípio | Aplicação |
|-----------|-----------|
| **Dependency Inversion** | Repositório depende da interface, não o contrário |
| **Repository Pattern** | Abstração do banco de dados |
| **Migrations** | Evolução do schema sem perda de dados |
| **Test Isolation** | Banco em memória para testes |
| **Configuration Management** | Settings centralizado |
| **Context Managers** | Gerenciamento seguro de conexões |

---

## 🔗 **Integração com Fases Anteriores e Futuras**

| Fase | Relacionamento |
|------|----------------|
| **FASE 1 (Domain)** | Implementa `RepositorioDocumento` e `RepositorioTraducao` |
| **FASE 2 (Application)** | Usada pelos casos de uso |
| **FASE 4 (CLI)** | Repositórios injetados nos casos de uso |
| **FASE 5 (Tradução)** | Usa `SQLiteTraducaoRepository` |
| **FASE 9 (Web)** | Mesmos repositórios, compartilhados |

---

## 🚀 **Evolução do Código**

### Antes (código legado - `db.py`)
```python
# Código espalhado, SQL na mão
def listar_documentos():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM documentos")
    return cursor.fetchall()
```

### Depois (Clean Architecture)
```python
# Repositório organizado e testável
def listar(self, offset, limite, centro=None, tipo=None):
    with self._conexao() as conn:
        cursor = conn.cursor()
        query = self._montar_query(centro, tipo)
        cursor.execute(query, params)
        return [self._row_para_entidade(row) for row in cursor.fetchall()]
```

---

## 📈 **Métricas do Projeto (Após FASE 3)**

```
📊 DOMAIN LAYER: 3 módulos | 13 testes
📊 APPLICATION LAYER: 4 casos de uso | 4 testes
📊 INFRASTRUCTURE LAYER: 3 módulos | 13 testes
📊 TOTAL: 30 testes passando
```

---

## 🔍 **Lições Aprendidas**

1. **Context managers são essenciais**: Garantem que conexões sejam sempre fechadas
2. **Banco em memória para testes**: Isola testes e acelera execução
3. **Migrações precisam ser idempotentes**: Podem rodar múltiplas vezes sem danos
4. **Conversão modelo ↔ entidade**: Centralizar lógica de mapeamento
5. **Configurações centralizadas**: Facilita mudanças e evita repetição

---

## 🏁 **Conclusão da Fase**

A FASE 3 estabeleceu a camada de infraestrutura com:

✅ 2 repositórios SQLite completos
✅ 2 modelos de dados
✅ Sistema de migrações
✅ 13 testes de integração
✅ Adaptador para Google Translate
✅ Configurações centralizadas
✅ Código pronto para ser usado pelas interfaces

---

## 👤 **Autor**

**Thiago Ribeiro** - Projeto de TCC

---

<div align="center">
  <sub>FASE 3 concluída em 15 de Fevereiro de 2024</sub>
  <br>
  <sub>✅ Pronto para a FASE 4 - Interface CLI</sub>
</div>
```
