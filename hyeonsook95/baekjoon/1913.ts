var fs = require("fs");
var input = fs.readFileSync('dev/stdin').toString().split('\n');

const N = parseInt(input[0]);
const target = parseInt(input[1]);

var tr = -1;
var tc = -1;
var maps = Array.from(Array(N), () => Array(N).fill(0));

var didx = 0;
const dr = [1, 0, -1, 0];
const dc = [0, 1, 0, -1];

var ridx = 0;
var cidx = 0;

for (var num = N ** 2; num > 0; num--) {
    if (num === target) {
        tr = ridx + 1;
        tc = cidx + 1;
    }

    maps[ridx][cidx] = num;
    if ((0 > ridx + dr[didx]) || (N - 1 < ridx + dr[didx]) || (0 > cidx + dc[didx]) || (N - 1 < cidx + dc[didx]) || (maps[ridx + dr[didx]][cidx + dc[didx]] !== 0)) {
        didx = (didx + 1) % 4;
    }
    ridx = ridx + dr[didx];
    cidx = cidx + dc[didx];

}

for (var row of maps) {
    console.log(...row);
}
console.log(tr, tc);