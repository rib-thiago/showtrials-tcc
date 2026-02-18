# FASE 4 - Interface CLI (Camada de Interface)

<div align="center">

**Interface de linha de comando com navegação interativa e rica experiência visual**

</div>

## 📅 **Informações da Fase**

| Item | Descrição |
|------|-----------|
| **Status** | ✅ Concluída |
| **Data de Conclusão** | 15 de Fevereiro de 2024 |
| **Artefatos** | CLI com Rich, Comandos, Presenters, Menus |
| **Testes** | Validação manual completa |
| **Dependências** | FASE 1, 2, 3 |

---

## 🎯 **Objetivo**

Implementar a interface de linha de comando (CLI) que:

- Ofereça navegação intuitiva por menus
- Apresente dados de forma rica e colorida
- Permita todas as operações do sistema
- Utilize a arquitetura limpa com injeção de dependência
- Proporcione experiência similar a aplicações desktop

---

## 📁 **Estrutura Criada**

```
src/
├── interface/
│   ├── __init__.py
│   ├── console.py                 # Configuração do Rich
│   └── cli/
│       ├── __init__.py
│       ├── app.py                  # Aplicação principal
│       ├── commands.py              # Comandos base
│       ├── commands_analise.py      # Comandos de análise
│       ├── commands_export.py       # Comandos de exportação
│       ├── commands_relatorio.py    # Comandos de relatórios
│       ├── commands_traducao.py     # Comandos de tradução
│       ├── menu.py                  # Menus interativos
│       ├── presenters.py            # Presenters base
│       ├── presenters_analise.py    # Presenters de análise
│       └── presenters_traducao.py   # Presenters de tradução
└── scripts/
    └── migrar_dados_existentes.py   # Script de migração
```

---

## 🧩 **Componentes Implementados**

### 1. Console (`console.py`)

**Responsabilidade:** Configurar o Rich e fornecer funções de UI padronizadas.

```python
# Configuração do Rich
tema = Theme({
    "primary": "bold cyan",
    "secondary": "bold yellow",
    "success": "bold green",
    "error": "bold red",
    "warning": "bold yellow",
    "info": "dim white",
    "destaque": "reverse white"
})

console = Console(theme=tema)
```

**Funções utilitárias:**

```python
def limpar_tela():
    """Limpa o terminal de forma cross-platform."""
    os.system('cls' if os.name == 'nt' else 'clear')
    if os.name != 'nt':
        print('\033[3J', end='')  # Limpa scrollback
        print('\033[H', end='')   # Posiciona cursor

def cabecalho(titulo: str):
    """Exibe cabeçalho padronizado."""
    console.rule(f"[primary]{titulo}[/primary]")
    console.print()

def mostrar_erro(mensagem: str):
    """Exibe mensagem de erro."""
    console.print(f"[error]✗[/error] {mensagem}")

def mostrar_sucesso(mensagem: str):
    """Exibe mensagem de sucesso."""
    console.print(f"[success]✓[/success] {mensagem}")

def mostrar_aviso(mensagem: str):
    """Exibe mensagem de aviso."""
    console.print(f"[warning]⚠[/warning] {mensagem}")

def spinner(mensagem: str, funcao, *args, **kwargs):
    """Executa função com spinner de carregamento."""
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
        transient=True
    ) as progress:
        progress.add_task(f"[cyan]{mensagem}[/cyan]", total=None)
        return funcao(*args, **kwargs)
```

---

### 2. Presenters (`presenters.py`, `presenters_analise.py`, `presenters_traducao.py`)

**Responsabilidade:** Formatar dados para exibição no terminal.

#### Badges e Ícones

