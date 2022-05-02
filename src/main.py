#!/usr/bin/python3
from morse_code_writer.string_writer import StringMorseLEDWriter
from morse_messages.morse_code.morse_code import internationalMorseCode


def main() -> None:
    w = StringMorseLEDWriter("P9_14", internationalMorseCode)
    print(w.write(bytearray("Hello world", encoding="utf-8")))


if __name__ == "__main__":
    main()
