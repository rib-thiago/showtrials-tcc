# src/application/use_cases/base.py
"""
Classe base para casos de uso com acesso a serviços via registry.
"""

from typing import Optional
from src.infrastructure.registry import ServiceRegistry


class BaseUseCase:
    """
    Classe base para casos de uso que precisam acessar serviços.
    Fornece acesso conveniente ao registry.
    """
    
    def __init__(self, registry: Optional[ServiceRegistry] = None):
        """
        Args:
            registry: Registry de serviços (usa singleton se None)
        """
        self._registry = registry or ServiceRegistry()
    
    @property
    def registry(self) -> ServiceRegistry:
        """Retorna o registry (injetado ou singleton)."""
        return self._registry
    
    def get_service(self, name: str, *args, **kwargs):
        """Obtém um serviço pelo nome."""
        return self.registry.get(name, *args, **kwargs)