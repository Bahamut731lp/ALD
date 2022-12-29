// Colours skillfully yoinked from TailwindCSS

//Constants
const ANCHOR_AMOUNT = 84;
const COLOURS = ["#ef4444", "#f97316", "#f59e0b", "#eab308", "#84cc16", "#22c55e", "#10b981", "#14b8a6", "#06b6d4", "#0ea5e9", "#3b82f6", "#6366f1", "#8b5cf6", "#a855f7", "#d946ef", "#ec4899", "#f43f5e"];
const SIZE = 16;

//Helper Constants
const ANCHORS = [];
const WIDTH = window.innerWidth;
const HEIGHT = window.innerHeight;
const TILES_PER_WIDTH = Math.ceil(WIDTH / SIZE);
const TILES_PER_HEIGHT = Math.ceil(HEIGHT / SIZE);
const TILES = [...Array(TILES_PER_HEIGHT)].map(_ => [...Array(TILES_PER_WIDTH)]);

//Canvas Configuration
const CANVAS = document.getElementById("target");
const CONTEXT = CANVAS.getContext("2d");

CANVAS.width = WIDTH;
CANVAS.height = HEIGHT;
CONTEXT.imageSmoothingEnabled = false;

//Helper Functions
const getRandomNumberFromInterval = (a, b) => Math.floor(Math.random() * (b - a + 1) + a);
const getRandomColour = () => getRandomNumberFromInterval(0, COLOURS.length - 1);
const getAnchorDistances = (x, y, arr = ANCHORS.slice()) => arr.slice().map(v => JSON.parse(v)).map((v, _) => Math.round(Math.sqrt(Math.pow(v[0] - y, 2) + Math.pow(v[1] - x, 2))));

function createInfo(label, value) {
    //Kde je react a JSX, když ho člověk potřebuje :(
    const container = document.createElement("span");
    const definition = document.createElement("dt");
    const field = document.createElement("dd");

    definition.innerText = label;
    field.innerText = value;

    container.append(definition, field);
    document.getElementById("info").append(container);
}

/**
 * Pomocná funkce pro pole tak, aby bylo indexování cyklické.
 * @param {number} n Index
 * @param {number} length Délka pole
 * @returns "Normalizovaný" (resp. cyklický) index
 */
function getCyclicIndex(n, length) {
    n = Math.trunc(n) || 0;
    if (n < 0) n += length;
    if (n >= length) n %= length;
    return n;
}

/**
 * Funkce pro vykreslení mřížky s dlaždicemi
 */
function RenderGrid() {
    let rowIndex = 0;
    let colIndex = 0;

    function drawPixel(context, x, y, color) {
        var roundedX = Math.round(x);
        var roundedY = Math.round(y);

        context.fillStyle = color || '#000';
        context.fillRect(roundedX, roundedY, SIZE, SIZE);
    }

    for (const ROW of TILES) {
        colIndex = 0;

        for (const TILE of ROW) {
            const colour = COLOURS.at(getCyclicIndex(TILE, COLOURS.length));
            drawPixel(CONTEXT, colIndex * SIZE, rowIndex * SIZE, colour);
            colIndex++;
        }

        rowIndex++;
    }
}

function main() {
    //Vytvoření kotev
    for (let index = 0; index < ANCHOR_AMOUNT; index++) {
        let coordinates;
        let RandomX, RandomY, RandomColour

        //DO-WHILE pro zajištění, že nebude více kotvících bodů na jednom místě
        //Šance je malá, ale je tam.
        do {
            RandomX = getRandomNumberFromInterval(0, TILES_PER_WIDTH - 1);
            RandomY = getRandomNumberFromInterval(0, TILES_PER_HEIGHT - 1);
            RandomColour = getRandomColour();
    
            coordinates = `[${RandomY},${RandomX}]`;
        } while (ANCHORS.includes(coordinates));

        ANCHORS.push(`[${RandomY},${RandomX}]`);
        TILES[RandomY][RandomX] = RandomColour;
    }

    //Vytvoření zón
    for (let index = 0; index < TILES_PER_WIDTH * TILES_PER_HEIGHT; index++) {
        const X = index % TILES_PER_WIDTH;
        const Y = Math.floor(index / TILES_PER_WIDTH);

        if (ANCHORS.includes(`[${Y},${X}]`)) continue;

        const distances = getAnchorDistances(X, Y);
        const minimum = Math.min(...distances);
        const minimumIndex = distances.indexOf(minimum);
        const [colourY, colourX] = JSON.parse(ANCHORS[minimumIndex]);

        TILES[Y][X] = TILES[colourY][colourX];
    }

    //Blending po ose X
    for (let index = 0; index < TILES_PER_WIDTH * TILES_PER_HEIGHT; index++) {
        const X = index % TILES_PER_WIDTH;
        const Y = Math.floor(index / TILES_PER_WIDTH);

        const dx = TILES[Y][X] - TILES[Y][Math.max(X - 1, 0)]

        if (Math.abs(dx) > 1) {
            const colour = TILES[Y][Math.max(X - 1, 0)] + Math.sign(dx);
            TILES[Y][X] = colour;
        }
    }

    //Blending po ose Y
    for (let index = 0; index < TILES_PER_WIDTH * TILES_PER_HEIGHT; index++) {
        const Y = index % TILES_PER_HEIGHT;
        const X = Math.floor(index / TILES_PER_HEIGHT);

        const dy = TILES[Y][X] - TILES[Math.max(Y - 1, 0)][X]

        if (Math.abs(dy) > 1) {
            const colour = TILES[Math.max(Y - 1, 0)][X] + Math.sign(dy);
            TILES[Y][X] = colour;
        }
    }

    RenderGrid();
}

const startTime = performance.now();
main();
const endTime = performance.now();

createInfo("Výška", `${WIDTH} px`);
createInfo("Šířka", `${HEIGHT} px`);
createInfo("Dlaždice", `${SIZE} px`);
createInfo("Dlaždice / Výšku", TILES_PER_WIDTH);
createInfo("Dlaždice / Šířku", TILES_PER_HEIGHT);
createInfo("Kotvy", ANCHOR_AMOUNT);
createInfo("Čas", `${Number((endTime - startTime)).toFixed(2)} ms`);

delete TILES;