# Fronteira do Sistema e Recortes de Modelagem

## 1. Objetivo do documento

Este documento consolida a delimitacao funcional do sistema para a frente de casos de uso, com foco em reduzir ambiguidades sobre o que deve ser tratado como parte do sistema e o que deve ser tratado como elemento externo.

Seu foco principal, nesta etapa, nao e definir fronteiras arquiteturais detalhadas para todos os artefatos futuros, mas estabelecer uma **fronteira funcional-base** que sustente os proximos insumos e o futuro diagrama de casos de uso.

## 2. Escopo deste insumo

Este insumo trata principalmente:

- da fronteira funcional do sistema para fins de casos de uso
- da posicao conceitual de elementos centrais como interfaces, persistencia, fontes externas e servicos externos
- da diferenca entre capacidades do sistema e mecanismos concretos de implementacao

Este documento nao pretende, nesta etapa:

- encerrar a modelagem arquitetural detalhada
- substituir futuras decisoes de C4, UML ou 4+1
- resolver todos os detalhes de infraestrutura e implementacao

## 3. Fronteira funcional-base do sistema

Para esta frente, a fronteira funcional-base do sistema e definida assim:

O sistema e a aplicacao que permite ao usuario:

- obter ou receber conteudo documental
- processar documentos
- traduzir
- aplicar OCR
- aplicar NLP
- realizar estatisticas e outras analises
- persistir e consultar dados
- configurar e executar fluxos e pipelines
- apresentar resultados por CLI e Web

Essa definicao descreve o que o sistema oferece como capacidade funcional ao usuario, e nao todos os mecanismos concretos usados para implementar essas capacidades.

## 4. O que fica dentro do sistema

Nesta leitura funcional-base, ficam dentro do sistema:

- CLI
- Web
- processamento documental
- traducao como capacidade
- OCR como capacidade
- NLP como capacidade
- estatisticas e analises como capacidades
- persistencia
- consulta
- configuracao de pipeline
- execucao de pipeline
- artefatos e resultados produzidos pelo sistema

## 5. O que fica fora do sistema

Nesta leitura funcional-base, ficam fora do sistema:

- usuarios
- fontes documentais externas
- APIs externas
- servicos externos
- infraestrutura externa de deploy
- recursos de terceiros consumidos pela aplicacao

## 6. Papel de CLI e Web

CLI e Web pertencem ao sistema como formas de interacao e acesso.

Nesta etapa, a leitura adotada e:

- CLI e Web sao partes relevantes do sistema
- CLI e Web nao devem ser tratadas como atores
- no contexto de casos de uso, elas funcionam como meios pelos quais o usuario interage com o sistema

## 7. Papel da persistência e do banco de dados

### 7.1 Persistencia

- `persistencia`: capacidade estrutural do sistema

A persistencia faz parte do que o sistema entrega, porque o sistema deve ser capaz de armazenar documentos, traducoes, analises e outros produtos derivados.

### 7.2 Banco de dados concreto

- `banco de dados concreto`: mecanismo ou infraestrutura de persistencia

Exemplos como SQLite, Postgres ou outros mecanismos concretos nao sao tratados aqui como capacidades de uso, mas como meios pelos quais o sistema implementa a persistencia.

## 8. Papel de fontes externas e sistemas externos

### 8.1 Fontes externas

- sites-fontes e outras origens documentais devem ser tratados, nesta etapa, como `fontes externas`

Elas estao fora da fronteira do sistema, embora possam ser essenciais para o seu funcionamento pratico.

### 8.2 Sistemas externos

- APIs de traducao, OCR ou servicos equivalentes devem ser tratados, nesta etapa, como `sistemas externos` consumidos pelo sistema

Essa classificacao e preferivel, neste momento, a trata-los como atores.

## 9. Capacidades do sistema e mecanismos de implementação

Uma distincao importante adotada neste insumo e:

- as capacidades pertencem ao sistema
- os mecanismos concretos de implementacao podem ser internos, bibliotecas ou sistemas externos

Exemplos:

- traduzir documentos e capacidade do sistema
- aplicar OCR e capacidade do sistema
- aplicar NLP e capacidade do sistema
- calcular estatisticas e capacidade do sistema

Mas isso nao significa que toda implementacao concreta dessas capacidades esteja dentro da fronteira funcional-base. O sistema pode depender de bibliotecas e servicos externos para entregar essas capacidades.

## 10. Fronteira funcional para casos de uso

No contexto especifico de casos de uso, a leitura adotada e:

- os casos de uso do sistema ficam dentro da fronteira do sistema
- os usuarios ficam fora da fronteira
- fontes externas e sistemas externos permanecem fora da fronteira, quando forem relevantes para o entendimento da interacao
- CLI e Web nao entram como atores; entram apenas como formas de acesso ao sistema

Assim, casos de uso como os abaixo pertencem ao interior da fronteira:

- coletar conteudo documental
- consultar acervo
- traduzir documento
- analisar documento
- configurar pipeline
- executar pipeline

## 11. Síntese operacional

Para fins da frente de casos de uso, a posicao consolidada neste insumo e:

- existe uma fronteira funcional-base do sistema
- essa fronteira e definida pelas capacidades oferecidas ao usuario
- persistencia fica dentro do sistema como capacidade estrutural
- banco de dados concreto e mecanismo de persistencia
- CLI e Web pertencem ao sistema como interfaces, nao como atores
- usuarios, fontes externas e sistemas externos ficam fora da fronteira funcional

## 12. Questões em aberto

Ainda precisam ser refinados em rodadas futuras:

- como certos elementos externos serao representados em artefatos arquiteturais mais detalhados
- como distinguir, em futuros diagramas, o nivel conceitual do nivel de implementacao
- como representar dependencias externas especificas quando a frente arquitetural estiver mais madura
