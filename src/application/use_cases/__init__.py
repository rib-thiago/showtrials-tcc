# src/application/use_cases/__init__.py
from src.application.use_cases.classificar_documento import ClassificarDocumento
from src.application.use_cases.listar_documentos import ListarDocumentos
from src.application.use_cases.obter_documento import ObterDocumento
from src.application.use_cases.estatisticas import ObterEstatisticas

__all__ = [
    'ClassificarDocumento',
    'ListarDocumentos',
    'ObterDocumento',
    'ObterEstatisticas'
]