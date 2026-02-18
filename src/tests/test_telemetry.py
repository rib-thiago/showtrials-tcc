"""Testes para o módulo de telemetria."""

import tempfile
import time
from pathlib import Path

from src.infrastructure.telemetry import Telemetry, monitor


def test_telemetry_basica():
    """Testa funcionalidade básica da telemetria."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Criar instância isolada para o teste
        telemetry = Telemetry(log_dir=tmpdir)

        # Versão manual sem decorator (para teste)
        start = time.time()
        resultado = 42
        elapsed = time.time() - start

        telemetry.metrics.append(
            {
                "type": "duration",
                "name": "teste",
                "value": elapsed,
                "timestamp": time.time(),
                "tags": {},
            }
        )
        telemetry.counters["teste.success"] += 1

        telemetry.flush()

        # Verificar se arquivos foram criados
        logs = list(Path(tmpdir).glob("*.jsonl"))
        assert len(logs) > 0, "Nenhum arquivo de log foi criado"

        # Verificar conteúdo
        with open(logs[0], "r") as f:
            linha = f.readline().strip()
            assert '"type": "duration"' in linha
            assert '"name": "teste"' in linha


def test_monitor_decorator():
    """Testa o decorator @monitor."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Substituir a instância global para o teste
        from src.infrastructure import telemetry as telemetry_module

        original_telemetry = telemetry_module.telemetry
        telemetry_module.telemetry = Telemetry(log_dir=tmpdir)

        try:

            @monitor("teste_decorator")
            def funcao_teste():
                return 42

            resultado = funcao_teste()
            assert resultado == 42

            # Forçar flush
            telemetry_module.telemetry.flush()

            # Verificar se arquivos foram criados
            logs = list(Path(tmpdir).glob("*.jsonl"))
            assert len(logs) > 0

        finally:
            # Restaurar instância original
            telemetry_module.telemetry = original_telemetry


def test_telemetry_increment():
    """Testa o método increment."""
    with tempfile.TemporaryDirectory() as tmpdir:
        telemetry = Telemetry(log_dir=tmpdir)

        telemetry.increment("contador.teste", value=5, tags={"tag": "valor"})
        telemetry.flush()

        # Verificar contadores
        counters_file = Path(tmpdir) / f"counters_{telemetry._session_id}.json"
        assert counters_file.exists()

        import json

        with open(counters_file, "r") as f:
            counters = json.load(f)
            assert counters.get("contador.teste") == 5
