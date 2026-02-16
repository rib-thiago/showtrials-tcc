# src/infrastructure/translation/google_translator.py
"""
Adaptador para o Google Cloud Translation API.
Reutiliza o tradutor existente do projeto.
"""

import os
from typing import Optional
from pathlib import Path

# Importar o tradutor existente (FALLBACK)
try:
    from translator import GoogleTranslator, TradutorComPersistencia
    from translator import criar_tradutor_da_configuracao as criar_tradutor_legado
    TRADUTOR_LEGADO_DISPONIVEL = True
except ImportError:
    TRADUTOR_LEGADO_DISPONIVEL = False
    print("⚠️ Tradutor legado não encontrado. Usando implementação simplificada.")

from src.infrastructure.config.settings import settings


class GoogleTranslatorAdapter:
    """
    Adaptador para o Google Translate.
    Encapsula a complexidade do tradutor original.
    """
    
    def __init__(self):
        self._tradutor = None
        self._inicializar()
    
    def _inicializar(self):
        """Inicializa o tradutor (tenta usar o legado primeiro)."""
        if TRADUTOR_LEGADO_DISPONIVEL:
            try:
                # Tenta usar o tradutor existente
                self._tradutor = criar_tradutor_legado()
                if self._tradutor:
                    print("✅ Tradutor Google inicializado (modo legado)")
                    return
            except Exception as e:
                print(f"⚠️ Erro ao inicializar tradutor legado: {e}")
        
        # Fallback: implementação simplificada
        print("⚠️ Usando implementação simplificada de tradução")
        self._tradutor = None
    
    def traduzir(self, texto: str, destino: str = 'en') -> str:
        """
        Traduz texto para o idioma destino.
        
        Args:
            texto: Texto original em russo
            destino: Código ISO do idioma (en, pt, es, fr)
        
        Returns:
            str: Texto traduzido
        """
        if not texto:
            return ""
        
        # Se tem tradutor legado, usa ele
        if self._tradutor:
            try:
                resultado = self._tradutor.traduzir_documento_completo(texto, destino=destino)
                return resultado.texto_traduzido
            except Exception as e:
                print(f"⚠️ Erro na tradução com legado: {e}")
                # Fallback para simulação
        
        # SIMULAÇÃO (apenas para testes)
        # Remove quando tiver a chave da API configurada
        return self._simular_traducao(texto, destino)
    
    def _simular_traducao(self, texto: str, destino: str) -> str:
        """
        Simula tradução para testes.
        Remove quando tiver a chave da API configurada.
        """
        prefixos = {
            'en': '[EN] ',
            'pt': '[PT] ',
            'es': '[ES] ',
            'fr': '[FR] '
        }
        prefixo = prefixos.get(destino, f'[{destino}] ')
        
        # Simplesmente adiciona um prefixo (apenas para teste)
        linhas = texto.split('\n')
        linhas_traduzidas = [f"{prefixo}{linha}" for linha in linhas if linha.strip()]
        
        return '\n'.join(linhas_traduzidas) if linhas_traduzidas else texto
    
    def testar_conexao(self) -> bool:
        """Testa se a API está respondendo."""
        if self._tradutor:
            try:
                return self._tradutor.testar_conexao()
            except:
                pass
        return False


# Adaptador com persistência (reutiliza o existente)
class TradutorComPersistenciaAdapter:
    """
    Adaptador que adiciona persistência às traduções.
    """
    
    def __init__(self, tradutor_adapter, repo_traducao):
        self.tradutor = tradutor_adapter
        self.repo = repo_traducao
    
    def traduzir_e_salvar(self, documento_id: int, texto: str, destino: str = 'en'):
        """
        Traduz e salva no banco.
        """
        from src.domain.entities.traducao import Traducao
        from datetime import datetime
        
        # Traduzir
        texto_traduzido = self.tradutor.traduzir(texto, destino)
        
        # Criar entidade
        traducao = Traducao(
            documento_id=documento_id,
            idioma=destino,
            texto_traduzido=texto_traduzido,
            data_traducao=datetime.now(),
            modelo='nmt',
            custo=len(texto) * 0.000020
        )
        
        # Salvar
        traducao.id = self.repo.salvar(traducao)
        
        return traducao