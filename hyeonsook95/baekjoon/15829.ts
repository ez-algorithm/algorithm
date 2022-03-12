var fs = require('fs');
var input = fs.readFileSync('dev/stdin').toString().split('\n');

const r = BigInt(31);
const M = BigInt(1234567891);

var L = parseInt(input[0]);
var string = input[1].split('').map(char => BigInt(char.charCodeAt(0) - 96));

var amount = BigInt(0);
for (var idx = BigInt(0); idx < L; idx++) {
    amount += string[idx] * (r ** idx);
}

console.log(Number(amount % M));