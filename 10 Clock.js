const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
});

/*
      |             0
    -   -   ->   3     1
      |             2
*/

//Funkce
const createSegment = () => Array.from({ length: 7 }, (value) => value ?? 0);
const rotationOfMinutes = (value) => value * 12 / 180;
const rotationOfHours = (value) => (value * 60 / 180) % 4;
const pipe = (...fns) => (x) => fns.reduce((res, fn) => fn(res), x);
const pad = (array, length = 4) => Array.from({ ...array, length }, (value) => value ?? null);
const extract = (line) => Array.from({ ...line.split(":"), length: 4 }, (value) => value ?? null).map(v => Number(v?.match(/\d+/)?.[0]));
const translate = ([clock, hours, minutes, seconds]) => [clock, rotationOfHours(hours), rotationOfMinutes(minutes), rotationOfMinutes(seconds)];
const bitwiseOR = (a, b) => a.map((v, i) => +v | +b[i]);

//Pole držící všechny inputy od uživatele
const clocks = [createSegment()];

//Konfigurace hodin, resp. které hodiny rozsvěcí co
const clockzones = [
    [3, 2, null, null, null, null, null],
    [null, null, 0, 3, null, null, null],
    [null, null, null, null, 2, 0, 1]
];

//Reverse lookup tabulka ve tvaru (bin. číslo) -> (dekadické)
//Vytvořená z pole binárních reprezentací rozsvícených displejů
//Generuje to basically dekadický dekodér
const lookup = Object.fromEntries([...
    [
        0b1111110,
        0b0110000,
        0b1101101,
        0b1111001,
        0b0110011,
        0b1011011,
        0b1011111,
        0b1110000,
        0b1111111,
        0b1111011
    ].entries()
].map(([key, value]) => [value, key]));

//Funkce pro tisknutí výstupu
const output = () => {
    let result = clocks
        .map((value) => parseInt(+value.join(""), 2))
        .map((value) => lookup[value] ?? "")
        .join("");

    console.log(result);
}

rl.on('line', (line) => {
    if (!line || line == "-") clocks.push(createSegment());
    if (line === "---") rl.close();

    const [clock, ...time] = pipe(extract, pad, translate)(line);

    if (clockzones[clock - 1] == undefined) return;

    const litSegmentsByThisClock = clockzones[clock - 1].map(v => v != null ? +time.includes(v) : 0);
    clocks[clocks.length - 1] = bitwiseOR(clocks[clocks.length - 1], litSegmentsByThisClock);
});

rl.on("close", output);

process.on("SIGINT", () => {
    output();
    process.exit();
});