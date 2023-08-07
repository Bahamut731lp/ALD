"""
    Skript pro úlohu 10 z ALD
    @author kevin.danek
"""
import sys

BCD = [
    "1111110",
    "0110000",
    "1101101",
    "1111001",
    "0110011",
    "1011011",
    "1011111",
    "1110000",
    "1111111",
    "1111011"
]

LOOKUP = dict([(value, key) for (key, value) in list(enumerate(BCD))])

def extract_clock_data(clock: str):
    """Funkce pro rozdělení stringu hodin na label a čas

    Args:
        clock (str): _description_

    Returns:
        _type_: _description_
    """
    return tuple(clock.split(":", 1))


def parse_clocks(input_clocks: list[str]):
    """Funkce pro parsování hodin

    Args:
        input_clocks (list[str]): _description_
    """

    test = [extract_clock_data(x) for x in input_clocks]
    
    
    print(test)

def main(input_string: list[str]):
    """Funkce vykonávající program

    Args:
        input_string (str): vstup z konzole
    """

    results = []
    buffer = []

    for line in input_string:
        print(line)
        if line in ["-", "---"]:
            results.append(parse_clocks(buffer))
            buffer = []

        buffer.append(line)

    if len(buffer) == 3:
        results.append(parse_clocks(buffer))


if __name__ == "__main__":
    # lines = []

    # for line in sys.stdin:
    #     lines.append(line)
    #     break

    main("""clock-1: 06:45:30
clock-2: 00:45:45
clock-3: 03:00:00
---""".splitlines())
