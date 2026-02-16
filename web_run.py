#!/usr/bin/env python3
# web_run.py
"""
Script para iniciar o servidor web.
"""

import uvicorn
from pathlib import Path
import sys

# Adicionar src ao path
sys.path.insert(0, str(Path(__file__).parent))

from src.interface.web.app import create_app

app = create_app()

if __name__ == "__main__":
    print("🚀 Iniciando servidor web...")
    print("📱 Acesse: http://localhost:8000")
    print("📚 Documentação: http://localhost:8000/docs")
    print("⏎ Ctrl+C para parar")
    print()
    
    uvicorn.run(
        "web_run:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # Recarrega automaticamente ao modificar código
        log_level="info"
    )