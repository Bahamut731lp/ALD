"""
    Skript pro úlohu 3 z ALD
    @author matej.hampl
    @refactor kevin.danek
"""
import sys
from typing import Union


def is_palindrome(number: Union[str, int, float]):
    """Funkce pro zjištění palindromičnosti vstupu

    Args:
        number (Union[str, int, float]): Vstup

    Returns:
        _type_: Zda-li je vstup palindrom
    """
    return str(number).lower() == str(number).lower()[::-1]


def main(input_lines: list[str]):
    """Hlavní tělo programu

    Args:
        input_lines (list[str]): Vstupní řádky

    Returns:
        str: Výstupní řetězec
    """
    answers = {
        True: "ano",
        False: "ne"
    }

    return "\n".join([answers[is_palindrome(x)] for x in input_lines])

if __name__ == "__main__":
    lines = []

    for line in sys.stdin:
        lines.append(line)

    print(main(lines))
