# src/domain/interfaces/repositorio_traducao.py
"""
Interface para repositório de traduções.
"""

from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.entities.traducao import Traducao


class RepositorioTraducao(ABC):
    """Interface para repositório de traduções."""

    @abstractmethod
    def salvar(self, traducao: Traducao) -> int:
        """Salva uma tradução."""
        pass

    @abstractmethod
    def buscar_por_id(self, id: int) -> Optional[Traducao]:
        """Busca tradução por ID."""
        pass

    @abstractmethod
    def buscar_por_documento(self, documento_id: int, idioma: str) -> Optional[Traducao]:
        """Busca tradução específica de um documento."""
        pass

    @abstractmethod
    def listar_por_documento(self, documento_id: int) -> List[Traducao]:
        """Lista todas as traduções de um documento."""
        pass

    @abstractmethod
    def contar_por_documento(self, documento_id: int) -> int:
        """Conta traduções de um documento."""
        pass
