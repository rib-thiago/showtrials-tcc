# src/tests/test_tipo_documento.py
"""
Testes para o Value Object TipoDocumento.
"""

from src.domain.value_objects.tipo_documento import TipoDocumento


class TestTipoDocumento:
    """Testes para classificação de documentos."""
    
    def test_classificar_interrogatorio(self):
        """Deve identificar interrogatório pelo título."""
        tipo = TipoDocumento.from_titulo('Протокол допроса Л.В. Николаева')
        assert tipo == TipoDocumento.INTERROGATORIO
        assert tipo.descricao_pt == 'Protocolo de Interrogatório'
        assert tipo.icone == '🔍'
    
    def test_classificar_acareacao(self):
        """Deve identificar acareação pelo título."""
        tipo = TipoDocumento.from_titulo(
            'Протокол очной ставки между Н.С. Антоновым и И.И. Котолыновым'
        )
        assert tipo == TipoDocumento.ACAREACAO
    
    def test_classificar_carta(self):
        """Deve identificar carta pelo título."""
        tipo = TipoDocumento.from_titulo(
            'Письмо В.В. Румянцева секретарю ЦК ВКП(б) И.В. Сталину'
        )
        assert tipo == TipoDocumento.CARTA
    
    def test_classificar_relatorio(self):
        """Deve identificar relatório NKVD."""
        tipo = TipoDocumento.from_titulo(
            'Спецсообщение Г.Г. Ягоды И.В. Сталину'
        )
        assert tipo == TipoDocumento.RELATORIO
    
    def test_classificar_depoimento_singular(self):
        """Deve identificar depoimento no singular."""
        tipo = TipoDocumento.from_titulo('Показание С.М. Гессена')
        assert tipo == TipoDocumento.DEPOIMENTO
    
    def test_classificar_depoimento_plural(self):
        """Deve identificar depoimento no plural."""
        tipo = TipoDocumento.from_titulo('Показания А.И. Анишева')
        assert tipo == TipoDocumento.DEPOIMENTO
    
    def test_titulo_desconhecido(self):
        """Título sem padrão conhecido deve retornar DESCONHECIDO."""
        tipo = TipoDocumento.from_titulo('Documento sem padrão')
        assert tipo == TipoDocumento.DESCONHECIDO
    
    def test_listar_todos(self):
        """Deve listar todos os tipos exceto desconhecido."""
        tipos = TipoDocumento.listar_todos()
        assert len(tipos) == 8
        assert TipoDocumento.DESCONHECIDO not in tipos