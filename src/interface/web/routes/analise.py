# src/interface/web/routes/analise.py
"""
Rotas para análise de texto.
"""

from fastapi import APIRouter, Request, HTTPException, Form
from fastapi.templating import Jinja2Templates
from pathlib import Path

router = APIRouter()
templates = Jinja2Templates(directory=Path(__file__).parent.parent / "templates")


@router.get("/acervo")
async def analisar_acervo(request: Request):
    """
    Análise global do acervo.
    """
    try:
        repo_doc = request.app.state.repo_doc
        total_docs = repo_doc.contar()
        
        # Dados seguros para o template
        stats = {
            "total_docs": total_docs,
            "total_palavras": 0,
            "media_palavras_por_doc": 0,
            "documentos_por_tamanho": {
                "pequeno (<1000 palavras)": 0,
                "médio (1000-5000 palavras)": 0,
                "grande (>5000 palavras)": 0
            },
            "pessoas_mais_citadas": [],
            "top_locais": [],
            "top_organizacoes": []
        }
        
        # Tentar usar o caso de uso se disponível
        use_case = request.app.state.analisar_acervo_use_case
        if use_case:
            try:
                stats_reais = use_case.estatisticas_globais()
                if stats_reais:
                    stats.update(stats_reais)
            except:
                pass
        
        return templates.TemplateResponse(
            "analise/acervo.html",
            {
                "request": request,
                "stats": stats
            }
        )
    except Exception as e:
        return templates.TemplateResponse(
            "erro.html",
            {
                "request": request,
                "mensagem": f"Erro na análise do acervo: {str(e)}",
                "voltar": "/"
            },
            status_code=500
        )

@router.get("/documento/{documento_id}")
async def analisar_documento_form(request: Request, documento_id: int):
    """
    Formulário para análise de documento.
    """
    return templates.TemplateResponse(
        "analise/form.html",
        {
            "request": request,
            "documento_id": documento_id
        }
    )


@router.post("/documento/{documento_id}")
async def analisar_documento(
    request: Request,
    documento_id: int,
    idioma: str = Form("ru"),
    gerar_wordcloud: bool = Form(False)
):
    """
    Executa análise de documento.
    """
    use_case = request.app.state.analisar_doc_use_case
    
    try:
        resultado = use_case.executar(
            documento_id=documento_id,
            idioma=idioma,
            gerar_wordcloud=gerar_wordcloud
        )
        
        if not resultado:
            return templates.TemplateResponse(
                "erro.html",
                {
                    "request": request,
                    "mensagem": f"Documento {documento_id} não encontrado",
                    "voltar": f"/documentos/{documento_id}"
                },
                status_code=404
            )
        
        return templates.TemplateResponse(
            "analise/resultado.html",
            {
                "request": request,
                "analise": resultado,
                "documento_id": documento_id
            }
        )
    except Exception as e:
        return templates.TemplateResponse(
            "erro.html",
            {
                "request": request,
                "mensagem": f"Erro na análise: {str(e)}",
                "voltar": f"/documentos/{documento_id}"
            },
            status_code=500
        )