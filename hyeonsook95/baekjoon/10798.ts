const rl = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});
let input: string[] = [];

rl.on('line', function (line) {
    input.push(line);
}).on('close', function () {
    const zip: Function = rows => rows[0].map((_, c) => rows.map(row => row[c]));
    let answer = input.map(chars => (chars.trim().split("").concat(Array(15 - chars.length).fill(' '))));
    console.log(zip(answer).map(chars => chars.join("").replace(" ", "")).join("").replace(" ", ""));
    process.exit();
});

