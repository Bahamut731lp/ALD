"""
    Skript pro úlohu 4 z ALD
    @author matej.hampl
    @refactor kevin.danek
"""
import sys
from palindrome import is_palindrome

def get_palindrome_number(input_string: str):
    """Funkce pro nalezení nejbližšího palindromického čísla

    Args:
        input_string (str): Vstupní číslo

    Returns:
        int: Nejbližší palindromické číslo
    """

    cislo = int(input_string)

    if cislo == -1:
        return ""

    if is_palindrome(cislo):
        cislo += 1

    string_cislo = str(cislo)
    string_length = len(string_cislo)

    if cislo > 9:
        if string_length % 2 == 0:
            polovina1 = string_cislo[0:string_length//2]
            polovina2 = string_cislo[string_length//2:]
            delka = len(str(polovina2))
            mocnina = pow(10, delka)
            cislo2 = int(polovina1) * mocnina + int(polovina1[::-1])

            if cislo2 > cislo:
                cislo = cislo2

        else:
            polovina1 = string_cislo[0:(string_length//2+1)]
            polovina2 = string_cislo[(string_length//2+1):]
            delka = len(str(polovina2))
            mocnina = pow(10, delka)
            cislo2 = int(polovina1) * mocnina + int(polovina1[:-1][::-1])
            if cislo2 > cislo:
                cislo = cislo2

    while True:
        if is_palindrome(cislo):
            print(cislo)
            break
        cislo += 1

    return cislo

def main(input_lines: list[str]):
    """Hlavní tělo programu

    Args:
        input_lines (list[str]): Vstupní řádky

    Returns:
        str: Výstupní řetězec
    """

    return "\n".join([str(get_palindrome_number(x)) for x in input_lines]).strip()

if __name__ == "__main__":
    lines = []

    for line in sys.stdin:
        lines.append(line)

    print(main(lines))
