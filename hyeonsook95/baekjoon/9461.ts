var fs = require('fs');
var input = fs.readFileSync('dev/stdin').toString().split('\n');

var P = [1, 1, 1, 2, 2];
const T = parseInt(input.shift());

for (var t = 0; t < T; t++) {
    const n = input[t];

    if (n < P.length + 1) {
        console.log(P[n - 1]);
        continue;
    }

    while (n != P.length) {
        var idx = P.length - 1;
        P.push(P[idx] + P[idx - 4]);
    }
    console.log(P[P.length - 1]);
}