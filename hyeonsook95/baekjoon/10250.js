var fs = require('fs');
var input = fs.readFileSync('dev/stdin').toString().split('\n');

const testCase = parseInt(input[0]);

for (var t = 0; t < testCase; t++) {
    const [h, w, guests] = input[t + 1].split(' ').map(num => parseInt(num));

    var floor = guests % h;
    var room = Math.floor(guests / h);

    if (floor == 0) {
        floor = h;
        room -= 1;
    }

    console.log(floor * 100 + (room + 1));
}
