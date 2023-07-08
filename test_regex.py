import regex

def test_output():
    """
        Test, zda výsledek funkce odpovídá zadání z e-learningu
    """
    vzor = """AI:
 1: M STARKOV Mikhail    AI  20000007
 2: M ELCHANINOV Fedor   AI  20000011
 3: M TASHCHILIN Nikita  AI  20000019
 4: M KINDERMANN Jakub   AI  20000037
 5: M HRUSKA Bohumil     AI  20000059
 6: M HUMPL Vojtech      AI  20000061
 7: M JANSA David        AI  20000063
 8: M PRYJMAK Jaroslav   AI  20000071
 9: M SRNKOVA Viktorie   AI  20000075
10: X VOLEMAN Vojtech    AI  20000081
11: M EFIMOV Nikita      AI  20000010
12: M FEDOROV Zakhar     AI  20000012
13: M STANKOV Vladimir   AI  20000018
14: M BALIK David        AI  20000032
15: M HOLUBIK Michal     AI  20000036
16: M VESELY Martin      AI  20000050
17: M CHAROUZD Filip     AI  20000062
18: M PECHOUT Matej      AI  20000068
19: M SOUREK Filip       AI  20000076
20: M CAMBOR Miroslav    AI  20000204
21: M NAJMAN Karel       AI  20000218
AVI:
 1: M HIMMEL Jan         AVI 19000131
 2: M LISKOVA Sarka      AVI 20000152
IS:
 1: M KORNER Jaroslav    IS  20000041
 2: M ROSOVA Anastazie   IS  20000045
 3: M GLENDA Filip       IS  20000056
 4: M PODAVKA Jan        IS  20000070
 5: M SERGEEVA Viktoriia IS  20000072
 6: M PESULA Filip       IS  20000222
IT:
 1: M KOCOVA Zuzana      IT  21000089
 2: Z VONDRA Daniel      IT  21000217"""

    vysledek = regex.main()
    assert vzor == vysledek
