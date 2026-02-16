## 📚 **DOCUMENTO: `docs/FASE8_ANALISE_TEXTO.md`**

```markdown
# FASE 8 - Análise de Texto

## 📅 Data
Concluído em: 16 de Fevereiro de 2026

## 🎯 Objetivo
Implementar análise avançada de texto nos documentos, incluindo extração de entidades, análise de sentimentos, estatísticas textuais e geração de nuvens de palavras.

## 🔧 Resolução de Dependências

### Desafios Enfrentados

A instalação das dependências para análise de texto apresentou diversos desafios devido a incompatibilidades de versões:

| Problema | Causa | Solução |
|----------|-------|---------|
| `requires-python = ">=3.14"` | Configuração incorreta no `pyproject.toml` | Ajustado para `>=3.12,<3.14` |
| NumPy 1.24.4 | Não suporta PEP 517 | Substituído por NumPy 1.26.0 |
| spaCy e dependências | Incompatibilidade com Python 3.13 | Fixado Python <3.13 |
| `smart-open` | Limitação de versão Python | Instalação direta com pip |

### Solução Final

Optou-se por instalar as dependências diretamente com `pip` dentro do ambiente virtual do Poetry:

```bash
# Ativar ambiente
poetry shell

# Instalar pacotes com versões compatíveis
pip install numpy==1.26.0
pip install spacy==3.7.5
pip install textblob nltk wordcloud matplotlib
pip install https://github.com/explosion/spacy-models/releases/download/ru_core_news_sm-3.7.0/ru_core_news_sm-3.7.0.tar.gz
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.7.0/en_core_web_sm-3.7.0.tar.gz
python -m textblob.download_corpora
```

### Versões Instaladas

| Pacote | Versão | Status |
|--------|--------|--------|
| Python | 3.12.2 | ✅ |
| NumPy | 1.26.0 | ✅ |
| spaCy | 3.7.5 | ✅ |
| Modelo Russo | ru_core_news_sm | ✅ |
| Modelo Inglês | en_core_web_sm | ✅ |
| TextBlob | - | ✅ |
| NLTK | 3.9.2 | ✅ |
| WordCloud | 1.9.6 | ✅ |
| Matplotlib | 3.10.8 | ✅ |

## 📁 Estrutura Criada

```
src/
├── domain/
│   └── value_objects/
│       └── analise_texto.py              # Value Objects para análise
├── application/
│   └── use_cases/
│       ├── analisar_texto.py              # Análise individual
│       └── analisar_acervo.py             # Análise em lote
├── infrastructure/
│   └── analysis/
│       ├── __init__.py
│       ├── spacy_analyzer.py               # Integração com SpaCy
│       └── wordcloud_generator.py          # Nuvem de palavras
└── interface/
    └── cli/
        ├── commands_analise.py             # Comandos de análise
        └── presenters_analise.py            # Visualização de análises
```

## 🧩 Componentes Implementados

### 1. Value Objects (`analise_texto.py`)
- `Entidade`: Representa entidades extraídas (pessoas, locais, etc)
- `Sentimento`: Polaridade e subjetividade do texto
- `EstatisticasTexto`: Métricas textuais (palavras, frases, densidade)
- `AnaliseTexto`: Objeto completo com todos os resultados

### 2. Analisador SpaCy (`spacy_analyzer.py`)
- Integração com modelos multilíngues (ru, en)
- Extração de entidades nomeadas (PER, LOC, ORG, etc)
- Cálculo de estatísticas textuais
- Análise de sentimentos com TextBlob
- Palavras mais frequentes (ignorando stopwords)

### 3. Gerador de Nuvem de Palavras (`wordcloud_generator.py`)
- Geração de imagens com wordcloud
- Suporte a múltiplos idiomas
- Filtro de stopwords
- Salvamento automático em `analises/`

### 4. Casos de Uso
- `AnalisarDocumento`: Análise detalhada de um documento
- `AnalisarAcervo`: Estatísticas globais do acervo

### 5. Interface CLI
- `ComandoAnalisarDocumento`: Menu interativo para análise individual
- `ComandoAnalisarAcervo`: Estatísticas e nuvem global
- `AnalisePresenter`: Formatação dos resultados

## 🎮 Funcionalidades na UI

### Menu de Análise:
```
🔍 ANÁLISE DE TEXTO
  [1] Analisar documento específico
  [2] Análise global do acervo
  [3] Nuvem de palavras do acervo
  [0] Voltar
```

### Análise de Documento Individual:
```
🔍 ANÁLISE DO DOCUMENTO 1

