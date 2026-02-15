# src/infrastructure/persistence/sqlite_repository.py
"""
Implementação concreta do repositório usando SQLite.
"""

import sqlite3
from typing import List, Optional
from contextlib import contextmanager
from datetime import datetime

from src.domain.entities.documento import Documento
from src.domain.interfaces.repositories import RepositorioDocumento
from src.infrastructure.config.settings import settings
from src.infrastructure.persistence.models import DocumentoModel


class SQLiteDocumentoRepository(RepositorioDocumento):
    """
    Repositório SQLite para documentos.
    Implementa a interface definida no domínio.
    """
    
    def __init__(self, db_path: Optional[str] = None):
        self.db_path = db_path or str(settings.DB_PATH)
    
    @contextmanager
    def _conexao(self):
        """Gerenciador de contexto para conexões SQLite."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Retorna dicionários
        try:
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()
    
# CORREÇÃO: substituir row.get() por verificação com 'in'

    def _row_para_entidade(self, row: sqlite3.Row) -> Documento:
        """Converte linha do banco para entidade Documento.
        
        NOTA: sqlite3.Row não tem método .get()
        Usamos 'if coluna in row.keys()' para verificar existência.
        """
        # Verificar quais colunas existem
        colunas = row.keys()
        
        modelo = DocumentoModel(
            id=row['id'],
            centro=row['centro'],
            titulo=row['titulo'],
            data_original=row['data_original'] if 'data_original' in colunas else None,
            url=row['url'],
            texto=row['texto'],
            data_coleta=row['data_coleta'],
            tipo_documento=row['tipo_documento'] if 'tipo_documento' in colunas else None,
            tipo_descricao=row['tipo_descricao'] if 'tipo_descricao' in colunas else None,
            pessoa_principal=row['pessoa_principal'] if 'pessoa_principal' in colunas else None,
            remetente=row['remetente'] if 'remetente' in colunas else None,
            destinatario=row['destinatario'] if 'destinatario' in colunas else None,
            envolvidos=row['envolvidos'] if 'envolvidos' in colunas else None,
            tem_anexos=row['tem_anexos'] if 'tem_anexos' in colunas else 0
        )
        return modelo.para_entidade()

    def salvar(self, documento: Documento) -> int:
        """
        Insere ou atualiza um documento.
        
        Args:
            documento: Entidade Documento
            
        Returns:
            int: ID do documento salvo
        """
        modelo = DocumentoModel.de_entidade(documento)
        
        with self._conexao() as conn:
            cursor = conn.cursor()
            
            if documento.id:  # Update
                cursor.execute("""
                    UPDATE documentos SET
                        centro = ?,
                        titulo = ?,
                        data_original = ?,
                        url = ?,
                        texto = ?,
                        data_coleta = ?,
                        tipo_documento = ?,
                        tipo_descricao = ?,
                        pessoa_principal = ?,
                        remetente = ?,
                        destinatario = ?,
                        envolvidos = ?,
                        tem_anexos = ?
                    WHERE id = ?
                """, (
                    modelo.centro,
                    modelo.titulo,
                    modelo.data_original,
                    modelo.url,
                    modelo.texto,
                    modelo.data_coleta,
                    modelo.tipo_documento,
                    modelo.tipo_descricao,
                    modelo.pessoa_principal,
                    modelo.remetente,
                    modelo.destinatario,
                    modelo.envolvidos,
                    modelo.tem_anexos,
                    modelo.id
                ))
                return documento.id
            else:  # Insert
                cursor.execute("""
                    INSERT INTO documentos (
                        centro, titulo, data_original, url, texto, data_coleta,
                        tipo_documento, tipo_descricao, pessoa_principal, remetente,
                        destinatario, envolvidos, tem_anexos
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    modelo.centro,
                    modelo.titulo,
                    modelo.data_original,
                    modelo.url,
                    modelo.texto,
                    modelo.data_coleta,
                    modelo.tipo_documento,
                    modelo.tipo_descricao,
                    modelo.pessoa_principal,
                    modelo.remetente,
                    modelo.destinatario,
                    modelo.envolvidos,
                    modelo.tem_anexos
                ))
                return cursor.lastrowid
    
    def buscar_por_id(self, id: int) -> Optional[Documento]:
        """Busca documento pelo ID."""
        with self._conexao() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM documentos WHERE id = ?", (id,))
            row = cursor.fetchone()
            
            if not row:
                return None
            
            return self._row_para_entidade(row)
    
    def listar(self, 
               offset: int = 0, 
               limite: int = 20,
               centro: Optional[str] = None,
               tipo: Optional[str] = None) -> List[Documento]:
        """Lista documentos com filtros."""
        with self._conexao() as conn:
            cursor = conn.cursor()
            
            query = "SELECT * FROM documentos WHERE 1=1"
            params = []
            
            if centro:
                query += " AND centro = ?"
                params.append(centro)
            
            if tipo:
                query += " AND tipo_documento = ?"
                params.append(tipo)
            
            query += " ORDER BY id LIMIT ? OFFSET ?"
            params.extend([limite, offset])
            
            cursor.execute(query, params)
            rows = cursor.fetchall()
            
            return [self._row_para_entidade(row) for row in rows]
    
    def contar(self, 
               centro: Optional[str] = None,
               tipo: Optional[str] = None) -> int:
        """Conta documentos com filtros."""
        with self._conexao() as conn:
            cursor = conn.cursor()
            
            query = "SELECT COUNT(*) FROM documentos WHERE 1=1"
            params = []
            
            if centro:
                query += " AND centro = ?"
                params.append(centro)
            
            if tipo:
                query += " AND tipo_documento = ?"
                params.append(tipo)
            
            cursor.execute(query, params)
            return cursor.fetchone()[0]
    
    def remover(self, id: int) -> bool:
        """Remove um documento pelo ID."""
        with self._conexao() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM documentos WHERE id = ?", (id,))
            return cursor.rowcount > 0
    
    def listar_traducoes(self, documento_id: int) -> List[dict]:
        """Lista traduções de um documento."""
        with self._conexao() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT idioma, data_traducao, modelo, custo
                FROM traducoes
                WHERE documento_id = ?
                ORDER BY idioma
            """, (documento_id,))
            
            rows = cursor.fetchall()
            return [
                {
                    'idioma': row[0],
                    'data_traducao': row[1],
                    'modelo': row[2],
                    'custo': row[3]
                }
                for row in rows
            ]