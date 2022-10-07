/*
    Komentář autora:
    Při psaní tohodle kódu jsem to ztratil.
*/

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
});

// Polyfill
Array.prototype.at = function(n) {
    // ToInteger() abstract op
    n = Math.trunc(n) || 0;
    // Allow negative indexing from the end
    if (n < 0) n += this.length;
    // OOB access is guaranteed to return undefined
    if (n < 0 || n >= this.length) return undefined;
    // Otherwise, this is just normal property access
    return this[n];
}

const jePalindrom = (line) => String(line).toLowerCase().split("").every((el, index, list) => el == list.at(list.length - 1 - index));
const zkontrolujPrenos = (array) => array.slice().map((num, index, list) => num > 9 ? (num -= 10, list[index + 1] += 1, num) : num);

rl.on('line', line => {
    if (Number(line) < 0) process.exit(0);

    let cislo = line.split("").map(v => Number(v));

    // Pokud dojde k přetečení do dalšího řádu, tak to uděláme rovnou
    // Taky pokud je input palindromem, tak ho musíme vychýlit, abychom mohli hledat další palindrom.
    // Tou druhou podmínkou se nám kryje i případ toho, kdy je inputem jenom jedna cifra.
    if (cislo.every(cifra => cifra == "9")) cislo = (+(cislo.join("")) + 1 + "").split("");

    const pulka = Math.floor(cislo.length / 2);
    const offset = cislo.length % 2;

    let levaPolovina = cislo.slice(0, pulka);
    let pravaPolovina = cislo.slice(pulka + offset);
    let prostredek = offset > 0 ? Number(cislo[pulka]) : "";
    let naive = +[...levaPolovina, prostredek, ...levaPolovina.slice().reverse()].join("");

    if (jePalindrom(cislo.join("")) || ((levaPolovina.join("") - pravaPolovina.join("")) < 0)) {
        if (prostredek !== "") prostredek += 1;
        else {
            let max = Math.max(levaPolovina.at(-1), pravaPolovina.at(0));
            levaPolovina.splice(-1, 1, max);
            pravaPolovina.splice(0, 1, max);
        };
    }

    pravaPolovina = levaPolovina.slice().reverse();

    //Kontrola přenosů do vyšších řádů
    //Levá se musí reversovat, protože kontrola probíhá zprava do leva, ale v levé polovině potřebuje jít přenos zleva do prava.
    levaPolovina = zkontrolujPrenos(levaPolovina.reverse()).reverse();
    pravaPolovina = zkontrolujPrenos(pravaPolovina);
  
    let vysledek = [...levaPolovina, prostredek, ...pravaPolovina].join("");
    let num = cislo.join("");

    if ((vysledek - num) < 0) {
        let dodatek = +(+!offset + "" + Math.pow(10, pulka - +!offset));
        vysledek = String(+vysledek + dodatek);
    }

    let naiveDiff = naive - cislo.join("");
    let mirrorDiff = vysledek - cislo.join("");

    if (+num + naiveDiff <= num) {
        naiveDiff = Infinity;

        if (prostredek !== "") prostredek += 1;
        else {
            let max = Math.max(levaPolovina.at(-1), pravaPolovina.at(0)) + 1;
            levaPolovina.splice(-1, 1, max);
            pravaPolovina.splice(0, 1, max);
        };
    }

    if (mirrorDiff == 0) return console.log(vysledek);
    console.log(+num + Math.min(naiveDiff, mirrorDiff));
})