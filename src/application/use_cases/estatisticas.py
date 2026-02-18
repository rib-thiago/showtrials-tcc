# src/application/use_cases/estatisticas.py
"""
Caso de uso: Obter estatísticas do acervo.
"""

from collections import Counter

from src.application.dtos.estatisticas_dto import EstatisticasDTO
from src.domain.interfaces.repositories import RepositorioDocumento
from src.domain.value_objects.nome_russo import NomeRusso


class ObterEstatisticas:
    """
    Caso de uso para gerar estatísticas completas.
    """

    def __init__(self, repo: RepositorioDocumento):
        self.repo = repo

    def executar(self) -> EstatisticasDTO:
        """
        Calcula estatísticas baseadas em todos os documentos.
        """
        # Buscar todos os documentos (limitado para performance)
        documentos = self.repo.listar(limite=5000)

        # Inicializar contadores
        centro_counter = Counter()
        tipo_counter = Counter()
        pessoa_counter = Counter()

        # Métricas especiais
        cartas = 0
        declaracoes = 0
        relatorios = 0
        acareacoes = 0
        acusacoes = 0
        laudos = 0
        anexos = 0

        # Processar documentos
        for doc in documentos:
            # Por centro
            centro_counter[doc.centro] += 1

            # Por tipo
            if doc.tipo:
                tipo_counter[doc.tipo] += 1

                # Contagens específicas
                if doc.tipo == "carta":
                    cartas += 1
                elif doc.tipo == "declaracao":
                    declaracoes += 1
                elif doc.tipo == "relatorio":
                    relatorios += 1
                elif doc.tipo == "acareacao":
                    acareacoes += 1
                elif doc.tipo == "acusacao":
                    acusacoes += 1
                elif doc.tipo == "laudo":
                    laudos += 1

            # Pessoas
            if doc.pessoa_principal:
                pessoa_counter[doc.pessoa_principal] += 1

            # Anexos
            if doc.tem_anexos:
                anexos += 1

        # Pessoas mais frequentes (com tradução)
        pessoas_frequentes = []
        for nome, count in pessoa_counter.most_common(15):
            try:
                nome_en = NomeRusso(nome).transliterar()
            except Exception:
                nome_en = nome
            pessoas_frequentes.append((nome, count, nome_en))

        # Traduções (mock por enquanto - será integrado depois)
        traducoes_por_idioma = {"en": 0, "pt": 0}

        return EstatisticasDTO(
            total_documentos=len(documentos),
            total_traducoes=0,  # Será implementado
            documentos_por_centro=dict(centro_counter),
            documentos_por_tipo=dict(tipo_counter),
            traducoes_por_idioma=traducoes_por_idioma,
            pessoas_frequentes=pessoas_frequentes,
            cartas=cartas,
            declaracoes=declaracoes,
            relatorios=relatorios,
            acareacoes=acareacoes,
            acusacoes=acusacoes,
            laudos=laudos,
            documentos_com_anexos=anexos,
            custo_total_traducoes=0.0,  # Será implementado
        )
