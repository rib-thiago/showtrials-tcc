# src/tests/test_documento.py
"""
Testes unitários para a entidade Documento.
"""

from datetime import datetime

import pytest

from src.domain.entities.documento import Documento


class TestDocumento:
    """Testes para a classe Documento."""

    def test_criar_documento_valido(self):
        """Deve criar documento com atributos mínimos."""
        doc = Documento(
            centro="lencenter",
            titulo="Протокол допроса Л.В. Николаева",
            url="http://teste.com",
            texto="Texto do interrogatório...",
            data_coleta=datetime.now(),
        )

        assert doc.centro == "lencenter"
        assert doc.titulo == "Протокол допроса Л.В. Николаева"
        assert doc.id is None
        assert doc.tamanho_caracteres == len("Texto do interrogatório...")

    def test_centro_invalido(self):
        """Deve rejeitar centro inválido."""
        with pytest.raises(ValueError, match="Centro inválido"):
            Documento(
                centro="invalido",
                titulo="Teste",
                url="http://teste.com",
                texto="texto",
                data_coleta=datetime.now(),
            )

    def test_titulo_vazio(self):
        """Deve rejeitar título vazio."""
        with pytest.raises(ValueError, match="Título não pode ser vazio"):
            Documento(
                centro="lencenter",
                titulo="",
                url="http://teste.com",
                texto="texto",
                data_coleta=datetime.now(),
            )

    def test_extrair_pessoas_do_titulo(self):
        """Deve extrair nomes russos do título."""
        doc = Documento(
            centro="lencenter",
            titulo="Протокол допроса Л.В. Николаева",
            url="http://teste.com",
            texto="texto",
            data_coleta=datetime.now(),
        )

        pessoas = doc.extrair_pessoas_do_titulo()
        assert len(pessoas) == 1
        assert pessoas[0] == "Л.В. Николаева"

    def test_to_dict_com_data(self):
        """Deve converter para dicionário corretamente."""
        data = datetime(2024, 1, 1, 12, 0)
        doc = Documento(
            id=1,
            centro="lencenter",
            titulo="Título",
            url="url",
            texto="texto",
            data_coleta=data,
            tipo="interrogatorio",
        )

        d = doc.to_dict()
        assert d["id"] == 1
        assert d["centro"] == "lencenter"
        assert d["data_coleta"] == "2024-01-01T12:00:00"
        assert d["tamanho"] == 5
