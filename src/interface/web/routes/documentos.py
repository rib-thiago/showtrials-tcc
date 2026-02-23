# src/interface/web/routes/documentos.py
"""
Rotas para documentos.
"""

from pathlib import Path

from fastapi import APIRouter, HTTPException, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory=Path(__file__).parent.parent / "templates")


@router.get("/")
async def listar_documentos(
    request: Request, pagina: int = 1, centro: str | None = None, tipo: str | None = None
):
    """
    Lista documentos com paginação.
    """
    use_case = request.app.state.listar_use_case

    resultados = use_case.executar(pagina=pagina, limite=15, centro=centro, tipo=tipo)

    return templates.TemplateResponse(
        "documentos/lista.html",
        {
            "request": request,
            "documentos": resultados["items"],
            "total": resultados["total"],
            "pagina": resultados["pagina"],
            "total_paginas": resultados["total_paginas"],
            "centro": centro,
            "tipo": tipo,
        },
    )


@router.get("/{documento_id}")
async def obter_documento(request: Request, documento_id: int):
    """
    Obtém detalhes de um documento.
    """
    use_case = request.app.state.obter_use_case
    documento = use_case.executar(documento_id)

    if not documento:
        raise HTTPException(status_code=404, detail="Documento não encontrado")

    return templates.TemplateResponse(
        "documentos/detalhe.html", {"request": request, "doc": documento}
    )


@router.get("/{documento_id}/json")
async def obter_documento_json(request: Request, documento_id: int):
    """
    Obtém documento em formato JSON (para API).
    """
    use_case = request.app.state.obter_use_case
    documento = use_case.executar(documento_id)

    if not documento:
        raise HTTPException(status_code=404, detail="Documento não encontrado")

    return documento
