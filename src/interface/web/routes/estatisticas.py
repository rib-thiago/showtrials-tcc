# src/interface/web/routes/estatisticas.py
"""
Rotas para estatísticas.
"""

from pathlib import Path

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory=Path(__file__).parent.parent / "templates")


@router.get("/")
async def estatisticas(request: Request):
    """
    Dashboard de estatísticas.
    """
    use_case = request.app.state.estatisticas_use_case
    stats = use_case.executar()

    return templates.TemplateResponse(
        "estatisticas/dashboard.html", {"request": request, "stats": stats}
    )


@router.get("/json")
async def estatisticas_json(request: Request):
    """
    Estatísticas em formato JSON.
    """
    use_case = request.app.state.estatisticas_use_case
    stats = use_case.executar()

    return {
        "total_documentos": stats.total_documentos,
        "total_traducoes": stats.total_traducoes,
        "por_centro": stats.documentos_por_centro,
        "por_tipo": stats.documentos_por_tipo,
        "pessoas_frequentes": [
            {"nome": nome_en, "frequencia": count}
            for nome_ru, count, nome_en in stats.pessoas_frequentes[:10]
        ],
    }
