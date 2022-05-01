# type: ignore
# pylint: disable = too-many-arguments
import pytest

from morse_messages.morse_code.morse_code import internationalMorseCode


@pytest.mark.parametrize(
    ("character", "code"),
    (
        ("A", ".-"),
        ("B", "-..."),
        ("z", "--.."),
        ("0", "-----"),
        ("9", "----."),
    ),
)
def test_MorseCode_encode_char(character, code):
    assert internationalMorseCode.encode_char(character) == code
