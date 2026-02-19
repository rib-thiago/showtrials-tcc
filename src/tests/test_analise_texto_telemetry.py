# src/tests/test_analise_texto_telemetry.py
"""
Testes de telemetria para os Value Objects de análise de texto.
"""

from datetime import datetime
from unittest.mock import MagicMock

import pytest

import src.domain.value_objects.analise_texto as analise_module


class TestAnaliseTextoTelemetry:
    """Testes específicos para telemetria."""

    def setup_method(self):
        """Reconfigura o módulo antes de cada teste."""
        analise_module._telemetry = None
        analise_module._monitor = lambda x: (lambda f: f)

    def test_telemetria_criacao_entidade(self):
        """Verifica se criação de entidade registra telemetria."""
        mock_telemetry = MagicMock()
        analise_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.domain.value_objects.analise_texto import Entidade

        entidade = Entidade("texto", "PERSON", 0.95, 0, 10)

        mock_telemetry.increment.assert_any_call("entidade.criada")

    def test_telemetria_erro_confianca(self):
        """Confiança inválida deve registrar erro."""
        mock_telemetry = MagicMock()
        analise_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.domain.value_objects.analise_texto import Entidade

        with pytest.raises(ValueError):
            Entidade("texto", "PERSON", 1.5, 0, 10)

        mock_telemetry.increment.assert_any_call("entidade.confianca_invalida")

    def test_telemetria_criacao_sentimento(self):
        """Verifica se criação de sentimento registra telemetria."""
        mock_telemetry = MagicMock()
        analise_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.domain.value_objects.analise_texto import Sentimento

        sentimento = Sentimento(0.5, 0.3, "positivo")

        mock_telemetry.increment.assert_any_call("sentimento.criado")

    def test_telemetria_criacao_estatisticas(self):
        """Verifica se criação de estatísticas registra telemetria."""
        mock_telemetry = MagicMock()
        analise_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.domain.value_objects.analise_texto import EstatisticasTexto

        stats = EstatisticasTexto(100, 20, 1, 5, 15, 0.75, 5.0, 10.0)

        mock_telemetry.increment.assert_any_call("estatisticas.criado")

    def test_telemetria_criacao_analise(self):
        """Verifica se criação de análise registra múltiplos contadores."""
        mock_telemetry = MagicMock()
        analise_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.domain.value_objects.analise_texto import (
            AnaliseTexto,
            Entidade,
            EstatisticasTexto,
            Sentimento,
        )

        entidades = [
            Entidade("Л.В. Николаева", "PERSON", 0.95, 0, 10),
            Entidade("Москва", "LOC", 0.90, 15, 20),
        ]
        entidades_por_tipo = {"Pessoa": ["Л.В. Николаева"], "Local": ["Москва"]}
        sentimento = Sentimento(0.2, 0.3, "neutro")
        estatisticas = EstatisticasTexto(1000, 200, 5, 20, 150, 0.75, 5.0, 10.0)

        analise = AnaliseTexto(
            documento_id=1,
            idioma="ru",
            data_analise=datetime.now(),
            estatisticas=estatisticas,
            entidades=entidades,
            entidades_por_tipo=entidades_por_tipo,
            sentimento=sentimento,
            palavras_frequentes=[],
            modelo_utilizado="spacy-ru",
            tempo_processamento=2.5,
        )

        # Verificar contadores
        mock_telemetry.increment.assert_any_call("analise.criada")
        mock_telemetry.increment.assert_any_call("analise.idioma.ru")
        mock_telemetry.increment.assert_any_call("analise.entidades", value=2)

    def test_telemetria_resumo_acessado(self):
        """Acesso ao resumo deve registrar telemetria."""
        mock_telemetry = MagicMock()
        analise_module.configure_telemetry(telemetry_instance=mock_telemetry)

        from src.domain.value_objects.analise_texto import (
            AnaliseTexto,
            Entidade,
            EstatisticasTexto,
            Sentimento,
        )

        entidades = [Entidade("texto", "PERSON", 0.95, 0, 10)]
        sentimento = Sentimento(0.2, 0.3, "neutro")
        estatisticas = EstatisticasTexto(100, 20, 1, 5, 15, 0.75, 5.0, 10.0)

        analise = AnaliseTexto(
            documento_id=1,
            idioma="ru",
            data_analise=datetime.now(),
            estatisticas=estatisticas,
            entidades=entidades,
            entidades_por_tipo={},
            sentimento=sentimento,
            palavras_frequentes=[],
            modelo_utilizado="spacy-ru",
            tempo_processamento=1.0,
        )

        resumo = analise.resumo
        mock_telemetry.increment.assert_any_call("analise.resumo_acessado")

    def test_sem_telemetria_nao_quebra(self):
        """Sem telemetria, o código deve funcionar normalmente."""
        from src.domain.value_objects.analise_texto import Entidade

        entidade = Entidade("texto", "PERSON", 0.95, 0, 10)
        assert entidade.texto == "texto"
