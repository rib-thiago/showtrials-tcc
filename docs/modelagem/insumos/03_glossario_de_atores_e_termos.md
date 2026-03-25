# Glossário de Atores e Termos

## 1. Objetivo do documento

Este documento consolida definições iniciais de atores, papéis, sistemas externos e termos centrais da frente de modelagem, com o objetivo de reduzir ambiguidades antes da abertura formal da frente de casos de uso.

Seu papel é estabilizar vocabulário, não encerrar definitivamente todas as definições. Alguns termos permanecem provisórios e deverão ser refinados em rodadas posteriores, especialmente quando a frente arquitetural estiver mais madura.

## 2. Observações de nomenclatura

Para fins desta frente:

- `ShowTrials` permanece como nome histórico do sistema atual
- `engine futura` permanece como designação provisória da arquitetura-alvo
- não há decisão final de branding nesta etapa

## 3. Atores humanos

### 3.1 Ator geral

- `usuario`: ator geral do sistema

### 3.2 Especializações provisórias do ator geral

- `usuario operador`: especialização mais aderente ao ShowTrials atual
- `usuario configurador`: especialização mais aderente à engine futura

### 3.3 Leitura conceitual adotada

A relação entre `usuario operador` e `usuario configurador` deve ser lida, por ora, como um caso de generalização/especialização:

- `usuario` é a categoria geral
- `usuario operador` representa o uso mais aderente ao sistema atual
- `usuario configurador` representa o uso mais aderente à futura arquitetura configurável

Essa distinção não implica ruptura total entre os dois perfis. Ao contrário, ela reconhece a evolução do uso do mesmo sistema em diferentes estágios de maturidade.

## 4. Papéis técnicos e organizacionais

### 4.1 Desenvolvedor

- `desenvolvedor`: stakeholder do projeto e termo relevante de glossário

Nesta etapa, `desenvolvedor` não é tratado como ator principal da modelagem de uso.

### 4.2 Mantenedor

- `mantenedor`: papel em amadurecimento, potencialmente associado ao `usuario configurador`

Nesta etapa, `mantenedor` ainda não é tratado como ator principal formal.

### 4.3 Administrador

A figura de um futuro `usuario administrador` foi identificada como possibilidade relevante para cenários colaborativos, mas ainda não foi incorporada ao conjunto principal de atores. Esse ponto permanece como dívida para revisão crítica futura.

## 5. Sistemas externos e dependências externas

### 5.1 Categoria adotada

- `sistemas externos`: categoria provisória para serviços, fontes e recursos externos ao sistema principal

### 5.2 Exemplos iniciais

- API de traducao
- sites-fontes e outras fontes documentais externas
- servicos externos de OCR, quando aplicavel

### 5.3 Observacao metodologica

O enquadramento exato desses elementos pode variar conforme o artefato:

- em alguns casos, aparecem como sistemas externos
- em outros, como dependencias tecnicas
- essa variacao sera detalhada em documento proprio sobre fronteira do sistema

## 6. Termos do sistema atual

### 6.1 ShowTrials

- `ShowTrials`: nome historico do sistema atual implementado

### 6.2 Acervo

- `acervo`: conjunto de fontes e materiais brutos utilizados no trabalho documental

O acervo pode ou nao ser persistido em banco de dados, a depender da conveniencia do usuario e do recorte de trabalho adotado.

### 6.3 Documento

- `documento`: abstracao central do sistema atual, historicamente utilizada para representar o conteudo de cada texto coletado

Este termo ainda se encontra em estabilizacao conceitual e devera ser refinado com apoio adicional dos documentos de fase e da futura frente arquitetural.

## 7. Termos da evolução para engine

### 7.1 Engine futura

- `engine futura`: arquitetura-alvo configuravel de processamento documental

### 7.2 Fluxo

- `fluxo`: forma conceitual de pensar o trabalho ou percurso desejado sobre os documentos e dados

### 7.3 Pipeline

- `pipeline`: concretizacao tecnica e configurada de um fluxo de trabalho

O pipeline representa a configuracao do sistema para executar um fluxo previamente concebido.

### 7.4 Step

- `step`: etapa individual de um pipeline

O termo `step` permanece preferencialmente em ingles, por consistencia com outros termos tecnicos ja utilizados no projeto.

### 7.5 Colecao

- `colecao`: produto derivado do acervo e estrutura persistivel de trabalho analitico

As colecoes podem servir de base para:

- redes de relacionamento
- graficos
- analises estatisticas
- organizacao de traducoes e outros produtos derivados

## 8. Termos ambíguos ou provisórios

### 8.1 Documento

O termo `documento` permanece ambiguo e em estabilizacao conceitual. Embora historicamente tenha sido usado como abstracao central do sistema atual, ainda precisa ser revisto com mais cuidado para acomodar:

- a leitura retrospectiva das fases do projeto
- a evolucao da arquitetura
- a relacao entre conteudo bruto, produtos derivados e colecoes

### 8.2 Processamento

- `processamento`: termo amplo para acoes realizadas sobre documentos ou dados

### 8.3 Analise

- `analise`: trabalho sobre os dados ja introduzidos no sistema, incluindo leitura, exploracao, visualizacao, interpretacao e geracao de novos insumos

### 8.4 Transformacao

- `transformacao`: termo atualmente proximo de `processamento`, ainda sem separacao conceitual rigorosa

### 8.5 Traducao

A `traducao` foi identificada como termo conceitualmente hibrido:

- pode funcionar como transformacao
- pode funcionar como recurso dentro de uma analise
- pode funcionar como produto derivado persistido

Seu reposicionamento conceitual fica em aberto para rodadas futuras.

## 9. Decisões de nomenclatura já tomadas

As decisoes provisoriamente consolidadas nesta rodada foram:

- usar `usuario` como ator geral
- usar `usuario operador` para o sistema atual
- usar `usuario configurador` para a engine futura
- manter `desenvolvedor` como stakeholder, e nao como ator principal
- manter `mantenedor` como papel em amadurecimento
- tratar APIs, fontes e servicos externos como `sistemas externos`
- manter `ShowTrials` e `engine futura` como termos de referencia
- distinguir `fluxo` de `pipeline`
- manter `step` como termo tecnico preferencial
- distinguir `acervo` de `colecao`
- explicitar que `documento` ainda e termo em estabilizacao

## 10. Questões em aberto

Ainda precisam ser refinados em rodadas futuras:

- definicao mais precisa de `documento`
- reposicionamento conceitual da `traducao`
- amadurecimento da figura de um futuro `usuario administrador`
- melhor separacao entre processamento automatizado, analise interativa e edicao do usuario
- ampliacao do glossario conforme avancarem os insumos de arquitetura e casos de uso
