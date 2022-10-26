const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
});

const numbers = [];

const getUniqueNumbers = (map) => [...map.keys()];
const getDuplicitNumbers = (map) => [...map.entries()].filter(([_, value]) => value > 1).map(([key, _]) => key);
const getNonDuplicitNumbers = (map) => [...map.entries()].filter(([_, value]) => value == 1).map(([key, _]) => key);

const printAllNumbers = () => {
    const frequencies = new Map();

    for (const number of numbers) {
        if (!frequencies.has(number)) frequencies.set(number, 0);
        frequencies.get(number);
        frequencies.set(number, frequencies.get(number) + 1);
    }

    const uniques = getUniqueNumbers(frequencies);
    const duplicits = getDuplicitNumbers(frequencies);
    const nonduplicits = getNonDuplicitNumbers(frequencies);

    console.log(`all: ${uniques.join()}`);
    console.log(`>1x: ${duplicits.join()}`);
    console.log(`=1x: ${nonduplicits.join()}`);
}

rl.on('line', line => {
    if (!line) return printAllNumbers();

    let input = line
        .split(",")
        .map(v => parseInt(v));

    numbers.push(...input);
});

rl.on("close", () => {
    printAllNumbers();
});