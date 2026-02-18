# translator.py
"""
Módulo de tradução profissional usando Google Cloud Translation API
Autor: Thiago Ribeiro
Versão: 1.0.0
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
    # Se python-dotenv não estiver instalado, segue sem
    pass

# Import da biblioteca oficial do Google
try:
    from google.cloud import translate_v2 as translate
    from google.cloud import translate_v3

    GOOGLE_CLIENT_AVAILABLE = True
except ImportError:
    GOOGLE_CLIENT_AVAILABLE = False
    print(
        "⚠️  google-cloud-translate não instalado. Instale com: pip install google-cloud-translate"
    )


@dataclass
class TraducaoResultado:
    """Resultado completo de uma tradução"""

    texto_original: str
    texto_traduzido: str
    idioma_origem: str
    idioma_destino: str
    modelo_utilizado: str
    caracteres_originais: int
    custo_estimado: float
    timestamp: datetime = None

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.utcnow()

    @property
    def resumo(self) -> str:
        """Resumo da tradução"""
        return (
            f"[{self.idioma_origem} → {self.idioma_destino}] "
            f"{self.caracteres_originais} chars, "
            f"custo: ${self.custo_estimado:.6f}"
        )


class GoogleTranslator:
    """
    Cliente profissional para Google Cloud Translation API
    Suporta tanto API Key quanto Conta de Serviço
    """

    # Tabela de preços (US$) por caractere - atualizada 2025
    PRICING = {
        "nmt": 0.000020,  # Neural Machine Translation
        "general": 0.000020,
        "default": 0.000020,
    }

    # Idiomas suportados (códigos ISO 639-1)
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
            project_id: ID do projeto Google Cloud (obrigatório para v3)
            location: Localização ('global' ou específica)
        """

        if not GOOGLE_CLIENT_AVAILABLE:
            raise ImportError("Biblioteca google-cloud-translate não encontrada")

        self.project_id = project_id
        self.location = location
        self._modo = "api_key" if api_key else "service_account"

        try:
            if api_key:
                # Modo Chave de API (mais simples)
                self.client = translate.Client(target_language="en", api_key=api_key)
                print("✅ Tradutor inicializado com Chave de API")
            else:
                # Modo Conta de Serviço (mais seguro)
                if credentials_path:
                    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path
                self.client = translate.Client(target_language="en")
                print("✅ Tradutor inicializado com Conta de Serviço")
        except Exception as e:
            raise ConnectionError(f"Falha ao inicializar cliente Google Translate: {e}")

    def traduzir(
        self,
        texto: Union[str, List[str]],
        destino: str = "en",
        origem: Optional[str] = None,
        modelo: str = "nmt",
    ) -> Union[TraducaoResultado, List[TraducaoResultado]]:
        """
        Traduz texto(s) do russo para o idioma destino.

        Args:
            texto: String ou lista de strings para traduzir
            destino: Código ISO do idioma destino (ex: 'en', 'pt')
            origem: Código ISO do idioma origem (None = detecção automática)
            modelo: 'nmt' (neural) ou 'base'

        Returns:
            TraducaoResultado ou lista de TraducaoResultado
        """

        # Validações
        if destino not in self.LINGUAS_SUPORTADAS and destino != "en":
            print(f"⚠️ Idioma '{destino}' não pré-configurado, mas tentaremos mesmo assim")

        # Converter string única em lista para processamento uniforme
        textos = [texto] if isinstance(texto, str) else texto

        try:
            # Chamada à API
            resultados_api = self.client.translate(
                textos, target_language=destino, source_language=origem, model=modelo
            )

            # Processar resultados
            resultados = []
            for i, res in enumerate(resultados_api):
                # Cálculo de custo
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
            raise RuntimeError(f"Falha na tradução: {e}")

    def traduzir_documento_completo(
        self, texto: str, destino: str = "en", chunk_size: int = 3000
    ) -> TraducaoResultado:
        """
        Traduz documentos grandes dividindo em chunks.

        Args:
            texto: Texto completo do documento
            destino: Idioma destino
            chunk_size: Tamanho máximo de cada chunk (limite da API é 30k)
        """

        # Dividir em parágrafos primeiro
        paragrafos = texto.split("\n")
        chunks = []
        chunk_atual = []
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

        # Traduzir cada chunk
        traducoes = []
        total_chars = 0

        for i, chunk in enumerate(chunks, 1):
            print(f"  ↳ Traduzindo parte {i}/{len(chunks)}...")
            try:
                resultado = self.traduzir(chunk, destino=destino)
                traducoes.append(resultado.texto_traduzido)
                total_chars += resultado.caracteres_originais
                time.sleep(0.5)  # Rate limiting
            except Exception as e:
                print(f"    ⚠️ Erro na parte {i}: {e}")
                traducoes.append("")  # Placeholder para erro

        texto_completo = "\n".join(traducoes)

        return TraducaoResultado(
            texto_original=texto,
            texto_traduzido=texto_completo,
            idioma_origem="ru",
            idioma_destino=destino,
            modelo_utilizado="nmt",
            caracteres_originais=total_chars,
            custo_estimado=total_chars * self.PRICING["nmt"],
        )

    def testar_conexao(self) -> bool:
        """Testa se a API está respondendo corretamente"""
        try:
            resultado = self.traduzir("Hello world", destino="pt")
            print(f"✅ Conexão OK! Tradução teste: 'Hello world' → '{resultado.texto_traduzido}'")
            return True
        except Exception as e:
            print(f"❌ Falha na conexão: {e}")
            return False


