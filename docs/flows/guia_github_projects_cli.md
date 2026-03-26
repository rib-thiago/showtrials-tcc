# Guia de GitHub Projects com gh CLI

## Objetivo

Este guia descreve como consultar projetos, identificar itens e atualizar o status de uma issue em GitHub Projects (v2) usando a CLI oficial do GitHub.

Seu objetivo e:

- apoiar a operacao do fluxo de status definido na politica de governanca
- facilitar a consulta de IDs necessarios para comandos de GitHub Projects
- evitar que detalhes tecnicos de CLI fiquem espalhados em documentos normativos

## Contexto de Uso

Este guia deve ser lido como apoio tecnico ao fluxo oficial de status do projeto.

Os IDs exibidos abaixo sao exemplos genericos. IDs reais de projeto, campo, item e opcao podem mudar e devem ser consultados em fonte operacional apropriada, nao em documentos publicos versionados.

## Identificadores Importantes

No Projects (v2) existem diferentes identificadores internos:

| Conceito                 | Exemplo                          | Onde é usado                        |
| ------------------------ | -------------------------------- | ----------------------------------- |
| **Project Number**       | `1`                              | Usado em `field-list` e `item-list` |
| **Project ID (GraphQL)** | `PVT_PROJECT_ID_EXEMPLO`         | Usado em `item-edit`                |
| **Item ID**              | `PVTI_ITEM_ID_EXEMPLO`           | Usado em `item-edit`                |
| **Field ID**             | `PVTSSF_FIELD_ID_EXEMPLO`        | Usado em `item-edit`                |
| **Option ID**            | `OPTION_ID_DONE_EXEMPLO`         | Usado em `item-edit`                |

Importante:
O número da issue (`#2`) **não é** o Item ID do Project.

## Listar Projetos e Obter o Project ID

```bash
gh project list --owner <OWNER> --format json
```

Exemplo:

```bash
gh project list --owner rib-thiago --format json
```

No JSON retornado, copie:

* `number` -> usado em `field-list`
* `id` -> usado em `item-edit`

## Listar Itens e Obter o Item ID

```bash
gh project item-list <PROJECT_NUMBER> --owner <OWNER>
```

Exemplo:

```bash
gh project item-list 1 --owner rib-thiago
```

Saída típica:

```
TYPE   TITLE                         NUMBER  REPOSITORY                  ID
Issue  Revisar documentacao           2       rib-thiago/showtrials-tcc  PVTI_ITEM_ID_EXEMPLO
```

Copie o valor da coluna **ID** correspondente à issue desejada.

## Listar Campos e Obter Field ID e Option ID

```bash
gh project field-list <PROJECT_NUMBER> --owner <OWNER> --format json
```

Exemplo:

```bash
gh project field-list 1 --owner rib-thiago --format json
```

Procure o campo `"Status"`:

```json
{
  "id": "PVTSSF_FIELD_ID_EXEMPLO",
  "name": "Status",
  "options": [
    { "id": "OPTION_ID_BACKLOG_EXEMPLO", "name": "Backlog" },
    { "id": "OPTION_ID_READY_EXEMPLO", "name": "Ready" },
    { "id": "OPTION_ID_IN_PROGRESS_EXEMPLO", "name": "In Progress" },
    { "id": "OPTION_ID_IN_REVIEW_EXEMPLO", "name": "In Review" },
    { "id": "OPTION_ID_DONE_EXEMPLO", "name": "Done" }
  ]
}
```

Você precisa copiar:

* `id` do campo `"Status"` -> **FIELD_ID**
* `id` da opcao `"Done"` -> **OPTION_ID**

## Atualizar o Status de um Item

Com todos os IDs em mãos:

```bash
gh project item-edit \
  --id <ITEM_ID> \
  --project-id <PROJECT_ID> \
  --field-id <FIELD_ID> \
  --single-select-option-id <OPTION_ID>
```

Exemplo completo:

```bash
gh project item-edit \
  --id PVTI_ITEM_ID_EXEMPLO \
  --project-id PVT_PROJECT_ID_EXEMPLO \
  --field-id PVTSSF_FIELD_ID_EXEMPLO \
  --single-select-option-id OPTION_ID_DONE_EXEMPLO
```

## Fluxo Resumido

1. `gh project list` → obter **Project ID**
2. `gh project item-list` → obter **Item ID**
3. `gh project field-list` → obter **Field ID** e **Option ID**
4. `gh project item-edit` → atualizar Status

## Observacoes Tecnicas

* Projects (v2) usa **GraphQL IDs**, nao nomes.
* `field-list` usa o **numero do projeto**, nao o ID GraphQL.
* `item-edit` exige todos os IDs internos.
* Campos do tipo *Single Select* (como Status) exigem `--single-select-option-id`.

## Documentos Relacionados

- [Politica de Governanca do Projeto](politica_de_governanca.md)
- [Protocolo de Git do Projeto](protocolo_de_git.md)
