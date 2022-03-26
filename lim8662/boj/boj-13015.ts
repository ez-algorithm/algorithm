const rl = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});
let input: string[] = [];

rl.on("line", function (line: string) {
  input.push(line);

}).on("close", function () {
  const N: number = parseInt(input.shift()!);
  const B: number = N - 2; // 공백의 수
  const BLANK: string = " ".repeat(B); // 공백 문자열
  const edge: string = "*".repeat(N) + " ".repeat(B * 2 + 1) + "*".repeat(N);
  const center: string = " ".repeat(N - 1) + "*" + BLANK + "*" + BLANK + "*\n";

  let result: string = edge + "\n";
  for (let i = 1, j = (B * 2 - 1); i <= B; i++, j-=2){
    result += " ".repeat(i) + "*" + BLANK + "*" + " ".repeat(j) + "*" + BLANK + "*\n" 
  }
  result += center;
  for (let i = B, j = 1; i >= 1; i--, j+=2){
    result += " ".repeat(i) + "*" + BLANK + "*" + " ".repeat(j) + "*" + BLANK + "*\n" 
  }
  result += edge;

  console.log(result);
  process.exit();
});