```python
@staticmethod
def badge_tipo(tipo: str) -> str:
    """Retorna badge colorido para tipo de documento."""
    badges = {
        'interrogatorio': '[bold cyan]🔍 INTERROGATÓRIO[/bold cyan]',
        'acareacao': '[bold yellow]⚖️ ACAREAÇÃO[/bold yellow]',
        'acusacao': '[bold red]📜 ACUSAÇÃO[/bold red]',
        'declaracao': '[bold blue]📝 DECLARAÇÃO[/bold blue]',
        'carta': '[bold green]✉️ CARTA[/bold green]',
        'relatorio': '[bold magenta]📋 RELATÓRIO NKVD[/bold magenta]',
        'depoimento': '[bold purple]🗣️ DEPOIMENTO[/bold purple]',
        'laudo': '[bold white]🏥 LAUDO[/bold white]',
        'desconhecido': '[dim]📄 DOCUMENTO[/dim]'
    }
    return badges.get(tipo, badges['desconhecido'])

@staticmethod
def badge_idioma(idioma: str) -> str:
    """Retorna badge de idioma."""
    badges = {
        'ru': '[bold white]🇷🇺 RU[/bold white]',
        'en': '[bold blue]🇺🇸 EN[/bold blue]',
        'pt': '[bold green]🇧🇷 PT[/bold green]',
        'es': '[bold yellow]🇪🇸 ES[/bold yellow]',
        'fr': '[bold magenta]🇫🇷 FR[/bold magenta]',
    }
    return badges.get(idioma, f'[dim]{idioma}[/dim]')
```

#### Tabela de Documentos

```python
@classmethod
def tabela_documentos(cls, resultados: Dict):
    """Cria tabela de documentos para listagem."""
    table = Table(
        title=f"[bold]📚 Documentos[/bold] (Página {resultados['pagina']}/{resultados['total_paginas']})",
        box=box.ROUNDED,
        header_style="bold cyan",
        border_style="bright_blue"
    )

    table.add_column("ID", width=4, justify="right")
    table.add_column("Tipo", width=20)
    table.add_column("Data", width=12)
    table.add_column("Pessoa", width=25)
    table.add_column("Título", width=35)
    table.add_column("🌐", width=8, justify="center")

    for item in resultados['items']:
        trad_badge = "[bold green]✓[/bold green]" if item.tem_traducao else "[dim]—[/dim]"

        table.add_row(
            str(item.id),
            cls.badge_tipo(item.tipo),
            item.data_original or "N/D",
            item.pessoa_principal_en or item.pessoa_principal or "",
            item.titulo[:35] + "…" if len(item.titulo) > 35 else item.titulo,
            trad_badge
        )

    console.print(table)
    console.print(f"[dim]Total: {resultados['total']} documentos[/dim]")
```

#### Documento Completo

```python
@classmethod
def documento_completo(cls, dto):
    """Exibe documento completo com metadados."""
    # Cabeçalho com título
    titulo_panel = Panel(
        f"[bold yellow]{dto.titulo}[/bold yellow]\n\n"
        f"{cls.badge_tipo(dto.tipo)}",
        border_style="bright_green",
        padding=(1, 2)
    )
    console.print(titulo_panel)

    # Metadados
    console.print("[bold cyan]📋 METADADOS[/bold cyan]")
    console.print(f"  🏛️ Centro: [yellow]{dto.centro}[/yellow]")
    console.print(f"  📅 Data original: {dto.data_original or 'Não informada'}")
    console.print(f"  🔗 URL: [blue]{dto.url}[/blue]")
    console.print(f"  📊 Tamanho: {dto.tamanho_caracteres} caracteres")

    # Conteúdo
    console.print("\n[bold white]📄 CONTEÚDO[/bold white]")
    console.print("─" * 80)

    texto = dto.texto
    if len(texto) > 2000:
        texto = texto[:2000] + "\n\n[dim]... (texto truncado)[/dim]"

    console.print(texto)
    console.print("─" * 80)
```

#### Badge de Idioma Atual

```python
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
```

---

### 3. Comandos (`commands.py`, `commands_analise.py`, `commands_export.py`, `commands_relatorio.py`, `commands_traducao.py`)

**Responsabilidade:** Implementar cada ação do usuário.

#### ComandoListar (`commands.py`)

