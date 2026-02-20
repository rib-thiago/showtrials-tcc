# src/tests/test_exportar_documento.py
"""
Testes para o caso de uso ExportarDocumento (sem telemetria).
"""

from datetime import datetime
from pathlib import Path
from unittest.mock import Mock, patch

import pytest

from src.application.use_cases.exportar_documento import ExportarDocumento


class TestExportarDocumento:
    """Testes para a lógica de exportação."""

    @pytest.fixture
    def repo_doc_mock(self):
        """Fixture para mock do repositório de documentos."""
        repo = Mock()

        # Documento de exemplo com data_coleta como datetime (NÃO string)
        doc = Mock()
        doc.id = 1
        doc.centro = "lencenter"
        doc.titulo = "Протокол допроса Л.В. Николаева"
        doc.data_original = "1934-12-04"
        doc.url = "http://test.com"
        doc.texto = "Texto longo do documento..." * 100
        doc.data_coleta = datetime.now()  # ← CRÍTICO: datetime, não string
        doc.tipo = "interrogatorio"
        doc.tipo_descricao = "Protocolo de Interrogatório"
        doc.pessoa_principal = "Л.В. Николаева"
        doc.remetente = None
        doc.destinatario = None
        doc.envolvidos = []
        doc.tem_anexos = False
        doc.tamanho_caracteres = len(doc.texto)

        repo.buscar_por_id.return_value = doc
        return repo

    @pytest.fixture
    def repo_trad_mock(self):
        """Fixture para mock do repositório de traduções."""
        repo = Mock()

        # Tradução de exemplo
        traducao = Mock()
        traducao.id = 1
        traducao.documento_id = 1
        traducao.idioma = "en"
        traducao.texto_traduzido = "English translation..." * 100
        traducao.data_traducao = datetime.now()
        traducao.modelo = "nmt"
        traducao.custo = 0.05
        traducao.idioma_nome = "Inglês"
        traducao.idioma_icone = "🇺🇸"

        repo.buscar_por_documento.return_value = traducao
        repo.listar_por_documento.return_value = [traducao]
        return repo

    def test_executar_com_sucesso_original(self, repo_doc_mock, tmp_path):
        """Deve exportar documento original com sucesso."""
        use_case = ExportarDocumento(repo_doc_mock)

        resultado = use_case.executar(
            documento_id=1, formato="txt", idioma="original", diretorio=str(tmp_path)
        )

        assert resultado["sucesso"] is True
        assert "caminho" in resultado
        assert resultado["tamanho"] > 0

        caminho = Path(resultado["caminho"])
        assert caminho.exists()
        assert caminho.suffix == ".txt"
        assert "original" in caminho.name

    def test_executar_com_traducao(self, repo_doc_mock, repo_trad_mock, tmp_path):
        """Deve exportar tradução com sucesso."""
        use_case = ExportarDocumento(repo_doc_mock, repo_trad_mock)

        resultado = use_case.executar(
            documento_id=1, formato="txt", idioma="en", diretorio=str(tmp_path)
        )

        assert resultado["sucesso"] is True
        caminho = Path(resultado["caminho"])
        assert caminho.exists()
        assert "en" in caminho.name

    def test_executar_formato_invalido(self, repo_doc_mock):
        """Formato inválido deve retornar erro."""
        use_case = ExportarDocumento(repo_doc_mock)

        resultado = use_case.executar(documento_id=1, formato="docx")

        assert resultado["sucesso"] is False
        assert "não suportado" in resultado["erro"].lower()

    def test_executar_documento_nao_encontrado(self, repo_doc_mock):
        """Documento inexistente deve retornar erro."""
        repo_doc_mock.buscar_por_id.return_value = None
        use_case = ExportarDocumento(repo_doc_mock)

        resultado = use_case.executar(documento_id=999)

        assert resultado["sucesso"] is False
        assert "não encontrado" in resultado["erro"].lower()

    def test_executar_traducao_nao_encontrada(self, repo_doc_mock, repo_trad_mock):
        """Tradução inexistente deve retornar erro."""
        repo_trad_mock.buscar_por_documento.return_value = None
        use_case = ExportarDocumento(repo_doc_mock, repo_trad_mock)

        resultado = use_case.executar(documento_id=1, idioma="fr")

        assert resultado["sucesso"] is False
        assert "não encontrado" in resultado["erro"].lower()

    def test_executar_pdf_nao_implementado(self, repo_doc_mock):
        """PDF deve retornar erro controlado."""
        use_case = ExportarDocumento(repo_doc_mock)

        resultado = use_case.executar(documento_id=1, formato="pdf")

        assert resultado["sucesso"] is False
        assert "PDF" in resultado["erro"]

    def test_sem_repo_trad_para_traducao(self, repo_doc_mock):
        """Sem repositório de tradução, deve falhar ao buscar tradução."""
        use_case = ExportarDocumento(repo_doc_mock, repo_trad=None)

        resultado = use_case._buscar_documento(1, "en")

        assert resultado is None

    def test_listar_idiomas_disponiveis(self, repo_doc_mock, repo_trad_mock):
        """Deve listar idiomas corretamente."""
        use_case = ExportarDocumento(repo_doc_mock, repo_trad_mock)

        idiomas = use_case.listar_idiomas_disponiveis(1)

        assert len(idiomas) == 2  # original + en
        assert idiomas[0]["codigo"] == "original"
        assert idiomas[1]["codigo"] == "en"
        assert "icone" in idiomas[1]

    def test_gerar_nome_arquivo_sanitizacao(self, repo_doc_mock):
        """Nome do arquivo deve ser sanitizado."""
        use_case = ExportarDocumento(repo_doc_mock)

        dto = Mock()
        dto.id = 1
        dto.titulo = "Arquivo: Teste? *especial"

        nome = use_case._gerar_nome_arquivo(dto, "txt", "original")

        assert "Arquivo Teste especial" in nome
        assert "original.txt" in nome

    def test_gerar_conteudo_txt_com_metadados(self, repo_doc_mock):
        """Conteúdo TXT deve incluir metadados quando solicitado."""
        use_case = ExportarDocumento(repo_doc_mock)

        dto = Mock()
        dto.titulo = "Título Teste"
        dto.centro = "lencenter"
        dto.data_original = "1934"
        dto.url = "http://test.com"
        dto.pessoa_principal = "Pessoa Teste"
        dto.remetente = "Remetente"
        dto.destinatario = "Destinatário"
        dto.envolvidos = ["Envolvido1", "Envolvido2"]
        dto.texto = "Conteúdo do documento"

        conteudo = use_case._gerar_conteudo_txt(dto, incluir_metadados=True)

        assert "TÍTULO: Título Teste" in conteudo
        assert "PESSOA PRINCIPAL: Pessoa Teste" in conteudo
        assert "ENVOLVIDOS: Envolvido1, Envolvido2" in conteudo
        assert "Conteúdo do documento" in conteudo

    def test_gerar_conteudo_txt_sem_metadados(self, repo_doc_mock):
        """Conteúdo TXT deve ter só texto quando sem metadados."""
        use_case = ExportarDocumento(repo_doc_mock)

        dto = Mock()
        dto.titulo = "Título Teste"
        dto.texto = "Conteúdo do documento"

        conteudo = use_case._gerar_conteudo_txt(dto, incluir_metadados=False)

        assert "TÍTULO:" not in conteudo
        assert conteudo == "Conteúdo do documento"

    def test_excecao_ao_escrever_arquivo(self, repo_doc_mock):
        """Erro ao escrever arquivo deve ser capturado."""
        use_case = ExportarDocumento(repo_doc_mock)

        # Forçar erro com patch
        with patch("builtins.open", side_effect=PermissionError("Permissão negada")):
            resultado = use_case.executar(documento_id=1)

            assert resultado["sucesso"] is False
            assert "Erro ao exportar" in resultado["erro"]
