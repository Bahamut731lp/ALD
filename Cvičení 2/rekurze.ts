const cache: { [key: number] : number } = {};
let i = 0;

function Fibonnaci(n: number): number {
    if (String(n) in cache) return cache[n];
    if (n == 0 || n == 1) return 1;
    
    const result = Fibonnaci(n - 1) + Fibonnaci(n - 2);
    cache[n] = result;
    i += 1;

    return result;
}

console.log(Fibonnaci(500));
//console.log(cache);