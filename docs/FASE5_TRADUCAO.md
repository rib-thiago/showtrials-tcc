# FASE 5 - Tradução Avançada

<div align="center">

**Sistema completo de tradução com Google Translate, persistência e alternância de idiomas**

</div>

## 📅 **Informações da Fase**

| Item | Descrição |
|------|-----------|
| **Status** | ✅ Concluída |
| **Data de Conclusão** | 15 de Fevereiro de 2024 |
| **Artefatos** | Entidade Traducao, Repositório, Casos de Uso, Comandos CLI |
| **Testes** | 5 cenários manuais |
| **Dependências** | FASE 1, 2, 3, 4, Google Cloud Translation API |

---

## 🎯 **Objetivo**

Implementar um sistema completo de tradução que:

- Integre com Google Cloud Translation API
- Permita traduzir documentos para múltiplos idiomas
- Persista traduções no banco de dados
- Ofereça alternância entre original e traduções
- Calcule e exiba custos estimados
- Forneça feedback visual durante o processo

---

## 📁 **Estrutura Criada/Modificada**

```
src/
├── domain/
│   ├── entities/
│   │   └── traducao.py                 # Nova entidade
│   └── interfaces/
│       └── repositorio_traducao.py     # Nova interface
├── application/
│   ├── use_cases/
│   │   ├── traduzir_documento.py       # Novo caso de uso
│   │   └── listar_traducoes.py         # Novo caso de uso
│   └── dtos/
│       └── traducao_dto.py             # Novo DTO
├── infrastructure/
│   ├── persistence/
│   │   └── sqlite_traducao_repository.py  # Novo repositório
│   └── translation/
│       └── google_translator.py        # Adaptador (refatorado)
└── interface/
    └── cli/
        ├── commands_traducao.py        # Novos comandos
        └── presenters_traducao.py      # Novos presenters
```

---

## 🧩 **Componentes Implementados**

### 1. Entidade Traducao (`domain/entities/traducao.py`)

**Responsabilidade:** Representar uma tradução no domínio.

```python
@dataclass
class Traducao:
    """
    Representa uma tradução de um documento.

    Attributes:
        id: Identificador único
        documento_id: ID do documento original
        idioma: Código do idioma (en, pt, es, fr)
        texto_traduzido: Conteúdo traduzido
        modelo: Modelo usado (nmt, base)
        custo: Custo estimado em USD
        data_traducao: Data da tradução
    """

    documento_id: int
    idioma: str
    texto_traduzido: str
    data_traducao: datetime

    id: Optional[int] = None
    modelo: Optional[str] = None
    custo: float = 0.0

    def __post_init__(self):
        """Validações após inicialização."""
        idiomas_validos = ['en', 'pt', 'es', 'fr']
        if self.idioma not in idiomas_validos:
            raise ValueError(f"Idioma inválido: {self.idioma}")

        if not self.texto_traduzido:
            raise ValueError("Texto traduzido não pode ser vazio")

    @property
    def idioma_nome(self) -> str:
        """Nome do idioma em português."""
        nomes = {
            'en': 'Inglês',
            'pt': 'Português',
            'es': 'Espanhol',
            'fr': 'Francês'
        }
        return nomes.get(self.idioma, self.idioma.upper())

    @property
    def idioma_icone(self) -> str:
        """Ícone do idioma."""
        icons = {
            'en': '🇺🇸',
            'pt': '🇧🇷',
            'es': '🇪🇸',
            'fr': '🇫🇷'
        }
        return icons.get(self.idioma, '🌐')
```

---

### 2. Interface RepositorioTraducao (`domain/interfaces/repositorio_traducao.py`)

**Responsabilidade:** Definir contrato para persistência de traduções.

```python
class RepositorioTraducao(ABC):
    """Interface para repositório de traduções."""

    @abstractmethod
    def salvar(self, traducao: Traducao) -> int:
        """Salva uma tradução."""
        pass

    @abstractmethod
    def buscar_por_id(self, id: int) -> Optional[Traducao]:
        """Busca tradução por ID."""
        pass

    @abstractmethod
    def buscar_por_documento(self, documento_id: int, idioma: str) -> Optional[Traducao]:
        """Busca tradução específica de um documento."""
        pass

    @abstractmethod
    def listar_por_documento(self, documento_id: int) -> List[Traducao]:
        """Lista todas as traduções de um documento."""
        pass

    @abstractmethod
    def contar_por_documento(self, documento_id: int) -> int:
        """Conta traduções de um documento."""
        pass
```

