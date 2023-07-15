"""
    Skript pro úlohu 9 z ALD
    @author matej.hampl
    @refactor kevin.danek
"""
import sys
import re
from collections import Counter

def main(input_lines: list[str]):
    """Hlavní funkce programu

    Args:
        input_lines (list[str]): Vstupní řádky
    """

    string = "\n".join(input_lines)
    words = word_count(string)
    phrase = phrase_count(string)
    total_words = words.total()
    total_phrases = phrase.total() + 1
    result = []

    result.append("Word Frequency:")
    for item in words.most_common(15):
        result.append(f" - {item[0]:12} {(item[1]/total_words)*100:2.2f}% ({item[1]})")

    result.append("Phrase Frequency:")
    for item in phrase.most_common(15):
        result.append(
            f" - {item[0]:20} {(item[1]/total_phrases)*100:2.2f}% ({item[1]})")

    return "\n".join(result)

def word_count(input_string: str):
    """Funkce pro vytvoření slovníku se slovy

    Args:
        input_string (str): _description_

    Returns:
        _type_: _description_
    """
    input_string = input_string.lower()
    words = re.split(r"[\b\W\b]+", input_string)

    return Counter(words)


def phrase_count(input_string: str):
    """Funkce pro vytvoření slovníku s frázemi

    Args:
        input_string (str): Vstupní řetězec, ze kterého se počítají fráze

    Returns:
        dict: Slovník s frázemi
    """
    input_string = input_string.lower()
    words = re.split(r"[\b\W\b]+", input_string)
    phrases = [' '.join([words[i-1], words[i]]) for i in range(1, len(words))]

    return Counter(phrases)


if __name__ == "__main__":
    contents = []
    for line in sys.stdin:
        contents.append(line)
