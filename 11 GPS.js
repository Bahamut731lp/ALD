const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
});

const mesta = ["liberec", "ceska-lipa", "chrastava", "new-york", "turnov", "jablonec-nad-nisou"];

const dojezd = [
    [0, 999, 12, 24, 22, 20],
    [999, 0, 40, 10, 52, 999],
    [12, 40, 0, 20, 999, 999],
    [24, 10, 20, 0, 15, 30],
    [22, 52, 999, 15, 0, 22],
    [20, 999, 999, 30, 22, 0]
];

const vzdalenost = [
    [0, 999, 10, 35, 26, 20],
    [999, 0, 47, 30, 67, 999],
    [10, 47, 0, 14, 999, 999],
    [35, 30, 14, 0, 40, 30],
    [26, 67, 999, 40, 0, 24],
    [20, 999, 999, 30, 24, 0]
];

// Nemáme operator overloading Sadge.
const add = (a, b) => Math.min(a, b);
const multiply = (a, b) => a + b;

// Násobení matic
const getMatrixProduct = (A, B) => {
    const P =  JSON.parse(JSON.stringify(A));

    const Q = A.map((row, i) =>
        B[0].map((_, j) =>
            {
                let t = row.reduce((acc, _, n) => {
                    if (!Array.isArray(P[i][j])) P[i][j] = [];
            
                    let product = multiply(A[i][n], B[n][j]);
                    let sum = add(acc, product);

                    if (acc != sum) P[i][j] = [...new Set([mesta[i], mesta[n], mesta[j]]).values()]
    
                    return sum;
                }, Infinity);

                return t;
            }
        )
    )

    return [Q, P];
}

const [dojezdVypocet, dojezdTrasa] = getMatrixProduct(dojezd, dojezd);
const [vzdalenostVypocet, vzdalenostTrasa] = getMatrixProduct(vzdalenost, vzdalenost);

const getDistanceForPath = (path) => {
    let sum = 0;

    for (let index = 1; index < path.length; index++) {
        sum += vzdalenost[mesta.indexOf(path[index - 1])][mesta.indexOf(path[index])];
    }

    return sum;
}

const getTimeForPath = (path) => {
    let sum = 0;

    for (let index = 1; index < path.length; index++) {
        const el = dojezd[mesta.indexOf(path[index - 1])][mesta.indexOf(path[index])];
        sum = sum + el;
    }

    return sum;
}

rl.on('line', (line) => {
    let [start, destination, mode] = line.trim().toLowerCase().split(/\s+/);

    const startIndex = mesta.indexOf(start);
    const endIndex = mesta.indexOf(destination);

    let vzdalenost_trasy = vzdalenostVypocet[startIndex][endIndex];
    let dojezd_trasy = dojezdVypocet[startIndex][endIndex];

    if (mode == "nejkratsi") {
        dojezd_trasy = getTimeForPath(vzdalenostTrasa[startIndex][endIndex]);
    }
    else {
        vzdalenost_trasy = getDistanceForPath(dojezdTrasa[startIndex][endIndex]);    
    }
    
    console.log("(%s min, %s km)", dojezd_trasy, vzdalenost_trasy, (mode == "nejkratsi" ? vzdalenostTrasa : dojezdTrasa)[startIndex][endIndex].join(" -> "));
});



//rl.on("close", output);

process.on("SIGINT", () => {
    output();
    process.exit();
});