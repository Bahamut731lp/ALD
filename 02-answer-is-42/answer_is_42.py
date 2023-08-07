"""
    Skript pro úlohu 2 z ALD
    @author kevin.danek
"""
import sys

def main(input_string: list[str]):
    """Funkce vykonávající program

    Args:
        input_string (str): vstup z konzole
    """

    try:
        answer_index = input_string.index("42")
    except ValueError:
        answer_index = len(input_string)

    return "\n".join(input_string[0:answer_index])


if __name__ == "__main__":
    lines = []

    for line in sys.stdin:
        lines.append(line)

    print(main(lines))
