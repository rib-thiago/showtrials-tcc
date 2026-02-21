## 📋 **DOCUMENTO 2: QUESTIONÁRIO DE LEVANTAMENTO DE REQUISITOS**

Para eu entender melhor sua visão e objetivos, por favor responda às perguntas abaixo:

---

## 🎯 **PARTE 1: VISÃO GERAL**

### **1.1 Propósito do Projeto**

1. Qual é o **objetivo principal** do seu TCC? (responda com suas palavras)

2. Este projeto é:
   - [ ] Acadêmico (apenas para o TCC)
   - [ ] Acadêmico com potencial de uso real
   - [ ] Ferramenta que você pretende usar depois
   - [ ] Plataforma para disponibilizar para outros pesquisadores

3. Quem é o **usuário-alvo** ideal?
   - [ ] Eu mesmo (uso pessoal)
   - [ ] Meu orientador
   - [ ] Historiadores/pesquisadores em geral
   - [ ] Jornalistas
   - [ ] Público em geral
   - [ ] Outro: ___________

### **1.2 Escopo e Abrangência**

4. A aplicação deve ser **específica para os processos de Moscou/Leningrado** ou **genérica para qualquer coleção documental**?

5. Você imagina outros pesquisadores usando sua ferramenta para **outros conjuntos de documentos**? Se sim, quais?

6. O nome "ShowTrials" deve permanecer ou você prefere um nome mais genérico (ex: "DocPipeline", "Historiograph")?

---

## 🔧 **PARTE 2: FUNCIONALIDADES**

### **2.1 Fontes de Dados**

7. Quais **fontes** você quer suportar? (múltipla escolha)
   - [ ] Sites web (como showtrials.ru) - já temos
   - [ ] PDFs locais
   - [ ] Imagens (com OCR)
   - [ ] Arquivos de texto (.txt, .docx)
   - [ ] APIs (ex: Arquivo Nacional)
   - [ ] Pastas locais com arquivos
   - [ ] Outro: ___________

8. Para sites web, como lidar com:
   - [ ] Sites com paginação (já temos)
   - [ ] Sites com login/autenticação
   - [ ] Sites com JavaScript pesado
   - [ ] Sites com rate limiting

### **2.2 Processamento**

9. Além dos **tipos de documento** atuais (interrogatório, carta, etc.), que outras **classificações** podem ser necessárias?

10. Quais **entidades** além de pessoas são importantes?
    - [ ] Locais (cidades, países)
    - [ ] Organizações (NKVD, Partido, etc.)
    - [ ] Datas
    - [ ] Eventos
    - [ ] Leis/decretos
    - [ ] Outro: ___________

11. A **tradução** deve ser:
    - [ ] Apenas para inglês/português (como hoje)
    - [ ] Para qualquer idioma (configurável)
    - [ ] Híbrido (detecta idioma e traduz)

12. Que **análises** além das atuais seriam úteis?
    - [ ] Nuvem de palavras (já temos)
    - [ ] Rede de relacionamentos (grafos)
    - [ ] Linha do tempo interativa
    - [ ] Estatísticas avançadas
    - [ ] Detecção de emoções
    - [ ] Similaridade entre documentos
    - [ ] Outro: ___________

### **2.3 Pipeline Customizável**

13. O quanto o pipeline deve ser **customizável**?
    - [ ] Fixo (como hoje)
    - [ ] Poucas opções (escolher ordem de etapas)
    - [ ] Totalmente configurável (usuário define etapas)
    - [ ] Extensível com plugins

14. Você prefere configurar o pipeline via:
    - [ ] Arquivo de configuração (YAML/JSON)
    - [ ] Interface gráfica (web)
    - [ ] CLI com perguntas interativas
    - [ ] Todas as opções

### **2.4 Exportação e Resultados**

15. Quais **formatos de exportação** são importantes?
    - [ ] TXT (já temos)
    - [ ] CSV (planilhas)
    - [ ] JSON (dados estruturados)
    - [ ] PDF (formatado)
    - [ ] HTML (página web)
    - [ ] Banco de dados SQL
    - [ ] API (para outras ferramentas consumirem)

16. Que tipo de **relatórios/visualizações** você imagina?
    - [ ] Tabelas e gráficos estáticos (já temos)
    - [ ] Gráficos interativos
    - [ ] Dashboards web
    - [ ] Mapas (para localizações)
    - [ ] Linhas do tempo

