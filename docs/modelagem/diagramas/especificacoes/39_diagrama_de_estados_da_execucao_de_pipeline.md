# Diagrama de Estados

## 1. Objetivo do documento

Este documento registra a avaliação e o recorte do **diagrama de estados** da frente.

Nesta etapa, o artefato deve ser lido como **especificação textual preparatória** do diagrama, e não como o diagrama materializado em si.

## 2. Decisão metodológica

Nesta frente, concluiu-se que **faz sentido** manter um diagrama de estados, mas com recorte focalizado:

- **estado de execução de pipeline**

Não faz sentido, por enquanto, tentar produzir um único diagrama de estados para o sistema inteiro.

## 3. Base de evidência utilizada

- [24_visao_de_processo_4mais1.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/visao_4mais1/24_visao_de_processo_4mais1.md)
- [31_c4_modelo_de_codigo.md](/home/thiago/coleta_showtrials/docs/modelagem/arquitetura/c4/31_c4_modelo_de_codigo.md)

## 4. Estados principais a representar

- configurado
- validado
- em execução
- concluído
- concluído com persistência
- falha parcial
- falha total
- aguardando revisão/intervenção

## 5. Transições principais a representar

- configurar → validar
- validar → executar
- executar → concluir
- executar → falha parcial
- executar → falha total
- concluir → persistir
- concluir ou persistir → aguardar revisão

## 6. Justificativa para fazer sentido

O diagrama de estados se justifica porque:

- a engine futura depende fortemente de estado explícito de execução
- a persistência configurável altera o ciclo de vida do resultado
- revisão humana introduz transições semanticamente relevantes

## 7. Inferências adotadas

- o diagrama de estados foi focalizado em execução, e não em `Documento` ou `Traducao`, por ser onde a frente já consolidou maior densidade semântica

## 8. Dívidas técnicas registradas

- decidir se resultados derivados também merecerão diagrama de estados próprio
- decidir quando background e reprocessamento passarão a exigir estados adicionais

## 9. Próximos passos

- abrir o bloco de padrões de projeto