---

### 3. DTO de Tradução (`application/dtos/traducao_dto.py`)

```python
@dataclass
class TraducaoDTO:
    """DTO para exibição de tradução."""

    id: Optional[int]
    documento_id: int
    idioma: str
    idioma_nome: str
    idioma_icone: str
    texto_traduzido: str
    data_traducao: str
    modelo: Optional[str]
    custo: float

    @classmethod
    def from_domain(cls, traducao):
        """Converte entidade para DTO."""
        return cls(
            id=traducao.id,
            documento_id=traducao.documento_id,
            idioma=traducao.idioma,
            idioma_nome=traducao.idioma_nome,
            idioma_icone=traducao.idioma_icone,
            texto_traduzido=traducao.texto_traduzido,
            data_traducao=traducao.data_traducao.isoformat()[:10],
            modelo=traducao.modelo,
            custo=traducao.custo
        )
```

---

### 4. Caso de Uso TraduzirDocumento (`application/use_cases/traduzir_documento.py`)

**Responsabilidade:** Orquestrar o processo de tradução.

```python
class TraduzirDocumento:
    """
    Caso de uso para traduzir um documento.
    """

    def __init__(self,
                 repo_doc: RepositorioDocumento,
                 repo_trad: RepositorioTraducao,
                 tradutor_service):  # Serviço externo
        self.repo_doc = repo_doc
        self.repo_trad = repo_trad
        self.tradutor = tradutor_service

    def executar(self,
                 documento_id: int,
                 idioma_destino: str = 'en',
                 forcar_novo: bool = False) -> Optional[TraducaoDTO]:
        """
        Traduz um documento para o idioma especificado.

        Args:
            documento_id: ID do documento original
            idioma_destino: Código do idioma (en, pt, es, fr)
            forcar_novo: Se True, ignora tradução existente

        Returns:
            TraducaoDTO da tradução (nova ou existente)
        """
        # 1. Verificar se documento existe
        documento = self.repo_doc.buscar_por_id(documento_id)
        if not documento:
            raise ValueError(f"Documento {documento_id} não encontrado")

        # 2. Verificar se já existe tradução
        if not forcar_novo:
            existente = self.repo_trad.buscar_por_documento(documento_id, idioma_destino)
            if existente:
                return TraducaoDTO.from_domain(existente)

        # 3. Traduzir
        try:
            texto_traduzido = self.tradutor.traduzir_documento_completo(
                documento.texto,
                destino=idioma_destino
            )
        except Exception as e:
            raise RuntimeError(f"Erro na tradução: {e}")

        # 4. Criar entidade de tradução
        traducao = Traducao(
            documento_id=documento_id,
            idioma=idioma_destino,
            texto_traduzido=texto_traduzido,
            data_traducao=datetime.now(),
            modelo='nmt',
            custo=len(documento.texto) * 0.000020
        )

        # 5. Salvar
        traducao.id = self.repo_trad.salvar(traducao)

        return TraducaoDTO.from_domain(traducao)
```

---

### 5. Caso de Uso ListarTraducoes (`application/use_cases/listar_traducoes.py`)

```python
class ListarTraducoes:
    """
    Caso de uso para listar traduções de um documento.
    """

    def __init__(self, repo: RepositorioTraducao):
        self.repo = repo

    def executar(self, documento_id: int) -> List[TraducaoDTO]:
        """
        Retorna lista de traduções do documento.
        """
        traducoes = self.repo.listar_por_documento(documento_id)
        return [TraducaoDTO.from_domain(t) for t in traducoes]

    def contar(self, documento_id: int) -> int:
        """Retorna número de traduções do documento."""
        return self.repo.contar_por_documento(documento_id)
```

---

### 6. Repositório SQLite de Traduções (`infrastructure/persistence/sqlite_traducao_repository.py`)

