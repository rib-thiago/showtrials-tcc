# src/domain/entities/documento.py
"""
Módulo: Documento
Entidade principal do sistema, representa um documento histórico.

Regras de negócio:
- Um documento tem título, texto, data de coleta
- Pode ser classificado por tipo (interrogatório, carta, etc)
- Pode ter pessoas envolvidas (réu, remetente, destinatário)
- O tamanho do texto é uma propriedade derivada
"""

from dataclasses import dataclass, field
from typing import Optional, List
from datetime import datetime
import re


@dataclass
class Documento:
    """
    Representa um documento histórico coletado.
    
    Attributes:
        id: Identificador único (None se não persistido)
        centro: Centro de origem ('lencenter' ou 'moscenter')
        titulo: Título original em russo
        data_original: Data do documento no formato original
        url: URL de origem
        texto: Conteúdo textual completo
        data_coleta: Timestamp da coleta
        
        # Metadados enriquecidos (opcionais)
        tipo: Tipo do documento (interrogatorio, carta, etc)
        tipo_descricao: Descrição amigável do tipo
        pessoa_principal: Pessoa focal do documento (réu, autor)
        remetente: Quem enviou (para cartas/relatórios)
        destinatario: Quem recebeu (para cartas/relatórios)
        envolvidos: Lista de pessoas envolvidas (acareações)
        tem_anexos: Se o documento possui anexos
    """
    
    # Atributos obrigatórios
    centro: str
    titulo: str
    url: str
    texto: str
    data_coleta: datetime
    
    # Atributos opcionais com valores padrão
    id: Optional[int] = None
    data_original: Optional[str] = None
    
    # Metadados enriquecidos (todos opcionais)
    tipo: Optional[str] = None
    tipo_descricao: Optional[str] = None
    pessoa_principal: Optional[str] = None
    remetente: Optional[str] = None
    destinatario: Optional[str] = None
    envolvidos: Optional[List[str]] = field(default_factory=list)
    tem_anexos: bool = False
    
    def __post_init__(self):
        """Validações após inicialização"""
        if self.centro not in ['lencenter', 'moscenter']:
            raise ValueError(f"Centro inválido: {self.centro}")
        
        if not self.titulo:
            raise ValueError("Título não pode ser vazio")
        
        if not self.url:
            raise ValueError("URL não pode ser vazia")
    
    @property
    def tamanho_caracteres(self) -> int:
        """
        Retorna o tamanho do texto em caracteres.
        Propriedade derivada (não armazenada).
        """
        return len(self.texto)
    
    @property
    def tamanho_palavras(self) -> int:
        """
        Retorna o número aproximado de palavras.
        Útil para estatísticas.
        """
        return len(self.texto.split())
    
    @property
    def resumo(self) -> str:
        """
        Resumo do documento para exibição rápida.
        """
        tipo_str = f" [{self.tipo_descricao}]" if self.tipo_descricao else ""
        pessoa_str = f" - {self.pessoa_principal}" if self.pessoa_principal else ""
        return f"{self.titulo[:50]}{tipo_str}{pessoa_str}"
    
    def extrair_pessoas_do_titulo(self) -> List[str]:
        """
        Extrai nomes no formato russo (Л.В. Николаева) do título.
        Regra de negócio: nomes russos seguem padrão de iniciais + sobrenome.
        """
        if not self.titulo:
            return []
        
        # Padrão: Letra.Inicial. Letra.Inicial. Sobrenome
        padrao = r'([А-Я]\. ?[А-Я]\. [А-Я][а-я]+)'
        return re.findall(padrao, self.titulo)
    
    def to_dict(self) -> dict:
        """
        Converte para dicionário (útil para serialização).
        """
        return {
            'id': self.id,
            'centro': self.centro,
            'titulo': self.titulo,
            'data_original': self.data_original,
            'url': self.url,
            'texto': self.texto,
            'data_coleta': self.data_coleta.isoformat() if self.data_coleta else None,
            'tipo': self.tipo,
            'tipo_descricao': self.tipo_descricao,
            'pessoa_principal': self.pessoa_principal,
            'remetente': self.remetente,
            'destinatario': self.destinatario,
            'envolvidos': self.envolvidos,
            'tem_anexos': self.tem_anexos,
            'tamanho': self.tamanho_caracteres
        }
    
    @classmethod
    def from_dict(cls, dados: dict) -> 'Documento':
        """
        Cria documento a partir de dicionário.
        """
        # Converte string ISO para datetime se necessário
        if isinstance(dados.get('data_coleta'), str):
            from datetime import datetime
            dados['data_coleta'] = datetime.fromisoformat(dados['data_coleta'])
        
        return cls(**dados)