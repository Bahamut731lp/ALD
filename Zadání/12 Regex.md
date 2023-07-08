Vaším cílem je si vyzkoušet regulární výrazy na html výstupu. Vhodnější by bylo použít nějaký HTML parser, ale soubor bohužel neobsahuje validní HTML kód a nelze jej použít. Naštěstí regulární výrazy budou pořád fungovat. Na vstupu je html soubor (téměř 2 tisíce řádků), který obsahuje ve výsledku soupisku studentů z předmětu NTI/ALD.

Va výstupu se očekává výpis všech studentů, roztříděných to skupin na základě jejich oboru (AVI, AI, IS, IT). Uvnitř skupiny jsou studenti řazeny vzestupně numericky dle jejich osobního čísla (bez prvního písmene), nejprve budou lichá čísla, poté sudá čísla.

_Pozn:. některá osobní čísla byla trochu pozměněna_

__Formát jednoho řádku je pak následující:
__
```
<pořadové číslo>: <první písmeno oč> <PŘÍJMENÍ> <Jméno> <obor> <zbytek oč>
```

## Ukázka výstupu
```
AI:
 1: M STARKOV Mikhail    AI  20000007
 2: M ELCHANINOV Fedor   AI  20000011
 3: M TASHCHILIN Nikita  AI  20000019
...
20: M CAMBOR Miroslav    AI  20000204
21: M NAJMAN Karel       AI  20000218

AVI:
 1: M HIMMEL Jan         AVI 19000131
 2: M LISKOVA Sarka      AVI 20000152
...

IT:
 1: M KOCOVA Zuzana      IT  21000089
 2: Z VONDRA Daniel      IT  21000217
```

_Pozn.: tři tečky ukazují pouze to, že byla pro ilustraci vynechána část výstupu_