---

## 👥 **PARTE 3: USUÁRIOS E EXPERIÊNCIA**

### **3.1 Perfil do Usuário**

17. O usuário típico tem **conhecimento técnico**?
    - [ ] Não (pesquisador de humanas, pouca técnica)
    - [ ] Médio (sabe usar computador, mas não programa)
    - [ ] Alto (programador/pesquisador técnico)

18. A aplicação deve ter **múltiplos usuários** ou é mono-usuário?

19. Precisa de **autenticação** (login/senha)?

### **3.2 Interfaces**

20. Qual interface você acha mais importante?
    - [ ] CLI (como hoje)
    - [ ] Web (como hoje)
    - [ ] API (para integrações)
    - [ ] Desktop (aplicativo instalável)
    - [ ] Todas

21. Para a CLI, que **comandos** seriam úteis além dos atuais?
    - [ ] `pipeline run` (executar pipeline configurado)
    - [ ] `pipeline create` (criar novo pipeline)
    - [ ] `pipeline list` (listar pipelines)
    - [ ] `source add` (adicionar nova fonte)
    - [ ] Outro: ___________

22. Para a Web, que **telas** seriam importantes?
    - [ ] Dashboard de visão geral
    - [ ] Configuração visual do pipeline
    - [ ] Visualização de documentos
    - [ ] Gráficos interativos
    - [ ] Área administrativa

---

## 🏗️ **PARTE 4: ARQUITETURA E TECNOLOGIAS**

### **4.1 Escalabilidade e Performance**

23. Qual o **volume esperado** de documentos?
    - [ ] Centenas (como hoje)
    - [ ] Milhares
    - [ ] Dezenas de milhares
    - [ ] Centenas de milhares

24. Precisa de **processamento em lote** (batch) ou em **tempo real**?

25. A aplicação deve ser **multi-threaded/paralela** para processar muitos documentos?

### **4.2 Implantação**

26. Como você imagina a **distribuição** da aplicação?
    - [ ] Local (usuário instala no computador)
    - [ ] Servidor web (acesso remoto)
    - [ ] Docker container
    - [ ] Pacote pip (biblioteca Python)
    - [ ] Tudo isso

27. Precisa de **instalador** para Windows/Mac?

### **4.3 Dados**

28. O **banco de dados** deve ser:
    - [ ] SQLite (como hoje) - simples
    - [ ] PostgreSQL - mais robusto
    - [ ] MySQL
    - [ ] MongoDB (NoSQL)
    - [ ] Vários (configurável)

29. Precisa de **migrações automáticas** quando o schema muda?

---

## 🎓 **PARTE 5: TCC E ENTREGA**

### **5.1 Objetivos Acadêmicos**

30. Qual o **diferencial** do seu TCC em relação a outros?
    - [ ] Arquitetura limpa bem aplicada
    - [ ] Pipeline customizável
    - [ ] Integração com NLP
    - [ ] Interface amigável para humanas
    - [ ] Outro: ___________

31. Você pretende **comparar** com outras ferramentas existentes?
    - [ ] NVivo
    - [ ] MAXQDA
    - [ ] ATLAS.ti
    - [ ] Zotero
    - [ ] Scripts manuais em Python
    - [ ] Outro: ___________

### **5.2 Prazos e Expectativas**

32. Qual o **prazo** para entrega do TCC? (ex: Dezembro/2026)

33. Quantas **horas por semana** você pretende dedicar ao projeto?

34. Você prefere:
    - [ ] Entregar algo sólido e bem feito, mesmo que menor
    - [ ] Entregar o máximo de funcionalidades possível

---

## 💡 **PARTE 6: IDEIAS ABERTAS**

35. Que **funcionalidade dos sonhos** você gostaria de ter, mesmo que pareça difícil?

36. Tem algum **projeto similar** que você admira e gostaria de se inspirar?

37. Algo mais que você gostaria de compartilhar sobre sua visão?

---

## 📋 **COMO RESPONDER**

Você pode:
1. Copiar as perguntas e responder diretamente aqui
2. Responder em um arquivo `.md` e enviar
3. Responder em tópicos, de forma livre

**O importante é eu entender SUA visão para poder ajudar a refinar os requisitos.** 🎯

---
