# ShowTrials - Sistema de Gestão de Documentos Históricos

<div align="center">

![Python](https://img.shields.io/badge/python-3.12-blue)
![CI](https://github.com/rib-thiago/showtrials-tcc/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/badge/license-MIT-green)
![Coverage](https://img.shields.io/badge/coverage-48%25-yellow)
![Code style](https://img.shields.io/badge/code%20style-black-000000.svg)
![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)
![FastAPI](https://img.shields.io/badge/FastAPI-0.129.0-009688)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57)

**Sistema para coleta, armazenamento, tradução e análise de documentos históricos**

[📚 Documentação](docs/) | [🚀 Instalação](#instalação) | [📊 Estatísticas](#estatísticas) | [🤝 Contribuir](#contribuindo)

</div>

---

## ✨ Funcionalidades

### 📋 **Gestão de Documentos**
- Coleta automatizada de documentos do site showtrials.ru
- Classificação automática por tipo (interrogatório, carta, acareação, etc)
- Extração de metadados (pessoas, datas, anexos)
- Armazenamento estruturado em SQLite

### 🌐 **Tradução Multilíngue**
- Integração com Google Cloud Translation API
- Suporte a 4 idiomas (Inglês, Português, Espanhol, Francês)
- Persistência de traduções no banco de dados
- Alternância entre original/tradução com um comando

### 🔍 **Análise de Texto**
- Extração de entidades (pessoas, locais, organizações)
- Análise de sentimentos (polaridade e subjetividade)
- Estatísticas textuais detalhadas
- Geração de nuvens de palavras

### 🖥️ **Múltiplas Interfaces**
- **CLI**: Interface de linha de comando com navegação interativa
- **Web**: Interface web moderna com FastAPI e templates
- **API**: Endpoints REST para integração

### 📊 **Relatórios e Exportação**
- Relatórios detalhados do acervo
- Exportação para TXT com metadados
- Estatísticas completas e gráficos interativos

---

## 🏗️ **Arquitetura**

O projeto segue os princípios da **Clean Architecture** com 4 camadas:

```
┌─────────────────────────────────────────────────────────────┐
│                    INTERFACE LAYER                           │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │     CLI     │  │  Web (API)  │  │   Web UI    │        │
│  │   (Rich)    │  │  (FastAPI)  │  │ (Templates) │        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   APPLICATION LAYER                          │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              Casos de Uso                            │   │
│  │  • ListarDocumentos    • TraduzirDocumento          │   │
│  │  • ObterDocumento      • ListarTraducoes            │   │
│  │  • ClassificarDocumento • AnalisarTexto             │   │
│  │  • ObterEstatisticas   • AnalisarAcervo             │   │
│  │  • ExportarDocumento   • GerarRelatorio             │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      DOMAIN LAYER                            │
│  ┌─────────────┐  ┌─────────────────┐  ┌─────────────┐    │
│  │  Entidades  │  │  Value Objects  │  │ Interfaces  │    │
│  │ • Documento │  │ • TipoDocumento │  │ Repositorio │    │
│  │ • Traducao  │  │ • NomeRusso     │  │   Documento │    │
│  │             │  │ • AnaliseTexto  │  │   Traducao  │    │
│  └─────────────┘  └─────────────────┘  └─────────────┘    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                  INFRASTRUCTURE LAYER                        │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │  SQLite     │  │   Google    │  │   SpaCy/    │        │
│  │ Repositório │  │  Translate  │  │   TextBlob  │        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
└─────────────────────────────────────────────────────────────┘
```

---

## 🚀 **Instalação**

### Pré-requisitos
- Python 3.12+
- Poetry
- Git

### Passos

```bash
# 1. Clonar o repositório
git clone https://github.com/seu-usuario/showtrials.git
cd showtrials

# 2. Instalar dependências
poetry install

# 3. Ativar ambiente virtual
poetry shell

# 4. Configurar variáveis de ambiente
cp .env.example .env
# Edite .env com suas chaves de API

# 5. Inicializar banco de dados
python scripts/migrar_dados_existentes.py

# 6. Executar a aplicação
python run.py        # CLI
# ou
python web_run.py    # Web (acesse http://localhost:8000)
```

---

## 📖 **Como Usar**

### Interface CLI

```bash
python run.py
```

**Menu principal:**
```
  [1] 📋 Listar todos os documentos
  [2] 🏛️  Listar por centro
  [3] 👁️  Visualizar documento
  [4] 📊 Estatísticas
  [5] 📈 Relatórios avançados
  [6] 🔍 Análise de texto
  [7] 🔄 Sair
```

**Comandos durante visualização:**
- `t` - Alternar entre original/tradução
- `n` - Nova tradução
- `e` - Exportar documento
- `Enter` - Voltar

### Interface Web

```bash
python web_run.py
# Acesse http://localhost:8000
```

---

## 🧪 **Testes**

```bash
# Executar todos os testes
poetry run pytest tests/ -v

# Com cobertura
poetry run pytest --cov=src tests/

# Gerar relatório HTML de cobertura
poetry run pytest --cov=src --cov-report=html tests/
open htmlcov/index.html
```

**Cobertura atual:** 48 testes automatizados

---

## 📁 **Estrutura do Projeto**

```
.
├── src/                          # Código fonte principal
│   ├── domain/                   # Camada de domínio
│   ├── application/              # Camada de aplicação
│   ├── infrastructure/           # Camada de infraestrutura
│   └── interface/                # Camada de interface (CLI/Web)
├── tests/                        # Testes automatizados
├── docs/                         # Documentação
│   ├── FASE1_DOMAIN.md
│   ├── FASE2_APPLICATION.md
│   ├── FASE3_INFRASTRUCTURE.md
│   ├── FASE4_CLI.md
│   ├── FASE5_TRADUCAO.md
│   ├── FASE6_EXPORTACAO.md
│   ├── FASE7_RELATORIOS.md
│   ├── FASE8_ANALISE_TEXTO.md
│   └── FASE9_WEB_INTERFACE.md
├── scripts/                       # Scripts utilitários
│   └── migrar_dados_existentes.py
├── data/                          # Banco de dados SQLite
│   └── showtrials.db
├── exportados/                    # Documentos exportados
├── relatorios/                    # Relatórios gerados
├── analises/                       # Nuvens de palavras
├── legacy/                         # Código legado (backup)
├── pyproject.toml                  # Dependências e configurações
├── poetry.lock                     # Lock file
├── .pre-commit-config.yaml         # Git hooks
├── .ruff.toml                      # Configuração do Ruff
├── .env.example                    # Exemplo de variáveis de ambiente
├── run.py                          # Ponto de entrada da CLI
├── web_run.py                      # Ponto de entrada da Web
└── README.md                       # Este arquivo
```

---

## 🤝 **Contribuindo**

1. Faça um fork do projeto
2. Crie uma branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'feat: adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

### Padrões de Commit

- `feat`: Nova funcionalidade
- `fix`: Correção de bug
- `docs`: Documentação
- `style`: Formatação
- `refactor`: Refatoração
- `test`: Testes
- `chore`: Tarefas de manutenção

---

## 📚 **Documentação Detalhada**

- [FASE 1 - Domain Layer](docs/FASE1_DOMAIN.md) - Entidades e regras de negócio
- [FASE 2 - Application Layer](docs/FASE2_APPLICATION.md) - Casos de uso e DTOs
- [FASE 3 - Infrastructure Layer](docs/FASE3_INFRASTRUCTURE.md) - Repositórios e serviços
- [FASE 4 - CLI Interface](docs/FASE4_CLI.md) - Interface de linha de comando
- [FASE 5 - Tradução Avançada](docs/FASE5_TRADUCAO.md) - Tradução e alternância
- [FASE 6 - Exportação](docs/FASE6_EXPORTACAO.md) - Exportação de documentos
- [FASE 7 - Relatórios](docs/FASE7_RELATORIOS.md) - Relatórios e estatísticas
- [FASE 8 - Análise de Texto](docs/FASE8_ANALISE_TEXTO.md) - NLP e entidades
- [FASE 9 - Web Interface](docs/FASE9_WEB_INTERFACE.md) - Interface web

---

## 🛠️ **Tecnologias Utilizadas**

| Categoria | Tecnologias |
|-----------|-------------|
| **Linguagem** | Python 3.12 |
| **Gerenciamento** | Poetry |
| **Banco de Dados** | SQLite |
| **CLI** | Rich |
| **Web** | FastAPI, Jinja2, Bootstrap, Chart.js |
| **Tradução** | Google Cloud Translation API |
| **Análise de Texto** | spaCy, TextBlob, NLTK, WordCloud, Matplotlib |
| **Qualidade** | Black, isort, Ruff, pre-commit |
| **Testes** | pytest, pytest-cov |

---

## 📄 **Licença**

Este projeto é desenvolvido para fins acadêmicos. Todos os documentos pertencem aos seus respectivos arquivos históricos.

Fonte: [showtrials.ru](http://showtrials.ru)

---

## 👤 **Autor**

**Thiago Ribeiro**
- Email: mackandalls@gmail.com
- GitHub: [@thiago](https://github.com/seu-usuario)
- Projeto de TCC - [Instituição]

---

## 🙏 **Agradecimentos**

- Aos arquivos históricos que tornaram esta pesquisa possível
- À comunidade open source pelas ferramentas utilizadas
- Aos orientadores e colaboradores do projeto

---

<div align="center">
  <sub>Built with ❤️ for historical research</sub>
  <br>
  <sub>© 2026 Thiago Ribeiro</sub>
</div>
```
