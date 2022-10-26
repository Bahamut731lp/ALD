const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
});

class Entry {
    data = null;
    previous = null;

    constructor(data, previous) {
        this.data = data;
        this.previous = previous;
    }
}

class LIFO {
    top = null;
    count = 0;

    push(data) {
        this.top = new Entry(data, this.peek());
        this.count++;
    }

    pop() {
        let current = this.top;
        this.top = current.previous;

        if (current != null) this.count--;

        return current.data;
    }

    peek() {
        return this.top;
    }

    isEmpty() {
        return this.count == 0;
    }
}


const vety = new LIFO();
const capitalize = (string) => string.split(/\s/).map((slovo) => (slovo.charAt(0).toUpperCase() + slovo.slice(1))).join(" ");
const vypisVety = () => {
    while (!vety.isEmpty()) console.log(capitalize(vety.pop()))
};


rl.on('line', line => {
    if (!line) return vypisVety();

    vety.push(line);
});

rl.on("close", () => {
    vypisVety();
});