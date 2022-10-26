const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
});

const numbers = [];

const getUniqueNumbers = (array) => [...new Set(array).values()];
const getDuplicitNumbers = (array) => [...new Set(array.filter((item, index) => index !== array.indexOf(item)).values())]
const getNonDuplicitNumbers = (array, duplicits) => array.filter(x => !duplicits.includes(x));

const printAllNumbers = () => {
    const frequencies = new Map();

    for (const number of numbers) {
        if (!frequencies.has(number)) frequencies.set(number, 0);
        frequencies.get(number);
        frequencies.set(number, frequencies.get(number) + 1);
    }

    console.log(frequencies);

    const uniques = [...frequencies.keys()];
    const duplicits = getDuplicitNumbers(numbers);
    const nonduplicits = getNonDuplicitNumbers(numbers, duplicits);

    console.log(`all: ${uniques.join()}`);
    console.log(`>1x: ${duplicits.sort((a, b) => a - b).join()}`);
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