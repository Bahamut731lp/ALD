const readline = require('readline');
const Process = require("process");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
});

rl.on('line', line => {
    if (parseInt(line) == 42) Process.exit(0);
    console.log(line);
})
