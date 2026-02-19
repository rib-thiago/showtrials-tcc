# src/domain/value_objects/tipo_documento.py
"""
Value Object: TipoDocumento
Representa os tipos possíveis de documentos históricos.
"""

from enum import Enum
from typing import Dict, List

# Telemetria opcional (pode ser None)
_telemetry = None


def _monitor(name=None):
    """Decorator dummy que não faz nada."""

    def decorator(func):
        return func

    return decorator


def configure_telemetry(telemetry_instance=None, monitor_decorator=None):
    """Configura telemetria para este módulo (usado apenas em testes)."""
    global _telemetry, _monitor
    _telemetry = telemetry_instance
    if monitor_decorator:
        _monitor = monitor_decorator


class TipoDocumento(Enum):
    """
    Enumeração dos tipos de documento identificados no acervo.
    """

    INTERROGATORIO = "interrogatorio"
    ACAREACAO = "acareacao"
    ACUSACAO = "acusacao"
    DECLARACAO = "declaracao"
    CARTA = "carta"
    RELATORIO = "relatorio"
    DEPOIMENTO = "depoimento"
    LAUDO = "laudo"
    DESCONHECIDO = "desconhecido"

    @property
    def descricao_pt(self) -> str:
        """Descrição em português para UI"""
        descricoes: Dict[TipoDocumento, str] = {
            TipoDocumento.INTERROGATORIO: "Protocolo de Interrogatório",
            TipoDocumento.ACAREACAO: "Protocolo de Acareação",
            TipoDocumento.ACUSACAO: "Auto de Acusação",
            TipoDocumento.DECLARACAO: "Declaração/Requerimento",
            TipoDocumento.CARTA: "Correspondência",
            TipoDocumento.RELATORIO: "Relatório Especial (NKVD)",
            TipoDocumento.DEPOIMENTO: "Depoimento Espontâneo",
            TipoDocumento.LAUDO: "Laudo Pericial",
            TipoDocumento.DESCONHECIDO: "Não classificado",
        }
        return descricoes[self]

    @property
    def descricao_en(self) -> str:
        """Descrição em inglês para exportação"""
        descricoes: Dict[TipoDocumento, str] = {
            TipoDocumento.INTERROGATORIO: "Interrogation Protocol",
            TipoDocumento.ACAREACAO: "Confrontation Protocol",
            TipoDocumento.ACUSACAO: "Indictment",
            TipoDocumento.DECLARACAO: "Statement",
            TipoDocumento.CARTA: "Correspondence",
            TipoDocumento.RELATORIO: "NKVD Special Report",
            TipoDocumento.DEPOIMENTO: "Testimony",
            TipoDocumento.LAUDO: "Forensic Report",
            TipoDocumento.DESCONHECIDO: "Unclassified",
        }
        return descricoes[self]

    @property
    def icone(self) -> str:
        """Ícone para UI"""
        icones: Dict[TipoDocumento, str] = {
            TipoDocumento.INTERROGATORIO: "🔍",
            TipoDocumento.ACAREACAO: "⚖️",
            TipoDocumento.ACUSACAO: "📜",
            TipoDocumento.DECLARACAO: "📝",
            TipoDocumento.CARTA: "✉️",
            TipoDocumento.RELATORIO: "📋",
            TipoDocumento.DEPOIMENTO: "🗣️",
            TipoDocumento.LAUDO: "🏥",
            TipoDocumento.DESCONHECIDO: "📄",
        }
        return icones[self]

    @classmethod
    @_monitor("tipo_documento.from_titulo")
    def from_titulo(cls, titulo: str) -> "TipoDocumento":
        """
        Classifica o tipo baseado no título em russo.
        """
        if not titulo:
            if _telemetry:
                _telemetry.increment("tipo_documento.titulo_vazio")
            return cls.DESCONHECIDO

        # Mapeamento de padrões para tipos
        padroes: Dict[str, List[str]] = {
            "interrogatorio": ["Протокол допроса"],
            "acareacao": ["Протокол очной ставки"],
            "acusacao": ["Проект обвинительного заключения", "Обвинительное заключение"],
            "declaracao": ["Заявление"],
            "carta": ["Письмо"],
            "relatorio": ["Спецсообщение"],
            "depoimento": ["Показания", "Показание"],
            "laudo": ["Акт судебно-медицинского"],
        }

        for tipo_str, padroes_lista in padroes.items():
            for padrao in padroes_lista:
                if padrao in titulo:
                    if _telemetry:
                        _telemetry.increment(f"tipo_documento.classificado.{tipo_str}")
                    return cls(tipo_str)

        if _telemetry:
            _telemetry.increment("tipo_documento.desconhecido")
        return cls.DESCONHECIDO

    @classmethod
    def listar_todos(cls) -> List["TipoDocumento"]:
        """Retorna todos os tipos válidos (exceto desconhecido)"""
        return [t for t in cls if t != cls.DESCONHECIDO]
