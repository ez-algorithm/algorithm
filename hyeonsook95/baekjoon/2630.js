var fs = require('fs');
var input = fs.readFileSync('dev/stdin').toString().split('\n');

const N = parseInt(input.shift());
const maps = input.map(nums => nums.split(' ').map(num => parseInt(num)));

var answer = [0, 0];

function cutPaper(startR, startC, d) {
    if (d == 1 || checkColor(startR, startC, d)) {
        answer[maps[startR][startC]] += 1;
        return;
    }

    var n = Math.ceil(d / 2);
    cutPaper(startR, startC, n);
    cutPaper(startR + n, startC, n);
    cutPaper(startR, startC + n, n);
    cutPaper(startR + n, startC + n, n);
    return;
}


function checkColor(startR, startC, d) {
    var color = maps[startR][startC];
    for (var r = startR; r < startR + d; r++) {
        for (var c = startC; c < startC + d; c++) {
            if (color != maps[r][c]) {
                return false;
            }
        }
    }
    return true;
}

cutPaper(0, 0, N);


for (a of answer) {
    console.log(a);
}