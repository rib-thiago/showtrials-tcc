# src/tests/test_tipo_documento.py
"""
Testes para a lógica de negócio do TipoDocumento (sem telemetria).
"""


from src.domain.value_objects.tipo_documento import TipoDocumento


class TestTipoDocumento:
    """Testes para classificação de documentos (sem telemetria)."""

    def test_classificar_interrogatorio(self):
        tipo = TipoDocumento.from_titulo("Протокол допроса Л.В. Николаева")
        assert tipo == TipoDocumento.INTERROGATORIO

    def test_classificar_acareacao(self):
        tipo = TipoDocumento.from_titulo(
            "Протокол очной ставки между Н.С. Антоновым и И.И. Котолыновым"
        )
        assert tipo == TipoDocumento.ACAREACAO

    def test_classificar_carta(self):
        tipo = TipoDocumento.from_titulo("Письмо В.В. Румянцева секретарю ЦК ВКП(б) И.В. Сталину")
        assert tipo == TipoDocumento.CARTA

    def test_classificar_relatorio(self):
        tipo = TipoDocumento.from_titulo("Спецсообщение Г.Г. Ягоды И.В. Сталину")
        assert tipo == TipoDocumento.RELATORIO

    def test_classificar_depoimento_singular(self):
        tipo = TipoDocumento.from_titulo("Показание С.М. Гессена")
        assert tipo == TipoDocumento.DEPOIMENTO

    def test_classificar_depoimento_plural(self):
        tipo = TipoDocumento.from_titulo("Показания А.И. Анишева")
        assert tipo == TipoDocumento.DEPOIMENTO

    def test_titulo_desconhecido(self):
        tipo = TipoDocumento.from_titulo("Documento sem padrão")
        assert tipo == TipoDocumento.DESCONHECIDO

    def test_titulo_vazio(self):
        tipo = TipoDocumento.from_titulo("")
        assert tipo == TipoDocumento.DESCONHECIDO

    def test_listar_todos(self):
        tipos = TipoDocumento.listar_todos()
        assert len(tipos) == 8
        assert TipoDocumento.DESCONHECIDO not in tipos