# ==============================================
# INTEGRAÇÃO COM SEU PROJETO EXISTENTE
# ==============================================


def criar_tradutor_da_configuracao() -> Optional[GoogleTranslator]:
    """
    Factory function que cria o tradutor a partir de variáveis de ambiente.
    Prioriza API Key, depois Conta de Serviço.
    """

    # Tentar primeiro com API Key
    api_key = os.getenv("GOOGLE_TRANSLATE_API_KEY")
    if api_key:
        try:
            return GoogleTranslator(api_key=api_key)
        except Exception as e:
            print(f"⚠️ Falha ao usar API Key: {e}")

    # Tentar com Conta de Serviço
    creds_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    if creds_path and Path(creds_path).exists():
        try:
            return GoogleTranslator(credentials_path=creds_path)
        except Exception as e:
            print(f"⚠️ Falha ao usar Conta de Serviço: {e}")

    print("❌ Nenhuma credencial válida encontrada")
    print("   Defina GOOGLE_TRANSLATE_API_KEY ou GOOGLE_APPLICATION_CREDENTIALS")
    return None


# Instância global para uso no app
tradutor_global = criar_tradutor_da_configuracao()

# translator.py - Adicione esta nova classe e funções

from db import obter_traducao, salvar_traducao


class TradutorComPersistencia:
    """
    Wrapper do GoogleTranslator que automaticamente salva no banco.
    """

    def __init__(self, translator_instance):
        self.translator = translator_instance

    def traduzir_e_salvar(self, documento_id: int, texto: str, destino: str = "en") -> dict:
        """
        Traduz um documento e salva automaticamente no banco.
        """
        print(f"\n🌐 Traduzindo documento {documento_id} para {destino}...")

        # Verificar se já existe tradução
        existente = obter_traducao(documento_id, destino)
        if existente:
            print(f"📚 Tradução existente encontrada! (ID: {existente['id']})")
            print(f"📅 Traduzido em: {existente['data_traducao']}")

            resposta = input("Usar tradução existente? (s/N): ").strip().lower()
            if resposta == "s":
                return existente

        # Traduzir
        resultado = self.translator.traduzir_documento_completo(texto, destino=destino)

        # Salvar no banco
        traducao_id = salvar_traducao(
            documento_id=documento_id,
            idioma=destino,
            texto_traduzido=resultado.texto_traduzido,
            modelo=resultado.modelo_utilizado,
            custo=resultado.custo_estimado,
        )

        return {
            "id": traducao_id,
            "documento_id": documento_id,
            "idioma": destino,
            "texto": resultado.texto_traduzido,
            "custo": resultado.custo_estimado,
            "data_traducao": datetime.utcnow().isoformat(),
        }
