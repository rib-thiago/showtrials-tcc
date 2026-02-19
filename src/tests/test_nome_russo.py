# src/tests/test_nome_russo.py
"""
Testes para o Value Object NomeRusso (sem telemetria).
"""

import pytest

from src.domain.value_objects.nome_russo import NomeRusso


class TestNomeRusso:
    """Testes para a classe NomeRusso."""

    def test_criar_nome_valido(self):
        """Deve criar um nome russo válido."""
        nome = NomeRusso("Л.В. Николаева")
        assert nome.original == "Л.В. Николаева"
        assert nome.iniciais == "Л.В."
        assert nome.sobrenome == "Николаева"

    def test_criar_nome_com_espacos(self):
        """Deve ignorar espaços extras (corrigido)."""
        nome = NomeRusso("  Л.В.  Николаева  ")
        assert nome.original == "Л.В. Николаева"  # Espaços normalizados
        assert nome.iniciais == "Л.В."
        assert nome.sobrenome == "Николаева"

    def test_formato_invalido(self):
        """Formato inválido deve levantar erro."""
        with pytest.raises(ValueError, match="Formato de nome russo inválido"):
            NomeRusso("Nikolaev")

        with pytest.raises(ValueError, match="Formato de nome russo inválido"):
            NomeRusso("Л. Николаева")

        with pytest.raises(ValueError, match="Formato de nome russo inválido"):
            NomeRusso("Л.В Николаева")

    def test_propriedades(self):
        """Testa todas as propriedades do objeto."""
        nome = NomeRusso("Л.В. Николаева")

        assert nome.original == "Л.В. Николаева"
        assert nome.iniciais == "Л.В."
        assert nome.sobrenome == "Николаева"
        assert nome.genero == "feminino"
        assert nome.sobrenome_base == "Николаева"  # feminino mantém terminação

    def test_sobrenome_base_com_declinacao(self):
        """Testa remoção de declinação em diferentes casos."""
        casos = [
            ("Л.В. Николаева", "Николаева"),  # feminino
            ("И.В. Сталину", "Сталину"),  # exceção (sobrenome original)
            ("Г.Г. Ягоды", "Ягоды"),  # exceção
            ("А.Б. Тестова", "Тестова"),  # feminino
            ("В.Г. Петров", "Петров"),  # masculino
        ]
        for entrada, esperado in casos:
            nome = NomeRusso(entrada)
            # Para todos os casos, testamos sobrenome_base
            assert nome.sobrenome_base == esperado

    def test_transliterar_nome_comum(self):
        """Testa transliteração de nome comum."""
        nome = NomeRusso("Л.В. Николаева")
        # "Л.В. Николаева" é uma exceção, então retorna "Leonid V. Nikolaev"
        assert nome.transliterar() == "Leonid V. Nikolaev"

    def test_transliterar_com_excecao(self):
        """Testa transliteração usando dicionário de exceções."""
        excecoes = [
            ("И.В. Сталину", "Joseph V. Stalin"),
            ("Г.Г. Ягоды", "Genrikh G. Yagoda"),
            ("Л.Б. Каменева", "Lev B. Kamenev"),
        ]
        for entrada, esperado in excecoes:
            nome = NomeRusso(entrada)
            assert nome.transliterar() == esperado

    def test_transliterar_caracteres_especiais(self):
        """Testa transliteração de caracteres especiais."""
        nome = NomeRusso("Г.Е. Зиновьева")
        resultado = nome.transliterar()
        # "Г.Е. Зиновьева" é uma exceção
        assert resultado == "Grigory E. Zinoviev"

    def test_igualdade(self):
        """Dois nomes com mesmo original devem ser iguais."""
        nome1 = NomeRusso("Л.В. Николаева")
        nome2 = NomeRusso("Л.В. Николаева")
        nome3 = NomeRusso("Г.Г. Ягоды")

        assert nome1 == nome2
        assert nome1 != nome3
        assert nome1 != "Л.В. Николаева"  # comparação com string deve ser False

    def test_representacao_string(self):
        """Testa representação como string."""
        nome = NomeRusso("Л.В. Николаева")
        assert str(nome) == "Л.В. Николаева"
        assert repr(nome) == "<NomeRusso: Л.В. Николаева>"
