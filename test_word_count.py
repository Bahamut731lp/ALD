import word_count

def test_trivial():
    """
        Test trivial
    """
    
    original = """Frequency

Frequency is the number of occurrences of a 
repeating event per unit of time
It is also referred to as temporal frequency
which emphasizes the contrast to spatial frequency
 and angular frequency

The period is the duration of time of one
cycle in a repeating event so the period
is the reciprocal of the frequency"""

    vzor = """Word Frequency:
 - the          12.50% (7)
 - frequency    10.71% (6)
 - of           10.71% (6)
 - is           7.14% (4)
 - a            3.57% (2)
 - repeating    3.57% (2)
 - event        3.57% (2)
 - time         3.57% (2)
 - to           3.57% (2)
 - period       3.57% (2)
 - number       1.79% (1)
 - occurrences  1.79% (1)
 - per          1.79% (1)
 - unit         1.79% (1)
 - it           1.79% (1)
Phrase Frequency:
 - is the               5.36% (3)
 - a repeating          3.57% (2)
 - repeating event      3.57% (2)
 - of time              3.57% (2)
 - the period           3.57% (2)
 - period is            3.57% (2)
 - frequency frequency  1.79% (1)
 - frequency is         1.79% (1)
 - the number           1.79% (1)
 - number of            1.79% (1)
 - of occurrences       1.79% (1)
 - occurrences of       1.79% (1)
 - of a                 1.79% (1)
 - event per            1.79% (1)
 - per unit             1.79% (1)"""

    vysledek = word_count.main(original.strip().splitlines())

    assert vzor == vysledek

def test_case_1():
    """
        Test case 1
    """

    with open("word_count/test_1.txt", encoding="utf-8") as file_handle:
        original = file_handle.read()

    with open("word_count/test_1_result.txt", encoding="utf-8") as file_handle:
        vzor = file_handle.read()
        
    vysledek = word_count.main(original.strip().splitlines())

    assert vzor == vysledek
    

def test_case_2():
    """
        Test case 2
    """

    with open("word_count/test_2.txt", encoding="utf-8") as file_handle:
        original = file_handle.read()

    with open("word_count/test_2_result.txt", encoding="utf-8") as file_handle:
        vzor = file_handle.read()
        
    vysledek = word_count.main(original.strip().splitlines())

    assert vzor == vysledek
    

def test_case_3():
    """
        Test case 3
    """

    with open("word_count/test_3.txt", encoding="utf-8") as file_handle:
        original = file_handle.read()

    with open("word_count/test_3_result.txt", encoding="utf-8") as file_handle:
        vzor = file_handle.read()
        
    vysledek = word_count.main(original.strip().splitlines())

    assert vzor == vysledek
    

def test_case_4():
    """
        Test case 4
    """

    with open("word_count/test_4.txt", encoding="utf-8") as file_handle:
        original = file_handle.read()

    with open("word_count/test_4_result.txt", encoding="utf-8") as file_handle:
        vzor = file_handle.read()
        
    vysledek = word_count.main(original.strip().splitlines())

    assert vzor == vysledek