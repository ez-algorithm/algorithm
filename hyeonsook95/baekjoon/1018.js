// 입력을 받습니다.
var fs = require('fs');
var input = fs.readFileSync('dev/stdin').toString().split('\n');

// 문제에서 주어진 n, m을 int값으로 변경합니다.
const [n, m] = input[0].split(' ').map(num => parseInt(num));

// 체스판의 크기는 8*8 이므로, 다시 칠해야 하는 칸의 개수는 8*8 이상이 될 수 없습니다.
// 따라서 처음의 minCount를 8*8 값으로 초기화합니다.
var minCount = 8 * 8;
var maps = [];
for (r = 0; r < n; r++) {
    maps.push(input[r + 1].trim());
}

// 체스판은 W로 시작할 때/B로 시작할 때, 2개의 답만을 가집니다.
const whiteAns = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
];
const blackAns = [
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
]

// 입력에서 체스판이 될 수 있는 첫 번째 칸은 [0:n-7][0:m-7] 이므로 해당 칸을 돌면서 체스판을 검사합니다.
for (r = 0; r < n - 7; r++) {
    for (c = 0; c < m - 7; c++) {
        var whiteCnt = 0;
        var blackCnt = 0;

        // 8*8 의 체스칸이므로 8*8을 돌면서 정답 체스판과 다른 칸을 비교합니다.
        // 정답 체스칸은 2개 이므로 두 개를 같이 비교합니다.
        for (y = 0; y < 8; y++) {
            for (x = 0; x < 8; x++) {
                if (whiteAns[y][x] != maps[r + y][c + x]) {
                    whiteCnt += 1;
                }
                if (blackAns[y][x] != maps[r + y][c + x]) {
                    blackCnt += 1;
                }
            }
        }
        minCount = Math.min(minCount, whiteCnt, blackCnt);
    }
}

console.log(minCount);