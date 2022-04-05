const fs = require('fs');
const input = fs.readFileSync('dev/stdin').toString().trim().split('\n');

const [N, K] = input[0].split(' ').map(num => parseInt(num));
var maps = Array(1000001).fill(0);

for (var inputIdx = 0; inputIdx < N; inputIdx++) {
    var [ice, idx] = input[inputIdx + 1].trim().split(' ').map(num => parseInt(num));
    maps[idx] = ice;
}

var result = 0;
var end = (2 * K + 1) > 1000001 ? 1000001 : (2 * K + 1);
for (var idx = 0; idx < end; idx++) {
    result += maps[idx];
}

var left = 0;
var right = 2 * K;
var pSum = result;
while (right < 1000000) {
    left += 1;
    right += 1;

    pSum = pSum - maps[left - 1] + maps[right];
    result = pSum > result ? pSum : result;
}

console.log(result);