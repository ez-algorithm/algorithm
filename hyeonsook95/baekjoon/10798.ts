const fs = require("fs");
const zip = rows => rows[0].map((_, c) => rows.map(row => row[c]));
var input = fs.readFileSync('dev/stdin').toString().split('\n').map(chars => (chars.trim().split("").concat(Array(15 - chars.length).fill(' '))));
console.log(zip(input).map(chars => chars.join("")).join("").replace(/(\s*)/g, ''));