const numberOfItems = 500;
const items = [...Array(numberOfItems).keys()];

const merge = (left: number[], right: number[]) => {
    const result: number[] = [];
    while (left.length || right.length) {
        if (left.length && right.length) {
            if (left[0] < right[0]) {
                result.push(left.shift() ?? 0);
            } else {
                result.push(right.shift() ?? 0);
            }
        } else if (left.length) {
            result.push(left.shift() ?? 0);
        } else {
            result.push(right.shift() ?? 0);
        }
    }
    return result;
};

const mergeSort = (arr: number[]): number[] => {
    arr = arr ?? [];
    if (arr.length <= 1) {
        return arr;
    }

    const pivot = arr.length / 2;
    const left = arr.slice(0, pivot);
    const right = arr.slice(pivot, arr.length);

    return merge(mergeSort(left), mergeSort(right));
};

// Přístup k prvku v poli
const Constant = () => {
    const _t = items[5];
};

// Hledání v poli
const Linear = () => {
    for (let index = 0; index < items.length; index++) {
        const _element = items[index];
    }
};

// Bisekce (Půlení intervalu)
const Logarithmic = () => {
    const x = items.slice(-1).pop() || numberOfItems;
    let start = 0, end = items.length - 1;

    // Iterate while start not meets end
    while (start <= end) {
        // Find the mid index
        const mid = Math.floor((start + end) / 2);

        // If element is present at mid, return True
        if (items[mid] === x) return;
        // Else look in left or right half accordingly
        else if (items[mid] < x) {
            start = mid + 1;
        } else {
            end = mid - 1;
        }
    }
};

const Linearithmic = () => {
    mergeSort(items);
};

const Quadratic = () => {
    const array = items.slice(); // creates a copy of the array

    for (let i = 0; i < array.length; i++) {
        for (let j = 0; j < array.length - 1; j++) {
            if (array[j] > array[j + 1]) {
                const swap = array[j];
                array[j] = array[j + 1];
                array[j + 1] = swap;
            }
        }
    }
};

const Cubic = () => {
    const solutions = [];
    const n = numberOfItems;

    for (let x = 0; x < n; x++) {
        for (let y = 0; y < n; y++) {
            for (let z = 0; z < n; z++) {
                if (3 * x + 9 * y + 8 * z === 79) {
                    solutions.push({ x, y, z });
                }
            }
        }
    }
};

Deno.bench(Constant);
Deno.bench(Logarithmic);
Deno.bench(Linear);
Deno.bench(Linearithmic);
Deno.bench(Quadratic);
Deno.bench(Cubic);
