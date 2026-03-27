# Guia de Refatoracao Segura

## Objetivo

Este guia organiza uma abordagem segura para refatorar codigo sem alterar comportamento externo de forma indevida.

Seu objetivo e:

- reduzir refatoracao oportunista ou misturada com outras mudancas
- manter rastreabilidade e reversibilidade do trabalho
- orientar verificacoes antes e depois da mudanca

## O Que Este Guia Considera Refatoracao

Neste contexto, refatoracao significa alterar a estrutura interna do codigo sem mudar intencionalmente seu comportamento externo.

Exemplos tipicos:

- renomear variaveis, funcoes ou metodos
- extrair metodo
- mover responsabilidade para modulo mais adequado
- remover duplicacao
- simplificar condicionais ou fluxos internos

Nao entram aqui como refatoracao pura:

- adicionar funcionalidade nova
- corrigir bug com mudanca de comportamento
- alterar API publica
- mudar regra de negocio

## Quando Refatorar

Refatoracao costuma fazer sentido quando houver:

- metodo excessivamente longo
- responsabilidades mal distribuidas
- codigo duplicado
- nomes pouco claros
- condicionais ou fluxos dificeis de entender

Boas janelas para refatorar:

- antes de adicionar funcionalidade nova, se o trecho estiver impedindo evolucao segura
- depois de entender um trecho confuso o suficiente para melhorar sua estrutura
- como parte de uma melhoria estrutural explicitamente delimitada

Este guia nao recomenda misturar refatoracao e funcionalidade nova no mesmo passo de trabalho.

## Regras Operacionais de Refatoracao

- fazer uma mudanca pequena por vez
- evitar misturar refatoracao com correcao de bug ou nova funcionalidade
- manter commits legiveis e atomicos
- buscar reduzir complexidade, e nao apenas redistribuir linhas
- preservar ou melhorar clareza, responsabilidades e testabilidade

Em termos praticos:

- se a mudanca alterar comportamento, ela deixa de ser refatoracao pura
- se a mudanca ficar grande demais, dividir em passos menores
- se a refatoracao comecar a esconder uma mudanca estrutural maior, ela deve ser explicitada como tal

## Verificacao Antes e Depois da Mudanca

Antes de iniciar, verificar no minimo:

- se o trecho realmente pede refatoracao
- se o comportamento esperado esta claro
- se existe base suficiente para validar a mudanca depois

Depois da refatoracao, verificar no minimo:

- o comportamento observado continua coerente com o esperado
- a mudanca nao introduziu erro evidente
- a estrutura ficou mais clara, e nao mais complexa
- validacoes tecnicas minimas aplicaveis continuam atendidas

Exemplos uteis:

```bash
task check
task test
task test-cov
```

## Quando Consultar Outros Guias

- consultar [Protocolo de Qualidade do Projeto](../protocolos/protocolo_de_qualidade.md) para criterios tecnicos minimos, coerencia arquitetural e clareza estrutural
- consultar [Guia de Auto-Revisao antes de PR e Merge](guia_de_auto_revisao.md) para a revisao final da mudanca antes de PR ou merge
- consultar [Guia de Debug do Projeto](guia_de_debug.md) se a refatoracao introduzir falha ou comportamento inesperado
- consultar [Automacao Operacional com Taskipy](automacao_operacional_com_taskipy.md) para a automacao atualmente disponivel

## Pendencias e Validacoes Necessarias

- comandos do documento legado como `task cov-file`, `radon` e `pylint` nao devem ser tratados aqui como fluxo vigente sem validacao adicional
- thresholds rigidos de cobertura por arquivo nao estao consolidados como regra atual do projeto
- estrategia especifica de merge ou branch para refatoracao continua ancorada nos documentos de Git e auto-revisao, nao neste guia

## Documentos Relacionados

- [Protocolo de Qualidade do Projeto](../protocolos/protocolo_de_qualidade.md)
- [Guia de Auto-Revisao antes de PR e Merge](guia_de_auto_revisao.md)
- [Guia de Debug do Projeto](guia_de_debug.md)
- [Automacao Operacional com Taskipy](automacao_operacional_com_taskipy.md)
- [Refactoring (Martin Fowler)](https://refactoring.com/)
- [Source Making - Refactoring](https://sourcemaking.com/refactoring)
