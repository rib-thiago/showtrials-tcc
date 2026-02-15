# FASE 1 - Domain Layer (Camada de Domínio)

## 📅 Data
Concluído em: 15 de Fevereiro de 2024

## 🎯 Objetivo
Implementar o núcleo do sistema com as regras de negócio puras, sem dependências externas.

## 📁 Estrutura Criada

~~~
src/
├── domain/
│ ├── init.py
│ ├── entities/
│ │ ├── init.py
│ │ └── documento.py
│ ├── value_objects/
│ │ ├── init.py
│ │ ├── tipo_documento.py
│ │ └── nome_russo.py
│ └── interfaces/
│ ├── init.py
│ └── repositories.py
└── tests/
├── init.py
├── test_documento.py
└── test_tipo_documento.py
~~~


## 🧩 Componentes Implementados

### 1. Entidade Documento (`entities/documento.py`)
- Representa um documento histórico
- Validações de negócio (centro, título, URL)
- Propriedades derivadas (tamanho, resumo)
- Extração de nomes russos do título

### 2. Value Object TipoDocumento (`value_objects/tipo_documento.py`)
- Enumeração com 8 tipos de documentos
- Classificação automática por padrões no título
- Descrições em português e inglês
- Ícones para UI

### 3. Value Object NomeRusso (`value_objects/nome_russo.py`)
- Validação de formato (Л.В. Николаева)
- Separação de iniciais e sobrenome
- Remoção de declinações (genitivo → nominativo)
- Transliteração GOST 7.79-2000
- Dicionário de exceções para nomes famosos

### 4. Interface RepositorioDocumento (`interfaces/repositories.py`)
- Contrato para persistência
- Métodos: salvar, buscar, listar, contar, remover
- Abstração para futuras implementações (SQLite, PostgreSQL)

## 🧪 Testes

~~~
src/tests/test_documento.py
├── test_criar_documento_valido
├── test_centro_invalido
├── test_titulo_vazio
├── test_extrair_pessoas_do_titulo
└── test_to_dict_com_data

src/tests/test_tipo_documento.py
├── test_classificar_interrogatorio
├── test_classificar_acareacao
├── test_classificar_carta
├── test_classificar_relatorio
├── test_classificar_depoimento_singular
├── test_classificar_depoimento_plural
├── test_titulo_desconhecido
└── test_listar_todos
~~~


**Total: 13 testes | Todos PASSANDO ✅**

## 📊 Resultados

```bash
poetry run pytest src/tests/ -v
==================================================================== 13 passed in 0.10s =====================================================================
```

## 🔧 Configurações Realizadas

> pyproject.toml (adições)

~~~
[tool.poetry]
packages = [{include = "src"}]

[tool.pytest.ini_options]
pythonpath = ["src"]
~~~

## 📚 Princípios Aplicados
| Princípio             | Aplicação                                      |
|-----------------------|-----------------------------------------------|
| Clean Architecture    | Domain isolado, sem dependências              |
| Value Objects         | TipoDocumento e NomeRusso imutáveis           |
| Interfaces (Ports)    | RepositorioDocumento como abstração           |
| Testes Unitários      | 13 testes validando regras                    |
| DRY                   | Lógica de nomes centralizada                  |


## 🚀 Próximos Passos (FASE 2)
- Application Layer: Casos de uso (listar, classificar, traduzir)

- DTOs: Objetos para transferência de dados

- Injeção de Dependência: Conectar casos de uso com repositórios

## 👤 Autor
Thiago Ribeiro - Projeto de TCC

