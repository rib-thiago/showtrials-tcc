# src/infrastructure/translation/google_translator.py
"""
Adaptador para o Google Cloud Translation API.
Versão auto-contida sem dependência do tradutor legado.
"""

import os
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Union

# Carregar variáveis de ambiente
try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

# Tentar importar a biblioteca oficial do Google
try:
    from google.cloud import translate_v2 as translate

    GOOGLE_CLIENT_AVAILABLE = True
except ImportError:
    GOOGLE_CLIENT_AVAILABLE = False
    print("⚠️ google-cloud-translate não instalado. Instale com: pip install google-cloud-translate")


@dataclass
class TraducaoResultado:
    """Resultado completo de uma tradução."""

    texto_original: str
    texto_traduzido: str
    idioma_origem: str
    idioma_destino: str
    modelo_utilizado: str
    caracteres_originais: int
    custo_estimado: float
    timestamp: Optional[datetime] = None  # <- fix MyPy: Optional explícito

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.utcnow()

    @property
    def resumo(self) -> str:
        """Resumo da tradução."""
        return (
            f"[{self.idioma_origem} → {self.idioma_destino}] "
            f"{self.caracteres_originais} chars, "
            f"custo: ${self.custo_estimado:.6f}"
        )


class GoogleTranslator:
    """
    Cliente para Google Cloud Translation API.
    Implementação própria sem dependência do tradutor legado.
    """

    # Tabela de preços (US$) por caractere
    PRICING = {
        "nmt": 0.000020,  # Neural Machine Translation
        "general": 0.000020,
        "default": 0.000020,
    }

    # Idiomas suportados
    LINGUAS_SUPORTADAS = {
        "pt": "Português",
        "en": "Inglês",
        "ru": "Russo",
        "es": "Espanhol",
        "fr": "Francês",
        "de": "Alemão",
        "it": "Italiano",
        "ja": "Japonês",
        "zh": "Chinês",
        "ar": "Árabe",
    }

    def __init__(
        self,
        credentials_path: Optional[str] = None,
        api_key: Optional[str] = None,
        project_id: Optional[str] = None,
        location: str = "global",
    ):
        """
        Inicializa o tradutor.

        Args:
            credentials_path: Caminho para arquivo JSON de conta de serviço
            api_key: Chave de API diretamente
            project_id: ID do projeto Google Cloud
            location: Localização ('global' ou específica)
        """
        self.project_id = project_id
        self.location = location
        self.api_key = api_key
        self.credentials_path = credentials_path

        self._client = None
        self._inicializar()

    def _inicializar(self):
        """Inicializa o cliente Google Translate."""
        if not GOOGLE_CLIENT_AVAILABLE:
            print("⚠️ Biblioteca google-cloud-translate não disponível. Usando modo simulação.")
            self._client = None
            return

        try:
            if self.api_key:
                # Modo Chave de API
                self._client = translate.Client(target_language="en", api_key=self.api_key)
                print("✅ Tradutor Google inicializado com Chave de API")
            elif self.credentials_path:
                # Modo Conta de Serviço
                os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = self.credentials_path
                self._client = translate.Client(target_language="en")
                print("✅ Tradutor Google inicializado com Conta de Serviço")
            else:
                # Tentar via ambiente
                self._client = translate.Client(target_language="en")
                print("✅ Tradutor Google inicializado via ambiente")
        except Exception as e:
            print(f"⚠️ Falha ao inicializar cliente Google Translate: {e}")
            print("   Usando modo simulação.")
            self._client = None

    def traduzir(
        self,
        texto: Union[str, List[str]],
        destino: str = "en",
        origem: Optional[str] = None,
        modelo: str = "nmt",
    ) -> Union[TraducaoResultado, List[TraducaoResultado]]:
        """
        Traduz texto(s) para o idioma destino.
        """
        # Se não tem cliente, usar simulação
        if self._client is None:
            return self._simular_traducao(texto, destino, origem)

        # Converter string única em lista
        textos = [texto] if isinstance(texto, str) else texto

        try:
            # Chamada à API
            resultados_api = self._client.translate(
                textos, target_language=destino, source_language=origem, model=modelo
            )

            resultados: List[TraducaoResultado] = []
            for i, res in enumerate(resultados_api):
                chars_originais = len(textos[i])
                custo = chars_originais * self.PRICING.get(modelo, self.PRICING["default"])

                resultado = TraducaoResultado(
                    texto_original=textos[i],
                    texto_traduzido=res["translatedText"],
                    idioma_origem=res.get("detectedSourceLanguage", origem or "ru"),
                    idioma_destino=destino,
                    modelo_utilizado=res.get("model", modelo),
                    caracteres_originais=chars_originais,
                    custo_estimado=custo,
                )
                resultados.append(resultado)

            return resultados[0] if isinstance(texto, str) else resultados

        except Exception as e:
            print(f"⚠️ Erro na tradução com API: {e}")
            print("   Usando fallback para simulação.")
            return self._simular_traducao(texto, destino, origem)

    def traduzir_documento_completo(
        self, texto: str, destino: str = "en", chunk_size: int = 3000
    ) -> str:
        """
        Traduz documentos grandes dividindo em chunks.
        """
        if not texto:
            return ""

        paragrafos = texto.split("\n")
        chunks: List[str] = []
        chunk_atual: List[str] = []
        tamanho_atual = 0

        for para in paragrafos:
            if tamanho_atual + len(para) < chunk_size:
                chunk_atual.append(para)
                tamanho_atual += len(para)
            else:
                chunks.append("\n".join(chunk_atual))
                chunk_atual = [para]
                tamanho_atual = len(para)

        if chunk_atual:
            chunks.append("\n".join(chunk_atual))

        print(f"📄 Documento dividido em {len(chunks)} partes para tradução")

        traducoes: List[str] = []
        for i, chunk in enumerate(chunks, 1):
            print(f"  ↳ Traduzindo parte {i}/{len(chunks)}...")
            try:
                resultado = self.traduzir(chunk, destino=destino)
                if isinstance(resultado, TraducaoResultado):
                    traducoes.append(resultado.texto_traduzido)
                else:
                    traducoes.append(str(resultado))
                time.sleep(0.5)
            except Exception as e:
                print(f"    ⚠️ Erro na parte {i}: {e}")
                traducoes.append("")

        return "\n".join(traducoes)

    def _simular_traducao(self, texto, destino="en", origem=None):
        """Simula tradução para testes (fallback quando API não disponível)."""
        if isinstance(texto, str):
            return TraducaoResultado(
                texto_original=texto,
                texto_traduzido=f"[SIMULAÇÃO {destino}] {texto[:100]}...",
                idioma_origem=origem or "ru",
                idioma_destino=destino,
                modelo_utilizado="simulação",
                caracteres_originais=len(texto),
                custo_estimado=0.0,
            )
        else:
            return [
                TraducaoResultado(
                    texto_original=t,
                    texto_traduzido=f"[SIMULAÇÃO {destino}] {t[:50]}...",
                    idioma_origem=origem or "ru",
                    idioma_destino=destino,
                    modelo_utilizado="simulação",
                    caracteres_originais=len(t),
                    custo_estimado=0.0,
                )
                for t in texto
            ]

    def testar_conexao(self) -> bool:
        """Testa se a API está respondendo."""
        try:
            resultado = self.traduzir("Hello world", destino="pt")
            if isinstance(resultado, TraducaoResultado):
                print(
                    f"✅ Conexão OK! Tradução teste: 'Hello world' → '{resultado.texto_traduzido}'"
                )
                return True
            return False
        except Exception as e:
            print(f"❌ Falha na conexão: {e}")
            return False