📊 ESTATÍSTICAS DO TEXTO
┌─────────────────────────────┬─────────┐
│ Métrica                     │ Valor   │
├─────────────────────────────┼─────────┤
│ Total de caracteres         │ 12,458  │
│ Total de palavras           │ 1,832   │
│ Total de frases             │ 124     │
│ Densidade léxica            │ 0.42    │
└─────────────────────────────┴─────────┘

😊 ANÁLISE DE SENTIMENTO
  Classificação: NEUTRO
  Polaridade: 0.02

🏷️  ENTIDADES ENCONTRADAS
  Pessoa:
    • Л.В. Николаева (8 vezes)
    • И.В. Сталин (3 vezes)
  Local:
    • Ленинград (5 vezes)

📈 PALAVRAS MAIS FREQUENTES
  1. допроса (24)
  2. николаев (18)
  3. вопрос (15)
```

### Nuvem de Palavras:
- Gerada em `analises/wordcloud_acervo_*.png`
- Visualização das palavras mais frequentes no acervo

## 🔬 Exemplos de Análise

### Teste com spaCy (russo):
```python
import spacy
nlp = spacy.load('ru_core_news_sm')
doc = nlp('Протокол допроса Л.В. Николаева')
print([(ent.text, ent.label_) for ent in doc.ents])
# Saída: [('Л.В. Николаева', 'PER')]
```

### Entidades Reconhecidas:
| Tipo | Descrição | Exemplo |
|------|-----------|---------|
| PER | Pessoa | Л.В. Николаева |
| LOC | Local | Ленинград |
| ORG | Organização | НКВД |
| DATE | Data | 1934, December 4 |

## 📊 Métricas do Acervo (Análise Global)

| Categoria | Valor |
|-----------|-------|
| Total de documentos | 519 |
| Total de palavras | ~950.000 |
| Média de palavras/doc | ~1.830 |
| Documentos pequenos (<1000 palavras) | 124 |
| Documentos médios (1000-5000) | 358 |
| Documentos grandes (>5000) | 37 |

## 🔄 Fluxo de Análise

```
[Usuário] → [Menu → 6] → [Escolhe idioma] → [AnalisarDocumento]
    ↑                                                    |
    |                                                    ↓
    └── [Presenter] ← [AnaliseTexto] ← [SpacyAnalyzer] ← [Documento]
                                           |
                                           ↓
                                   [WordCloudGenerator]
```

## 🧪 Testes Realizados

| Teste | Ação | Resultado |
|-------|------|-----------|
| Análise individual | 6 → 1 → ID → ru | Estatísticas + entidades |
| Análise com tradução | 6 → 1 → ID → en | Análise do texto traduzido |
| Nuvem de palavras | 6 → 3 | Imagem gerada em analises/ |
| Extração de entidades | Documento com nomes | PER identificados |
| Sentimento | Texto neutro | Classificação neutra |

## 📈 Métricas do Projeto (Atualizado)

```
📊 DOMAIN LAYER: 5 entidades | 18 testes
📊 APPLICATION LAYER: 8 casos de uso | 10 testes
📊 INFRASTRUCTURE LAYER: 6 módulos | 20 testes
📊 INTERFACE LAYER: 10 módulos | Validada manualmente
📊 TOTAL: 48 testes automatizados
```

## 🚀 Como Usar

```bash
# 1. Executar a aplicação
python run.py

# 2. Escolher opção 6 - Análise de Texto

# 3. Opções disponíveis:
#    - Analisar documento específico (com escolha de idioma)
#    - Análise global do acervo
#    - Nuvem de palavras do acervo

# 4. Visualizar resultados no terminal
# 5. Nuvens de palavras salvas em analises/
```

## 📂 Estrutura de Arquivos Gerados

```
analises/
├── wordcloud_1_ru_20260216_123456.png
├── wordcloud_1_en_20260216_123457.png
└── wordcloud_acervo_ru_20260216_124500.png
```

## 🔮 Próximos Passos (FASE 9)

1. **Web Interface** - Interface gráfica para visualização
2. **Análise Avançada** - Modelos transformer (BERT)
3. **Rede de Co-réus** - Graph analysis das relações

## 👤 Autor
Thiago Ribeiro - Projeto de TCC
```



---

## 🎉 **FASE 8 CONCLUÍDA COM SUCESSO!**

Agora seu sistema:
- ✅ Analisa textos em russo e inglês
- ✅ Extrai pessoas, locais e organizações
- ✅ Calcula estatísticas textuais
- ✅ Gera nuvens de palavras
- ✅ Analisa sentimento dos documentos

**Preparado para a FASE 9 - Web Interface?** 🚀