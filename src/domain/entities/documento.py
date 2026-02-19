# src/domain/entities/documento.py
"""
Módulo: Documento
Entidade principal do sistema, representa um documento histórico.
"""

import re
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional

# Telemetria opcional
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


@dataclass
class Documento:
    """
    Representa um documento histórico coletado.
    """

    # Atributos obrigatórios
    centro: str
    titulo: str
    url: str
    texto: str
    data_coleta: datetime

    # Atributos opcionais com valores padrão
    id: Optional[int] = None
    data_original: Optional[str] = None

    # Metadados enriquecidos (todos opcionais)
    tipo: Optional[str] = None
    tipo_descricao: Optional[str] = None
    pessoa_principal: Optional[str] = None
    remetente: Optional[str] = None
    destinatario: Optional[str] = None
    envolvidos: Optional[List[str]] = field(default_factory=list)
    tem_anexos: bool = False

    def __post_init__(self):
        """Validações após inicialização"""
        if self.centro not in ["lencenter", "moscenter"]:
            if _telemetry:
                _telemetry.increment("documento.centro_invalido")
            raise ValueError(f"Centro inválido: {self.centro}")

        if not self.titulo:
            if _telemetry:
                _telemetry.increment("documento.titulo_vazio")
            raise ValueError("Título não pode ser vazio")

        if not self.url:
            if _telemetry:
                _telemetry.increment("documento.url_vazia")
            raise ValueError("URL não pode ser vazia")

        if _telemetry:
            _telemetry.increment("documento.criado")

    @property
    def tamanho_caracteres(self) -> int:
        """
        Retorna o tamanho do texto em caracteres.
        """
        return len(self.texto)

    @property
    def tamanho_palavras(self) -> int:
        """
        Retorna o número aproximado de palavras.
        """
        if not self.texto:
            return 0
        return len(self.texto.split())

    @property
    def resumo(self) -> str:
        """
        Resumo do documento para exibição rápida.
        """
        tipo_str = f" [{self.tipo_descricao}]" if self.tipo_descricao else ""
        pessoa_str = f" - {self.pessoa_principal}" if self.pessoa_principal else ""
        return f"{self.titulo[:50]}{tipo_str}{pessoa_str}"

    @_monitor("documento.extrair_pessoas")
    def extrair_pessoas_do_titulo(self) -> List[str]:
        """
        Extrai nomes no formato russo (Л.В. Николаева) do título.
        """
        if not self.titulo:
            return []

        padrao = r"([А-Я]\. ?[А-Я]\. [А-Я][а-я]+)"
        resultado = re.findall(padrao, self.titulo)

        if _telemetry:
            _telemetry.increment("documento.pessoas_extraidas", value=len(resultado))

        return resultado

    def to_dict(self) -> Dict[str, Any]:
        """
        Converte para dicionário (útil para serialização).
        """
        return {
            "id": self.id,
            "centro": self.centro,
            "titulo": self.titulo,
            "data_original": self.data_original,
            "url": self.url,
            "texto": self.texto,
            "data_coleta": self.data_coleta.isoformat() if self.data_coleta else None,
            "tipo": self.tipo,
            "tipo_descricao": self.tipo_descricao,
            "pessoa_principal": self.pessoa_principal,
            "remetente": self.remetente,
            "destinatario": self.destinatario,
            "envolvidos": self.envolvidos,
            "tem_anexos": self.tem_anexos,
            "tamanho": self.tamanho_caracteres,
        }

    @classmethod
    def from_dict(cls, dados: Dict[str, Any]) -> "Documento":
        """
        Cria documento a partir de dicionário.
        """
        # Converte string ISO para datetime se necessário
        if isinstance(dados.get("data_coleta"), str):
            from datetime import datetime

            dados["data_coleta"] = datetime.fromisoformat(dados["data_coleta"])

        if _telemetry:
            _telemetry.increment("documento.from_dict")

        return cls(**dados)
