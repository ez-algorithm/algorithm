const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let input: number[] = [];
rl.on("line", function (line: string) {
  input = line.split(" ").map((el: string) => parseInt(el));
  rl.close();
  
}).on("close", function () {
  console.log(getMinDistance(input));
  process.exit();
});

function getMinDistance(input: number[]) : number {
  const [x, y, w, h] = input;
  let minX = x > w - x ? w - x : x;
  let minY = y > h - y ? h - y : y;
  return minX > minY ? minY : minX;
}