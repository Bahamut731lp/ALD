'''
Test suite pro úlohu 6
'''
import gps

def test_case_trivial_1():
    """
        Test triviálního případu ze zadání
    """
    original = """ceska-lipa chrastava nejkratsi"""

    vzor = """(30 min, 44 km) ceska-lipa -> new-york -> chrastava"""

    vysledek = gps.main(original.strip().splitlines())
    assert vzor == vysledek

def test_case_trivial_2():
    """
        Test triviálního případu ze zadání 2
    """
    original = """chrastava turnov nejlepsi"""

    vzor = """(34 min, 36 km) chrastava -> liberec -> turnov"""

    vysledek = gps.main(original.strip().splitlines())
    assert vzor == vysledek

def test_case_1():
    """
        Testovací případ 1
    """
    original = """new-york liberec nejlepsi"""

    vzor = """(24 min, 35 km) new-york -> liberec"""

    vysledek = gps.main(original.strip().splitlines())
    assert vzor == vysledek

def test_case_2():
    """
        Testovací případ 2
    """
    original = """new-york liberec nejlepsi
liberec jablonec-nad-nisou nejlepsi
jablonec-nad-nisou liberec nejlepsi"""

    vzor = """(24 min, 35 km) new-york -> liberec
(20 min, 20 km) liberec -> jablonec-nad-nisou
(20 min, 20 km) jablonec-nad-nisou -> liberec"""

    vysledek = gps.main(original.strip().splitlines())
    assert vzor == vysledek

def test_case_3_0():
    """
        Testovací případ 3.0
    """
    original = """new-york turnov nejkratsi
turnov jablonec-nad-nisou nejlepsi
chrastava jablonec-nad-nisou nejlepsi
ceska-lipa new-york nejlepsi
turnov chrastava nejkratsi"""

    vzor = """(15 min, 40 km) new-york -> turnov
(22 min, 24 km) turnov -> jablonec-nad-nisou
(32 min, 30 km) chrastava -> liberec -> jablonec-nad-nisou
(10 min, 30 km) ceska-lipa -> new-york
(34 min, 36 km) turnov -> liberec -> chrastava"""

    vysledek = gps.main(original.strip().splitlines())
    assert vzor == vysledek

def test_case_3_1():
    """
        Testovací případ 3.1
    """
    original = """jablonec-nad-nisou chrastava nejlepsi
ceska-lipa jablonec-nad-nisou nejlepsi
new-york jablonec-nad-nisou nejkratsi
ceska-lipa new-york nejlepsi
new-york liberec nejkratsi"""

    vzor = """(32 min, 30 km) jablonec-nad-nisou -> liberec -> chrastava
(40 min, 60 km) ceska-lipa -> new-york -> jablonec-nad-nisou
(30 min, 30 km) new-york -> jablonec-nad-nisou
(10 min, 30 km) ceska-lipa -> new-york
(32 min, 24 km) new-york -> chrastava -> liberec"""

    vysledek = gps.main(original.strip().splitlines())
    assert vzor == vysledek

def test_case_3_2():
    """
        Testovací případ 3.2
    """
    original = """liberec jablonec-nad-nisou nejlepsi
turnov liberec nejlepsi
jablonec-nad-nisou new-york nejkratsi
ceska-lipa jablonec-nad-nisou nejlepsi
jablonec-nad-nisou turnov nejlepsi"""

    vzor = """(20 min, 20 km) liberec -> jablonec-nad-nisou
(22 min, 26 km) turnov -> liberec
(30 min, 30 km) jablonec-nad-nisou -> new-york
(40 min, 60 km) ceska-lipa -> new-york -> jablonec-nad-nisou
(22 min, 24 km) jablonec-nad-nisou -> turnov"""

    vysledek = gps.main(original.strip().splitlines())
    assert vzor == vysledek
