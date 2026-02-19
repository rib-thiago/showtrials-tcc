# src/tests/test_analise_texto.py
"""
Testes para os Value Objects de análise de texto (sem telemetria).
"""

from datetime import datetime

import pytest

from src.domain.value_objects.analise_texto import (
    AnaliseTexto,
    Entidade,
    EstatisticasTexto,
    Sentimento,
)


class TestEntidade:
    """Testes para a classe Entidade."""

    def test_criar_entidade_valida(self):
        """Deve criar uma entidade válida."""
        entidade = Entidade(
            texto="Л.В. Николаева",
            tipo="PERSON",
            confianca=0.95,
            posicao_inicio=10,
            posicao_fim=25,
        )
        assert entidade.texto == "Л.В. Николаева"
        assert entidade.tipo == "PERSON"
        assert entidade.confianca == 0.95
        assert entidade.posicao_inicio == 10
        assert entidade.posicao_fim == 25

    def test_confianca_invalida(self):
        """Confiança fora do intervalo deve levantar erro."""
        with pytest.raises(ValueError, match="Confiança deve estar entre 0 e 1"):
            Entidade("texto", "PERSON", 1.5, 0, 10)

        with pytest.raises(ValueError, match="Confiança deve estar entre 0 e 1"):
            Entidade("texto", "PERSON", -0.5, 0, 10)

    def test_posicao_invalida(self):
        """Posições inválidas devem levantar erro."""
        with pytest.raises(ValueError, match="Posições inválidas"):
            Entidade("texto", "PERSON", 0.5, -1, 10)

        with pytest.raises(ValueError, match="Posições inválidas"):
            Entidade("texto", "PERSON", 0.5, 10, 5)


class TestSentimento:
    """Testes para a classe Sentimento."""

    def test_criar_sentimento_valido(self):
        """Deve criar um sentimento válido."""
        sentimento = Sentimento(
            polaridade=0.5,
            subjetividade=0.3,
            classificacao="positivo",
        )
        assert sentimento.polaridade == 0.5
        assert sentimento.subjetividade == 0.3
        assert sentimento.classificacao == "positivo"

    def test_polaridade_invalida(self):
        """Polaridade fora do intervalo deve levantar erro."""
        with pytest.raises(ValueError, match="Polaridade deve estar entre -1 e 1"):
            Sentimento(1.5, 0.5, "positivo")

        with pytest.raises(ValueError, match="Polaridade deve estar entre -1 e 1"):
            Sentimento(-1.5, 0.5, "positivo")

    def test_subjetividade_invalida(self):
        """Subjetividade fora do intervalo deve levantar erro."""
        with pytest.raises(ValueError, match="Subjetividade deve estar entre 0 e 1"):
            Sentimento(0.5, 1.5, "positivo")

    def test_classificacao_invalida(self):
        """Classificação inválida deve levantar erro."""
        with pytest.raises(ValueError, match="Classificação inválida"):
            Sentimento(0.5, 0.5, "muito_bom")


class TestEstatisticasTexto:
    """Testes para a classe EstatisticasTexto."""

    def test_criar_estatisticas_validas(self):
        """Deve criar estatísticas válidas."""
        stats = EstatisticasTexto(
            total_caracteres=1000,
            total_palavras=200,
            total_paragrafos=5,
            total_frases=20,
            palavras_unicas=150,
            densidade_lexica=0.75,
            tamanho_medio_palavra=5.0,
            tamanho_medio_frase=10.0,
        )
        assert stats.total_caracteres == 1000
        assert stats.total_palavras == 200
        assert stats.densidade_lexica == 0.75

    def test_palavras_negativas(self):
        """Total de palavras negativo deve levantar erro."""
        with pytest.raises(ValueError, match="Total de palavras não pode ser negativo"):
            EstatisticasTexto(100, -5, 1, 5, 3, 0.6, 5.0, 20.0)

    def test_unicas_maior_que_total(self):
        """Palavras únicas maior que total deve levantar erro."""
        with pytest.raises(ValueError, match="Palavras únicas não pode ser maior que total"):
            EstatisticasTexto(100, 10, 1, 5, 15, 1.5, 5.0, 20.0)


