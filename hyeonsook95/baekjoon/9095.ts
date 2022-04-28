var fs = require("fs");
var input = fs.readFileSync('dev/stdin').toString().split('\n');
const T = parseInt(input.shift());

function dfs(number, count) {
    if (number == 0) {
        return count + 1
    }

    for (var num of [1, 2, 3]) {
        if (number >= num) {
            count = dfs((number - num), count);
        }
    }
    return count;
}

for (var t = 0; t < T; t++) {
    var number = parseInt(input[t]);
    console.log(dfs(number, 0));
}