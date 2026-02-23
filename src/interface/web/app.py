# src/interface/web/app.py
"""
Aplicação FastAPI com lazy loading via Service Registry.
"""

import logging
import sys
from pathlib import Path
from typing import Any, Callable, cast

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Adicionar src ao path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from src.application.use_cases.analisar_acervo import AnalisarAcervo
from src.application.use_cases.analisar_texto import AnalisarDocumento
from src.application.use_cases.estatisticas import ObterEstatisticas
from src.application.use_cases.listar_documentos import ListarDocumentos
from src.application.use_cases.obter_documento import ObterDocumento
from src.application.use_cases.traduzir_documento import TraduzirDocumento
from src.infrastructure.config import ApplicationConfig
from src.infrastructure.factories import SERVICE_FACTORIES
from src.infrastructure.persistence.sqlite_repository import SQLiteDocumentoRepository
from src.infrastructure.persistence.sqlite_traducao_repository import SQLiteTraducaoRepository
from src.infrastructure.registry import ServiceRegistry
from src.interface.web.routes import admin, analise, documentos, estatisticas, traducoes

logger = logging.getLogger(__name__)


def create_app(config_path: str = "config.yaml"):
    """
    Factory para criar a aplicação FastAPI com lazy loading.

    Args:
        config_path: Caminho para arquivo de configuração
    """
    # 1. Carregar configuração
    config_file = Path(config_path)
    config = ApplicationConfig.from_file(config_file if config_file.exists() else None)
    logger.info(f"📋 Configuração carregada (ambiente: {config.environment})")

    # 2. Criar registry
    registry = ServiceRegistry()

    # 3. Registrar serviços baseado na configuração
    for name, svc_config in config.services.items():
        if not svc_config.enabled:
            logger.info(f"⏸️ Serviço {name} desabilitado na configuração")
            continue

        factory = SERVICE_FACTORIES.get(name)
        if not factory:
            logger.warning(f"⚠️ Factory não encontrada para serviço: {name}")
            continue

        # Tipagem local para satisfazer o mypy (sem alterar lógica)
        factory_typed = cast(Callable[..., Any], factory)

        registry.register(
            name=name,
            factory=factory_typed,
            lazy=svc_config.lazy,
            singleton=svc_config.singleton,
            **svc_config.options,
        )
        logger.info(f"✅ Serviço {name} registrado (lazy={svc_config.lazy})")

    # 4. Inicializar serviços eager
    eager_times = registry.start_eager_services()
    if eager_times:
        logger.info(f"🚀 Serviços eager inicializados: {eager_times}")

    # 5. Inicializar repositórios (sempre eager)
    repo_doc = SQLiteDocumentoRepository()
    repo_trad = SQLiteTraducaoRepository()
    logger.info("✅ Repositórios inicializados")

    # 6. Inicializar casos de uso (com registry)
    listar_use_case = ListarDocumentos(repo_doc).com_traducao_nomes(True)
    obter_use_case = ObterDocumento(repo_doc, repo_trad).com_traducao_nomes(True)
    estatisticas_use_case = ObterEstatisticas(repo_doc)

    # Casos que usam serviços (COM registry)
    analisar_doc_use_case = AnalisarDocumento(
        repo_doc=repo_doc, repo_trad=repo_trad, registry=registry
    )

    analisar_acervo_use_case = AnalisarAcervo(repo_doc=repo_doc, registry=registry)

    traduzir_use_case = TraduzirDocumento(repo_doc=repo_doc, repo_trad=repo_trad, registry=registry)

    # 7. Criar app FastAPI
    app = FastAPI(
        title="ShowTrials - Documentos Históricos",
        description="API para acesso ao acervo de documentos dos processos de Moscou e Leningrado",
        version="1.0.0",
    )

    # 8. Configurar templates e arquivos estáticos
    templates = Jinja2Templates(directory=Path(__file__).parent / "templates")
    static_dir = Path(__file__).parent / "static"
    static_dir.mkdir(exist_ok=True)
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

    # 9. Registrar rotas (injetando dependências)
    app.include_router(documentos.router, prefix="/documentos", tags=["documentos"])
    app.include_router(analise.router, prefix="/analise", tags=["análise"])
    app.include_router(traducoes.router, prefix="/traducoes", tags=["traduções"])
    app.include_router(estatisticas.router, prefix="/estatisticas", tags=["estatísticas"])
    app.include_router(admin.router, prefix="/admin", tags=["admin"])

    # 10. Disponibilizar dependências via app.state
    app.state.registry = registry
    app.state.config = config
    app.state.repo_doc = repo_doc
    app.state.repo_trad = repo_trad
    app.state.listar_use_case = listar_use_case
    app.state.obter_use_case = obter_use_case
    app.state.estatisticas_use_case = estatisticas_use_case
    app.state.analisar_doc_use_case = analisar_doc_use_case
    app.state.analisar_acervo_use_case = analisar_acervo_use_case

    # 11. Rota de status
    @app.get("/status")
    async def service_status():
        """Endpoint para verificar status dos serviços."""
        return {
            "status": "running",
            "environment": config.environment,
            "services": registry.get_status(),
        }

    # 12. Rota principal
    @app.get("/")
    async def home(request: Request):
        """Página inicial."""
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "total_docs": repo_doc.contar(),
                "total_trad": len(repo_trad.listar_por_documento(0)),  # Placeholder
            },
        )

    logger.info("🚀 Aplicação web inicializada com lazy loading")
    return app