```python
class ComandoListar:
    """Comando para listar documentos."""

    def __init__(self, listar_use_case):
        self.listar_use_case = listar_use_case
        self.presenter = DocumentoPresenter()

    def executar(self, centro: Optional[str] = None, tipo: Optional[str] = None):
        """Executa listagem interativa."""
        pagina = 1
        limite = 15

        while True:
            limpar_tela()
            cabecalho(f"📋 Documentos - {centro or 'Todos'}")

            resultados = self.listar_use_case.executar(
                pagina=pagina,
                limite=limite,
                centro=centro,
                tipo=tipo
            )

            self.presenter.tabela_documentos(resultados)

            # Menu de navegação
            console.print("\n[dim]─────────────────────────────────[/dim]")
            console.print("[bold cyan]COMANDOS[/bold cyan]")
            console.print("  [green]n[/green] - Próxima página")
            console.print("  [green]p[/green] - Página anterior")
            console.print("  [green][número][/green] - Ver documento")
            console.print("  [green]m[/green] - Menu principal")

            cmd = input("\nComando: ").strip().lower()

            if cmd == 'n' and pagina < resultados['total_paginas']:
                pagina += 1
            elif cmd == 'p' and pagina > 1:
                pagina -= 1
            elif cmd == 'm':
                break
            elif cmd.isdigit():
                return int(cmd)
            else:
                mostrar_erro("Comando inválido")
```

#### ComandoTraduzir (`commands_traducao.py`)

```python
class ComandoTraduzir:
    """Comando para criar nova tradução."""

    def executar(self, documento_id: int):
        """Executa tradução interativa."""
        # 1. Mostrar traduções existentes
        traducoes = self.listar_trad_use_case.executar(documento_id)

        # 2. Escolher idioma
        console.print("\n[bold cyan]Idiomas disponíveis:[/bold cyan]")
        console.print("  [1] 🇺🇸 Inglês (en)")
        console.print("  [2] 🇧🇷 Português (pt)")
        console.print("  [3] 🇪🇸 Espanhol (es)")
        console.print("  [4] 🇫🇷 Francês (fr)")

        # 3. Verificar se já existe
        if existente:
            console.print(f"\n[yellow]⚠ Já existe tradução[/yellow]")
            confirmar = input("Substituir? (s/N): ").strip().lower()

        # 4. Estimar custo
        console.print("\n[bold]📊 Estimativa de custo:[/bold]")

        # 5. Traduzir com spinner
        resultado = spinner(
            f"🌐 Traduzindo...",
            self.traduzir_use_case.executar,
            documento_id,
            idioma,
            forcar_novo=True
        )
```

#### ComandoExportar (`commands_export.py`)

```python
class ComandoExportar:
    """Comando para exportar documento."""

    def executar(self, documento_id: int):
        """Executa exportação interativa."""
        # 1. Listar idiomas disponíveis
        idiomas = self.exportar_use_case.listar_idiomas_disponiveis(documento_id)

        # 2. Escolher formato
        console.print("\n[bold]Formatos disponíveis:[/bold]")
        console.print("  [1] 📄 TXT")
        console.print("  [2] 📑 PDF (em breve)")

        # 3. Incluir metadados?
        console.print("\n[bold]Incluir metadados?[/bold]")

        # 4. Exportar
        resultado = self.exportar_use_case.executar(...)

        if resultado['sucesso']:
            mostrar_sucesso(f"Documento exportado para: {resultado['caminho']}")
```

---

### 4. Menus (`menu.py`)

**Responsabilidade:** Gerenciar a navegação entre telas.

#### MenuPrincipal

```python
class MenuPrincipal:
    """Menu principal da aplicação."""

    def mostrar(self) -> str:
        limpar_tela()

        banner = """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                    ◈ ◈ ◈ SHOW TRIALS ◈ ◈ ◈                 ║
║                    Coleta • Tradução • Análise              ║
╚══════════════════════════════════════════════════════════════╝
"""
        console.print(banner, style="bold cyan")
        console.print()

        console.print("[bold cyan]MENU PRINCIPAL[/bold cyan]")
        console.print()
        console.print("  [1] 📋 Listar todos os documentos")
        console.print("  [2] 🏛️  Listar por centro")
        console.print("  [3] 👁️  Visualizar documento")
        console.print("  [4] 📊 Estatísticas")
        console.print("  [5] 📈 Relatórios avançados")
        console.print("  [6] 🔍 Análise de texto")
        console.print("  [7] 🔄 Sair")
        console.print()

        return input("[cyan]Escolha[/cyan] ").strip()
```

