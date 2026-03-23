# src/tests/test_gerar_relatorio.py
"""
Testes para o caso de uso GerarRelatorio (sem telemetria).
"""

from pathlib import Path
from unittest.mock import Mock

import pytest

from src.application.use_cases.gerar_relatorio import GerarRelatorio


class TestGerarRelatorio:
    """Testes para a lógica de geração de relatórios."""

    @pytest.fixture
    def repo_doc_mock(self):
        """Fixture para mock do repositório de documentos."""
        repo = Mock()

        # Criar documentos de exemplo
        docs = []
        for i in range(10):
            doc = Mock()
            doc.id = i + 1
            doc.centro = "lencenter" if i < 5 else "moscenter"
            doc.tipo = "interrogatorio"
            doc.pessoa_principal = "Л.В. Николаева" if i < 3 else "И.В. Сталин"
            doc.tem_anexos = i % 2 == 0
            doc.data_original = f"1934-{i+1:02d}-04"
            docs.append(doc)

        repo.listar.return_value = docs
        return repo

    @pytest.fixture
    def repo_trad_mock(self):
        """Fixture para mock do repositório de traduções."""
        repo = Mock()

        # Simular traduções para alguns documentos
        def listar_por_documento(doc_id):
            if doc_id <= 3:
                return [Mock(idioma="en"), Mock(idioma="pt")]
            return []

        repo.listar_por_documento.side_effect = listar_por_documento
        return repo

    def test_coletar_dados_basico(self, repo_doc_mock):
        """Deve coletar dados básicos corretamente."""
        use_case = GerarRelatorio(repo_doc_mock)

        dados = use_case._coletar_dados()

        assert dados["total_documentos"] == 10
        assert "lencenter" in dados["documentos_por_centro"]
        assert "moscenter" in dados["documentos_por_centro"]
        assert dados["documentos_por_centro"]["lencenter"] == 5
        assert dados["documentos_por_centro"]["moscenter"] == 5

    def test_coletar_dados_com_traducoes(self, repo_doc_mock, repo_trad_mock):
        """Deve incluir dados de tradução quando disponível."""
        use_case = GerarRelatorio(repo_doc_mock, repo_trad_mock)

        dados = use_case._coletar_dados()

        assert dados["total_traducoes"] == 6  # 3 docs * 2 traduções
        assert "en" in dados["traducoes_por_idioma"]
        assert "pt" in dados["traducoes_por_idioma"]
        assert dados["traducoes_por_idioma"]["en"] == 3
        assert dados["traducoes_por_idioma"]["pt"] == 3

    def test_coletar_dados_com_contagens_especificas(self, repo_doc_mock):
        """Deve contar corretamente tipos específicos de documentos."""
        # Configurar documentos com tipos variados
        docs = []
        tipos = ["carta", "declaracao", "relatorio", "acareacao", "acusacao", "laudo"]

        for i, tipo in enumerate(tipos):
            doc = Mock()
            doc.tipo = tipo
            doc.centro = "lencenter"
            doc.pessoa_principal = "Pessoa Teste"
            doc.tem_anexos = False
            doc.data_original = "1934"
            docs.append(doc)

        repo_doc_mock.listar.return_value = docs
        use_case = GerarRelatorio(repo_doc_mock)

        dados = use_case._coletar_dados()

        assert dados["cartas"] == 1
        assert dados["declaracoes"] == 1
        assert dados["relatorios"] == 1
        assert dados["acareacoes"] == 1
        assert dados["acusacoes"] == 1
        assert dados["laudos"] == 1

    def test_coletar_dados_com_anexos(self, repo_doc_mock):
        """Deve contar documentos com anexos corretamente."""
        # Configurar documentos com anexos
        docs = []
        for i in range(5):
            doc = Mock()
            doc.tem_anexos = i % 2 == 0
            doc.centro = "lencenter"
            doc.tipo = "interrogatorio"
            doc.pessoa_principal = None
            doc.data_original = None
            docs.append(doc)

        repo_doc_mock.listar.return_value = docs
        use_case = GerarRelatorio(repo_doc_mock)

        dados = use_case._coletar_dados()

        assert dados["documentos_com_anexos"] == 3  # índices 0,2,4

    def test_coletar_dados_com_anos(self, repo_doc_mock):
        """Deve extrair anos das datas corretamente."""
        docs = []
        anos = ["1934", "1935", "1934", "1936", "1935"]

        for i, ano in enumerate(anos):
            doc = Mock()
            doc.data_original = f"{ano}-12-04"
            doc.centro = "lencenter"
            doc.tipo = "interrogatorio"
            doc.pessoa_principal = None
            doc.tem_anexos = False
            docs.append(doc)

        repo_doc_mock.listar.return_value = docs
        use_case = GerarRelatorio(repo_doc_mock)

        dados = use_case._coletar_dados()

        assert dados["anos"]["1934"] == 2
        assert dados["anos"]["1935"] == 2
        assert dados["anos"]["1936"] == 1

    def test_gerar_relatorio_txt_formato(self, repo_doc_mock):
        """Relatório TXT deve ter formato esperado."""
        use_case = GerarRelatorio(repo_doc_mock)

        relatorio = use_case.gerar_relatorio_txt()

        # Verificar seções principais
        assert "RELATÓRIO DO ACERVO" in relatorio
        assert "📊 VISÃO GERAL" in relatorio
        assert "🏛️  DOCUMENTOS POR CENTRO" in relatorio
        assert "📋 DOCUMENTOS POR TIPO" in relatorio
        assert "👤 PESSOAS MAIS FREQUENTES" in relatorio
        assert "📌 DOCUMENTOS ESPECIAIS" in relatorio

    def test_salvar_relatorio_txt(self, repo_doc_mock, tmp_path):
        """Deve salvar relatório em arquivo TXT."""
        use_case = GerarRelatorio(repo_doc_mock)

        caminho = use_case.salvar_relatorio(formato="txt", diretorio=str(tmp_path))

        assert caminho.endswith(".txt")
        assert Path(caminho).exists()
        assert Path(caminho).stat().st_size > 0

    def test_salvar_relatorio_html_placeholder(self, repo_doc_mock):
        """HTML deve retornar placeholder."""
        use_case = GerarRelatorio(repo_doc_mock)

        resultado = use_case.salvar_relatorio(formato="html")

        assert "html" in resultado.lower()
        assert "desenvolvimento" in resultado.lower()

    def test_salvar_relatorio_formato_invalido(self, repo_doc_mock):
        """Formato inválido deve retornar string vazia."""
        use_case = GerarRelatorio(repo_doc_mock)

        resultado = use_case.salvar_relatorio(formato="pdf")

        assert resultado == ""

    def test_pessoas_frequentes_com_traducao(self, repo_doc_mock):
        """Pessoas frequentes devem ter nomes traduzidos."""
        use_case = GerarRelatorio(repo_doc_mock)

        dados = use_case._coletar_dados()

        for nome_ru, count, nome_en in dados["pessoas_frequentes"]:
            assert nome_ru in ["Л.В. Николаева", "И.В. Сталин"]
            assert nome_en in ["Leonid V. Nikolaev", "Joseph V. Stalin"]

    def test_sem_repo_trad_nao_quebra(self, repo_doc_mock):
        """Sem repositório de tradução, deve funcionar."""
        use_case = GerarRelatorio(repo_doc_mock, repo_trad=None)

        dados = use_case._coletar_dados()

        assert dados["total_traducoes"] == 0
        assert dados["traducoes_por_idioma"] == {}

    def test_documentos_sem_tipo_sao_ignorados(self, repo_doc_mock):
        """Documentos sem tipo não devem quebrar contagens."""
        docs = []
        for i in range(3):
            doc = Mock()
            doc.tipo = None
            doc.centro = "lencenter"
            doc.pessoa_principal = None
            doc.tem_anexos = False
            doc.data_original = None
            docs.append(doc)

        repo_doc_mock.listar.return_value = docs
        use_case = GerarRelatorio(repo_doc_mock)

        # Não deve lançar exceção
        dados = use_case._coletar_dados()

        assert dados["documentos_por_tipo"] == {}
