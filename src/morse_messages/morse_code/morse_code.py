# ###########################################################
# International Morse Code
# 1. The length of a dot is one unit.
# 2. A dash is three units.
# 3. The space between parts of the same letter is one unit.
# 4. The space between letters is three units.
# 5. The space between words is seven units.
# ###########################################################
from abc import ABC, abstractmethod
from typing import Dict


class MorseCode(ABC):
    @abstractmethod
    def code(self) -> Dict[str, tuple[int, ...]]:
        return {}

    @abstractmethod
    def unit(self) -> int:
        return 0

    @abstractmethod
    def dot(self) -> int:
        return 0

    @abstractmethod
    def dash(self) -> int:
        return 0


class InternationalMorseCode(MorseCode):
    UNIT: int = 1
    DOT = 1 * UNIT
    DASH = 3 * UNIT
    LETTER_PART_SPACING = 1 * UNIT
    LETTER_SPACING = 3 * UNIT
    WORD_SPACING = 7 * UNIT

    CODE: Dict[str, tuple[int, ...]] = {
        "A": (DOT, DASH),
    }
