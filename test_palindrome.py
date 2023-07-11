import palindrome

def test_trivial():
    """
        Triviální případ ze zadání
    """
    original = """Kajak
koleno"""
    vzor = """ano
ne"""

    vysledek = palindrome.main(original.strip().splitlines())

    assert vzor == vysledek

def test_case_1():
    """
        Testovací případ 1
    """
    original = """Jelen
Kajak
anna"""
    vzor = """ne
ano
ano"""

    vysledek = palindrome.main(original.strip().splitlines())

    assert vzor == vysledek
