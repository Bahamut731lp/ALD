//https://cainos.itch.io/pixel-art-top-down-basic

/*
    Step 1: Nějak narandom vygenerovat povrch
    Step 2: Potom řešit spoje

    Mít mapu možných kombinací a nějak iterovat / náhodně vybírat??? (+ asi nějakej stack pro historii, kdyby se něco dojebalo)
*/

const TIMERS = {
    grid: "Grid Render"
}

const TESTRULES = {
    "red": ["pink", "red", "orange"],
    "orange": ["red", "orange", "yellow"],
    "yellow": ["orange", "yellow", "yellowgreen"],
    "yellowgreen": ["yellow", "yellowgreen", "green"],
    "green": ["yellowgreen", "green", "teal"],
    "teal": ["green", "teal", "blue"],
    "blue": ["teal", "blue", "darkslateblue"],
    "darkslateblue": ["blue", "darkslateblue", "purple"],
    "purple": ["darkslateblue", "purple", "fuchsia"],
    "fuchsia": ["purple", "fuchsia", "pink"],
    "pink": ["fuchsia", "pink", "red"],
}

const getRandom = (arr) => arr[Math.floor(Math.random() * arr.length)]

function grid(target) {
    const SIZE = 32;
    const WIDTH = window.innerWidth;
    const HEIGHT = window.innerHeight;
    const TILES_PER_WIDTH = Math.ceil(WIDTH / SIZE);
    const TILES_PER_HEIGHT = Math.ceil(HEIGHT / SIZE);
    const fragment = new DocumentFragment();
    
    console.log(TILES_PER_WIDTH, TILES_PER_HEIGHT);
    
    console.time(TIMERS.grid);
    for (let index = 0; index < TILES_PER_WIDTH * TILES_PER_HEIGHT; index++) {
        const tile = document.createElement("div");
        let colour;

        if (index == 0) {
            colour = getRandom(Object.keys(TESTRULES));
        }
        else {
            colour = "white";
        }

        
        //const colour = Math.floor(Math.random()*16777215).toString(16);


        tile.style = `background: ${colour}; width: ${SIZE}px; height: ${SIZE}px`;
        tile.id = `${Math.floor(index / TILES_PER_WIDTH)}_${index % TILES_PER_WIDTH}`;

        fragment.append(tile);




    }

    console.timeLog(TIMERS.grid);

    requestAnimationFrame(() => {
        target.append(fragment);
        console.timeEnd(TIMERS.grid);
    });
}



grid(document.body);