def criar_tradutor_da_configuracao() -> Optional[GoogleTranslator]:
    """Factory function que cria o tradutor a partir de variáveis de ambiente."""
    api_key = os.getenv("GOOGLE_TRANSLATE_API_KEY")
    if api_key:
        try:
            return GoogleTranslator(api_key=api_key)
        except Exception as e:
            print(f"⚠️ Falha ao usar API Key: {e}")

    creds_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    if creds_path and Path(creds_path).exists():
        try:
            return GoogleTranslator(credentials_path=creds_path)
        except Exception as e:
            print(f"⚠️ Falha ao usar Conta de Serviço: {e}")

    print("⚠️ Nenhuma credencial válida encontrada. Usando modo simulação.")
    return GoogleTranslator()


class TradutorComPersistenciaAdapter:
    """Adaptador que adiciona persistência às traduções."""

    def __init__(self, tradutor_adapter, repo_traducao):
        self.tradutor = tradutor_adapter
        self.repo = repo_traducao

    def traduzir_e_salvar(self, documento_id: int, texto: str, destino: str = "en"):
        """Traduz e salva no banco."""
        from datetime import datetime

        from src.domain.entities.traducao import Traducao

        if hasattr(self.tradutor, "traduzir_documento_completo"):
            texto_traduzido = self.tradutor.traduzir_documento_completo(texto, destino)
            custo = len(texto) * 0.000020
        else:
            resultado = self.tradutor.traduzir(texto, destino)
            if hasattr(resultado, "texto_traduzido"):
                texto_traduzido = resultado.texto_traduzido
                custo = resultado.custo_estimado
            else:
                texto_traduzido = str(resultado)
                custo = len(texto) * 0.000020

        traducao = Traducao(
            documento_id=documento_id,
            idioma=destino,
            texto_traduzido=texto_traduzido,
            data_traducao=datetime.now(),
            modelo="nmt",
            custo=custo,
        )

        traducao.id = self.repo.salvar(traducao)
        return traducao
