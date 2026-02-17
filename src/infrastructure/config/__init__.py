# src/infrastructure/config.py
"""
Configuração de serviços da aplicação.
Suporte a carregamento de YAML/JSON e variáveis de ambiente.
"""

import os
import json
from pathlib import Path
from typing import Dict, Any, Optional
from dataclasses import dataclass, field, asdict
import yaml
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()


@dataclass
class ServiceConfig:
    """Configuração de um serviço individual."""
    enabled: bool = True
    lazy: bool = True
    singleton: bool = True
    options: Dict[str, Any] = field(default_factory=dict)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ServiceConfig':
        """Cria configuração a partir de dicionário."""
        return cls(
            enabled=data.get('enabled', True),
            lazy=data.get('lazy', True),
            singleton=data.get('singleton', True),
            options=data.get('options', {})
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """Converte para dicionário."""
        return {
            'enabled': self.enabled,
            'lazy': self.lazy,
            'singleton': self.singleton,
            'options': self.options
        }


@dataclass
class ApplicationConfig:
    """Configuração completa da aplicação."""
    services: Dict[str, ServiceConfig] = field(default_factory=dict)
    environment: str = "development"
    debug: bool = False
    data_dir: Path = Path("data")
    export_dir: Path = Path("exportados")
    reports_dir: Path = Path("relatorios")
    analysis_dir: Path = Path("analises")
    
    def __post_init__(self):
        """Cria diretórios se não existirem."""
        for dir_path in [self.data_dir, self.export_dir, self.reports_dir, self.analysis_dir]:
            dir_path.mkdir(exist_ok=True)
    
    @classmethod
    def from_file(cls, path: Optional[Path] = None) -> 'ApplicationConfig':
        """
        Carrega configuração de arquivo YAML/JSON.
        
        Args:
            path: Caminho do arquivo (opcional)
        
        Returns:
            ApplicationConfig com configurações carregadas
        """
        # Configuração padrão
        config = cls()
        
        if not path or not path.exists():
            # Cria config padrão se não existir
            config.create_default_config(path)
            return config
        
        # Carrega baseado na extensão
        with open(path, 'r', encoding='utf-8') as f:
            if path.suffix in ['.yaml', '.yml']:
                data = yaml.safe_load(f)
            elif path.suffix == '.json':
                data = json.load(f)
            else:
                raise ValueError(f"Formato não suportado: {path.suffix}")
        
        # Aplica configurações
        if 'environment' in data:
            config.environment = data['environment']
        if 'debug' in data:
            config.debug = data['debug']
        
        # Carrega serviços
        if 'services' in data:
            for name, svc_data in data['services'].items():
                config.services[name] = ServiceConfig.from_dict(svc_data)
        
        return config
    
    def create_default_config(self, path: Optional[Path] = None) -> None:
        """Cria arquivo de configuração padrão."""
        # Configuração padrão dos serviços
        self.services = {
            'translator': ServiceConfig(
                enabled=True,
                lazy=True,
                options={
                    'api_key_required': True,
                    'default_target': 'en',
                    'timeout': 30
                }
            ),
            'spacy': ServiceConfig(
                enabled=True,
                lazy=True,
                options={
                    'models': {
                        'ru': 'ru_core_news_sm',
                        'en': 'en_core_web_sm'
                    },
                    'preload': [],  # modelos a carregar na inicialização
                    'auto_download': False
                }
            ),
            'wordcloud': ServiceConfig(
                enabled=True,
                lazy=True,
                options={
                    'default_size': [800, 400],
                    'max_words': 200,
                    'background_color': 'white'
                }
            ),
            'pdf_exporter': ServiceConfig(
                enabled=False,  # desabilitado por padrão
                lazy=True,
                options={
                    'template_dir': 'templates/pdf'
                }
            )
        }
        
        # Salva se path fornecido
        if path:
            data = {
                'environment': self.environment,
                'debug': self.debug,
                'services': {
                    name: svc.to_dict() for name, svc in self.services.items()
                }
            }
            
            path.parent.mkdir(exist_ok=True)
            with open(path, 'w', encoding='utf-8') as f:
                if path.suffix in ['.yaml', '.yml']:
                    yaml.dump(data, f, default_flow_style=False, allow_unicode=True)
                else:
                    json.dump(data, f, indent=2, ensure_ascii=False)
            
            logger.info(f"✅ Arquivo de configuração criado: {path}")
    
    def is_enabled(self, service: str) -> bool:
        """Verifica se serviço está habilitado."""
        return self.services.get(service, ServiceConfig()).enabled
    
    def is_lazy(self, service: str) -> bool:
        """Verifica se serviço é lazy."""
        return self.services.get(service, ServiceConfig()).lazy
    
    def get_options(self, service: str) -> Dict[str, Any]:
        """Retorna opções de um serviço."""
        return self.services.get(service, ServiceConfig()).options


# Instância global de configuração (será sobrescrita na inicialização)
config = ApplicationConfig()


# Configura logger
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)