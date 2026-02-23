# src/application/use_cases/traduzir_documento.py
"""
Caso de uso: Traduzir um documento com telemetria.
Integra com Google Translate via Service Registry.
"""

from datetime import datetime
from typing import Optional

from src.application.dtos.traducao_dto import TraducaoDTO
from src.domain.entities.traducao import Traducao
from src.domain.interfaces.repositories import RepositorioDocumento
from src.domain.interfaces.repositorio_traducao import RepositorioTraducao
from src.infrastructure.registry import ServiceRegistry

# Telemetria opcional
_telemetry = None


def configure_telemetry(telemetry_instance=None):
    """Configura telemetria para este módulo (usado apenas em testes)."""
    global _telemetry
    _telemetry = telemetry_instance


class TraduzirDocumento:
    """
    Caso de uso para traduzir um documento.
    Agora usa Service Registry para obter o tradutor sob demanda.
    """

    def __init__(
        self,
        repo_doc: RepositorioDocumento,
        repo_trad: RepositorioTraducao,
        registry: Optional[ServiceRegistry] = None,
    ):
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
        return self.registry.get("translator")

    def executar(
        self, documento_id: int, idioma_destino: str = "en", forcar_novo: bool = False
    ) -> Optional[TraducaoDTO]:
        """
        Traduz um documento para o idioma especificado.
        """
        if _telemetry:
            _telemetry.increment("traduzir_documento.executar.iniciado")
            _telemetry.increment(f"traduzir_documento.idioma.{idioma_destino}")

        # 1. Verificar se documento existe
        documento = self.repo_doc.buscar_por_id(documento_id)
        if not documento:
            if _telemetry:
                _telemetry.increment("traduzir_documento.erro.documento_nao_encontrado")
            raise ValueError(f"Documento {documento_id} não encontrado")

        # 2. Verificar se já existe tradução (a menos que force nova)
        if not forcar_novo:
            existente = self.repo_trad.buscar_por_documento(documento_id, idioma_destino)
            if existente:
                if _telemetry:
                    _telemetry.increment("traduzir_documento.traducao_existente")
                return TraducaoDTO.from_domain(existente)

        # 3. Obter tradutor do registry e traduzir
        try:
            tradutor = self._get_translator()
            texto_traduzido = tradutor.traduzir_documento_completo(
                documento.texto, destino=idioma_destino
            )

            if _telemetry:
                _telemetry.increment("traduzir_documento.traducao_sucesso")
                _telemetry.increment("traduzir_documento.caracteres", value=len(documento.texto))

        except Exception as e:
            if _telemetry:
                _telemetry.increment("traduzir_documento.erro.traducao")
            raise RuntimeError(f"Erro na tradução: {e}") from e

        # 4. Criar entidade de tradução
        traducao = Traducao(
            documento_id=documento_id,
            idioma=idioma_destino,
            texto_traduzido=texto_traduzido,
            data_traducao=datetime.now(),
            modelo="nmt",
            custo=len(documento.texto) * 0.000020,
        )

        # 5. Salvar no repositório
        traducao.id = self.repo_trad.salvar(traducao)

        if _telemetry:
            _telemetry.increment("traduzir_documento.traducao_salva")

        return TraducaoDTO.from_domain(traducao)
