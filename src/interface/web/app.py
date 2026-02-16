# src/interface/web/app.py
"""
Aplicação FastAPI principal.
"""

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import sys

# Adicionar src ao path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from src.infrastructure.persistence.sqlite_repository import SQLiteDocumentoRepository
from src.infrastructure.persistence.sqlite_traducao_repository import SQLiteTraducaoRepository
from src.application.use_cases.listar_documentos import ListarDocumentos
from src.application.use_cases.obter_documento import ObterDocumento
from src.application.use_cases.estatisticas import ObterEstatisticas
from src.application.use_cases.analisar_texto import AnalisarDocumento
from src.application.use_cases.analisar_acervo import AnalisarAcervo
from src.interface.web.routes import documentos, analise, traducoes, estatisticas


def create_app():
    """Factory para criar a aplicação FastAPI com injeção de dependência."""
    
    # 1. Inicializar repositórios
    repo_doc = SQLiteDocumentoRepository()
    repo_trad = SQLiteTraducaoRepository()
    
    # 2. Inicializar casos de uso
    listar_use_case = ListarDocumentos(repo_doc).com_traducao_nomes(True)
    obter_use_case = ObterDocumento(repo_doc, repo_trad).com_traducao_nomes(True)
    estatisticas_use_case = ObterEstatisticas(repo_doc)
    analisar_doc_use_case = AnalisarDocumento(repo_doc, repo_trad)
    analisar_acervo_use_case = AnalisarAcervo(repo_doc)
    
    # 3. Criar app FastAPI
    app = FastAPI(
        title="ShowTrials - Documentos Históricos",
        description="API para acesso ao acervo de documentos dos processos de Moscou e Leningrado",
        version="1.0.0"
    )
    
    # 4. Configurar templates e arquivos estáticos
    templates = Jinja2Templates(directory=Path(__file__).parent / "templates")
    app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")
    
    # 5. Registrar rotas (passando casos de uso)
    app.include_router(
        documentos.router,
        prefix="/documentos",
        tags=["documentos"],
        dependencies=[],  # Injeção será feita via dependências
    )
    app.include_router(
        analise.router,
        prefix="/analise",
        tags=["análise"],
    )
    app.include_router(
        traducoes.router,
        prefix="/traducoes",
        tags=["traduções"],
    )
    app.include_router(
        estatisticas.router,
        prefix="/estatisticas",
        tags=["estatísticas"],
    )
    
    # 6. Rota principal
    @app.get("/")
    async def home(request: Request):
        """Página inicial."""
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "total_docs": repo_doc.contar(),
                "total_trad": repo_trad.contar_por_documento(0)  # Placeholder
            }
        )
    
    # 7. Disponibilizar casos de uso para as rotas
    app.state.repo_doc = repo_doc
    app.state.repo_trad = repo_trad
    app.state.listar_use_case = listar_use_case
    app.state.obter_use_case = obter_use_case
    app.state.estatisticas_use_case = estatisticas_use_case
    app.state.analisar_doc_use_case = analisar_doc_use_case
    app.state.analisar_acervo_use_case = analisar_acervo_use_case
    
    return app