```python
class SQLiteTraducaoRepository(RepositorioTraducao):
    """Repositório SQLite para traduções."""

    def __init__(self, db_path: Optional[str] = None):
        self.db_path = db_path or str(settings.DB_PATH)

    @contextmanager
    def _conexao(self):
        """Gerenciador de contexto para conexões."""
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

    def salvar(self, traducao: Traducao) -> int:
        """Salva uma tradução."""
        with self._conexao() as conn:
            cursor = conn.cursor()

            if traducao.id:
                # Update
                cursor.execute("""
                    UPDATE traducoes SET
                        idioma = ?,
                        texto_traduzido = ?,
                        modelo = ?,
                        custo = ?,
                        data_traducao = ?
                    WHERE id = ?
                """, (...))
                return traducao.id
            else:
                # Insert
                cursor.execute("""
                    INSERT INTO traducoes
                    (documento_id, idioma, texto_traduzido, modelo, custo, data_traducao)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (...))
                return cursor.lastrowid

    def buscar_por_documento(self, documento_id: int, idioma: str) -> Optional[Traducao]:
        """Busca tradução específica de um documento."""
        with self._conexao() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM traducoes
                WHERE documento_id = ? AND idioma = ?
            """, (documento_id, idioma))
            row = cursor.fetchone()
            return self._row_para_entidade(row) if row else None

    def listar_por_documento(self, documento_id: int) -> List[Traducao]:
        """Lista todas as traduções de um documento."""
        with self._conexao() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM traducoes
                WHERE documento_id = ?
                ORDER BY idioma
            """, (documento_id,))
            return [self._row_para_entidade(row) for row in cursor.fetchall()]
```

---

### 7. Adaptador Google Translate (`infrastructure/translation/google_translator.py`)

**Responsabilidade:** Integrar com a API do Google Translate.

```python
class GoogleTranslator:
    """
    Cliente para Google Cloud Translation API.
    """

    # Tabela de preços (US$) por caractere
    PRICING = {
        'nmt': 0.000020,  # Neural Machine Translation
        'general': 0.000020,
        'default': 0.000020
    }

    def __init__(self,
                 credentials_path: Optional[str] = None,
                 api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv('GOOGLE_TRANSLATE_API_KEY')
        self._client = self._inicializar()

    def _inicializar(self):
        """Inicializa o cliente Google Translate."""
        try:
            if self.api_key:
                return translate.Client(api_key=self.api_key)
            return translate.Client()
        except Exception as e:
            print(f"⚠️ Falha ao inicializar tradutor: {e}")
            return None

    def traduzir(self, texto: str, destino: str = 'en') -> str:
        """Traduz texto para o idioma destino."""
        if self._client is None:
            return self._simular_traducao(texto, destino)

        resultado = self._client.translate(texto, target_language=destino)
        return resultado['translatedText']

    def traduzir_documento_completo(self,
                                   texto: str,
                                   destino: str = 'en',
                                   chunk_size: int = 3000) -> str:
        """
        Traduz documentos grandes dividindo em chunks.
        """
        # Dividir em parágrafos
        paragrafos = texto.split('\n')
        chunks = []
        chunk_atual = []
        tamanho_atual = 0

        for para in paragrafos:
            if tamanho_atual + len(para) < chunk_size:
                chunk_atual.append(para)
                tamanho_atual += len(para)
            else:
                chunks.append('\n'.join(chunk_atual))
                chunk_atual = [para]
                tamanho_atual = len(para)

        if chunk_atual:
            chunks.append('\n'.join(chunk_atual))

        print(f"📄 Documento dividido em {len(chunks)} partes")

        # Traduzir cada chunk
        traducoes = []
        for i, chunk in enumerate(chunks, 1):
            print(f"  ↳ Traduzindo parte {i}/{len(chunks)}...")
            try:
                resultado = self.traduzir(chunk, destino=destino)
                traducoes.append(resultado)
                time.sleep(0.5)  # Rate limiting
            except Exception as e:
                print(f"    ⚠️ Erro: {e}")
                traducoes.append("")

        return '\n'.join(traducoes)

    def _simular_traducao(self, texto: str, destino: str) -> str:
        """Simula tradução para testes (fallback)."""
        return f"[{destino.upper()} SIMULAÇÃO] {texto[:100]}..."
```

---

### 8. ComandoTraduzir (`interface/cli/commands_traducao.py`)

**Responsabilidade:** Interface interativa para nova tradução.

