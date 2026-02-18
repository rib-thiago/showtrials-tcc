# src/infrastructure/export/txt_exporter.py
"""
Exportador para formato TXT.
"""

from datetime import datetime
from pathlib import Path

from src.application.dtos.documento_dto import DocumentoDTO


class TxtExporter:
    """
    Exporta documentos para formato TXT.
    """

    def __init__(self, diretorio_base: str = "exportados"):
        self.diretorio_base = Path(diretorio_base)
        self.diretorio_base.mkdir(exist_ok=True)

    def _gerar_cabecalho(self, dto: DocumentoDTO) -> str:
        """
        Gera cabeçalho com metadados.
        """
        linhas = []
        linhas.append("=" * 80)
        linhas.append(f"TÍTULO: {dto.titulo}")
        linhas.append(f"CENTRO: {dto.centro}")
        linhas.append(f"DATA ORIGINAL: {dto.data_original or 'Não informada'}")
        linhas.append(f"URL: {dto.url}")
        linhas.append(f"EXPORTADO EM: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        if dto.pessoa_principal:
            linhas.append(f"PESSOA PRINCIPAL: {dto.pessoa_principal}")
        if dto.remetente:
            linhas.append(f"REMETENTE: {dto.remetente}")
        if dto.destinatario:
            linhas.append(f"DESTINATÁRIO: {dto.destinatario}")
        if dto.envolvidos:
            linhas.append(f"ENVOLVIDOS: {', '.join(dto.envolvidos)}")

        linhas.append("=" * 80)
        linhas.append("")

        return "\n".join(linhas)

    def _gerar_nome_arquivo(self, dto: DocumentoDTO, idioma: str) -> str:
        """
        Gera nome do arquivo.
        """
        # Sanitizar título
        titulo = "".join(c for c in dto.titulo if c.isalnum() or c in (" ", "-", "_")).rstrip()
        titulo = titulo[:50]

        return f"{dto.id}_{titulo}_{idioma}.txt"

    def exportar(
        self, dto: DocumentoDTO, idioma: str = "original", incluir_metadados: bool = True
    ) -> Path:
        """
        Exporta documento para TXT.
        """
        nome_arquivo = self._gerar_nome_arquivo(dto, idioma)
        caminho = self.diretorio_base / nome_arquivo

        with open(caminho, "w", encoding="utf-8") as f:
            if incluir_metadados:
                f.write(self._gerar_cabecalho(dto))
            f.write(dto.texto)

        return caminho
