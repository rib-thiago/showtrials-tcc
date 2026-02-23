"""Telemetria básica sem dependências externas."""

import json
import time
from collections import defaultdict
from datetime import datetime
from functools import wraps
from pathlib import Path
from typing import Any, Callable, Dict, Optional


class Telemetry:
    """Coleta métricas de operação do sistema."""

    # Anotações dos atributos de instância (resolve var-annotated no __init__)
    metrics: list[dict[str, Any]]
    counters: defaultdict[str, int]

    def __init__(self, log_dir: str = "logs"):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(exist_ok=True)

        self.metrics = []
        self.counters = defaultdict(int)
        self._session_id = datetime.now().strftime("%Y%m%d_%H%M%S")

    def record_time(self, name: str, tags: Optional[Dict[str, Any]] = None):
        """Decorator para medir tempo de execução."""

        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(*args, **kwargs):
                start = time.time()
                try:
                    result = func(*args, **kwargs)
                    elapsed = time.time() - start

                    self.metrics.append(
                        {
                            "type": "duration",
                            "name": name,
                            "value": elapsed,
                            "timestamp": datetime.now().isoformat(),
                            "tags": tags or {},
                        }
                    )

                    self.counters[f"{name}.success"] += 1
                    return result

                except Exception as e:
                    self.counters[f"{name}.error"] += 1
                    self.metrics.append(
                        {
                            "type": "error",
                            "name": name,
                            "error": str(e),
                            "timestamp": datetime.now().isoformat(),
                            "tags": tags or {},
                        }
                    )
                    raise

            return wrapper

        return decorator

    def increment(
        self, name: str | None = None, value: int = 1, tags: Optional[Dict[str, Any]] = None
    ) -> None:
        """Incrementa um contador manualmente."""
        if name is None:
            name = "unknown"

        self.counters[name] += value
        self.metrics.append(
            {
                "type": "counter",
                "name": name,
                "value": value,
                "timestamp": datetime.now().isoformat(),
                "tags": tags or {},
            }
        )

    def flush(self):
        """Salva métricas em disco."""
        if not self.metrics and not self.counters:
            return

        # Salva métricas em JSONL
        filename = self.log_dir / f"metrics_{self._session_id}.jsonl"
        with open(filename, "a") as f:
            for metric in self.metrics:
                f.write(json.dumps(metric) + "\n")

        # Salva contadores
        counters_file = self.log_dir / f"counters_{self._session_id}.json"
        with open(counters_file, "w") as f:
            json.dump(dict(self.counters), f, indent=2)

        print(f"📊 Telemetria salva em {filename}")
        self.metrics = []


# Instância global
telemetry = Telemetry()


def monitor(name: str | None = None):
    """Decorator de atalho para telemetry.record_time."""

    def decorator(func):
        nonlocal name
        if name is None:
            name = func.__name__
        return telemetry.record_time(name)(func)

    return decorator