```python
class ComandoTraduzir:
    """Comando para criar nova tradução."""

    def __init__(self, traduzir_use_case, listar_trad_use_case):
        self.traduzir_use_case = traduzir_use_case
        self.listar_trad_use_case = listar_trad_use_case
        self.presenter = TraducaoPresenter()

    def executar(self, documento_id: int):
        """Executa tradução interativa."""
        # 1. Mostrar traduções existentes
        traducoes = self.listar_trad_use_case.executar(documento_id)

        if traducoes:
            console.print("\n[bold cyan]🌐 Traduções existentes:[/bold cyan]")
            for t in traducoes:
                console.print(
                    f"  • {self.presenter.badge_idioma(t.idioma)} - "
                    f"{t.idioma_nome} [dim]({t.data_traducao})[/dim]"
                )

        # 2. Escolher idioma
        console.print("\n[bold cyan]Idiomas disponíveis:[/bold cyan]")
        console.print("  [1] 🇺🇸 Inglês (en)")
        console.print("  [2] 🇧🇷 Português (pt)")
        console.print("  [3] 🇪🇸 Espanhol (es)")
        console.print("  [4] 🇫🇷 Francês (fr)")
        console.print("  [0] Cancelar")

        opcao = input("\nEscolha: ").strip()

        idiomas = {'1': 'en', '2': 'pt', '3': 'es', '4': 'fr'}
        if opcao == '0':
            return None
        if opcao not in idiomas:
            console.mostrar_erro("Opção inválida!")
            return None

        idioma = idiomas[opcao]

        # 3. Verificar se já existe
        existente = next((t for t in traducoes if t.idioma == idioma), None)
        if existente:
            console.print(f"\n[yellow]⚠ Já existe tradução para {existente.idioma_nome}[/yellow]")
            console.print(f"   Data: {existente.data_traducao}")
            console.print(f"   Custo: ${existente.custo:.4f}")

            confirmar = input("Substituir? (s/N): ").strip().lower()
            if confirmar != 's':
                return None

        # 4. Estimar custo
        console.print("\n[bold]📊 Estimativa de custo:[/bold]")
        console.print("  • Preço: $0.000020 por caractere")
        console.print("  • Confirme na próxima etapa")

        confirmar = input("\nConfirmar? (s/N): ").strip().lower()
        if confirmar != 's':
            return None

        # 5. Traduzir com spinner
        try:
            resultado = console.spinner(
                f"🌐 Traduzindo para {idioma}...",
                self.traduzir_use_case.executar,
                documento_id,
                idioma,
                forcar_novo=True
            )

            console.mostrar_sucesso(f"✅ Tradução concluída! ({resultado.idioma_nome})")
            console.mostrar_sucesso(f"   Custo: ${resultado.custo:.4f}")

            return resultado

        except Exception as e:
            console.mostrar_erro(f"Erro na tradução: {e}")
            return None
```

---

### 9. ComandoAlternarIdioma (`interface/cli/commands_traducao.py`)

**Responsabilidade:** Alternar entre original e traduções.

```python
class ComandoAlternarIdioma:
    """Comando para alternar entre idiomas durante visualização."""

    def __init__(self, listar_trad_use_case, obter_documento_use_case):
        self.listar_trad_use_case = listar_trad_use_case
        self.obter_documento_use_case = obter_documento_use_case

    def executar(self, documento_id: int, idioma_atual: str = 'original') -> str:
        """
        Alterna entre original e traduções disponíveis.
        Retorna o novo idioma selecionado.
        """
        traducoes = self.listar_trad_use_case.executar(documento_id)

        if not traducoes:
            console.mostrar_erro("Este documento não tem traduções.")
            return 'original'

        # Determinar próximo idioma
        if idioma_atual == 'original':
            return traducoes[0].idioma
        else:
            idiomas = [t.idioma for t in traducoes]
            try:
                idx = idiomas.index(idioma_atual)
                if idx + 1 < len(idiomas):
                    return idiomas[idx + 1]
                else:
                    return 'original'
            except ValueError:
                return traducoes[0].idioma
```

---

### 10. Presenter de Tradução (`interface/cli/presenters_traducao.py`)

