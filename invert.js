import { readFileSync, writeFileSync } from 'fs';
import { join } from 'path';
import invert from 'invert-color';

const postfixes = ["code", "-settings"];


for (const postfix of ["code", "-settings"]) {
    const sourceFilePath = join(`core/dark${postfix}.json`);
    const destinationFilePath = join(`core/light${postfix}.json`);

    const sourceLines = readFileSync(sourceFilePath, 'utf-8').split('\n');
    const destinationLines = sourceLines.map(line => {
        line = line.replace("Dark", "Light")
        line = line.replace("dark", "light")
        const hexValues = line.match(/#[a-fA-F0-9]{6}/g) || [];
        for (const hexValue of hexValues) {
            line = line.replace(hexValue, invert(hexValue));
        }
        return line;
    });

    writeFileSync(destinationFilePath, destinationLines.join('\n'), 'utf-8');
}


// postfixes.forEach(postfix => {
//     const sourceFilePath = join("core", `dark${postfix}.json`);
//     const destinationFilePath = join("core", `light${postfix}.json`);

//     readFile(sourceFilePath, 'utf-8', (err, content) => {
//         if (err) throw err;

//         const hexValues = content.match(/\#[a-fA-F0-9]{6}/g) || [];
//         hexValues.forEach(hexValue => {
//             const lighterHexValue = invert(hexValue);
//             content = content.replace("Dark", "Light")
//             content = content.replace("dark", "light")
//             content = content.replace(hexValue, lighterHexValue);
//         });

//         writeFile(destinationFilePath, content, 'utf-8', err => {
//             if (err) throw err;
//         });
//     });
// });