#### MenuCentro

```python
class MenuCentro:
    """Menu para escolha de centro."""

    @staticmethod
    def mostrar() -> str:
        console.print()
        console.print("[bold cyan]Centros disponíveis:[/bold cyan]")
        console.print("  [1] 🏛️ Leningrad Center")
        console.print("  [2] 🏛️ Moscow Center")
        console.print("  [0] ↩️  Voltar")

        opcao = input("\nEscolha o centro: ").strip()

        if opcao == '1':
            return 'lencenter'
        elif opcao == '2':
            return 'moscenter'
        return None
```

#### Menu de Análise

```python
def _menu_analise(self):
    """Menu de análise de texto."""
    while True:
        limpar_tela()
        cabecalho("🔍 ANÁLISE DE TEXTO")

        console.print("[bold cyan]Opções:[/bold cyan]")
        console.print("  [1] Analisar documento específico")
        console.print("  [2] Análise global do acervo")
        console.print("  [3] Nuvem de palavras do acervo")
        console.print("  [0] Voltar")

        opcao = input("\nEscolha: ").strip()

        if opcao == '0':
            break
        elif opcao == '1':
            doc_id = int(input("ID do documento: "))
            self.cmd_analisar_doc.executar(doc_id)
        elif opcao == '2':
            self.cmd_analisar_acervo.executar()
        elif opcao == '3':
            caminho = self.analisar_acervo_use_case.gerar_wordcloud_geral()
            mostrar_sucesso(f"Nuvem gerada em: {caminho}")
```

---

### 5. Aplicação Principal (`app.py`)

**Responsabilidade:** Inicializar e orquestrar todos os componentes.

```python
class ShowTrialsApp:
    """Aplicação principal com injeção de dependência."""

    def __init__(self):
        # =====================================================
        # 1. INFRAESTRUTURA
        # =====================================================
        self.repo = SQLiteDocumentoRepository()
        self.repo_traducao = SQLiteTraducaoRepository()
        self.registry = ServiceRegistry()

        # Registrar serviços
        self.registry.register('translator', create_translator, lazy=True)
        self.registry.register('spacy', create_spacy_analyzer, lazy=True)
        self.registry.register('wordcloud', create_wordcloud_generator, lazy=True)

        # =====================================================
        # 2. CASOS DE USO
        # =====================================================
        self.listar_use_case = ListarDocumentos(self.repo).com_traducao_nomes(True)
        self.obter_use_case = ObterDocumento(self.repo, self.repo_traducao)
        self.estatisticas_use_case = ObterEstatisticas(self.repo)
        self.exportar_use_case = ExportarDocumento(self.repo, self.repo_traducao)
        self.relatorio_use_case = GerarRelatorio(self.repo, self.repo_traducao)

        # Casos com registry
        self.traduzir_use_case = TraduzirDocumento(
            repo_doc=self.repo,
            repo_trad=self.repo_traducao,
            registry=self.registry
        )

        self.analisar_documento_use_case = AnalisarDocumento(
            repo_doc=self.repo,
            repo_trad=self.repo_traducao,
            registry=self.registry
        )

        self.analisar_acervo_use_case = AnalisarAcervo(
            repo_doc=self.repo,
            registry=self.registry
        )

        self.listar_traducoes_use_case = ListarTraducoes(self.repo_traducao)

        # =====================================================
        # 3. COMANDOS
        # =====================================================
        self.cmd_listar = ComandoListar(self.listar_use_case)
        self.cmd_visualizar = ComandoVisualizar(self.obter_use_case)
        self.cmd_estatisticas = ComandoEstatisticas(self.estatisticas_use_case)
        self.cmd_exportar = ComandoExportar(self.exportar_use_case)
        self.cmd_relatorio = ComandoRelatorio(self.relatorio_use_case)

        self.cmd_traduzir = ComandoTraduzir(
            self.traduzir_use_case,
            self.listar_traducoes_use_case
        )

        self.cmd_alternar_idioma = ComandoAlternarIdioma(
            self.listar_traducoes_use_case,
            self.obter_use_case
        )

        self.cmd_analisar_doc = ComandoAnalisarDocumento(self.analisar_documento_use_case)
        self.cmd_analisar_acervo = ComandoAnalisarAcervo(self.analisar_acervo_use_case)

        # =====================================================
        # 4. MENUS
        # =====================================================
        self.menu_principal = MenuPrincipal(self)
        self.menu_centro = MenuCentro()
```