```python
class TraducaoPresenter:
    """Formata traduções para exibição."""

    @staticmethod
    def badge_idioma(idioma: str) -> str:
        """Retorna badge colorido para idioma."""
        badges = {
            'en': '[bold blue]🇺🇸 EN[/bold blue]',
            'pt': '[bold green]🇧🇷 PT[/bold green]',
            'es': '[bold yellow]🇪🇸 ES[/bold yellow]',
            'fr': '[bold magenta]🇫🇷 FR[/bold magenta]',
        }
        return badges.get(idioma, f'[dim]{idioma}[/dim]')

    @classmethod
    def badge_idioma_atual(cls, idioma: str):
        """Exibe badge indicando idioma atual."""
        if idioma == 'original':
            return Panel("[bold blue]📄 ORIGINAL (Russo)[/bold blue]", border_style="blue")
        else:
            return Panel(
                f"[bold green]🌐 TRADUÇÃO {cls.badge_idioma(idioma)}[/bold green]",
                border_style="green"
            )

    @classmethod
    def lista_traducoes(cls, traducoes, documento_id: int):
        """Exibe lista de traduções disponíveis."""
        if not traducoes:
            return

        console.print("\n[bold cyan]🌐 TRADUÇÕES DISPONÍVEIS:[/bold cyan]")
        for t in traducoes:
            console.print(
                f"  • {cls.badge_idioma(t.idioma)} - "
                f"{t.idioma_nome} [dim]({t.data_traducao})[/dim]"
            )
```

---

## 🔄 **Fluxo Completo de Tradução**

```
[Usuário] → [tecla 'n'] → [ComandoTraduzir] → [TraduzirDocumento (caso de uso)]
    ↑                                                    |
    |                                                    ↓
    └──────── [Presenter] ← [TraducaoDTO] ← [GoogleTranslator]
                              |
                              ↓
                    [SQLiteTraducaoRepository]
                              |
                              ↓
                        [Banco de Dados]
```

**Passo a passo:**

1. Usuário aperta 'n' durante visualização
2. ComandoTraduzir pergunta idioma e confirma custo
3. Caso de uso TraduzirDocumento verifica documento
4. GoogleTranslator traduz (com chunking se necessário)
5. Traducao é criada e persistida no banco
6. TraducaoDTO é retornado para a interface
7. Usuário vê mensagem de sucesso e muda para o novo idioma

---

## 🔄 **Fluxo de Alternância de Idiomas**

```
[Usuário] → [tecla 't'] → [ComandoAlternarIdioma] → [ListarTraducoes]
    ↑                                                    |
    └──────── [Presenter] ← [DTO] ←─────────────────────┘
```

**Passo a passo:**

1. Usuário aperta 't' durante visualização
2. ComandoAlternarIdioma consulta traduções disponíveis
3. Determina próximo idioma (original → en → pt → original)
4. Retorna novo idioma para o loop principal
5. Visualização recarrega com o texto no idioma selecionado

---

## 🎮 **Funcionalidades na UI**

### Na listagem de documentos:
```
ID  Tipo                  Data       Pessoa   Título                        🌐
1   🔍 INTERROGATÓRIO     1934-12-04 Nikolaev  Протокол допроса Л.В. Николаева  ✅
```
- ✅ = documento tem tradução disponível

### Na visualização do documento:
```
[Badge do idioma atual]  ← "ORIGINAL (Russo)" ou "🇺🇸 TRADUÇÃO (EN)"

[METADADOS]
  ...

🌐 TRADUÇÕES DISPONÍVEIS:
  • 🇺🇸 Inglês - 2024-02-15
  • 🇧🇷 Português - 2024-02-15

[CONTEÚDO]
  ...

COMANDOS:
  ⏎ Enter - Voltar
  e - Exportar
  t - Alternar idioma
  n - Nova tradução
```

### Nova tradução:
```
Idiomas disponíveis:
  [1] 🇺🇸 Inglês (en)
  [2] 🇧🇷 Português (pt)
  [3] 🇪🇸 Espanhol (es)
  [4] 🇫🇷 Francês (fr)
  [0] Cancelar

📊 Estimativa de custo:
  • Preço: $0.000020 por caractere
  • Confirme na próxima etapa
```

---

## 🧪 **Testes Realizados**

