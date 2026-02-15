# src/tests/test_use_cases.py
"""
Testes para os casos de uso da camada Application.
"""

import pytest
from datetime import datetime
from unittest.mock import Mock, MagicMock
from src.domain.entities.documento import Documento
from src.application.use_cases.classificar_documento import ClassificarDocumento
from src.application.use_cases.listar_documentos import ListarDocumentos
from src.application.use_cases.obter_documento import ObterDocumento
from src.application.use_cases.estatisticas import ObterEstatisticas


class TestClassificarDocumento:
    """Testes para o caso de uso ClassificarDocumento."""
    
    def test_classificar_interrogatorio(self):
        # Mock do repositório
        mock_repo = Mock()
        
        # Documento de teste
        doc = Documento(
            id=1,
            centro='lencenter',
            titulo='Протокол допроса Л.В. Николаева',
            url='http://teste.com',
            texto='...',
            data_coleta=datetime.now()
        )
        
        mock_repo.buscar_por_id.return_value = doc
        
        # Executar caso de uso
        caso_uso = ClassificarDocumento(mock_repo)
        resultado = caso_uso.executar(1)
        
        # Verificações
        assert resultado.tipo == 'interrogatorio'
        assert resultado.tipo_descricao == 'Protocolo de Interrogatório'
        assert resultado.pessoa_principal == 'Л.В. Николаева'
        mock_repo.salvar.assert_called_once()
    
    def test_documento_nao_encontrado(self):
        mock_repo = Mock()
        mock_repo.buscar_por_id.return_value = None
        
        caso_uso = ClassificarDocumento(mock_repo)
        resultado = caso_uso.executar(999)
        
        assert resultado is None
        mock_repo.salvar.assert_not_called()


class TestListarDocumentos:
    """Testes para o caso de uso ListarDocumentos."""
    
    def test_listar_com_paginacao(self):
        mock_repo = Mock()
        
        # Mock de documentos
        docs = [
            Documento(
                id=i,
                centro='lencenter',
                titulo=f'Documento {i}',
                url='http://teste.com',
                texto='...',
                data_coleta=datetime.now()
            ) for i in range(1, 6)
        ]
        
        mock_repo.listar.return_value = docs
        mock_repo.contar.return_value = 50
        
        caso_uso = ListarDocumentos(mock_repo)
        resultado = caso_uso.executar(pagina=2, limite=5)
        
        # Verificações
        assert len(resultado['items']) == 5
        assert resultado['total'] == 50
        assert resultado['pagina'] == 2
        assert resultado['total_paginas'] == 10
        
        # Verificar chamadas
        mock_repo.listar.assert_called_with(
            offset=5, limite=5, centro=None, tipo=None
        )


class TestObterDocumento:
    """Testes para o caso de uso ObterDocumento."""
    
    def test_obter_documento_completo(self):
        mock_repo = Mock()
        
        doc = Documento(
            id=1,
            centro='lencenter',
            titulo='Протокол допроса Л.В. Николаева',
            url='http://teste.com',
            texto='Texto longo...',
            data_coleta=datetime.now(),
            tipo='interrogatorio',
            tipo_descricao='Protocolo de Interrogatório',
            pessoa_principal='Л.В. Николаева'
        )
        
        mock_repo.buscar_por_id.return_value = doc
        
        caso_uso = ObterDocumento(mock_repo)
        dto = caso_uso.executar(1)
        
        assert dto.id == 1
        assert dto.titulo == 'Протокол допроса Л.В. Николаева'
        assert dto.tipo == 'interrogatorio'
        assert dto.tamanho_caracteres == len('Texto longo...')