# src/interface/web/routes/admin.py
"""
Rotas administrativas para gerenciamento de serviços.
"""

from pathlib import Path

from fastapi import APIRouter, HTTPException, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory=Path(__file__).parent.parent / "templates")


@router.get("/services")
async def admin_services(request: Request):
    """
    Painel de controle dos serviços.
    """
    registry = request.app.state.registry
    config = request.app.state.config

    status = registry.get_status()

    return templates.TemplateResponse(
        "admin/services.html", {"request": request, "status": status, "config": config}
    )


@router.post("/services/{name}/clear-cache")
async def clear_service_cache(request: Request, name: str):
    """
    Limpa cache de um serviço (força recarga).
    """
    registry = request.app.state.registry

    try:
        registry.clear_cache(name)
        return {"status": "ok", "message": f"Cache limpo para {name}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e


@router.get("/services/{name}/preload")
async def preload_service(request: Request, name: str, lang: str = None):
    """
    Pré-carrega um serviço/modelo.
    """
    try:
        service = request.app.state.registry.get(name)

        if name == "spacy" and lang:
            # Para spaCy, permite pré-carregar modelo específico
            if hasattr(service, "preload_model"):
                success = service.preload_model(lang)
                return {"status": "ok", "preloaded": lang, "success": success}

        return {"status": "ok", "message": f"Serviço {name} já está disponível"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
