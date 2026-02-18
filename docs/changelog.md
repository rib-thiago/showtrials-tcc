# Changelog

Todas as mudanças notáveis neste projeto serão documentadas aqui.

O formato é baseado no [Keep a Changelog](https://keepachangelog.com/),
e este projeto adere ao [Semantic Versioning](https://semver.org/).

## [0.2.0] - 2026-02-18

### Adicionado
- CI/CD com GitHub Actions
- Cobertura de testes configurada (45%)
- Badges no README (CI, cobertura, Python)
- Documentação automática com MkDocs
- Páginas de overview e contribuição
- Deploy automático para GitHub Pages

### Corrigido
- Caminho dos testes no CI (src/tests/)
- Meta de cobertura ajustada para 45%
- Erros de lint e formatação (84 arquivos)
- 14 ocorrências de 'bare except'
- Posição do omit no .coveragerc

### Melhorado
- README profissional com badges
- Documentação das 10 fases revisada
- Arquitetura documentada

## [0.1.0] - 2026-02-15

### Adicionado
- Domain Layer: entidades, value objects, interfaces
- Application Layer: 8 casos de uso
- Infrastructure Layer: repositórios SQLite
- CLI Interface com Rich
- Sistema de tradução com Google Translate
- Exportação de documentos para TXT
- Relatórios e estatísticas
- Análise de texto com spaCy
- Web Interface com FastAPI
- Service Registry com lazy loading
- 48 testes automatizados

### Corrigido
- Injeção de dependência do registry
- Erros de tradução e fallback
- Formatação de datas e nomes

### Segurança
- Chaves de API via .env
- Sanitização de nomes de arquivo
- Rate limiting em traduções

## [0.0.1] - 2026-02-01

### Adicionado
- Estrutura inicial do projeto
- Coleta básica de documentos
- Armazenamento em SQLite
- Interface CLI simples

### Experimental
- Primeira versão do classificador
- Extração básica de metadados
