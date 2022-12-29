// Colours skillfully yoinked from TailwindCSS
const ANCHOR_AMOUNT = 16;
const ANCHORS = [];
const COLOURS = ["#ef4444", "#f97316", "#f59e0b", "#eab308", "#84cc16", "#22c55e", "#10b981", "#14b8a6", "#06b6d4", "#0ea5e9", "#3b82f6", "#6366f1", "#8b5cf6", "#a855f7", "#d946ef", "#ec4899", "#f43f5e"];
const SIZE = 64;
const WIDTH = window.innerWidth;
const HEIGHT = window.innerHeight;
const TILES_PER_WIDTH = Math.ceil(WIDTH / SIZE);
const TILES_PER_HEIGHT = Math.ceil(HEIGHT / SIZE);
const TILES = [...Array(TILES_PER_HEIGHT)].map(_ => [...Array(TILES_PER_WIDTH)]);

const fragment = document.createDocumentFragment();

const getRandomNumberFromInterval = (a, b) => Math.floor(Math.random() * (b - a + 1) + a);
const getRandomColour = () => getRandomNumberFromInterval(0, COLOURS.length - 1);
const getAnchorDistances = (x, y, arr = ANCHORS.slice()) => arr.slice().map(v => JSON.parse(v)).map((v, _) => Math.round(Math.sqrt(Math.pow(v[0] - y, 2) + Math.pow(v[1] - x, 2))));

function cyclic(n, length) {
    // ToInteger() abstract op
    n = Math.trunc(n) || 0;
    // Allow negative indexing from the end
    if (n < 0) n += length;
    // OOB access is guaranteed to return undefined
    if (n >= length) n %= length;
    // Otherwise, this is just normal property access
    return n;
}


/**
 * Funkce pro vykreslení mřížky s dlaždicemi
 */
function RenderGrid() {
    let rowIndex = 0;
    let colIndex = 0;

    for (const ROW of TILES) {
        colIndex = 0;

        for (const TILE of ROW) {
            const tileContainer = document.createElement("div");
            const colour = COLOURS.at(cyclic(TILE, COLOURS.length));

            tileContainer.style = `background-color: ${colour}; width: ${SIZE}px; height: ${SIZE}px;`;
            tileContainer.id = `${rowIndex}_${colIndex}`;
            tileContainer.setAttribute("data-tile", TILE);

            /*if (ANCHORS.includes(`[${rowIndex},${colIndex}]`)) {
                tileContainer.style = `background-color: ${colour}; width: ${SIZE}px; height: ${SIZE}px; box-shadow: inset 0 0 10px #000;`
            }*/

            fragment.append(tileContainer);
            colIndex++;
        }

        rowIndex++;
    }

    document.body.append(fragment);
    //requestAnimationFrame(() => {
    //});
}

/**
 * Funkce pro vytvoření gridu na obrazovce
 */
function main() {
    //Vytvoření kotev
    for (let index = 0; index < ANCHOR_AMOUNT; index++) {
        const RandomX = getRandomNumberFromInterval(0, TILES_PER_WIDTH - 1);
        const RandomY = getRandomNumberFromInterval(0, TILES_PER_HEIGHT - 1);
        const RandomColour = getRandomColour();

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

main();
delete TILES;