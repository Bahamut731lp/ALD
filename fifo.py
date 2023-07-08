"""
    Skript pro úlohu 5 z ALD
"""
import sys
import string

class Item:
    """Třída realizující frontu
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class FIFO:
    """
        Třída realizující frontu
    """

    def __init__(self):
        self.head = None
        self.prev = None

    def add(self, item):
        """Funkce pro přidání položky do fronty

        Args:
            item (Item): Instance třídy Item, která reprezentuje položku fronty
        """
        temp = Item(item)
        if self.head is None:
            self.head = temp
            self.prev = temp

        self.prev.next = temp
        self.prev = self.prev.next

    def print(self):
        """Funkce pro vytištění seznamu na standardní výstup
        """
        result = ""

        while self.head is not None:
            result += self.head.data
            result += "\n"
            self.head = self.head.next
            #print(self.head.data)
        return result.strip()

def main(input_str: list[str]):
    """Metoda vykonávající hlavní funkci programu

    Args:
        input (str): Vstup z testu

    Returns:
        str: Výsledek
    """

    my_list = FIFO()

    for line in input_str:
        my_list.add(string.capwords(line, sep=None))

    return my_list.print()

if __name__ == "__main__":
    print(main(["Pro apliakci zásobník", "toto je ukázka vstupu"]))
