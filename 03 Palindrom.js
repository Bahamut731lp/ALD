const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
});

const jePalindrom = (line) => line.toLowerCase().split("").reduce((acc, element, index, arr) => {
    if (acc != null && !acc) return acc;
    return element == arr[arr.length - 1 - index]
}, null);

rl.on('line', line => {
    console.log(jePalindrom(line) ? "ano" : "ne");
})