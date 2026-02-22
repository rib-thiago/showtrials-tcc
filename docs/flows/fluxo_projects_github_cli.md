# Gerenciamento de Issues em GitHub Projects (v2) usando `gh` CLI

Este documento descreve como listar projetos, identificar itens (issues) dentro de um Project e mover uma issue entre colunas (ex: para **Done**) usando a CLI oficial do GitHub.

---

# 1. Conceitos Importantes

No **Projects (v2)** existem três tipos de identificadores diferentes:

| Conceito                 | Exemplo                          | Onde é usado                        |
| ------------------------ | -------------------------------- | ----------------------------------- |
| **Project Number**       | `1`                              | Usado em `field-list` e `item-list` |
| **Project ID (GraphQL)** | `PVT_kwHOBE0jLc4BPrP8`           | Usado em `item-edit`                |
| **Item ID**              | `PVTI_lAHOBE0jLc4BPrP8zgl0lkE`   | Usado em `item-edit`                |
| **Field ID**             | `PVTSSF_lAHOBE0jLc4BPrP8zg-BEh0` | Usado em `item-edit`                |
| **Option ID**            | `98236657`                       | Usado em `item-edit`                |

Importante:
O número da issue (`#2`) **não é** o Item ID do Project.

---

# 2. Listar Projects e obter o Project ID

```bash
gh project list --owner <OWNER> --format json
```

Exemplo:

```bash
gh project list --owner rib-thiago --format json
```

No JSON retornado, copie:

* `number` → usado em `field-list`
* `id` → usado em `item-edit`

---

# 3. Listar Itens do Project e obter o ITEM_ID

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
Issue  Revisar documentação           2       rib-thiago/showtrials-tcc  PVTI_lAHOBE0jLc4BPrP8zgl0lkE
```

Copie o valor da coluna **ID** correspondente à issue desejada.

---

# 4. Listar Campos do Project e obter FIELD_ID + OPTION_ID

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
  "id": "PVTSSF_lAHOBE0jLc4BPrP8zg-BEh0",
  "name": "Status",
  "options": [
    { "id": "f75ad846", "name": "Backlog" },
    { "id": "61e4505c", "name": "Ready" },
    { "id": "47fc9ee4", "name": "In progress" },
    { "id": "df73e18b", "name": "In review" },
    { "id": "98236657", "name": "Done" }
  ]
}
```

Você precisa copiar:

* `id` do campo `"Status"` → **FIELD_ID**
* `id` da opção `"Done"` → **OPTION_ID**

---

# 5. Mover uma Issue para "Done"

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
  --id PVTI_lAHOBE0jLc4BPrP8zgl0lkE \
  --project-id PVT_kwHOBE0jLc4BPrP8 \
  --field-id PVTSSF_lAHOBE0jLc4BPrP8zg-BEh0 \
  --single-select-option-id 98236657
```

---

# 6. Fluxo Resumido

1. `gh project list` → obter **Project ID**
2. `gh project item-list` → obter **Item ID**
3. `gh project field-list` → obter **Field ID** e **Option ID**
4. `gh project item-edit` → atualizar Status

---

# 7. Observações Técnicas

* Projects (v2) usa **GraphQL IDs**, não nomes.
* `field-list` usa o **número do projeto**, não o ID GraphQL.
* `item-edit` exige todos os IDs internos.
* Campos do tipo *Single Select* (como Status) exigem `--single-select-option-id`.

---

Este procedimento permite gerenciar completamente o fluxo de status de issues em um GitHub Project usando apenas a CLI.
