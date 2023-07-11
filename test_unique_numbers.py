import unique_numbers

def test_case_trivial():
    """
        Test triviálního případu ze zadání
    """
    original = """1,2,38,4,5,6,7,8,9,10
1,2,3
4,5,6,0,2"""

    vzor = """all: 1,2,38,4,5,6,7,8,9,10,3,0
>1x: 1,2,4,5,6
=1x: 38,7,8,9,10,3,0"""

    vysledek = unique_numbers.main(original.strip().splitlines())
    assert vzor == vysledek

def test_case_1():
    """
    Test případu 1
    """
    original = """1,2,3,4,5,6,7,8,9,10
1,2,3
4,5,6,0,2"""

    vzor = """all: 1,2,3,4,5,6,7,8,9,10,0
>1x: 1,2,3,4,5,6
=1x: 7,8,9,10,0"""

    vysledek = unique_numbers.main(original.strip().splitlines())
    assert vzor == vysledek
    
def test_case_2_0():
    """
    Test případu 2.0
    """
    original = """7,3,3,3,3,0,2
5,4
4,1,3,1,0,8,0
4,8,2"""

    vzor = """all: 7,3,0,2,5,4,1,8
>1x: 3,0,2,4,1,8
=1x: 7,5"""

    vysledek = unique_numbers.main(original.strip().splitlines())
    assert vzor == vysledek
    
def test_case_2_1():
    """
    Test případu 2.1
    """
    original = """1,1,7,0
3,1,2,3,1
0,7,3,6,3,0,3
2,8,6,1,1,5,5"""

    vzor = """all: 1,7,0,3,2,6,8,5
>1x: 1,7,0,3,2,6,5
=1x: 8"""

    vysledek = unique_numbers.main(original.strip().splitlines())
    assert vzor == vysledek
    
def test_case_2_2():
    """
    Test případu 2.2
    """
    original = """6,7,5,2,4
1,4,1,8,1
7,2,5,5,6
8,7,0"""

    vzor = """all: 6,7,5,2,4,1,8,0
>1x: 6,7,5,2,4,1,8
=1x: 0"""

    vysledek = unique_numbers.main(original.strip().splitlines())
    assert vzor == vysledek
    
def test_case_2_3():
    """
    Test případu 2.3
    """
    original = """5,0,7,2,4,8
5,4,2,0,8,1
4,2
0,1,6,3,5,4"""

    vzor = """all: 5,0,7,2,4,8,1,6,3
>1x: 5,0,2,4,8,1
=1x: 7,6,3"""

    vysledek = unique_numbers.main(original.strip().splitlines())
    assert vzor == vysledek
    
def test_case_2_4():
    """
    Test případu 2.4
    """
    original = """2,1
0,3
5,3,0
7,2,2,2"""

    vzor = """all: 2,1,0,3,5,7
>1x: 2,0,3
=1x: 1,5,7"""

    vysledek = unique_numbers.main(original.strip().splitlines())
    assert vzor == vysledek
    
def test_case_3_0():
    """
    Test případu 3_0
    """
    original = """10,26,28,22,27,11
4,55,48,33
19,12,12
9,15,17,19,58,4,11,54
10,55,43,0,2
28,18,32,1,12,38
17,25,26,34,37
42,59,40,34,16,39,14
45,37,50,52,50,43,50,35
48
41
46,28,51,51,7,54
18
21
2,33,17
13,10,9,4,23
19,8
7,50
46,48
2,7,22
20,30,30,4,5,4,44
37,53,1,41
14,25,16
3,50,51
53,30,30,19
13,6,22
43,13,11,24,31,13,1,12
58,54,16,22,48
17,4,41,19
40"""

    vzor = """all: 10,26,28,22,27,11,4,55,48,33,19,12,9,15,17,58,54,43,0,2,18,32,1,38,25,34,37,42,59,40,16,39,14,45,50,52,35,41,46,51,7,21,13,23,8,20,30,5,44,53,3,6,24,31
>1x: 10,26,28,22,11,4,55,48,33,19,12,9,17,58,54,43,2,18,1,25,34,37,40,16,14,50,41,46,51,7,13,30,53
=1x: 27,15,0,32,38,42,59,39,45,52,35,21,23,8,20,5,44,3,6,24,31"""

    vysledek = unique_numbers.main(original.strip().splitlines())
    assert vzor == vysledek
    
def test_case_3_1():
    """
    Test případu 3_1
    """
    original = """11
19,29,45,13,43
24,55,40,3,32,33
53,59,15
37,17,31,48,50,31,4
4,41,38,44,42,35,16
20,35,5,8,23,30
7,47,37,9,40,39,37
20,57,15,34
6,13,43,28
17,21,19,43,16,23,60,27
4
52,16,22,44,55
60,46,11,59
12,34,58,3,10,32,46,9
55,32,23,35,5,53,17
55
26,59,23,50
50,42,31,39,57,10,54
60,39,49,9,18,39,2,4
2,52,4,28,48
32,30
32
11,13
48,51,16,7,20,8
37,35
13,57,20,31,36
28
47,32,34,30,27,50,17,54
14"""

    vzor = """all: 11,19,29,45,13,43,24,55,40,3,32,33,53,59,15,37,17,31,48,50,4,41,38,44,42,35,16,20,5,8,23,30,7,47,9,39,57,34,6,28,21,60,27,52,22,46,12,58,10,26,54,49,18,2,51,36,14
>1x: 11,19,13,43,55,40,3,32,53,59,15,37,17,31,48,50,4,44,42,35,16,20,5,8,23,30,7,47,9,39,57,34,28,60,27,52,46,10,54,2
=1x: 29,45,24,33,41,38,6,21,22,12,58,26,49,18,51,36,14"""

    vysledek = unique_numbers.main(original.strip().splitlines())
    assert vzor == vysledek
