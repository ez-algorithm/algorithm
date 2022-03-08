const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let input: string[] = [];
let paper: string[][] = [];
let whitePieceCnt: number = 0; // 흰 종이 조각 수
let bluePieceCnt: number = 0; // 파란 종이 조각 수

rl.on("line", function (line: string) {
  input.push(line);

}).on("close", function () {
  input.shift();
  paper = input.map((row) => row.split(" "));
  let N = input.length;

  division(0, 0, N);

  console.log(whitePieceCnt);
  console.log(bluePieceCnt);
  process.exit();
});

function division(x: number, y: number, n: number) {
  
  if (n === 1 || isSame(x, y, n)) {
    if (paper[x][y] === '0') whitePieceCnt++;
    else bluePieceCnt++;
    return;

  } else {
    division(x, y, n/2);
    division(x + n/2, y, n/2);
    division(x, y + n/2, n/2);
    division(x + n/2, y + n/2, n/2);
  }
}

function isSame(x: number, y: number, l: number) : boolean{
  const color: string = paper[x][y];

  for (let row = 0; row < l; row++) 
  for (let col = 0; col < l; col++) {
    if (paper[x + row][y + col] !== color) return false;
  }
  return true;

}
