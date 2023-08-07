"""
    Skript pro úlohu 1 z ALD
    @author kevin.danek
"""
import sys

def main(input_string: str):
    """Funkce vykonávající program

    Args:
        input_string (str): vstup z konzole
    """

    number_of_lines = int(input_string.strip())
    return "\n".join(["Hello world!"] * number_of_lines)


if __name__ == "__main__":
    lines = []

    for line in sys.stdin:
        lines.append(line)
        break

    print(main(lines[0]))
