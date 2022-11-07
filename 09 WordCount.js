const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
});

const lines = [];
const words = new Map();
const phrases = new Map();

const add = (dict, word) => dict.set(word, (dict.get(word) ?? 0) + 1);

const processLines = () => {
    let all = lines.flat();
    console.log(all, all.length);

    all.forEach((word) => add(words, word));
    for (let index = 1; index <= all.length; index++) add(phrases, [all[index - 1], all[index]].join(" "));
}

const format = (header, map) => {
    const output = [header];
    const indent = " - ";
    const entries = [...map.entries()];
    const count = entries.reduce((acc, v) => acc + v[1], 0);
    const numberToBePrinted = Math.min(entries.length, 15);
    const wordLength = Math.max(...entries.map(v => v[0].length));

    console.log(count);

    entries
        //Seřazení podle počtu výskytů
        //a i b jsou ve tvaru [key, value]
        .sort((a, b) => b[1] - a[1])
        //Použil jsem entry, protože ten se v moment, co se vrátí false, přeruší
        //Je to efektivně jako break; ve for-loopu
        //for-each by musel běžet na prázdno, což není úplně cool.
        .every(([key, value], index) => {
            if (index > (numberToBePrinted - 1)) return false;

            const line = [indent];
            line.push(String(key).padEnd(wordLength));
            line.push(Number(100 * value / count).toFixed(2) + "%");
            line.push(`(${value})`);

            output.push(line.join(" "));
            return true;
        })

    console.log(output.join("\n"));
}

const output = () => {
    processLines();
    format("Word Frequency:", words);
    format("Phrase Frequency:", phrases);
    process.exit();
}

rl.on('line', (line) => {
    if (!line) return;

    let wordsInLine = line.trim().split(/\W+/g).map(v => v.toLowerCase());
    lines.push(wordsInLine);
});

rl.on("close", output);
process.on("SIGINT", output);

/*
Frequency

Frequency is the number of occurrences of a 
repeating event per unit of time
It is also referred to as temporal frequency
which emphasizes the contrast to spatial frequency and angular frequency

The period is the duration of time of one
cycle in a repeating event so the period
is the reciprocal of the frequency
*/