class TestAnaliseTexto:
    """Testes para a classe AnaliseTexto."""

    @pytest.fixture
    def entidades(self):
        """Fixture com lista de entidades."""
        return [
            Entidade("Л.В. Николаева", "PERSON", 0.95, 10, 25),
            Entidade("Москва", "LOC", 0.90, 30, 35),
        ]

    @pytest.fixture
    def entidades_por_tipo(self):
        """Fixture com entidades agrupadas por tipo."""
        return {
            "Pessoa": ["Л.В. Николаева"],
            "Local": ["Москва"],
        }

    @pytest.fixture
    def sentimento(self):
        """Fixture com sentimento."""
        return Sentimento(0.2, 0.3, "neutro")

    @pytest.fixture
    def estatisticas(self):
        """Fixture com estatísticas."""
        return EstatisticasTexto(1000, 200, 5, 20, 150, 0.75, 5.0, 10.0)

    def test_criar_analise_valida(self, entidades, entidades_por_tipo, sentimento, estatisticas):
        """Deve criar uma análise válida."""
        analise = AnaliseTexto(
            documento_id=1,
            idioma="ru",
            data_analise=datetime.now(),
            estatisticas=estatisticas,
            entidades=entidades,
            entidades_por_tipo=entidades_por_tipo,
            sentimento=sentimento,
            palavras_frequentes=[("допрос", 10), ("николаев", 8)],
            modelo_utilizado="spacy-ru",
            tempo_processamento=2.5,
        )
        assert analise.documento_id == 1
        assert analise.idioma == "ru"
        assert len(analise.entidades) == 2
        assert len(analise.palavras_frequentes) == 2

    def test_tempo_negativo(self, entidades, entidades_por_tipo, sentimento, estatisticas):
        """Tempo de processamento negativo deve levantar erro."""
        with pytest.raises(ValueError, match="Tempo de processamento não pode ser negativo"):
            AnaliseTexto(
                documento_id=1,
                idioma="ru",
                data_analise=datetime.now(),
                estatisticas=estatisticas,
                entidades=entidades,
                entidades_por_tipo=entidades_por_tipo,
                sentimento=sentimento,
                palavras_frequentes=[],
                modelo_utilizado="spacy-ru",
                tempo_processamento=-1.0,
            )

    def test_idioma_nao_suportado(self, entidades, entidades_por_tipo, sentimento, estatisticas):
        """Idioma não suportado deve levantar erro."""
        with pytest.raises(ValueError, match="Idioma não suportado"):
            AnaliseTexto(
                documento_id=1,
                idioma="fr",  # Francês não suportado
                data_analise=datetime.now(),
                estatisticas=estatisticas,
                entidades=entidades,
                entidades_por_tipo=entidades_por_tipo,
                sentimento=sentimento,
                palavras_frequentes=[],
                modelo_utilizado="spacy-ru",
                tempo_processamento=2.5,
            )

    def test_resumo(self, entidades, entidades_por_tipo, sentimento, estatisticas):
        """Testa a propriedade resumo."""
        analise = AnaliseTexto(
            documento_id=42,
            idioma="en",
            data_analise=datetime.now(),
            estatisticas=estatisticas,
            entidades=entidades,
            entidades_por_tipo=entidades_por_tipo,
            sentimento=sentimento,
            palavras_frequentes=[],
            modelo_utilizado="spacy-en",
            tempo_processamento=1.5,
        )
        resumo = analise.resumo
        assert "Doc 42 (en)" in resumo
        assert "200 palavras" in resumo
        assert "2 entidades" in resumo
        assert "neutro" in resumo
