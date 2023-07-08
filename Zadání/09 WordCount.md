Vaším úkolem je napsat program, který ze vstupu určí četnost a frekvenci [slov](http://www.writewords.org.uk/word_count.asp) a [frází](http://www.writewords.org.uk/phrase_count.asp).

Na vstupu je text, který obsahuje pouze znaky a-z, A-Z, mezery a \n (tj. nový řádek).

## Ukázka vstupu
```
Frequency

Frequency is the number of occurrences of a 
repeating event per unit of time
It is also referred to as temporal frequency
which emphasizes the contrast to spatial frequency
 and angular frequency

The period is the duration of time of one
cycle in a repeating event so the period
is the reciprocal of the frequency
```

## Ukázka výstupu
```
Word Frequency:
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
 - per unit             1.79% (1)
```

# Formátování výstupu
Výstup je formátovaný a to následovně:

- frekvence slov (15 nejfrekventovanějších)
    - slovo doplněné o mezery (celkem 12 znaků) + mezera
mezera
    - frekvence v procentech (zaukrouhleno na 2 desetinná místa)
mezera
    - počet výskytů (uzávorkováno)

- frekvence frází (15 nejfrekventovanějších):
    - stejný formát jako u frekvence slov, bude doplňeno na 20 znaků (+ mezera)

pokud mají slova (případně fráze) stejný počet výskytů, jejich pořadí bude určené prvním výskytem daného slova (fráze).

tj.: například fráze `frequency frequency` a `frequency is` mají jeden výskyt, ale `frequency frequency` se na vstupu vyskytla jako první.

__Využijte__ formatovacích řetězců:

- Java: String.format("...", )
- Python: "...".format nebo f"{}"
- C#: $"...",
- C/C++: printf("...", )

__Využijte__ slovníků.