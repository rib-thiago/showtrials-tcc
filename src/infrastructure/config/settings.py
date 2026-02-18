# src/infrastructure/config/settings.py
"""
Configurações do sistema usando python-dotenv.
Carrega variáveis de ambiente do arquivo .env.
"""

import os
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()


class Settings:
    """Configurações centralizadas da aplicação."""

    # Diretório raiz do projeto
    BASE_DIR = Path(__file__).parent.parent.parent.parent

    # Banco de dados
    DB_PATH = BASE_DIR / "data" / "showtrials.db"
    DB_PATH.parent.mkdir(exist_ok=True)

    # Google Cloud Translation
    GOOGLE_TRANSLATE_API_KEY: Optional[str] = os.getenv("GOOGLE_TRANSLATE_API_KEY")
    GOOGLE_APPLICATION_CREDENTIALS: Optional[str] = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

    # URLs dos sites
    LENCENTER_URL = "http://showtrials.ru/glavnaya/lencenter/lencenter-materials/"
    MOSCENTER_URL = "http://showtrials.ru/glavnaya/moscow-center-trial/materialy-sledstviya-1935/"

    # Configurações de scraping
    REQUEST_TIMEOUT = 30
    REQUEST_DELAY = 1  # segundos entre requisições

    # Configurações de UI
    ITENS_POR_PAGINA = 15
    MAX_TEXTO_PREVIEW = 2000

    @property
    def modo_desenvolvimento(self) -> bool:
        """Verifica se está em modo desenvolvimento."""
        return os.getenv("ENV", "development") == "development"

    @property
    def db_url(self) -> str:
        """URL do banco para SQLAlchemy (futuro)."""
        return f"sqlite:///{self.DB_PATH}"


settings = Settings()
