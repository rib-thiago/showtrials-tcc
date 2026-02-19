# src/domain/value_objects/nome_russo.py
"""
Value Object: NomeRusso
Representa nomes russos no formato "Л.В. Николаева" com telemetria.
"""

import re
from typing import Dict, Tuple

# Telemetria opcional
_telemetry = None


def _monitor(name=None):
    """Decorator dummy que não faz nada."""

    def decorator(func):
        return func

    return decorator


def configure_telemetry(telemetry_instance=None, monitor_decorator=None):
    """Configura telemetria para este módulo (usado apenas em testes)."""
    global _telemetry, _monitor
    _telemetry = telemetry_instance
    if monitor_decorator:
        _monitor = monitor_decorator


class NomeRusso:
    """
    Value Object imutável para nomes russos.

    Exemplos válidos:
    - Л.В. Николаева
    - Г.Г. Ягоды
    - И.В. Сталину
    """

    # Tabela de transliteração GOST 7.79-2000
    TRANSLIT_MAP: Dict[str, str] = {
        "А": "A",
        "Б": "B",
        "В": "V",
        "Г": "G",
        "Д": "D",
        "Е": "E",
        "Ё": "Yo",
        "Ж": "Zh",
        "З": "Z",
        "И": "I",
        "Й": "Y",
        "К": "K",
        "Л": "L",
        "М": "M",
        "Н": "N",
        "О": "O",
        "П": "P",
        "Р": "R",
        "С": "S",
        "Т": "T",
        "У": "U",
        "Ф": "F",
        "Х": "Kh",
        "Ц": "Ts",
        "Ч": "Ch",
        "Ш": "Sh",
        "Щ": "Shch",
        "Ъ": "",
        "Ы": "Y",
        "Ь": "",
        "Э": "E",
        "Ю": "Yu",
        "Я": "Ya",
        # minúsculas
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
        "ё": "yo",
        "ж": "zh",
        "з": "z",
        "и": "i",
        "й": "y",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "kh",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ъ": "",
        "ы": "y",
        "ь": "",
        "э": "e",
        "ю": "yu",
        "я": "ya",
    }

    # Exceções conhecidas (nomes que fogem do padrão)
    EXCECOES: Dict[str, str] = {
        "И.В. Сталину": "Joseph V. Stalin",
        "И.В. Сталин": "Joseph V. Stalin",
        "Л.Б. Каменева": "Lev B. Kamenev",
        "Л.Б. Каменев": "Lev B. Kamenev",
        "Г.Е. Зиновьева": "Grigory E. Zinoviev",
        "Г.Е. Зиновьев": "Grigory E. Zinoviev",
        "Г.Г. Ягоды": "Genrikh G. Yagoda",
        "Г.Г. Ягода": "Genrikh G. Yagoda",
        "Л.В. Николаева": "Leonid V. Nikolaev",
        "Л.В. Николаев": "Leonid V. Nikolaev",
    }

    # Terminações femininas
    TERMINACOES_FEMININAS = ("а", "я")

    def __init__(self, nome_completo: str):
        """
        Inicializa um nome russo.

        Args:
            nome_completo: String no formato "Л.В. Николаева"

        Raises:
            ValueError: Se o formato for inválido
        """
        # Normalizar espaços (remover extras, manter um espaço entre partes)
        self._original = " ".join(nome_completo.split())

        if not self._validar_formato():
            if _telemetry:
                _telemetry.increment("nome_russo.formato_invalido")
            raise ValueError(f"Formato de nome russo inválido: {nome_completo}")

        self._iniciais, self._sobrenome = self._extrair_partes()

        if _telemetry:
            _telemetry.increment("nome_russo.criado")

    def _validar_formato(self) -> bool:
        """Valida se o nome está no formato correto."""
        # Padrão: Letra.Inicial. Letra.Inicial. Sobrenome
        padrao = r"^[А-Я]\. ?[А-Я]\. [А-Я][а-я]+$"
        return bool(re.match(padrao, self._original))

    def _extrair_partes(self) -> Tuple[str, str]:
        """Separa iniciais do sobrenome."""
        partes = self._original.split(" ")
        if len(partes) == 2:
            return partes[0], partes[1]
        return self._original, ""

    @property
    def original(self) -> str:
        """Nome original em russo."""
        return self._original

    @property
    def iniciais(self) -> str:
        """Iniciais (ex: 'Л.В.')."""
        return self._iniciais

    @property
    def sobrenome(self) -> str:
        """Sobrenome em russo."""
        return self._sobrenome

    @property
    def genero(self) -> str:
        """Detecta o gênero baseado na terminação."""
        if self._sobrenome.endswith(self.TERMINACOES_FEMININAS):
            return "feminino"
        return "masculino"

    @property
    def sobrenome_base(self) -> str:
        """
        Remove declinação russa (genitivo → nominativo) para nomes masculinos.
        Para nomes femininos, mantém a forma original.
        Ex: 'Николаева' (feminino) → 'Николаева'
            'Николаев' (masculino) → 'Николаев'
        """
        # Se o nome inteiro é uma exceção, retorna o sobrenome original
        if self._original in self.EXCECOES:
            return self._sobrenome

        # Para nomes masculinos, remove terminações de caso genitivo
        if self.genero == "masculino" and self._sobrenome.endswith(("а", "у")):
            return self._sobrenome[:-1]

        # Para femininos, mantém como está
        return self._sobrenome

    @_monitor("nome_russo.transliterar")
    def transliterar(self) -> str:
        """
        Converte para inglês usando GOST 7.79-2000.
        Primeiro verifica exceções, depois aplica regras.
        """
        # 1. Verificar exceções
        if self._original in self.EXCECOES:
            if _telemetry:
                _telemetry.increment("nome_russo.transliterado.excecao")
            return self.EXCECOES[self._original]

        # 2. Aplicar transliteração ao sobrenome base
        sobrenome_en = []
        for char in self.sobrenome_base:
            if char in self.TRANSLIT_MAP:
                sobrenome_en.append(self.TRANSLIT_MAP[char])
            else:
                sobrenome_en.append(char)

        # Capitalizar
        sobrenome_str = "".join(sobrenome_en)
        if sobrenome_str:
            sobrenome_str = sobrenome_str[0].upper() + sobrenome_str[1:]

        if _telemetry:
            _telemetry.increment("nome_russo.transliterado.regra")

        return f"{self._iniciais} {sobrenome_str}"

    def __eq__(self, other) -> bool:
        """Dois nomes são iguais se o original russo for igual."""
        if not isinstance(other, NomeRusso):
            return False
        return self._original == other._original

    def __str__(self) -> str:
        return self._original

    def __repr__(self) -> str:
        return f"<NomeRusso: {self._original}>"
