#!/usr/bin/python3
from morse_code_writer.string_writer import StringMorseLEDWriter
from morse_messages.morse_code.morse_code import internationalMorseCode

w = StringMorseLEDWriter("P9_14", internationalMorseCode)


def main(arg: str = "Hello world") -> None:
    print(f"Echo: {arg}")
    print(w.write(bytearray(arg, encoding="utf-8")))


if __name__ == "__main__":
    import argparse
    from sys import stdin

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--file",
        default=stdin,
        type=argparse.FileType("r"),
        nargs="?",
        help="",
    )

    args = parser.parse_args()
    for line in args.file.readlines():
        if "Exit" == line.rstrip():
            break
        main(line.strip())
