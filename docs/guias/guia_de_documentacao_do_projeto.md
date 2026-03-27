# Guia de Documentacao do Projeto

## Objetivo

Este guia organiza a manutencao documental do projeto em nivel geral.

Seu objetivo e:

- manter coerencia entre codigo, documentacao e navegacao publica
- orientar a manutencao dos principais tipos documentais vivos
- reduzir desatualizacao entre implementacao, README, changelog e documentacao tecnica

## Contexto de Uso

Este guia deve ser consultado quando houver:

- mudanca de comportamento ou interface que exija atualizacao documental
- manutencao de README, changelog ou docstrings
- necessidade de revisar coerencia entre documentacao e estado real do projeto

Para regras especificas sobre historicos de fase, rodadas operacionais e manutencao do site documental, consultar os documentos dedicados relacionados ao final deste guia.

## Tipos de Documentacao do Projeto

Hoje o projeto convive com pelo menos quatro grupos principais de documentacao:

- documentacao viva de projeto, como README, changelog e guias em `docs/guias/`
- documentacao historica de intervencoes em `docs/historico/fases/`
- registros operacionais curtos em `docs/planejamento/rodadas/`
- documentacao publica navegavel via MkDocs

Cada grupo tem papel proprio. Este guia trata apenas da manutencao documental geral e da coerencia entre esses grupos.

## Docstrings

O projeto deve preferir docstrings claras e proporcionais ao valor da funcao ou metodo documentado.

Boas praticas minimas:

- explicar o que a unidade faz, sem transformar a docstring em tutorial
- documentar parametros e retornos quando isso reduz ambiguidade
- registrar excecoes relevantes quando fizer sentido
- atualizar a docstring sempre que o comportamento publico mudar

Quando houver padrao mais detalhado de estilo, ele deve ser aplicado com sobriedade, sem inflar funcoes simples.

## README e Documentos Publicos de Entrada

README e paginas publicas de entrada devem permanecer:

- factualmente aderentes ao projeto
- curtos o suficiente para orientar leitura
- livres de badges, links ou exemplos desatualizados

Sempre que houver mudanca relevante de uso, instalacao, navegacao ou posicionamento do projeto, vale revisar:

- instrucoes de instalacao
- exemplos de uso
- links internos
- referencia para a documentacao principal

## Changelog

O changelog deve registrar mudancas notaveis sem tentar narrar toda a historia do projeto.

Boas praticas minimas:

- atualizar em releases ou marcos realmente relevantes
- manter categorias claras de mudanca
- evitar inventario inflado de detalhes menores
- nao apresentar como release consolidada algo que ainda nao foi validado como tal

## Cuidados Gerais de Manutencao

Ao atualizar documentacao do projeto, verificar no minimo:

- se os links continuam validos
- se o texto descreve o estado real do codigo e da configuracao
- se o documento ainda tem estatuto semantico claro
- se o detalhe pertence realmente a esse documento, e nao a outro guia
- se a mudanca exige atualizacao de README, changelog, guias tecnicos ou historicos

Problemas comuns:

- docstring desatualizada em relacao ao comportamento atual
- README prometendo mais do que o projeto realmente entrega
- documento vivo carregando contexto historico demais
- historico de fase lido como se fosse norma vigente

## Quando Consultar Outros Guias

- consultar [Regime Documental de Fases e Rodadas](/home/thiago/coleta_showtrials/docs/projeto/regime_documental_de_fases_e_rodadas.md) para regras de historico, rodadas e rastreabilidade de intervencoes
- consultar [Guia de Manutencao do Site Documental](guia_de_manutencao_do_site_documental.md) para build, navegacao e publicacao via MkDocs
- consultar [Politica de Governanca do Projeto](../politicas/politica_de_governanca.md) e os protocolos correlatos quando a atualizacao documental afetar fluxo operacional ou criterios normativos

## Documentos Relacionados

- [Regime Documental de Fases e Rodadas](/home/thiago/coleta_showtrials/docs/projeto/regime_documental_de_fases_e_rodadas.md)
- [Guia de Manutencao do Site Documental](guia_de_manutencao_do_site_documental.md)
- [Guia de Contribuicao](/home/thiago/coleta_showtrials/docs/contributing.md)
- [Changelog](/home/thiago/coleta_showtrials/docs/changelog.md)
