# src/application/use_cases/traduzir_documento.py
"""
Caso de uso: Traduzir um documento.
Integra com Google Translate via Service Registry.
"""

from typing import Optional
from datetime import datetime

from src.domain.entities.traducao import Traducao
from src.domain.interfaces.repositories import RepositorioDocumento
from src.domain.interfaces.repositorio_traducao import RepositorioTraducao
from src.infrastructure.registry import ServiceRegistry
from src.application.dtos.traducao_dto import TraducaoDTO


class TraduzirDocumento:
    """
    Caso de uso para traduzir um documento.
    Agora usa Service Registry para obter o tradutor sob demanda.
    """
    
    def __init__(self, 
                 repo_doc: RepositorioDocumento,
                 repo_trad: RepositorioTraducao,
                 registry: Optional[ServiceRegistry] = None):
        """
        Args:
            repo_doc: Repositório de documentos
            repo_trad: Repositório de traduções
            registry: Registry de serviços (para lazy loading)
        """
        self.repo_doc = repo_doc
        self.repo_trad = repo_trad
        self.registry = registry or ServiceRegistry()
    
    def _get_translator(self):
        """Obtém tradutor do registry (lazy)."""
        return self.registry.get('translator')
    
    def executar(self, 
                 documento_id: int, 
                 idioma_destino: str = 'en',
                 forcar_novo: bool = False) -> Optional[TraducaoDTO]:
        """
        Traduz um documento para o idioma especificado.
        """
        print(f"🔍 DEBUG: executar tradução - documento {documento_id}, idioma {idioma_destino}")
        
        # 1. Verificar se documento existe
        documento = self.repo_doc.buscar_por_id(documento_id)
        if not documento:
            raise ValueError(f"Documento {documento_id} não encontrado")
        
        print(f"   ✅ Documento encontrado: {documento.titulo[:50]}...")
        
        # 2. Verificar se já existe tradução (a menos que force nova)
        if not forcar_novo:
            existente = self.repo_trad.buscar_por_documento(documento_id, idioma_destino)
            if existente:
                print(f"   📚 Tradução existente encontrada")
                return TraducaoDTO.from_domain(existente)
        
        # 3. Obter tradutor do registry e traduzir
        print(f"   🔧 Obtendo tradutor do registry...")
        tradutor = self._get_translator()
        print(f"   ✅ Tradutor obtido: {type(tradutor).__name__}")
        print(f"   📋 Métodos: {[m for m in dir(tradutor) if not m.startswith('_')]}")
        
        try:
            print(f"   🌐 Chamando tradutor.traduzir_documento_completo...")
            texto_traduzido = tradutor.traduzir_documento_completo(
                documento.texto,
                destino=idioma_destino
            )
            print(f"   ✅ Tradução concluída, tamanho: {len(texto_traduzido)} caracteres")
            
        except Exception as e:
            print(f"   ❌ ERRO: {e}")
            print(f"   🔍 Tipo do erro: {type(e).__name__}")
            import traceback
            traceback.print_exc()
            raise RuntimeError(f"Erro na tradução: {e}")
        
        # 4. Criar entidade de tradução
        traducao = Traducao(
            documento_id=documento_id,
            idioma=idioma_destino,
            texto_traduzido=texto_traduzido,
            data_traducao=datetime.now(),
            modelo='nmt',
            custo=len(documento.texto) * 0.000020
        )
        
        # 5. Salvar no repositório
        traducao.id = self.repo_trad.salvar(traducao)
        
        return TraducaoDTO.from_domain(traducao)