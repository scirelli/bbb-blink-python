# ###########################################################
# International Morse Code
# 1. The length of a dot is one unit.
# 2. A dash is three units.
# 3. The space between parts of the same letter is one unit.
# 4. The space between letters is three units.
# 5. The space between words is seven units.
# ###########################################################
from dataclasses import dataclass, field
from typing import Tuple


@dataclass(frozen=True)
class Timing:
    dot: int
    dash: int
    letter_part_spacing: int
    letter_spacing: int
    word_spacing: int


@dataclass(frozen=True)
class MorseCode:
    """
    Codes should list numbers first then alphabet
    """

    code: Tuple[str, ...] = field(default_factory=tuple)
    time: Timing = field(default_factory=lambda: Timing(0, 0, 0, 0, 0))

    def encode_char(self, c: str) -> str:
        """
        Will raise on str length if empty str provided
        Will raise if c is not alpha numeric
        """
        c = c[0].upper()

        # numbers ...
        if c >= "0" and c <= "9":
            return self.code[ord(c) - ord("0")]

        # letters
        return self.code[ord(c) - ord("A") + 10]


internationalMorseCode = MorseCode(
    time=Timing(dot=1, dash=3, letter_part_spacing=1, letter_spacing=3, word_spacing=7),
    code=(
        "-----",  # 0
        ".----",  # 1
        "..---",
        "...--",
        "....-",
        ".....",
        "-....",
        "--...",
        "---..",
        "----.",
        ".-",  # "A"
        "-...",
        "-.-.",
        "-..",
        ".",
        "..-.",
        "--.",
        "....",
        "..",
        ".---",
        "-.-",
        ".-..",
        "--",
        "-.",
        "---",
        ".--.",
        "--.-",
        ".-.",
        "...",
        "-",
        "..-",
        "...-",
        ".--",
        "-..-",
        "-.--",
        "--..",  # Z
    ),
)
