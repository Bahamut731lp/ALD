import readline from 'readline';

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
});

const jePalindrom = (line) => String(line)
.toLowerCase()
.split("")
.every((el, index, list) => el == list.at(list.length - 1 - index));

rl.on('line', line => {
    console.log(jePalindrom(line) ? "ano" : "ne");
})