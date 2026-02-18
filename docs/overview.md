# Visão Geral do Projeto

ShowTrials é um sistema para coleta, armazenamento, tradução e análise de documentos históricos dos processos de Moscou e Leningrado (1934-1935).

## 🎯 Objetivo

Fornecer uma ferramenta para pesquisadores e historiadores acessarem, analisarem e traduzirem documentos históricos de forma eficiente.

## 🏗️ Arquitetura

O projeto segue os princípios da Clean Architecture, com camadas bem definidas:

- **Domain Layer**: Regras de negócio e entidades
- **Application Layer**: Casos de uso e orquestração
- **Infrastructure Layer**: Repositórios e serviços externos
- **Interface Layer**: CLI e Web

## 📊 Estatísticas

- 519 documentos
- 16 traduções
- 48 testes automatizados
- 45% de cobertura

## 🛠️ Tecnologias

- Python 3.12
- Poetry
- SQLite
- FastAPI
- Rich (CLI)
- spaCy (NLP)
- Google Cloud Translation API

## 📁 Estrutura do Projeto

```
.
├── src/                          # Código fonte
│   ├── domain/                   # Camada de domínio
│   ├── application/              # Camada de aplicação
│   ├── infrastructure/           # Camada de infraestrutura
│   └── interface/                # Interfaces (CLI/Web)
├── tests/                        # Testes
├── docs/                         # Documentação
├── data/                         # Banco de dados
├── exportados/                   # Arquivos exportados
├── relatorios/                   # Relatórios
├── analises/                      # Nuvens de palavras
└── legacy/                        # Código legado
```

## 🔄 Fluxo de Desenvolvimento

1. Feature branch a partir da `main`
2. Commits com mensagens padronizadas
3. Pre-commit hooks rodam localmente
4. CI roda testes no GitHub
5. Review e merge

## 📈 Qualidade

- ✅ 48 testes automatizados
- ✅ 45% de cobertura
- ✅ Linting com Ruff
- ✅ Type checking com MyPy (parcial)
- ✅ Formatação com Black/isort
- ✅ CI/CD com GitHub Actions

## 👤 Autor

**Thiago Ribeiro** - Projeto de TCC

- GitHub: [@rib-thiago](https://github.com/rib-thiago)
- Email: mackandalls@gmail.com
