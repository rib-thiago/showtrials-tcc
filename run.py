#!/usr/bin/env python3
# run.py
"""
Ponto de entrada principal do sistema.
"""

import sys
from pathlib import Path

# Adicionar src ao path
sys.path.insert(0, str(Path(__file__).parent))

from src.interface.cli.app import main

if __name__ == "__main__":
    main()