# FASE 2 - Application Layer (Camada de Aplicação)

## 📅 Data
Concluído em: 15 de Fevereiro de 2024

## 🎯 Objetivo
Implementar os casos de uso que orquestram as regras de negócio do domínio, criando uma camada de aplicação independente de infraestrutura.

## 📁 Estrutura Criada
~~~
src/
├── application/
│ ├── init.py
│ ├── use_cases/
│ │ ├── init.py
│ │ ├── classificar_documento.py
│ │ ├── listar_documentos.py
│ │ ├── obter_documento.py
│ │ └── estatisticas.py
│ └── dtos/
│ ├── init.py
│ ├── documento_dto.py
│ └── estatisticas_dto.py
└── tests/
└── test_use_cases.py
~~~


## 🧩 Componentes Implementados

### 1. Data Transfer Objects (DTOs)

#### `DocumentoDTO` e `DocumentoListaDTO`
- **Responsabilidade:** Separar os dados do domínio do que é exposto para a UI
- **Benefício:** A UI não precisa conhecer a estrutura completa da entidade
- **Métodos:** `from_domain()` - conversão segura de entidade para DTO

#### `EstatisticasDTO`
- **Responsabilidade:** Agregar todas as métricas do acervo
- **Propriedades:** totais, distribuições, pessoas frequentes, custos
- **Propriedades derivadas:** `percentual_traduzido`, `resumo`

### 2. Casos de Uso

#### `ClassificarDocumento`
- **Responsabilidade:** Classificar documentos baseado no título
- **Métodos:**
  - `executar(documento_id)`: Classifica um documento específico
  - `executar_em_lote(limite)`: Classifica múltiplos documentos
- **Regras aplicadas:**
  - Detecção de tipo (interrogatório, carta, etc)
  - Extração de nomes russos
  - Detecção de anexos

#### `ListarDocumentos`
- **Responsabilidade:** Listar documentos com paginação e filtros
- **Filtros:** centro, tipo de documento
- **Paginação:** offset/limite com cálculo de total de páginas
- **Retorno:** Dicionário com items, total, página atual, total_páginas

#### `ObterDocumento`
- **Responsabilidade:** Buscar documento completo por ID
- **Diferencial:** Retorna DTO já com tradução de nomes (opcional)
- **Tratamento:** Retorna None se documento não existir

#### `ObterEstatisticas`
- **Responsabilidade:** Calcular estatísticas completas do acervo
- **Métricas:**
  - Total de documentos e traduções
  - Distribuição por centro e tipo
  - Pessoas mais frequentes
  - Documentos especiais (cartas, relatórios, etc)
  - Documentos com anexos

## 🧪 Testes

```bash
poetry run pytest src/tests/test_use_cases.py -v
```

## Resultado

```
src/tests/test_use_cases.py::TestClassificarDocumento::test_classificar_interrogatorio PASSED
src/tests/test_use_cases.py::TestClassificarDocumento::test_documento_nao_encontrado PASSED
src/tests/test_use_cases.py::TestListarDocumentos::test_listar_com_paginacao PASSED
src/tests/test_use_cases.py::TestObterDocumento::test_obter_documento_completo PASSED
```

Total: 4 testes | Todos PASSANDO ✅

## 🔄 Fluxo de Dados

```
[UI/CLI] → [Caso de Uso] → [Repositório (interface)] → [Domínio]
    ↑            ↑                    ↓                      ↓
    └────[DTO]───┘            [Implementação futura]   [Entidades]

```

## 📊 Princípios Aplicados


| Princípio | Aplicação |
|-----------|-----------|
|Injeção de Dependência |	Casos de uso recebem repositório via construtor|
|Interface Segregation|	DTOs expõem apenas dados necessários|
|Single Responsibility|	Cada caso de uso tem uma única responsabilidade|
|Testabilidade|	Uso de mocks para testar isoladamente|
|Imutabilidade|	DTOs são dataclasses imutáveis|

## 🚀 Integração com FASE 1

A FASE 2 depende exclusivamente da FASE 1:

Usa Documento (entidade)

Usa TipoDocumento e NomeRusso (value objects)

Usa RepositorioDocumento (interface)

Nenhuma dependência para fora do domínio! ✅

## 📈 Métricas do Projeto (Atualizado)

📊 DOMAIN LAYER: 3 módulos | 13 testes
📊 APPLICATION LAYER: 4 casos de uso | 4 testes
📊 TOTAL: 17 testes passando

## 🔜 Próximos Passos (FASE 3)

- Infrastructure Layer: Implementar repositórios concretos (SQLite)

- Integração com dados reais: Conectar casos de uso ao banco existente

- CLI Refatorada: Usar os casos de uso na interface

## 👤 Autor

Thiago Ribeiro - Projeto de TCC