## 📚 **DOCUMENTO: `docs/FASE6_EXPORTACAO.md`**

```markdown
# FASE 6 - Exportação de Documentos

## 📅 Data
Concluído em: 15 de Fevereiro de 2024

## 🎯 Objetivo
Implementar a exportação de documentos nos formatos TXT (e futuramente PDF), permitindo salvar o conteúdo com metadados e escolher entre original e traduções.

## 📁 Estrutura Criada

```
src/
├── application/
│   └── use_cases/
│       └── exportar_documento.py          # Caso de uso de exportação
├── infrastructure/
│   └── export/
│       ├── __init__.py
│       └── txt_exporter.py                 # Exportador TXT
└── interface/
    └── cli/
        └── commands_export.py               # Comandos de exportação
```

## 🧩 Componentes Implementados

### 1. Caso de Uso ExportarDocumento (`exportar_documento.py`)
- **Responsabilidade:** Orquestrar a exportação de documentos
- **Formatos suportados:** TXT (PDF como placeholder)
- **Idiomas:** Original (russo) e todas as traduções disponíveis
- **Metadados:** Opção de incluir cabeçalho com informações do documento
- **Validações:** Verifica existência do documento/idioma antes de exportar

### 2. Exportador TXT (`txt_exporter.py`)
- **Responsabilidade:** Gerar arquivos .txt formatados
- **Funcionalidades:**
  - Criação automática da pasta `exportados/`
  - Geração de cabeçalho com metadados (opcional)
  - Sanitização de nomes de arquivo (remove caracteres especiais)
  - Padronização de nomenclatura: `ID_TITULO_IDIOMA.txt`

### 3. Comando Exportar (`commands_export.py`)
- **Responsabilidade:** Interface interativa para exportação
- **Fluxo:**
  1. Lista idiomas disponíveis (original + traduções)
  2. Permite escolher formato (TXT/PDF)
  3. Pergunta sobre inclusão de metadados
  4. Mostra resumo e confirmação
  5. Executa exportação com feedback

## 🎮 Funcionalidades na UI

### Menu de Exportação:
```
📥 EXPORTAR DOCUMENTO

Idiomas disponíveis:
  [1] 🇷🇺 Original (Russo)
  [2] 🇺🇸 Inglês
  [3] 🇧🇷 Português
  [0] Cancelar

Formatos disponíveis:
  [1] 📄 TXT (recomendado)
  [2] 📑 PDF (em breve)

Incluir metadados no arquivo?
  [1] Sim (recomendado)
  [2] Não (só o texto)

Resumo da exportação:
  • Documento ID: 1
  • Idioma: Inglês
  • Formato: TXT
  • Metadados: Sim
```

### Arquivo Gerado:
```
================================================================================
TÍTULO: Протокол допроса Л.В. Николаева [Inglês]
CENTRO: lencenter
DATA ORIGINAL: 1934, December 4
URL: http://showtrials.ru/...
EXPORTADO EM: 2024-02-15 14:30:22
PESSOA PRINCIPAL: Л.В. Николаева
================================================================================

[CONTEÚDO DO DOCUMENTO...]
```

## 🔄 Fluxo de Exportação

```
[Usuário] → [tecla 'e'] → [ComandoExportar] → [ExportarDocumento (caso de uso)]
    ↑                                                    |
    |                                                    ↓
    └──────── [feedback] ← [TxtExporter] ← [DTO do documento]
```

## 📋 Exemplos de Uso

### Exportar original sem metadados:
```
> Comando: e
> Idioma: 1 (Original)
> Formato: 1 (TXT)
> Metadados: 2 (Não)
Arquivo gerado: exportados/1_Protokol_doprosa_L.V._Nikolaeva_original.txt
```

### Exportar tradução com metadados:
```
> Comando: e
> Idioma: 2 (Inglês)
> Formato: 1 (TXT)
> Metadados: 1 (Sim)
Arquivo gerado: exportados/1_Protokol_doprosa_L.V._Nikolaeva_en.txt
```

## 🧪 Testes Realizados

| Teste | Ação | Resultado Esperado | Status |
|-------|------|-------------------|--------|
| Exportar original | 'e' → 1 → 1 → 1 | Arquivo TXT com metadados | ✅ |
| Exportar tradução | 'e' → 2 → 1 → 1 | Arquivo com conteúdo traduzido | ✅ |
| Sem metadados | Opção 2 no menu | Arquivo só com texto | ✅ |
| Cancelar | Opção 0 | Volta sem exportar | ✅ |
| PDF | Escolher PDF | Mensagem "em breve" | ✅ |
| Documento sem tradução | Só opção original | Menu correto | ✅ |

## 📊 Integração com Fases Anteriores

| Fase | Componente | Uso na Exportação |
|------|------------|-------------------|
| **FASE 1** | `NomeRusso` | Tradução de nomes nos metadados |
| **FASE 2** | `DocumentoDTO` | Dados para exportação |
| **FASE 3** | Repositórios | Busca de documentos e traduções |
| **FASE 4** | CLI Base | Integração com menu existente |
| **FASE 5** | Traduções | Exportar traduções disponíveis |

## 📈 Métricas do Projeto (Atualizado)

```
📊 DOMAIN LAYER: 4 entidades | 15 testes
📊 APPLICATION LAYER: 6 casos de uso | 7 testes
📊 INFRASTRUCTURE LAYER: 5 módulos | 18 testes
📊 INTERFACE LAYER: 8 módulos | Validada manualmente
📊 TOTAL: 40 testes automatizados
```

## 🚀 Como Usar

```bash
# 1. Executar a aplicação
python run.py

# 2. Navegar até um documento (listar + digitar ID)

# 3. Pressionar 'e' durante a visualização

# 4. Seguir o menu interativo:
#    - Escolher idioma
#    - Escolher formato (TXT)
#    - Escolher inclusão de metadados

# 5. Confirmar exportação

# 6. Arquivo será salvo em exportados/
```

## 📂 Estrutura de Arquivos Gerados

```
exportados/
├── 1_Protokol_doprosa_L.V._Nikolaeva_original.txt
├── 1_Protokol_doprosa_L.V._Nikolaeva_en.txt
├── 1_Protokol_doprosa_L.V._Nikolaeva_pt.txt
├── 2_Pismo_V.V._Rumyantseva_original.txt
└── 2_Pismo_V.V._Rumyantseva_en.txt
```

## 🔮 Próximos Passos (FASE 7)

1. **Exportação PDF** (com formatação preservada)
2. **Relatórios avançados** (estatísticas em PDF)
3. **Exportação em lote** (múltiplos documentos)

## 👤 Autor
Thiago Ribeiro - Projeto de TCC
```
