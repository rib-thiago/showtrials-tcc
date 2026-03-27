# Diagrama de Sequência — Fluxos Atuais

## 1. Objetivo do documento

Este documento registra o recorte do **diagrama de sequência dos fluxos atuais**.

Seu objetivo é explicitar as mensagens principais dos casos de uso centrais do sistema atual.

Nesta etapa, o artefato deve ser lido como **especificação textual preparatória** do diagrama, e não como o diagrama materializado em si.

## 2. Base de evidência utilizada

- [13_especificacoes_textuais_de_casos_de_uso_prioritarios.md](/home/thiago/coleta_showtrials/docs/modelagem/analise/principais/13_especificacoes_textuais_de_casos_de_uso_prioritarios.md)
- `src/interface/cli/app.py`
- `src/interface/web/app.py`
- `src/application/use_cases/`

## 3. Fluxos atuais prioritários para sequência

- `ObterDocumento`
- `TraduzirDocumento`
- `AnalisarDocumento`

## 4. Participantes principais

- Usuário
- Interface CLI ou Web
- Caso de uso
- Repositório de documentos
- Repositório de traduções
- Serviço analítico ou de tradução

## 5. Leitura recomendada do diagrama

O diagrama deve mostrar:

- chamada da interface ao caso de uso
- recuperação no repositório
- consumo de serviço externo quando houver
- persistência ou retorno do resultado

## 6. Inferências adotadas

- os fluxos atuais foram tratados como predominantemente síncronos

## 7. Dívidas técnicas registradas

- granularidade futura entre sequência CLI e sequência Web

## 8. Próximos passos

- abrir o diagrama de sequência dos fluxos da engine
