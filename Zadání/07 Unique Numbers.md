Vaším úkolem je napsat program, který na vstupu očekává n řádků, na každém řádku se vyskytují celá čísla oddělená čárkou.

Vaším úkolem je nalézt:

1. všechna čísla (bez opakování) a vypsat je na výstup (v pořadí, v jakém se vyskytují oddělená čárkou), řádek začíná `all`:
2. všechna čísla, která se vyskytují více než jednou a vypsat je na výstup (v pořadí, v jakém se vyskytují oddělená čárkou), řádek začíná `>1x`:
3. všechna čísla, která se vyskytují právě jednou a vypsat je na výstup (v pořadí, v jakém se vyskytují oddělená čárkou), řádek začíná `=1x`:

## Ukázka vstupu
```
1,2,38,4,5,6,7,8,9,10
1,2,3
4,5,6,0,2
```

## Ukázka výstupu
```
all: 1,2,38,4,5,6,7,8,9,10,3,0
>1x: 1,2,4,5,6
=1x: 38,7,8,9,10,3,0
```