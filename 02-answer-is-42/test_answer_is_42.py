import answer_is_42

def test_case_trivial():
    """
        Triviální případ ze zadání
    """
    original = """10
49
42
89
5"""

    vzor = """10
49"""

    vysledek = answer_is_42.main(original.splitlines())

    assert vzor == vysledek

def test_case_1():
    """
        Testovací případ 1
    """
    original = """10
15
46
42
16
48"""
    vzor = """10
15
46"""

    vysledek = answer_is_42.main(original.splitlines())

    assert vzor == vysledek

def test_case_2():
    """
        Testovací případ 2
    """
    original = """100
57
15
1
12
75
5
86
89
11
13
99
46
31
3
4
3
42
83
80
62
79
60
20
12
24
92
15
2
65
63
32
9
86
70
60
9
77
87
12
66
75
6
35
72
9
83
39
62
46"""

    vzor = """100
57
15
1
12
75
5
86
89
11
13
99
46
31
3
4
3"""

    vysledek = answer_is_42.main(original.splitlines())

    assert vzor == vysledek

def test_case_3_0():
    """
        Testovací případ 3.0
    """
    original = """60
72
36
12
82
46
21
42
14
100
42
37
53
8
41"""

    vzor = """60
72
36
12
82
46
21"""

    vysledek = answer_is_42.main(original.splitlines())

    assert vzor == vysledek

def test_case_3_1():
    """
        Testovací případ 3.1
    """
    original = """67
96
72
21
87
42
72
36
56
86
70
33
91
14
7"""

    vzor = """67
96
72
21
87"""

    vysledek = answer_is_42.main(original.splitlines())

    assert vzor == vysledek

def test_case_3_2():
    """
        Testovací případ 3.2
    """
    original = """42
97
16
40
16
96
82
78
16
97
58
34
6
8
42"""

    vzor = """"""

    vysledek = answer_is_42.main(original.splitlines())

    assert vzor == vysledek

def test_case_3_3():
    """
        Testovací případ 3.3
    """
    original = """84
42
76
67
17
11
11
89
33
11
92
100
89
68
37"""

    vzor = """84"""

    vysledek = answer_is_42.main(original.splitlines())

    assert vzor == vysledek

def test_case_3_4():
    """
        Testovací případ 3.4
    """
    original = """6
98
97
5
42
54
46
65
56
38
2
56
51
66
64"""

    vzor = """6
98
97
5"""

    vysledek = answer_is_42.main(original.splitlines())

    assert vzor == vysledek
