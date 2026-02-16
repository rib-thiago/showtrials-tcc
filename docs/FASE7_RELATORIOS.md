## 📚 **DOCUMENTO: `docs/FASE7A_RELATORIOS.md`**

```markdown
# FASE 7 - Relatórios Avançados

## 📅 Data
Concluído em: 15 de Fevereiro de 2026

## 🎯 Objetivo
Implementar relatórios detalhados do acervo, com estatísticas completas e insights sobre os documentos históricos.

## 📁 Estrutura Criada

```
src/
├── application/
│   └── use_cases/
│       └── gerar_relatorio.py              # Caso de uso de relatórios
├── infrastructure/
│   └── reports/
│       └── __init__.py
└── interface/
    └── cli/
        └── commands_relatorio.py            # Comandos de relatório
```

## 🧩 Componentes Implementados

### 1. Caso de Uso GerarRelatorio (`gerar_relatorio.py`)
- **Responsabilidade:** Coletar e processar dados do acervo
- **Métricas calculadas:**
  - Total de documentos e traduções
  - Distribuição por centro (Leningrad/Moscow)
  - Distribuição por tipo de documento
  - Distribuição por ano (1934/1935)
  - Top 20 pessoas mais frequentes (com tradução)
  - Documentos especiais (cartas, relatórios, acareações)
  - Traduções por idioma
  - Documentos com anexos

### 2. Comando Relatório (`commands_relatorio.py`)
- **Responsabilidade:** Interface interativa para geração
- **Fluxo:**
  1. Escolha de formato (TXT por enquanto)
  2. Preview do relatório antes de salvar
  3. Salvamento automático na pasta `relatorios/`

## 📊 Exemplo de Relatório Gerado

```text
================================================================================
                       RELATÓRIO DO ACERVO - SHOW TRIALS                        
                                Data: 2026-02-15                                
================================================================================

📊 VISÃO GERAL
----------------------------------------
Total de documentos: 519
Total de traduções: 16
Documentos com anexos: 4
Percentual traduzido: 3.1%

🏛️  DOCUMENTOS POR CENTRO
----------------------------------------
Leningrad: 152 (29.3%)
Moscow: 367 (70.7%)

📋 DOCUMENTOS POR TIPO
----------------------------------------
Protocolo de Interrogatório: 429 (82.7%)
Protocolo de Acareação: 36 (6.9%)
Declaração/Requerimento: 22 (4.2%)
Depoimento Espontâneo: 17 (3.3%)
Correspondência: 7 (1.3%)
Relatório Especial (NKVD): 6 (1.2%)
Laudo Pericial: 1 (0.2%)
Auto de Acusação: 1 (0.2%)

👤 PESSOAS MAIS FREQUENTES
----------------------------------------
 1. Leonid V. Nikolaev (Л.В. Николаева): 42
 2. Г.И. Safarov (Г.И. Сафарова): 29
 3. И.И. Kotolynov (И.И. Котолынова): 13
 4. И.С. Gorshenin (И.С. Горшенина): 12
 5. А.И. Anishev (А.И. Анишева): 12
 6. Г.Е. Evdokimov (Г.Е. Евдокимова): 11
 7. В.В. Rumyantsev (В.В. Румянцева): 10
 8. Н.С. Antonov (Н.С. Антонова): 10
 9. В.И. Zvezdov (В.И. Звездова): 9
10. И.П. Bakaev (И.П. Бакаева): 9
```

## 📈 Métricas do Acervo (Atualizadas)

| Categoria | Quantidade | % |
|-----------|------------|-----|
| **Total de documentos** | 519 | 100% |
| **Documentos classificados** | 519 | 100% |
| **Documentos com tradução** | 16 | 3.1% |
| **Documentos com anexos** | 4 | 0.8% |
| **Total de traduções** | 16 | - |

### Distribuição por Tipo
| Tipo | Quantidade | % |
|------|------------|-----|
| Protocolo de Interrogatório | 429 | 82.7% |
| Protocolo de Acareação | 36 | 6.9% |
| Declaração/Requerimento | 22 | 4.2% |
| Depoimento Espontâneo | 17 | 3.3% |
| Correspondência | 7 | 1.3% |
| Relatório Especial (NKVD) | 6 | 1.2% |
| Laudo Pericial | 1 | 0.2% |
| Auto de Acusação | 1 | 0.2% |

## 🔄 Fluxo de Geração de Relatórios

```
[Usuário] → [Menu → 5] → [ComandoRelatorio] → [GerarRelatorio (caso de uso)]
    ↑                                                    |
    |                                                    ↓
    └── [Preview] ← [Relatório TXT] ← [Coleta de Dados]
```

## 🧪 Testes Realizados

| Teste | Ação | Resultado |
|-------|------|-----------|
| Gerar relatório | Menu → 5 → 1 → s | Arquivo gerado em relatorios/ |
| Preview | Durante geração | Primeiras 15 linhas mostradas |
| Cancelar | Opção 0 | Volta ao menu |
| Formato HTML | Opção 2 | Mensagem "em breve" |

## 📊 Integração com Fases Anteriores

| Fase | Componente | Uso no Relatório |
|------|------------|------------------|
| **FASE 1** | `TipoDocumento`, `NomeRusso` | Classificação e tradução de nomes |
| **FASE 2** | Casos de uso | Estrutura de aplicação |
| **FASE 3** | Repositórios | Acesso aos dados |
| **FASE 4** | CLI | Menu e comandos |
| **FASE 5** | Traduções | Dados de tradução no relatório |
| **FASE 6** | Exportação | Padrão de salvamento em arquivo |

## 📈 Métricas do Projeto (Atualizado)

```
📊 DOMAIN LAYER: 4 entidades | 15 testes
📊 APPLICATION LAYER: 7 casos de uso | 8 testes
📊 INFRASTRUCTURE LAYER: 5 módulos | 18 testes
📊 INTERFACE LAYER: 9 módulos | Validada manualmente
📊 TOTAL: 41 testes automatizados
```

## 🚀 Como Usar

```bash
# 1. Executar a aplicação
python run.py

# 2. Escolher opção 5 - Relatórios avançados

# 3. Escolher formato (1 - TXT)

# 4. Confirmar geração

# 5. Relatório salvo em relatorios/relatorio_YYYYMMDD_HHMMSS.txt
```

## 📂 Estrutura de Arquivos Gerados

```
relatorios/
├── relatorio_20260215_234144.txt
├── relatorio_20260215_235012.txt
└── relatorio_20260216_001203.txt
```

## 🔮 Próximos Passos (FASE 8)

1. **Análise de Texto** (Nuvem de palavras, entidades, sentimentos)
2. **Gráficos visuais** (quando tivermos interface web)
3. **Relatórios interativos** (HTML com JavaScript)

## 👤 Autor
Thiago Ribeiro - Projeto de TCC
```




## 🚀 **PRONTO PARA FASE 8 - ANÁLISE DE TEXTO!**

A FASE 8 vai adicionar:
- Nuvem de palavras
- Extração de entidades (pessoas, locais)
- Análise de sentimentos
- Linha do tempo interativa

**Posso começar a FASE 8 quando você confirmar!** 🎯