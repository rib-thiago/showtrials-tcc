# src/domain/value_objects/tipo_documento.py
"""
Value Object: TipoDocumento
Representa os tipos possíveis de documentos históricos com type hints e telemetria.
"""

from enum import Enum
from typing import Callable, Dict, List, Optional

# Telemetria opcional
try:
    from src.infrastructure.telemetry import monitor as telemetry_monitor

    TELEMETRY_AVAILABLE = True
    monitor = telemetry_monitor
except ImportError:
    TELEMETRY_AVAILABLE = False

    def monitor(name: Optional[str] = None) -> Callable:
        def decorator(func: Callable) -> Callable:
            return func

        return decorator


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
        descricoes: Dict[str, str] = {
            "interrogatorio": "Protocolo de Interrogatório",
            "acareacao": "Protocolo de Acareação",
            "acusacao": "Auto de Acusação",
            "declaracao": "Declaração/Requerimento",
            "carta": "Correspondência",
            "relatorio": "Relatório Especial (NKVD)",
            "depoimento": "Depoimento Espontâneo",
            "laudo": "Laudo Pericial",
            "desconhecido": "Não classificado",
        }
        return descricoes[self.value]

    @property
    def descricao_en(self) -> str:
        """Descrição em inglês para exportação"""
        descricoes: Dict[str, str] = {
            "interrogatorio": "Interrogation Protocol",
            "acareacao": "Confrontation Protocol",
            "acusacao": "Indictment",
            "declaracao": "Statement",
            "carta": "Correspondence",
            "relatorio": "NKVD Special Report",
            "depoimento": "Testimony",
            "laudo": "Forensic Report",
            "desconhecido": "Unclassified",
        }
        return descricoes[self.value]

    @property
    def icone(self) -> str:
        """Ícone para UI"""
        icones: Dict[str, str] = {
            "interrogatorio": "🔍",
            "acareacao": "⚖️",
            "acusacao": "📜",
            "declaracao": "📝",
            "carta": "✉️",
            "relatorio": "📋",
            "depoimento": "🗣️",
            "laudo": "🏥",
            "desconhecido": "📄",
        }
        return icones[self.value]

    @classmethod
    @monitor("tipo_documento.from_titulo")
    def from_titulo(cls, titulo: str) -> "TipoDocumento":
        """
        Classifica o tipo baseado no título em russo.
        """
        if not titulo:
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
                    return cls(tipo_str)

        return cls.DESCONHECIDO

    @classmethod
    def listar_todos(cls) -> List["TipoDocumento"]:
        """Retorna todos os tipos válidos (exceto desconhecido)"""
        return [t for t in cls if t != cls.DESCONHECIDO]
