# src/domain/value_objects/tipo_documento.py
"""
Value Object: TipoDocumento
Representa os tipos possíveis de documentos históricos.

Value Objects são imutáveis e definidos por seus atributos.
Dois objetos com mesmo tipo são considerados iguais.
"""

from enum import Enum
from typing import Dict, List


class TipoDocumento(Enum):
    """
    Enumeração dos tipos de documento identificados no acervo.
    Baseado na análise real dos 519 documentos.
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
        return {
            self.INTERROGATORIO: "Protocolo de Interrogatório",
            self.ACAREACAO: "Protocolo de Acareação",
            self.ACUSACAO: "Auto de Acusação",
            self.DECLARACAO: "Declaração/Requerimento",
            self.CARTA: "Correspondência",
            self.RELATORIO: "Relatório Especial (NKVD)",
            self.DEPOIMENTO: "Depoimento Espontâneo",
            self.LAUDO: "Laudo Pericial",
            self.DESCONHECIDO: "Não classificado",
        }[self]

    @property
    def descricao_en(self) -> str:
        """Descrição em inglês para exportação"""
        return {
            self.INTERROGATORIO: "Interrogation Protocol",
            self.ACAREACAO: "Confrontation Protocol",
            self.ACUSACAO: "Indictment",
            self.DECLARACAO: "Statement",
            self.CARTA: "Correspondence",
            self.RELATORIO: "NKVD Special Report",
            self.DEPOIMENTO: "Testimony",
            self.LAUDO: "Forensic Report",
            self.DESCONHECIDO: "Unclassified",
        }[self]

    @property
    def icone(self) -> str:
        """Ícone para UI"""
        return {
            self.INTERROGATORIO: "🔍",
            self.ACAREACAO: "⚖️",
            self.ACUSACAO: "📜",
            self.DECLARACAO: "📝",
            self.CARTA: "✉️",
            self.RELATORIO: "📋",
            self.DEPOIMENTO: "🗣️",
            self.LAUDO: "🏥",
            self.DESCONHECIDO: "📄",
        }[self]

    @classmethod
    def from_titulo(cls, titulo: str) -> "TipoDocumento":
        """
        Classifica o tipo baseado no título em russo.
        Regras baseadas em padrões observados no acervo real.
        """
        if not titulo:
            return cls.DESCONHECIDO

        # Mapeamento de padrões para tipos
        padroes: Dict[List[str], TipoDocumento] = {
            "interrogatorio": (["Протокол допроса"], cls.INTERROGATORIO),
            "acareacao": (["Протокол очной ставки"], cls.ACAREACAO),
            "acusacao": (
                ["Проект обвинительного заключения", "Обвинительное заключение"],
                cls.ACUSACAO,
            ),
            "declaracao": (["Заявление"], cls.DECLARACAO),
            "carta": (["Письмо"], cls.CARTA),
            "relatorio": (["Спецсообщение"], cls.RELATORIO),
            "depoimento": (["Показания", "Показание"], cls.DEPOIMENTO),
            "laudo": (["Акт судебно-медицинского"], cls.LAUDO),
        }

        for _, (padroes_lista, tipo) in padroes.items():
            for padrao in padroes_lista:
                if padrao in titulo:
                    return tipo

        return cls.DESCONHECIDO

    @classmethod
    def listar_todos(cls) -> List["TipoDocumento"]:
        """Retorna todos os tipos válidos (exceto desconhecido)"""
        return [t for t in cls if t != cls.DESCONHECIDO]
