# Guia de Debug do Projeto

## Objetivo

Este guia organiza uma abordagem sistematica para identificar, reproduzir e corrigir problemas no projeto.

Seu objetivo e:

- reduzir depuracao por tentativa e erro
- ajudar a isolar causa raiz antes de modificar codigo
- orientar a verificacao da correcao antes de seguir para revisao e merge

## Contexto de Uso

Este documento deve ser usado quando uma falha, comportamento inesperado ou regressao ja foi detectada.

Ele nao substitui:

- o protocolo de qualidade, que define criterios tecnicos minimos
- o guia de auto-revisao, que integra verificacoes antes de PR e merge
- o guia de telemetria, quando a falha envolver contadores, instrumentacao ou testes especificos de telemetria

## Etapas de Debug

### Reproduzir o Problema

Antes de corrigir, buscar um cenario minimo e repetivel.

Exemplos uteis:

```bash
poetry run pytest src/tests/test_arquivo.py -k "nome_do_teste" -v
poetry run pytest -vv --log-cli-level=DEBUG
gh run view <ID> --log
```

Verificar no minimo:

- se o erro acontece localmente
- se a reproducao e consistente ou intermitente
- qual e o input minimo que aciona o problema
- qual e o comportamento esperado versus o observado

### Isolar

Depois de reproduzir, identificar onde a falha realmente acontece.

Tecnicas uteis:

- reduzir o cenario ao menor trecho possivel
- usar `breakpoint()` ou `pdb`
- adicionar logs temporarios e localizados
- inspecionar tipos e estado real dos objetos

Exemplo:

```python
breakpoint()

logger.debug("Valor de x: %s", x)
```

### Entender a Causa Raiz

Antes de alterar o codigo, responder:

- o que deveria acontecer
- o que realmente aconteceu
- qual e a diferenca entre os dois
- por que essa diferenca existe
- se o problema ocorre so em teste, so em producao ou em ambos

Categorias comuns:

- problema de tipo
- problema de logica
- problema de estado
- problema de dependencia
- problema de concorrencia

### Corrigir

Aplicar a menor mudanca necessaria para resolver o problema.

Boas praticas:

- nao misturar correcao e refatoracao no mesmo passo
- adicionar ou ajustar teste quando isso ajudar a fixar a regressao
- evitar introduzir funcionalidade nova junto com a correcao

### Testar a Correcao

Depois de corrigir, verificar:

- o cenario especifico que falhava agora passa
- testes relacionados ao modulo nao foram degradados
- a mudanca nao introduziu erro colateral evidente
- validacoes tecnicas minimas aplicaveis continuam atendidas

Exemplos uteis:

```bash
poetry run pytest src/tests/test_arquivo.py -k "nome_do_teste" -v
poetry run pytest src/tests/test_*_telemetry.py -v
poetry run pytest -v --pdb
poetry run pytest --durations=10
```

### Prevenir Recorrencia

Quando fizer sentido:

- adicionar teste para o caso corrigido
- fortalecer type hints, contratos ou guard clauses
- registrar comportamento esperado de forma mais clara

### Documentar o Achado

Quando a correcao tiver valor de rastreabilidade, registrar:

- comentario ou fechamento na issue
- mensagem de commit clara
- observacao em changelog, se houver impacto relevante para usuarios
- comentario no codigo, apenas se a decisao nao for obvia

## Ferramentas e Tecnicas Uteis

Ferramentas recorrentes:

- `pytest -v --pdb`
- `pytest -vv --log-cli-level=DEBUG`
- `pytest --durations=10`
- `python -m pdb ...`
- `breakpoint()`
- `gh run view <ID> --log`
- `git bisect`

Essas ferramentas devem ser usadas com foco em isolamento e entendimento da causa, e nao como substituto para uma leitura cuidadosa do fluxo e do contexto da falha.

## Verificacao da Correcao

Antes de considerar o debug encerrado, verificar no minimo:

- o erro foi reproduzido antes da correcao
- a causa raiz foi entendida com clareza suficiente
- a correcao resolveu o problema observado
- a verificacao minima aplicavel foi executada
- nao restaram artefatos temporarios de debug no codigo

## Quando Consultar Outros Guias

- consultar [Protocolo de Qualidade do Projeto](protocolo_de_qualidade.md) para criterios tecnicos minimos e coerencia arquitetural
- consultar [Guia de Auto-Revisao antes de PR e Merge](guia_de_auto_revisao.md) para revisao final da mudanca antes de PR ou merge
- consultar [Guia de Telemetria do Projeto](guia_de_telemetria.md) quando a falha envolver instrumentacao, contadores ou testes de telemetria
- consultar [Automacao Operacional com Taskipy](automacao_operacional_com_taskipy.md) para a automacao atualmente disponivel

## Pendencias e Validacoes Necessarias

- comandos por arquivo mencionados no documento legado nao estao confirmados no `taskipy` atual e nao devem ser tratados aqui como fluxo vigente
- exemplos antigos centrados em telemetria e fases especificas nao representam, sozinhos, o uso total deste guia
- este guia nao define criterios normativos de qualidade, merge ou review; ele apenas organiza a pratica de depuracao antes da revisao final

## Documentos Relacionados

- [Protocolo de Qualidade do Projeto](protocolo_de_qualidade.md)
- [Guia de Auto-Revisao antes de PR e Merge](guia_de_auto_revisao.md)
- [Guia de Telemetria do Projeto](guia_de_telemetria.md)
- [Automacao Operacional com Taskipy](automacao_operacional_com_taskipy.md)
- [Pytest Documentation](https://docs.pytest.org/)
- [Python Debugger (pdb)](https://docs.python.org/3/library/pdb.html)
