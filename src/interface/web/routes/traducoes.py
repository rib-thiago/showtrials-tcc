# src/interface/web/routes/traducoes.py
"""
Rotas para traduções.
"""

from fastapi import APIRouter, Request, HTTPException
from fastapi.templating import Jinja2Templates
from pathlib import Path

router = APIRouter()
templates = Jinja2Templates(directory=Path(__file__).parent.parent / "templates")


@router.get("/")
async def listar_todas_traducoes(request: Request):
    """
    Lista todas as traduções do acervo.
    """
    return templates.TemplateResponse(
        "traducoes/todas.html",
        {
            "request": request,
            "mensagem": "Funcionalidade em desenvolvimento"
        }
    )


@router.get("/documento/{documento_id}")
async def listar_traducoes(request: Request, documento_id: int):
    """
    Lista traduções de um documento.
    """
    try:
        repo_trad = request.app.state.repo_trad
        repo_doc = request.app.state.repo_doc
        
        # Buscar documento
        documento = repo_doc.buscar_por_id(documento_id)
        if not documento:
            return templates.TemplateResponse(
                "erro.html",
                {
                    "request": request,
                    "mensagem": f"Documento {documento_id} não encontrado",
                    "voltar": "/documentos/"
                },
                status_code=404
            )
        
        # Buscar traduções
        traducoes = repo_trad.listar_por_documento(documento_id)
        
        return templates.TemplateResponse(
            "traducoes/lista.html",
            {
                "request": request,
                "documento_id": documento_id,
                "documento_titulo": documento.titulo,
                "traducoes": traducoes
            }
        )
    except Exception as e:
        return templates.TemplateResponse(
            "erro.html",
            {
                "request": request,
                "mensagem": f"Erro ao buscar traduções: {str(e)}",
                "voltar": f"/documentos/{documento_id}"
            },
            status_code=500
        )


@router.get("/documento/{documento_id}/{idioma}")
async def ver_traducao(request: Request, documento_id: int, idioma: str):
    """
    Visualiza uma tradução específica.
    """
    try:
        repo_trad = request.app.state.repo_trad
        repo_doc = request.app.state.repo_doc
        
        # Buscar tradução
        traducao = repo_trad.buscar_por_documento(documento_id, idioma)
        if not traducao:
            return templates.TemplateResponse(
                "erro.html",
                {
                    "request": request,
                    "mensagem": f"Tradução {idioma} para documento {documento_id} não encontrada",
                    "voltar": f"/traducoes/documento/{documento_id}"
                },
                status_code=404
            )
        
        # Buscar documento original
        documento = repo_doc.buscar_por_id(documento_id)
        
        return templates.TemplateResponse(
            "traducoes/detalhe.html",
            {
                "request": request,
                "traducao": traducao,
                "documento": documento,
                "idioma": idioma
            }
        )
    except Exception as e:
        return templates.TemplateResponse(
            "erro.html",
            {
                "request": request,
                "mensagem": f"Erro ao visualizar tradução: {str(e)}",
                "voltar": f"/traducoes/documento/{documento_id}"
            },
            status_code=500
        )