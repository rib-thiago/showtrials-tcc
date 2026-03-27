# Protocolo de Qualidade do Projeto

## Objetivo

Este protocolo define criterios minimos de qualidade para mudancas no projeto.

Seu objetivo e:

- tratar qualidade como criterio de aceite
- reforcar clareza estrutural e coerencia arquitetural
- reduzir mudancas implícitas ou mal delimitadas
- orientar verificacoes minimas antes de revisao e merge

## Escopo

Este protocolo se aplica a:

- mudancas de codigo
- revisao tecnica
- tipagem
- testabilidade
- coerencia arquitetural
- verificacoes minimas antes de merge

## Principios de Qualidade

O projeto adota os principios abaixo:

- correcao funcional antes de otimizacao
- clareza estrutural antes de abstracao
- arquitetura explicita antes de conveniencia
- mudancas pequenas e verificaveis
- nenhuma mudanca estrutural implicita
- qualidade como criterio de aceite, nao como melhoria opcional

## Criterios Minimos de Qualidade

Antes de considerar uma mudanca pronta para merge, verificar no minimo:

- criterios de aceite atendidos
- codigo executa sem erro no escopo da mudanca
- tipagem coerente com o contexto do modulo
- ausencia de codigo morto, prints ou logs temporarios
- ausencia de `TODO` sem justificativa
- ausencia de efeitos colaterais nao documentados
- responsabilidade no modulo correto

Parte dessas verificacoes pode ser apoiada pela automacao operacional atualmente disponivel, sem substituir a revisao tecnica necessaria antes de pull request e merge.

## Tipagem e Clareza Estrutural

Os criterios minimos incluem:

- evitar `Any` sem justificativa
- manter contratos explicitos quando forem relevantes
- evitar interfaces ambiguas
- manter responsabilidades claras por modulo

## Coerencia Arquitetural

Antes de merge, a mudanca deve ser avaliada quanto a:

- acoplamento indevido com persistencia
- mistura entre logica e IO
- manutencao da separacao entre execucao e configuracao
- responsabilidade no modulo correto
- carater explicito de qualquer mudanca estrutural

Mudanca estrutural implicita deve ser tratada como problema de qualidade.

## Testabilidade

Como criterio minimo de qualidade:

- a logica deve ser estruturada de forma testavel
- dependencias externas devem ser isolaveis ou injetaveis quando apropriado
- transformacoes puras devem permanecer separadas de efeitos colaterais
- codigo novo nao deve dificultar arbitrariamente a verificacao da mudanca

## Pendencias e Validacoes Necessarias

- comandos detalhados de verificacao por arquivo mencionados no documento legado nao estao confirmados no estado atual de `taskipy`
- metas especificas como cobertura por arquivo ou `cov-file >= 85%` nao devem ser tratadas como fluxo vigente sem validacao adicional
- a relacao entre checklist manual e automacao real de qualidade deve continuar sendo refinada ao longo da frente

## Documentos Relacionados

- [Politica de Governanca do Projeto](../politicas/politica_de_governanca.md)
- [Protocolo de Git do Projeto](protocolo_de_git.md)
- [Automacao Operacional com Taskipy](../guias/automacao_operacional_com_taskipy.md)
