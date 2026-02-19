# src/tests/test_traducao.py
"""
Testes para a entidade Traducao (sem telemetria).
"""

from datetime import datetime

import pytest

from src.domain.entities.traducao import Traducao


class TestTraducao:
    """Testes para a classe Traducao."""

    def test_criar_traducao_valida(self):
        """Deve criar uma tradução válida."""
        data = datetime.now()
        traducao = Traducao(
            documento_id=1,
            idioma="en",
            texto_traduzido="Hello world",
            data_traducao=data,
        )

        assert traducao.documento_id == 1
        assert traducao.idioma == "en"
        assert traducao.texto_traduzido == "Hello world"
        assert traducao.data_traducao == data
        assert traducao.id is None
        assert traducao.modelo is None
        assert traducao.custo == 0.0

    def test_criar_com_id_e_custo(self):
        """Deve criar com campos opcionais preenchidos."""
        data = datetime.now()
        traducao = Traducao(
            documento_id=1,
            idioma="pt",
            texto_traduzido="Olá mundo",
            data_traducao=data,
            id=42,
            modelo="nmt",
            custo=0.15,
        )

        assert traducao.id == 42
        assert traducao.modelo == "nmt"
        assert traducao.custo == 0.15

    def test_idioma_invalido(self):
        """Idioma inválido deve levantar erro."""
        with pytest.raises(ValueError, match="Idioma inválido"):
            Traducao(
                documento_id=1,
                idioma="de",  # Alemão não suportado
                texto_traduzido="Hallo Welt",
                data_traducao=datetime.now(),
            )

    def test_texto_vazio(self):
        """Texto vazio deve levantar erro."""
        with pytest.raises(ValueError, match="Texto traduzido não pode ser vazio"):
            Traducao(
                documento_id=1,
                idioma="en",
                texto_traduzido="",
                data_traducao=datetime.now(),
            )

    def test_idioma_nome_conhecido(self):
        """Deve retornar nome correto para idiomas conhecidos."""
        traducao_en = Traducao(1, "en", "text", datetime.now())
        traducao_pt = Traducao(1, "pt", "text", datetime.now())
        traducao_es = Traducao(1, "es", "text", datetime.now())
        traducao_fr = Traducao(1, "fr", "text", datetime.now())

        assert traducao_en.idioma_nome == "Inglês"
        assert traducao_pt.idioma_nome == "Português"
        assert traducao_es.idioma_nome == "Espanhol"
        assert traducao_fr.idioma_nome == "Francês"

    def test_idioma_nome_desconhecido(self):
        """Idioma desconhecido deve retornar código em maiúsculo."""
        # Isso não deve acontecer devido à validação, mas testamos o fallback
        traducao = Traducao(
            documento_id=1,
            idioma="en",  # válido
            texto_traduzido="text",
            data_traducao=datetime.now(),
        )
        # Forçar idioma inválido para testar fallback
        traducao.idioma = "xx"
        assert traducao.idioma_nome == "XX"

    def test_idioma_icone_conhecido(self):
        """Deve retornar ícone correto para idiomas conhecidos."""
        traducao_en = Traducao(1, "en", "text", datetime.now())
        traducao_pt = Traducao(1, "pt", "text", datetime.now())
        traducao_es = Traducao(1, "es", "text", datetime.now())
        traducao_fr = Traducao(1, "fr", "text", datetime.now())

        assert traducao_en.idioma_icone == "🇺🇸"
        assert traducao_pt.idioma_icone == "🇧🇷"
        assert traducao_es.idioma_icone == "🇪🇸"
        assert traducao_fr.idioma_icone == "🇫🇷"

    def test_idioma_icone_desconhecido(self):
        """Idioma desconhecido deve retornar ícone genérico."""
        traducao = Traducao(
            documento_id=1,
            idioma="en",  # válido
            texto_traduzido="text",
            data_traducao=datetime.now(),
        )
        traducao.idioma = "xx"
        assert traducao.idioma_icone == "🌐"
