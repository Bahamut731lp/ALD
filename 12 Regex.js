const fs = require('fs');

const students = {};

const getStudentID = (value) => value.match(/(?<=data-header="Fakulta:\s+?"\>\s+)\w+/gim)?.[0];
const getStudentProgram = (value) => value.match(/(?<=data-header="Stav:\s+?"\>)\w+/gim)?.[0];
const getStudentOrderNumber = (value) => value.match(/(?<=data-header="Por\.:\s+?"\><b>).+(?=<\/b>)/gim)?.[0];
const getStudentName = (value) => value.match(/(?<=data-header="Por.:\s+"\>\<.+"\>).+(?=\<\/a\>,)/gim)?.[0]?.trim();

function processFile(data) {
    const teloTabulky = data.split("<tbody>")?.pop();
    const radky = teloTabulky.split("</tr>");
    const osekane = radky.slice(0, radky.length).map((radek) => radek.replace(/(\r\n|\n|\r)/gm, "").trim()).map(radek => radek.replace(/\s+/g,' '));

    //TODO: Ztrácí se mi lidi
    for (const radek of osekane) {
        const id = getStudentID(radek);
        const program = getStudentProgram(radek);
        const order = getStudentOrderNumber(radek);
        const name = getStudentName(radek);

        if ([id, program, order, name].some(v => !v)) continue;

        students[program] = students[program] ?? [];
        students[program].push({ id, name, program, order});
    }

    const delka = Math.max(...Object.values(students).flat().map(v => parseInt(v.name.length)));
    const keys = Object.keys(students).sort();

    for (const obor of keys) {
        console.log(`${obor.toUpperCase()}:`);

        let liche = students[obor]
        .filter((student) => parseInt(student.id.slice(1)) % 2 == 1)
        .sort((a, b) => parseInt(a.id.slice(1)) - parseInt(b.id.slice(1)));

        let sude = students[obor]
        .filter((student) => parseInt(student.id.slice(1)) % 2 == 0)
        .sort((a, b) => parseInt(a.id.slice(1)) - parseInt(b.id.slice(1)));

        
        const radky = [...liche, ...sude].map((student, index) => {
            const [prijmeni, jmeno] = student.name.split(/\s+/);

            return (
                `${String(index + 1).padStart(2)}: ${student.id[0]} ${[prijmeni.toUpperCase(), jmeno].join(" ").padEnd(delka)} ${student.program.padEnd(3)} ${student.id.slice(1)}`
            )
        });

        console.log(radky.join("\n"));
        console.log();
    }
} 

const data = fs.readFileSync("./vstup.html", "utf-8");
processFile(data);