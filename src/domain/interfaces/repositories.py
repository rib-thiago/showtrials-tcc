# src/domain/interfaces/repositories.py
"""
Ports (interfaces) para persistência.
Define contratos que a infraestrutura deve implementar.
"""

from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.entities.documento import Documento


class RepositorioDocumento(ABC):
    """
    Interface para repositório de documentos.

    Esta é uma PORT na terminologia da Clean Architecture.
    A implementação concreta será fornecida pela camada de infraestrutura.
    """

    @abstractmethod
    def salvar(self, documento: Documento) -> int:
        """
        Persiste um documento (insert ou update).

        Args:
            documento: Entidade Documento a ser persistida

        Returns:
            int: ID do documento salvo
        """
        pass

    @abstractmethod
    def buscar_por_id(self, id: int) -> Optional[Documento]:
        """
        Busca documento pelo ID.

        Args:
            id: Identificador único

        Returns:
            Documento ou None se não encontrado
        """
        pass

    @abstractmethod
    def listar(
        self,
        offset: int = 0,
        limite: int = 20,
        centro: Optional[str] = None,
        tipo: Optional[str] = None,
    ) -> List[Documento]:
        """
        Lista documentos com paginação e filtros.

        Args:
            offset: Deslocamento para paginação
            limite: Número máximo de registros
            centro: Filtrar por centro ('lencenter' ou 'moscenter')
            tipo: Filtrar por tipo de documento

        Returns:
            List[Documento]: Lista de documentos
        """
        pass

    @abstractmethod
    def contar(self, centro: Optional[str] = None, tipo: Optional[str] = None) -> int:
        """
        Conta documentos com filtros opcionais.

        Args:
            centro: Filtrar por centro
            tipo: Filtrar por tipo

        Returns:
            int: Número total de documentos
        """
        pass

    @abstractmethod
    def remover(self, id: int) -> bool:
        """
        Remove um documento pelo ID.

        Args:
            id: Identificador do documento

        Returns:
            bool: True se removido, False se não encontrado
        """
        pass
