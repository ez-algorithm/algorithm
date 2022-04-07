const fs = require('fs');
const input = fs.readFileSync('dev/stdin').toString().trim().split('\n');

const N = parseInt(input[0]);
const nums = input[1].trim().split(' ').map(num => parseInt(num));
const T = parseInt(input[2]);

for (var inputIdx = 0; inputIdx < T; inputIdx++) {
    var [start, end] = input[inputIdx + 3].trim().split(' ').map(num => parseInt(num));

    var selectionSum = 0;
    for (var numIdx = start; numIdx < end + 1; numIdx++) {
        selectionSum += nums[numIdx];
    }
    console.log(selectionSum);
}