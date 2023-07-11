"""
    Skript pro úlohu 6 z ALD
    @author matej.hampl
    @refactor kevin.danek
"""
import sys
import string


class Block:
    """
        Třída reprezentující položku v zásobníku
    """

    def __init__(self, content: str = None, next_item = None):
        self._str = content
        self._next = next_item

    @property
    def content(self):
        """Setter pro str

        Returns:
            str: Obsah bloku
        """
        return self._str

    @property
    def next(self):
        """Setter pro další blok

        Returns:
            Block: Reference na další blok v seznamu
        """
        return self._next


class LIFO:
    """
        Třída reprezentující zásobník
    """
    def __init__(self, top: Block = None):
        self.top = top

    def push(self, content: str):
        """Metoda pro přidání položky na vrchol zásobníku

        Args:
            str (str): Položka na přidání
        """
        self.top = Block(content, self.top)

    def pop(self) -> str:
        """Metoda pro odstranění vrcholu zásobníku

        Returns:
            str: Vrchol zásobníku
        """
        if self.top is None:
            return "LIFO is empty"

        temp = self.top.content
        self.top = self.top.next
        return temp

    def is_empty(self) -> bool:
        """Metoda zjištující prázdnost zásobníku

        Returns:
            bool: Zda-li je zásobník prázdný
        """
        return self.top is None

    def print(self):
        """Funkce pro vytištění zásobníku
        """
        result = ""

        while not self.is_empty():
            result += self.pop()
            result += "\n"

        return result.strip()

def main(input_str: list[str]):
    """Metoda vykonávající hlavní funkci programu

    Args:
        input_str (str): Vstup z testu

    Returns:
        str: Výsledek
    """

    my_list = LIFO()

    for line_str in input_str:
        my_list.push(string.capwords(line_str, sep=None))

    return my_list.print()

if __name__ == "__main__":
    lines = []

    for line in sys.stdin:
        lines.append(line)

    print(main(lines))
