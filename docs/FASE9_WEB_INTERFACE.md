## 📚 **DOCUMENTO: `docs/FASE9_WEB_INTERFACE.md`**

```markdown
# FASE 9 - Web Interface

## 📅 Data
Concluído em: 16 de Fevereiro de 2026

## 🎯 Objetivo
Implementar uma interface web completa para acesso ao acervo de documentos, utilizando FastAPI e templates Jinja2, com simetria funcional à interface CLI.

## 📁 Estrutura Criada

```
src/
└── interface/
    └── web/
        ├── __init__.py
        ├── app.py                          # Aplicação FastAPI principal
        ├── routes/
        │   ├── __init__.py
        │   ├── documentos.py                # Rotas de documentos
        │   ├── analise.py                    # Rotas de análise
        │   ├── traducoes.py                  # Rotas de traduções
        │   └── estatisticas.py               # Rotas de estatísticas
        ├── templates/
        │   ├── base.html                     # Template base
        │   ├── index.html                     # Página inicial
        │   ├── erro.html                       # Página de erro
        │   ├── construcao.html                 # Página em construção
        │   ├── documentos/
        │   │   ├── lista.html                  # Lista de documentos
        │   │   └── detalhe.html                # Detalhe do documento
        │   ├── analise/
        │   │   ├── form.html                    # Formulário de análise
        │   │   ├── resultado.html               # Resultado da análise
        │   │   └── acervo.html                  # Análise global
        │   ├── traducoes/
        │   │   ├── todas.html                   # Todas as traduções
        │   │   ├── lista.html                   # Traduções de um documento
        │   │   └── detalhe.html                 # Visualização de tradução
        │   └── estatisticas/
        │       └── dashboard.html               # Dashboard com gráficos
        └── static/
            ├── css/
            │   └── style.css                    # Estilos personalizados
            └── js/
                └── main.js                       # JavaScript principal
```

## 🧩 Componentes Implementados

### 1. Aplicação FastAPI (`app.py`)
- Factory pattern com injeção de dependência
- Repositórios compartilhados via `app.state`
- Templates Jinja2 configurados
- Arquivos estáticos servidos

### 2. Rotas Implementadas

#### Documentos (`/documentos`)
- `GET /` - Lista paginada com filtros
- `GET /{id}` - Detalhe do documento
- `GET /{id}/json` - Versão JSON para API

#### Análise (`/analise`)
- `GET /acervo` - Análise global do acervo
- `GET /documento/{id}` - Formulário de análise
- `POST /documento/{id}` - Executa análise

#### Traduções (`/traducoes`)
- `GET /` - Lista todas (em desenvolvimento)
- `GET /documento/{id}` - Traduções de um documento
- `GET /documento/{id}/{idioma}` - Visualizar tradução

#### Estatísticas (`/estatisticas`)
- `GET /` - Dashboard com gráficos
- `GET /json` - Dados em formato JSON

### 3. Templates
- **Base**: Navbar, footer, estrutura responsiva
- **Documentos**: Lista com badges e detalhe completo
- **Análise**: Formulário e resultados com métricas
- **Traduções**: Cards e visualização de conteúdo
- **Estatísticas**: Gráficos com Chart.js

### 4. Design e Estilização
- Gradientes e animações CSS
- Cards com efeito hover
- Métricas em destaque
- Breadcrumbs para navegação
- Scrollbar personalizada
- Totalmente responsivo

## 🎮 Funcionalidades na Web

### Página Inicial
```
🏛️ ShowTrials
├── 📋 Documentos: 519
├── 🌐 Traduções: 16
└── 📊 Estatísticas
```

### Lista de Documentos
```
ID | Tipo | Data | Pessoa | Título | Ações
1  | 🔍 INTERROGATÓRIO | 1934 | Nikolaev | Протокол... | [Ver] [Analisar]
```

### Detalhe do Documento
- Metadados completos
- Conteúdo com scroll
- Lista de traduções disponíveis
- Links para análise

### Análise de Texto
- Escolha de idioma
- Opção de nuvem de palavras
- Estatísticas textuais
- Entidades encontradas
- Sentimento do texto

### Dashboard de Estatísticas
- Gráficos interativos (Chart.js)
- Distribuição por centro/tipo
- Pessoas mais frequentes
- Documentos especiais

## 🔧 Desafios Técnicos e Soluções

### 1. Integração com Repositórios
```python
# Injeção de dependência via app.state
app.state.repo_doc = repo_doc
app.state.repo_trad = repo_trad
```

### 2. Templates Jinja2 com JavaScript
```html
{# Passagem de dados do servidor para o cliente #}
const valores = [
    {{ stats.documentos_por_tamanho['pequeno (<1000 palavras)'] }},
    {{ stats.documentos_por_tamanho['médio (1000-5000 palavras)'] }},
    {{ stats.documentos_por_tamanho['grande (>5000 palavras)'] }}
];
```

### 3. Tratamento de Erros
```python
try:
    resultado = use_case.executar(...)
except Exception as e:
    return templates.TemplateResponse(
        "erro.html",
        {"mensagem": str(e), "voltar": "/"},
        status_code=500
    )
```

## 📊 Métricas do Projeto (Atualizado)

```
📊 DOMAIN LAYER: 5 entidades | 18 testes
📊 APPLICATION LAYER: 8 casos de uso | 10 testes
📊 INFRASTRUCTURE LAYER: 6 módulos | 20 testes
📊 INTERFACE LAYER: 
   ├── CLI: 10 módulos | Validada manualmente
   └── Web: 15+ templates | 15+ rotas
📊 TOTAL: 48 testes automatizados + interfaces funcionais
```

## 🚀 Como Executar

```bash
# Instalar dependências
poetry add fastapi uvicorn jinja2 aiofiles python-multipart

# Iniciar servidor
python web_run.py

# Acessar
# http://localhost:8000
# http://localhost:8000/docs (documentação automática)
```

## 🔗 Mapeamento CLI ↔ Web

| Funcionalidade | CLI | Web |
|----------------|-----|-----|
| Listar documentos | Menu → 1 | `/documentos/` |
| Filtrar por centro | Menu → 2 | `?centro=lencenter` |
| Visualizar documento | Digitar ID | `/documentos/1` |
| Estatísticas | Menu → 4 | `/estatisticas/` |
| Análise individual | Menu → 6 → 1 | `/analise/documento/1` |
| Análise do acervo | Menu → 6 → 2 | `/analise/acervo` |
| Nuvem de palavras | Menu → 6 → 3 | `/analise/acervo/wordcloud` |
| Ver traduções | Tecla 't' | `/traducoes/documento/1` |

## 📈 Próximas Melhorias

1. **Autenticação** para acesso remoto
2. **Exportação em PDF** via web
3. **Busca full-text** nos documentos
4. **WebSockets** para análises em tempo real
5. **Modo escuro** (dark mode)

## 👤 Autor
Thiago Ribeiro - Projeto de TCC
```

---



