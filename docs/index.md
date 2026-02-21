# ShowTrials - Documentação


**Sistema para coleta, armazenamento, tradução e análise de documentos históricos**



![Python](https://img.shields.io/badge/python-3.12-blue)
![CI](https://github.com/rib-thiago/showtrials-tcc/actions/workflows/ci.yml/badge.svg)
![Coverage](https://img.shields.io/badge/coverage-45%25-yellow)
![Docs](https://img.shields.io/badge/docs-mkdocs-blue)
![License](https://img.shields.io/badge/license-MIT-green)



## 📚 Sobre o Projeto

ShowTrials é um sistema desenvolvido para pesquisadores e historiadores que necessitam acessar, analisar e traduzir documentos históricos dos processos políticos de Moscou e Leningrado (1934-1935).

O sistema automatiza a coleta de documentos, organiza o acervo em banco de dados relacional, oferece interfaces para visualização e análise, e integra serviços de tradução automática.

## 🎯 Funcionalidades

| Categoria | Funcionalidades |
|-----------|-----------------|
| **Gestão** | Coleta, classificação, metadados, busca |
| **Tradução** | 4 idiomas, persistência, alternância |
| **Análise** | Entidades, sentimentos, estatísticas, wordcloud |
| **Interfaces** | CLI (Rich), Web (FastAPI), API REST |
| **Relatórios** | Estatísticas, exportação TXT, gráficos |

## 🏗️ Arquitetura

O projeto segue **Clean Architecture** com 4 camadas independentes:

- **Domain**: Regras de negócio puras (sem dependências)
- **Application**: Casos de uso e orquestração
- **Infrastructure**: Repositórios e serviços externos
- **Interface**: CLI, Web e API

## 📊 Estatísticas

- **Documentos**: 519
- **Traduções**: 16
- **Testes**: 48 automatizados
- **Cobertura**: 45%
- **Linhas de código**: ~3.500
- **Fases concluídas**: 10

## 🚀 Comece Aqui

- [Visão Geral](overview.md)
- [Arquitetura](ARCHITECTURE.md)
- [Contribuir](contributing.md)
- [Changelog](changelog.md)

## 📁 Navegação Rápida

### Fases do Projeto

- [FASE 1 - Domain Layer](fases/FASE1_DOMAIN.md)
- [FASE 2 - Application Layer](fases/FASE2_APPLICATION.md)
- [FASE 3 - Infrastructure Layer](fases/FASE3_INFRASTRUCTURE.md)
- [FASE 4 - CLI Interface](fases/FASE4_CLI.md)
- [FASE 5 - Tradução Avançada](fases/FASE5_TRADUCAO.md)
- [FASE 6 - Exportação](fases/FASE6_EXPORTACAO.md)
- [FASE 7 - Relatórios](fases/FASE7_RELATORIOS.md)
- [FASE 8 - Análise de Texto](fases/FASE8_ANALISE_TEXTO.md)
- [FASE 9 - Web Interface](fases/FASE9_WEB_INTERFACE.md)
- [FASE 10 - Service Registry](fases/FASE10_SERVICE_REGISTRY.md)

## 👤 Autor

**Thiago Ribeiro** - Projeto de TCC

[GitHub](https://github.com/rib-thiago) | [Email](mailto:mackandalls@gmail.com)

---

<div align="center">
  <sub>Documentação gerada com MkDocs</sub>
  <br>
  <sub>© 2026 Thiago Ribeiro</sub>
</div>
