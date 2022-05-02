from __future__ import annotations

import time
from abc import ABC, abstractmethod

import Adafruit_BBIO.GPIO as GPIO  # type: ignore

from morse_messages.morse_code.morse_code import MorseCode


class Reader(ABC):
    @abstractmethod
    def read(self, p: bytearray) -> int:
        pass


# Imcomplete
class MorseCodeReader(Reader):
    HIGH = b"\x01"
    LOW = b"\x00"

    def __init__(self, language: MorseCode, message: str):
        self.language = language
        self.message = ""
        self.FLAG = {
            ".": bytearray(self.HIGH + (self.language.time.dot).to_bytes(1, "big")),
            "-": bytearray(self.HIGH + self.language.time.dash.to_bytes(1, "big")),
            "p": bytearray(self.LOW + self.language.time.dash.to_bytes(1, "big")),
        }

        self.set_message(message)

    def set_message(self, message: str) -> MorseCodeReader:
        self.message = message.upper()
        return self

    def read(self, p: bytearray) -> int:
        for c in self.message:
            if c >= "A" and c <= "Z" or c >= "0" and c <= "9":
                morse_chars = self.language.encode_char(c)
                for morse_char in morse_chars:
                    p.extend(self.FLAG[morse_char])
            else:  # " "
                p.extend(self.FLAG[morse_char])

        return 0


class Writer(ABC):
    @abstractmethod
    def write(self, p: bytearray) -> int:
        pass


class LEDWriter_old(Writer):
    TIME_UNIT_SEC = 1 / 10

    """
    Takes a bytearray of command "words" (two bytes) which are groups of on/off flag and a delay.
    The flag sets the pin HIGH or LOW
    The delay keeps pin at that level for that time before reading next command.
    """

    def __init__(self, pin: str):
        self.pin = pin

    def write(self, p: bytearray) -> int:
        index = 0
        while index < len(p) - 1:
            toggle, delay = p[index : index + 2]
            toggle = GPIO.HIGH if toggle else GPIO.LOW
            GPIO.output(self.pin, toggle)
            time.sleep(delay * self.TIME_UNIT_SEC)
        return 0


class StringMorseLEDWriter(Writer):
    TIME_UNIT_SEC = 1 / 10

    """
    Takes a bytearray of strings and writes them to an LED at pin "pin" in morse code
    """

    def __init__(self, pin: str, language: MorseCode):
        self.pin = pin
        GPIO.setup(pin, GPIO.OUT)
        self.language = language

    def write(self, p: bytearray) -> int:
        bytecount = 0
        for char in p.decode().strip().upper():
            if char >= "A" and char <= "Z" or char >= "0" and char <= "9":
                bytecount += 1
                self._write_letter(char)
                self.sleep(
                    self.language.time.letter_spacing
                    - self.language.time.letter_part_spacing
                )
            else:
                bytecount += 1
                GPIO.output(self.pin, GPIO.LOW)
                self.sleep(
                    self.language.time.word_spacing - self.language.time.letter_spacing
                )
        return bytecount

    def _write_letter(self, char: str) -> None:
        letter = self.language.encode_char(char)
        for mchar in letter:
            d = self.language.time.dot if letter == "." else self.language.time.dash
            GPIO.output(self.pin, GPIO.HIGH)
            self.sleep(d)
            GPIO.output(self.pin, GPIO.LOW)
            self.sleep(self.language.time.letter_part_spacing)

    def sleep(self, t: int) -> None:
        time.sleep(t * self.TIME_UNIT_SEC)
