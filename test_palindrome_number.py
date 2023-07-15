import palindrome_number

def test_case_1():
    """
        Testovací případ 1
    """
    original = """100
321
123421
1
999
-1"""
    vzor = """101
323
124421
2
1001"""

    vysledek = palindrome_number.main(original.strip().splitlines())

    assert vzor == vysledek

def test_case_2():
    """
        Testovací případ 2
    """
    original = """4456
89123
879
123469
7984
123
4123
786
1
71123
0
-1"""
    vzor = """4554
89198
888
124421
7997
131
4224
787
2
71217
1"""

    vysledek = palindrome_number.main(original.strip().splitlines())

    assert vzor == vysledek

def test_case_3():
    """
        Testovací případ 3
    """
    original = """123457719123
-1"""
    vzor = """123457754321"""

    vysledek = palindrome_number.main(original.strip().splitlines())

    assert vzor == vysledek
    
def test_case_4():
    """
        Testovací případ 4
    """
    original = """112233445566778899999999999999998877660000000000
-1"""
    vzor = """112233445566778899999999999999998877665544332211"""

    vysledek = palindrome_number.main(original.strip().splitlines())

    assert vzor == vysledek