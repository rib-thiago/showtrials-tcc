# Manual de Gestao do Projeto

## Objetivo

Este manual apresenta uma visao operacional resumida de como o projeto organiza:

- issues;
- milestones;
- status no GitHub Project;
- branches e pull requests;
- rastreabilidade entre trabalho, codigo e documentacao.

Ele nao substitui os documentos normativos e guias especializados. Seu papel e funcionar como mapa de consulta rapida para a gestao cotidiana do projeto.

## Escopo e Relacao com Outros Documentos

Este manual consolida a visao geral da gestao operacional, mas os detalhes de cada dominio ficam nos artefatos especificos:

- [politica_de_governanca.md](../politicas/politica_de_governanca.md): regras de issues, labels, milestones e status.
- [protocolo_de_git.md](../protocolos/protocolo_de_git.md): fluxo de branch, commit, pull request e merge.
- [guia_github_projects_cli.md](../guias/guia_github_projects_cli.md): operacao do GitHub Project via `gh`.
- [guia_de_auto_revisao.md](../guias/guia_de_auto_revisao.md): verificacao antes de PR e merge.
- [protocolo_de_qualidade.md](../protocolos/protocolo_de_qualidade.md): criterios tecnicos minimos.
- [guia_de_correcao_urgente.md](../guias/guia_de_correcao_urgente.md): tratamento de correcoes urgentes.
- [versionamento_e_releases.md](../projeto/versionamento_e_releases.md): versoes, tags e releases.
- [regime_documental_de_fases_e_rodadas.md](../projeto/regime_documental_de_fases_e_rodadas.md): relacao entre historicos de fase e rodadas operacionais.

## Elementos Centrais da Gestao

### Issues

Issues sao a unidade rastreavel de trabalho do projeto. Cada issue deve ter enquadramento minimo coerente com a governanca vigente:

- um tipo principal;
- prioridade;
- milestone estrutural, quando fizer sentido;
- criterio de aceite;
- relacao clara com o trabalho que sera executado.

Issue nao e fase historica. Historicos de fase pertencem ao regime documental proprio e nao substituem o backlog operacional.

### Milestones

Milestones representam entregaveis estruturais ou marcos relevantes do projeto. Elas nao devem ser tratadas como simples periodos de calendario.

O uso correto de milestone ajuda a responder:

- que bloco do projeto esta sendo atacado;
- quais issues pertencem a esse entregavel;
- o que ainda esta pendente dentro desse recorte.

### GitHub Project

O GitHub Project organiza o estado operacional das issues e PRs no fluxo:

`Backlog -> Ready -> In Progress -> In Review -> Done`

O Project nao substitui a issue e nao substitui o PR. Ele mostra o estado visivel do trabalho.

### Branches e Pull Requests

O trabalho tecnico se conecta a gestao por meio da relacao:

`issue -> branch -> pull request -> merge`

Cada branch deve refletir um trabalho real e rastreavel. A nomenclatura e o fluxo operacional devem seguir o protocolo de Git vigente, nao padroes antigos do projeto.

### Rodadas e Fases

Rodadas registram execucao curta, analise, decisao e fechamento. Documentos de fase registram historicos consolidados de intervencoes relevantes.

Nem toda rodada gera fase, e fase nao deve ser tratada como unidade operacional corrente do backlog.

## Fluxo Operacional Resumido

O fluxo minimo de gestao cotidiana do projeto pode ser lido assim:

1. identificar ou abrir a issue correta;
2. enquadrar a issue com labels, prioridade, milestone e criterio de aceite;
3. garantir que o item esteja no status correto no Project;
4. criar ou continuar a branch correspondente segundo o protocolo de Git;
5. desenvolver, validar e revisar a mudanca;
6. abrir ou atualizar o pull request quando aplicavel;
7. mover o item no Project conforme o estado real;
8. registrar rodadas e historicos quando a natureza do trabalho pedir isso.

## Consultas Operacionais Frequentes

### Issues

```bash
gh issue list
gh issue list --state all
gh issue view <numero>
gh issue edit <numero> --add-label "priority:P1"
gh issue edit <numero> --milestone "MVP - Engine de Pipeline"
```

### Project

```bash
gh project list --owner rib-thiago
gh project item-list 1 --owner rib-thiago
gh project field-list 1 --owner rib-thiago
```

Para atualizar status de item, consultar o guia especifico:
- [guia_github_projects_cli.md](../guias/guia_github_projects_cli.md)

### Branches e Pull Requests

```bash
git branch
git branch -a
gh pr list
gh pr view <numero>
```

Para abertura, atualizacao e merge de PR:
- [protocolo_de_git.md](../protocolos/protocolo_de_git.md)

### Revisao e qualidade

Antes de integrar trabalho:

- consultar [guia_de_auto_revisao.md](../guias/guia_de_auto_revisao.md)
- confirmar aderencia a [protocolo_de_qualidade.md](../protocolos/protocolo_de_qualidade.md)

### Correcao urgente e releases

Quando o trabalho envolver contingencia ou versao:

- consultar [guia_de_correcao_urgente.md](../guias/guia_de_correcao_urgente.md)
- consultar [versionamento_e_releases.md](../projeto/versionamento_e_releases.md)

## Nota Historica da Reescrita

Este manual substitui uma versao anterior que refletia um regime operacional mais antigo do projeto. Na reescrita atual:

- issue deixou de ser tratada como fase;
- milestones temporais foram removidas em favor de milestones estruturais;
- a taxonomia antiga de labels e branches foi substituida pela terminologia vigente;
- `FASE*.md` deixou de aparecer como unidade operacional corrente e passou a ser tratada segundo o regime documental atual;
- blocos antigos sobre Git Flow, review, emergency, releases e flows futuros foram removidos do corpo do manual e redistribuidos para os documentos especializados ja saneados.

## Documentos Relacionados

- [politica_de_governanca.md](../politicas/politica_de_governanca.md)
- [protocolo_de_git.md](../protocolos/protocolo_de_git.md)
- [guia_github_projects_cli.md](../guias/guia_github_projects_cli.md)
- [guia_de_auto_revisao.md](../guias/guia_de_auto_revisao.md)
- [protocolo_de_qualidade.md](../protocolos/protocolo_de_qualidade.md)
- [guia_de_correcao_urgente.md](../guias/guia_de_correcao_urgente.md)
- [versionamento_e_releases.md](../projeto/versionamento_e_releases.md)
- [regime_documental_de_fases_e_rodadas.md](../projeto/regime_documental_de_fases_e_rodadas.md)