---

### 6. Visualização de Documento com Traduções

```python
def _visualizar_e_aguardar(self, doc_id: int):
    """Visualiza documento com alternância de idiomas."""
    idioma_atual = 'original'

    while True:
        # Buscar documento (original ou tradução)
        if idioma_atual == 'original':
            dto = self.obter_use_case.executar(doc_id)
        else:
            # Buscar tradução específica
            traducoes = self.listar_traducoes_use_case.executar(doc_id)
            traducao = next((t for t in traducoes if t.idioma == idioma_atual), None)

            if traducao:
                dto = self.obter_use_case.executar(doc_id)
                dto.texto = traducao.texto_traduzido
                dto.titulo = f"{dto.titulo} [{traducao.idioma_nome}]"
            else:
                dto = self.obter_use_case.executar(doc_id)
                idioma_atual = 'original'

        # Mostrar badge do idioma atual
        console.print(TraducaoPresenter.badge_idioma_atual(idioma_atual))

        # Mostrar documento
        DocumentoPresenter.documento_completo(dto)

        # Mostrar traduções disponíveis
        traducoes = self.listar_traducoes_use_case.executar(doc_id)
        if traducoes:
            console.print("\n[bold cyan]🌐 TRADUÇÕES DISPONÍVEIS:[/bold cyan]")
            for t in traducoes:
                console.print(f"    {t.idioma_icone} {t.idioma_nome}")

        # Comandos
        console.print("\n[dim]─────────────────────────────────[/dim]")
        console.print("[bold cyan]COMANDOS[/bold cyan]")
        console.print("  [green]⏎ Enter[/green] - Voltar")
        console.print("  [yellow]e[/yellow] - Exportar")
        console.print("  [cyan]t[/cyan] - Alternar idioma")
        console.print("  [blue]n[/blue] - Nova tradução")

        cmd = input("\nComando: ").strip().lower()

        if cmd == '':
            break
        elif cmd == 't':
            idioma_atual = self.cmd_alternar_idioma.executar(doc_id, idioma_atual)
        elif cmd == 'n':
            resultado = self.cmd_traduzir.executar(doc_id)
            if resultado:
                idioma_atual = resultado.idioma
        elif cmd == 'e':
            self.cmd_exportar.executar(doc_id)
```

---

## 🧪 **Testes (Manuais)**

### Checklist de Validação

| Cenário | Ação | Resultado Esperado |
|---------|------|-------------------|
| **Menu principal** | Executar `python run.py` | Banner + 7 opções |
| **Listar todos** | Opção 1 | Tabela paginada com 15 itens |
| **Navegação** | Tecla 'n' | Próxima página |
| **Navegação** | Tecla 'p' | Página anterior |
| **Ver documento** | Digitar ID | Metadados + conteúdo |
| **Filtro por centro** | Opção 2 → 1 | Apenas Leningrad |
| **Traduções** | Visualizar doc com tradução | Badge ✅ na coluna |
| **Alternar idioma** | Tecla 't' | Muda entre original/tradução |
| **Nova tradução** | Tecla 'n' | Menu de idiomas |
| **Exportar** | Tecla 'e' | Menu de exportação |
| **Estatísticas** | Opção 4 | Dashboard completo |
| **Relatórios** | Opção 5 | Menu de relatórios |
| **Análise** | Opção 6 | Menu de análise |
| **Sair** | Opção 7 | Mensagem de despedida |

---

## 🔄 **Fluxo de Dados na CLI**

```
[Usuário] → [Menu] → [Comando] → [Caso de Uso] → [Repositório]
    ↑          ↑          ↑             ↑               ↑
    └──────────┴──────────┴─────────────┴───────────────┘
                         [DTOs]
```

