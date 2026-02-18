# Guia de Contribuição

## 🚀 Primeiros Passos

### 1. Fork e Clone

```bash
git clone https://github.com/seu-usuario/showtrials-tcc.git
cd showtrials-tcc
```

### 2. Ambiente Virtual

```bash
# Instalar Poetry (se não tiver)
curl -sSL https://install.python-poetry.org | python3 -

# Instalar dependências
poetry install

# Ativar ambiente
poetry shell
```

### 3. Configurar Git Hooks

```bash
pre-commit install
pre-commit install --hook-type pre-push
```

### 4. Variáveis de Ambiente

```bash
cp .env.example .env
# Edite .env com suas chaves (Google Translate, etc)
```

## 📝 Padrões de Commit

Usamos [Conventional Commits](https://www.conventionalcommits.org/):

| Tipo | Descrição | Exemplo |
|------|-----------|---------|
| `feat` | Nova funcionalidade | `feat: adiciona exportação PDF` |
| `fix` | Correção de bug | `fix: corrige erro no tradutor` |
| `docs` | Documentação | `docs: atualiza README` |
| `style` | Formatação | `style: aplica black` |
| `refactor` | Refatoração | `refactor: simplifica caso de uso` |
| `test` | Testes | `test: adiciona testes do registry` |
| `chore` | Tarefas | `chore: atualiza dependências` |

## 🧪 Testes

### Executar todos os testes
```bash
poetry run pytest tests/ -v
```

### Com cobertura
```bash
poetry run pytest --cov=src tests/
```

### Ver cobertura no HTML
```bash
poetry run pytest --cov=src --cov-report=html tests/
open htmlcov/index.html
```

## 🔍 Verificações de Qualidade

### Linting
```bash
poetry run ruff check src/
```

### Type Checking
```bash
poetry run mypy src/
```

### Formatação
```bash
poetry run black src/
poetry run isort src/
```

## 📚 Documentação

### Servir localmente
```bash
poetry run mkdocs serve
# Acesse http://127.0.0.1:8000
```

### Publicar no GitHub Pages
```bash
poetry run mkdocs gh-deploy
```

## 🚀 Fluxo de Trabalho

### 1. Criar branch
```bash
git checkout -b feat/nova-funcionalidade
```

### 2. Desenvolver com commits pequenos
```bash
git add .
git commit -m "feat: adiciona parte X"
```

### 3. Manter sincronizado
```bash
git fetch origin
git rebase origin/main
```

### 4. Push e criar PR
```bash
git push origin feat/nova-funcionalidade
# Abrir Pull Request no GitHub
```

### 5. Aguardar CI passar
- ✅ Ruff
- ✅ MyPy
- ✅ Testes
- ✅ Cobertura

## 🐛 Reportar Bugs

Ao reportar bugs, inclua:

- Descrição clara do problema
- Passos para reproduzir
- Comportamento esperado
- Logs de erro (se houver)
- Versão do Python e SO

## 💡 Sugerir Melhorias

Use Issues para sugerir:

- Novas funcionalidades
- Melhorias na documentação
- Otimizações de performance
- Ideias para pesquisa histórica

## 🤝 Código de Conduta

- Seja respeitoso
- Aceite feedback construtivo
- Foque no que é melhor para o projeto
- Mostre empatia com outros contribuidores

## 📄 Licença

Este projeto é acadêmico. Todo código é aberto para fins educacionais.
