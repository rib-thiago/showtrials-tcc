# src/interface/web/__init__.py
"""
Web Interface - Adaptador FastAPI.
"""

from src.interface.web.app import create_app

__all__ = ["create_app"]