**Exemplo prático (Listar documentos):**

```
1. Usuário digita '1' no menu
2. Menu chama self.cmd_listar.executar()
3. Comando chama listar_use_case.executar(pagina=1)
4. Caso de uso calcula offset e chama repo.listar()
5. Repositório retorna entidades
6. Caso de uso converte para DTOs
7. Presenter formata DTOs em tabela
8. Usuário vê resultado
```

---

## 📊 **Métricas da Fase**

| Métrica | Valor |
|---------|-------|
| Arquivos de interface | 12 |
| Comandos implementados | 8 |
| Presenters | 3 |
| Menus | 3 |
| Linhas de código | ~1500 |
| Testes manuais | 15 cenários |

---

## 📚 **Princípios Aplicados**

| Princípio | Aplicação |
|-----------|-----------|
| **Injeção de Dependência** | Casos de uso injetados nos comandos |
| **Separação de Responsabilidades** | Presenters formatam, comandos orquestram |
| **Single Responsibility** | Cada comando faz uma coisa |
| **Composição** | App composto por casos de uso e comandos |
| **DRY** | Funções de UI centralizadas no console.py |

---

## 🔗 **Integração com Fases Anteriores e Futuras**

| Fase | Relacionamento |
|------|----------------|
| **FASE 1 (Domain)** | Usa value objects via presenters |
| **FASE 2 (Application)** | Usa casos de uso e DTOs |
| **FASE 3 (Infrastructure)** | Repositórios injetados nos casos de uso |
| **FASE 5 (Tradução)** | Comandos de tradução integrados |
| **FASE 6 (Exportação)** | Comandos de exportação |
| **FASE 7 (Relatórios)** | Comandos de relatórios |
| **FASE 8 (Análise)** | Comandos de análise |
| **FASE 9 (Web)** | Mesmos casos de uso, presenters diferentes |

---

## 🚀 **Evolução do Código**

### Antes (código legado - `nav_ui.py`)
```python
# Código misturado, SQL na UI
def navegar_lista():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM documentos")
    # Lógica de paginação manual
    # Formatação manual
```

### Depois (Clean Architecture)
```python
# UI pura, sem saber de banco
def navegar_lista(self):
    resultados = self.listar_use_case.executar(pagina=pagina)
    self.presenter.tabela_documentos(resultados)
```

---

## 📈 **Métricas do Projeto (Após FASE 4)**

```
📊 DOMAIN LAYER: 3 módulos | 13 testes
📊 APPLICATION LAYER: 4 casos de uso | 4 testes
📊 INFRASTRUCTURE LAYER: 3 módulos | 13 testes
📊 INTERFACE LAYER: 12 módulos | Validada manualmente
📊 TOTAL: 30 testes automatizados + interface validada
```

---

## 🔍 **Lições Aprendidas**

1. **Rich é poderoso**: Tabelas, painéis e spinners melhoram muito a experiência
2. **Presenters simplificam a UI**: Separam formatação da lógica
3. **Comandos devem ser pequenos**: Cada comando faz uma coisa bem feita
4. **Menus aninhados funcionam bem**: Submenus para funcionalidades complexas
5. **Feedback é essencial**: Spinners e mensagens de erro/sucesso
6. **Injeção de dependência facilita testes**: Comandos podem ser testados com mocks

---

## 🏁 **Conclusão da Fase**

A FASE 4 entregou uma CLI profissional com:

✅ Navegação intuitiva por menus
✅ Tabelas coloridas e paginadas
✅ Visualização detalhada de documentos
✅ Alternância entre original/tradução
✅ Exportação de documentos
✅ Relatórios e estatísticas
✅ Análise de texto
✅ Integração completa com todas as fases
✅ Código limpo e organizado

---

## 👤 **Autor**

**Thiago Ribeiro** - Projeto de TCC

---

<div align="center">
  <sub>FASE 4 concluída em 15 de Fevereiro de 2024</sub>
  <br>
  <sub>✅ Pronto para a FASE 5 - Tradução Avançada</sub>
</div>
```
