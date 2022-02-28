var fs = require('fs');
var input = fs.readFileSync('dev/stdin').toString().split(' ');

const [x, y, w, h] = input.map(num => parseInt(num));
console.log(x, y, (w - x), (h - y));