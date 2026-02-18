# src/infrastructure/registry.py
"""
Service Registry - Implementa o padrão Registry com Lazy Loading.
Permite registro e acesso centralizado a serviços com inicialização sob demanda.
"""

import logging
import time
from dataclasses import dataclass, field
from datetime import datetime
from threading import Lock
from typing import Any, Callable, Dict, Optional

logger = logging.getLogger(__name__)


@dataclass
class ServiceStats:
    """Estatísticas de uso de um serviço."""

    calls: int = 0
    last_call: Optional[datetime] = None
    load_time: Optional[float] = None
    registered_at: datetime = field(default_factory=datetime.now)
    errors: int = 0


@dataclass
class ServiceInfo:
    """Informações de registro de um serviço."""

    name: str
    factory: Callable
    lazy: bool = True
    config: Dict[str, Any] = field(default_factory=dict)
    singleton: bool = True  # Se True, mesma instância para todas as chamadas


class ServiceRegistry:
    """
    Registro central de serviços com lazy loading.

    Características:
    - Thread-safe (usa Lock para acesso concorrente)
    - Suporte a serviços eager e lazy
    - Cache de instâncias após primeira inicialização
    - Estatísticas de uso por serviço
    """

    _instance = None
    _lock = Lock()

    def __new__(cls):
        """Singleton thread-safe."""
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        """Inicialização (executada apenas uma vez devido ao singleton)."""
        if self._initialized:
            return

        self._services: Dict[str, ServiceInfo] = {}
        self._instances: Dict[str, Any] = {}
        self._stats: Dict[str, ServiceStats] = {}
        self._lock = Lock()
        self._initialized = True
        logger.info("🔧 Service Registry inicializado")

    def register(
        self, name: str, factory: Callable, lazy: bool = True, singleton: bool = True, **config
    ) -> None:
        """
        Registra um serviço no registry.

        Args:
            name: Nome único do serviço
            factory: Função que cria a instância do serviço
            lazy: Se True, serviço só é inicializado quando requisitado
            singleton: Se True, mesma instância para todas as chamadas
            **config: Configuração específica do serviço
        """
        with self._lock:
            if name in self._services:
                logger.warning(f"⚠️ Serviço {name} já registrado. Substituindo.")

            self._services[name] = ServiceInfo(
                name=name, factory=factory, lazy=lazy, singleton=singleton, config=config
            )
            self._stats[name] = ServiceStats()
            logger.info(f"✅ Serviço registrado: {name} (lazy={lazy})")

    def get(self, name: str, *args, **kwargs) -> Any:
        """
        Obtém instância de um serviço (inicializa se necessário).

        Args:
            name: Nome do serviço
            *args, **kwargs: Argumentos para a factory (se primeira vez)

        Returns:
            Instância do serviço

        Raises:
            KeyError: Se serviço não registrado
            RuntimeError: Se serviço eager não inicializado
        """
        # Atualiza estatísticas
        with self._lock:
            if name not in self._services:
                available = ", ".join(self._services.keys())
                raise KeyError(f"Serviço não registrado: {name}. Disponíveis: {available}")

            self._stats[name].calls += 1
            self._stats[name].last_call = datetime.now()

        service_info = self._services[name]

        # Se já tem instância e é singleton, retorna
        if service_info.singleton and name in self._instances:
            return self._instances[name]

        # Se não é lazy, deveria já ter sido inicializado
        if not service_info.lazy and service_info.singleton and name not in self._instances:
            raise RuntimeError(
                f"❌ Serviço eager {name} não foi inicializado. "
                "Chame start_eager_services() primeiro."
            )

        # Inicialização (thread-safe)
        with self._lock:
            # Verifica novamente dentro do lock (para singletons)
            if service_info.singleton and name in self._instances:
                return self._instances[name]

            logger.info(f"🔄 Inicializando serviço: {name}")
            start = time.time()

            try:
                # Mescla config com args/kwargs
                factory_kwargs = service_info.config.copy()
                factory_kwargs.update(kwargs)

                instance = service_info.factory(*args, **factory_kwargs)

                if service_info.singleton:
                    self._instances[name] = instance

                elapsed = time.time() - start
                self._stats[name].load_time = elapsed
                logger.info(f"✅ Serviço {name} inicializado em {elapsed:.2f}s")

                return instance

            except Exception as e:
                self._stats[name].errors += 1
                logger.error(f"❌ Falha ao inicializar {name}: {e}")
                raise

    def start_eager_services(self) -> Dict[str, float]:
        """
        Inicializa todos os serviços marcados como eager.

        Returns:
            Dict com tempos de inicialização por serviço
        """
        results = {}
        for name, info in self._services.items():
            if not info.lazy and info.singleton and name not in self._instances:
                logger.info(f"🚀 Inicializando serviço eager: {name}")
                start = time.time()
                try:
                    instance = info.factory(**info.config)
                    self._instances[name] = instance
                    elapsed = time.time() - start
                    results[name] = elapsed
                    self._stats[name].load_time = elapsed
                    logger.info(f"✅ {name} pronto em {elapsed:.2f}s")
                except Exception as e:
                    logger.error(f"❌ Falha ao inicializar {name}: {e}")
                    results[name] = -1
        return results

    def get_status(self) -> Dict[str, Dict]:
        """Retorna status de todos os serviços registrados."""
        status = {}
        for name, info in self._services.items():
            stats = self._stats[name]
            status[name] = {
                "registered": True,
                "lazy": info.lazy,
                "singleton": info.singleton,
                "loaded": name in self._instances,
                "calls": stats.calls,
                "last_call": stats.last_call.isoformat() if stats.last_call else None,
                "load_time": stats.load_time,
                "errors": stats.errors,
                "registered_at": stats.registered_at.isoformat(),
                "config": info.config,
            }
        return status

    def get_service(self, name: str) -> Optional[ServiceInfo]:
        """Retorna informações de registro de um serviço."""
        return self._services.get(name)

    def reset(self) -> None:
        """Reset completo (útil para testes)."""
        with self._lock:
            self._services.clear()
            self._instances.clear()
            self._stats.clear()
            logger.info("🔄 Registry resetado")

    def clear_cache(self, name: Optional[str] = None) -> None:
        """
        Limpa instâncias em cache (força recarga na próxima chamada).

        Args:
            name: Nome do serviço (None para todos)
        """
        with self._lock:
            if name:
                if name in self._instances:
                    del self._instances[name]
                    logger.info(f"🧹 Cache limpo para: {name}")
            else:
                self._instances.clear()
                logger.info("🧹 Cache completo limpo")
