# tests/test_registry.py
"""
Testes para o Service Registry.
"""


import pytest

from src.infrastructure.registry import ServiceRegistry


class TestServiceRegistry:
    """Testes para o registry de serviços."""

    def setup_method(self):
        """Limpa registry antes de cada teste."""
        self.registry = ServiceRegistry()
        self.registry.reset()

    def test_registrar_e_obter_servico(self):
        """Deve registrar e obter serviço."""

        def factory():
            return {"servico": "teste"}

        self.registry.register("teste", factory)
        servico = self.registry.get("teste")

        assert servico["servico"] == "teste"
        assert self.registry.get_status()["teste"]["calls"] == 1

    def test_lazy_loading_so_carrega_quando_chamado(self):
        """Serviço lazy só deve ser carregado na primeira chamada."""
        carregado = False

        def factory():
            nonlocal carregado
            carregado = True
            return {"servico": "lazy"}

        self.registry.register("lazy", factory, lazy=True)
        assert not carregado  # Ainda não carregou

        servico = self.registry.get("lazy")
        assert carregado  # Carregou agora
        assert servico["servico"] == "lazy"

    def test_servico_eager_carrega_na_inicializacao(self):
        """Serviço eager deve carregar ao chamar start_eager_services."""
        carregado = False

        def factory():
            nonlocal carregado
            carregado = True
            return {"servico": "eager"}

        self.registry.register("eager", factory, lazy=False)
        assert not carregado  # Ainda não

        self.registry.start_eager_services()
        assert carregado  # Agora sim

        # Não precisa chamar get
        assert "eager" in self.registry._instances

    def test_singleton_retorna_mesma_instancia(self):
        """Serviço singleton deve retornar mesma instância em múltiplas chamadas."""
        instancias = []

        def factory():
            instancias.append(1)
            return {"id": len(instancias)}

        self.registry.register("singleton", factory, singleton=True)

        s1 = self.registry.get("singleton")
        s2 = self.registry.get("singleton")

        assert s1 is s2  # Mesmo objeto
        assert len(instancias) == 1  # Factory chamada uma vez

    def test_nao_singleton_cria_novas_instancias(self):
        """Serviço não-singleton deve criar nova instância a cada chamada."""
        instancias = []

        def factory():
            instancias.append(1)
            return {"id": len(instancias)}

        self.registry.register("multi", factory, singleton=False)

        s1 = self.registry.get("multi")
        s2 = self.registry.get("multi")

        assert s1 is not s2  # Objetos diferentes
        assert len(instancias) == 2  # Factory chamada duas vezes

    def test_clear_cache(self):
        """Limpar cache deve forçar recarga na próxima chamada."""
        cargas = 0

        def factory():
            nonlocal cargas
            cargas += 1
            return {"carga": cargas}

        self.registry.register("cache", factory)

        s1 = self.registry.get("cache")
        assert s1["carga"] == 1
        assert cargas == 1

        self.registry.clear_cache("cache")

        s2 = self.registry.get("cache")
        assert s2["carga"] == 2
        assert cargas == 2

    def test_servico_nao_registrado(self):
        """Acessar serviço não registrado deve gerar erro."""
        with pytest.raises(KeyError):
            self.registry.get("nao_existe")

    def test_eager_nao_inicializado(self):
        """Serviço eager não inicializado deve gerar erro ao tentar usar."""

        def factory():
            return {"servico": "eager"}

        self.registry.register("eager", factory, lazy=False)

        with pytest.raises(RuntimeError):
            self.registry.get("eager")  # Não chamou start_eager_services
