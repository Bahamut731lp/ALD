import hello_world

def test_case_trivial():
    """
        Triviální případ ze zadání
    """
    original = "2"
    vzor = """Hello world!
Hello world!"""

    vysledek = hello_world.main(original)

    assert vzor == vysledek

def test_case_1():
    """
        Testovací případ 1
    """
    original = "1"
    vzor = """Hello world!"""

    vysledek = hello_world.main(original)

    assert vzor == vysledek

def test_case_2():
    """
        Testovací případ 2
    """
    original = "3"
    vzor = """Hello world!
Hello world!
Hello world!"""

    vysledek = hello_world.main(original)

    assert vzor == vysledek

def test_case_3():
    """
        Testovací případ 3
    """
    original = "12"
    vzor = """Hello world!
Hello world!
Hello world!
Hello world!
Hello world!
Hello world!
Hello world!
Hello world!
Hello world!
Hello world!
Hello world!
Hello world!"""

    vysledek = hello_world.main(original)

    assert vzor == vysledek