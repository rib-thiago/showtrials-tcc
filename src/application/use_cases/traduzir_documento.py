# src/application/use_cases/traduzir_documento.py
"""
Caso de uso: Traduzir um documento.
Integra com Google Translate e salva no repositório.
"""

from typing import Optional
from datetime import datetime

from src.domain.entities.traducao import Traducao
from src.domain.interfaces.repositories import RepositorioDocumento  # <-- CORRIGIDO
from src.domain.interfaces.repositorio_traducao import RepositorioTraducao
from src.application.dtos.traducao_dto import TraducaoDTO


class TraduzirDocumento:
    """
    Caso de uso para traduzir um documento.
    """
    
    def __init__(self, 
                 repo_doc: RepositorioDocumento,
                 repo_trad: RepositorioTraducao,
                 tradutor_service):  # Serviço externo (Google Translate)
        self.repo_doc = repo_doc
        self.repo_trad = repo_trad
        self.tradutor = tradutor_service
    
    def executar(self, 
                 documento_id: int, 
                 idioma_destino: str = 'en',
                 forcar_novo: bool = False) -> Optional[TraducaoDTO]:
        """
        Traduz um documento para o idioma especificado.
        
        Args:
            documento_id: ID do documento original
            idioma_destino: Código do idioma (en, pt, es, fr)
            forcar_novo: Se True, ignora tradução existente
        
        Returns:
            TraducaoDTO da tradução (nova ou existente)
        """
        # 1. Verificar se documento existe
        documento = self.repo_doc.buscar_por_id(documento_id)
        if not documento:
            raise ValueError(f"Documento {documento_id} não encontrado")
        
        # 2. Verificar se já existe tradução (a menos que force nova)
        if not forcar_novo:
            existente = self.repo_trad.buscar_por_documento(documento_id, idioma_destino)
            if existente:
                return TraducaoDTO.from_domain(existente)
        
        # 3. Traduzir usando serviço externo
        try:
            texto_traduzido = self.tradutor.traduzir(
                documento.texto,
                destino=idioma_destino
            )
        except Exception as e:
            raise RuntimeError(f"Erro na tradução: {e}")
        
        # 4. Criar entidade de tradução
        traducao = Traducao(
            documento_id=documento_id,
            idioma=idioma_destino,
            texto_traduzido=texto_traduzido,
            data_traducao=datetime.now(),
            modelo='nmt',
            custo=len(documento.texto) * 0.000020  # Estimativa
        )
        
        # 5. Salvar no repositório
        traducao.id = self.repo_trad.salvar(traducao)
        
        return TraducaoDTO.from_domain(traducao)