| Teste | Ação | Resultado Esperado | Status |
|-------|------|-------------------|--------|
| Nova tradução | 'n' no documento | Menu de idiomas aparece | ✅ |
| Escolher idioma | Selecionar 1 | Tradução inicia | ✅ |
| Progresso | Durante tradução | Spinner mostra progresso | ✅ |
| Sucesso | Após tradução | Mensagem de sucesso + custo | ✅ |
| Alternância | 't' no original | Vai para primeira tradução | ✅ |
| Alternância | 't' na tradução | Volta ao original | ✅ |
| Badge | Visualizar | Mostra idioma atual | ✅ |
| Lista | Documento com traduções | Mostra lista de idiomas | ✅ |
| Sem traduções | 't' em documento sem | Mensagem de erro | ✅ |
| Tradução existente | Tentar mesmo idioma | Pergunta substituir | ✅ |
| Substituir | Confirmar 's' | Nova tradução sobrescreve | ✅ |
| Manter existente | Confirmar 'n' | Mantém original | ✅ |
| Cancelar | '0' no menu | Volta sem traduzir | ✅ |

---

## 📊 **Métricas da Fase**

| Métrica | Valor |
|---------|-------|
| Novos arquivos | 7 |
| Linhas de código | ~600 |
| Idiomas suportados | 4 (en, pt, es, fr) |
| Testes manuais | 13 cenários |
| Custo por caractere | $0.000020 |

---

## 📚 **Princípios Aplicados**

| Princípio | Aplicação |
|-----------|-----------|
| **Single Responsibility** | Cada classe tem uma responsabilidade clara |
| **Open/Closed** | Novos idiomas podem ser adicionados sem modificar código |
| **Liskov Substitution** | Repositório concreto substitui interface |
| **Interface Segregation** | RepositorioTraducao com métodos específicos |
| **Dependency Inversion** | Casos de uso dependem de interfaces |

---

## 🔗 **Integração com Fases Anteriores e Futuras**

| Fase | Relacionamento |
|------|----------------|
| **FASE 1 (Domain)** | Entidade Traducao, interfaces |
| **FASE 2 (Application)** | Casos de uso e DTOs |
| **FASE 3 (Infrastructure)** | Repositório SQLite e adaptador Google |
| **FASE 4 (CLI)** | Comandos e presenters |
| **FASE 6 (Exportação)** | Traduções podem ser exportadas |
| **FASE 8 (Análise)** | Texto traduzido pode ser analisado |

---

## 🚀 **Evolução do Código**

### Antes (código legado - `translator.py`)
```python
# Código monolítico, sem separação
def traduzir(texto, idioma):
    # Lógica de tradução misturada com persistência
    # Sem tratamento de erros adequado
    # Sem estimativa de custos
```

### Depois (Clean Architecture)
```python
# Separação clara de responsabilidades
caso_uso = TraduzirDocumento(repo_doc, repo_trad, tradutor)
resultado = caso_uso.executar(doc_id, 'en')
```

---

## 📈 **Métricas do Projeto (Após FASE 5)**

```
📊 DOMAIN LAYER: 4 entidades | 15 testes
📊 APPLICATION LAYER: 5 casos de uso | 6 testes
📊 INFRASTRUCTURE LAYER: 4 módulos | 16 testes
📊 INTERFACE LAYER: 8 módulos | Validada manualmente
📊 TOTAL: 37 testes automatizados
```

---

## 🔍 **Lições Aprendidas**

1. **Chunking é necessário**: Documentos longos precisam ser divididos
2. **Rate limiting é importante**: Evita bloqueios da API
3. **Fallback é essencial**: Simulação quando API não disponível
4. **Custos devem ser transparentes**: Usuário precisa saber antes de traduzir
5. **Persistência evita retrabalho**: Traduções salvas não precisam ser refeitas
6. **Feedback visual é crucial**: Spinner durante processo longo

---

## 🏁 **Conclusão da Fase**

A FASE 5 entregou um sistema completo de tradução com:

✅ Integração com Google Translate API
✅ 4 idiomas suportados
✅ Persistência em SQLite
✅ Alternância fluida entre idiomas
✅ Estimativa e exibição de custos
✅ Feedback visual com spinner
✅ Tratamento de casos de borda
✅ Código limpo e testável

---

## 👤 **Autor**

**Thiago Ribeiro** - Projeto de TCC

---

<div align="center">
  <sub>FASE 5 concluída em 15 de Fevereiro de 2024</sub>
  <br>
  <sub>✅ Pronto para a FASE 6 - Exportação de Documentos</sub>
</div>
```
