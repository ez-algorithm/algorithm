const fs = require("fs");
const input = fs.readFileSync('dev/stdin').toString().trim();

const N = parseInt(input);

var dp = [0, 1, 2];
var idx = dp.length;

while (N > dp.length - 1) {
    dp.push(dp[idx - 1] + dp[idx - 2]);
    idx += 1;
}

console.log(dp[N]);