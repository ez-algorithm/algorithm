const rl = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});
let input: string[] = [];

rl.on("line", function (line: string) {
  input.push(line);

}).on("close", function () {
  const L: number = parseInt(input.shift()!);
  let answer = 0;
  const M: number = 1234567891;

  let r = 1;
  for (let l = 0; l < L; l++) {
    let a = input[0].charCodeAt(l) - 96;
    // mod는 덧셈,곱셈 분배 법칙 성립
    answer += (a * r) % M;
    r = (r * 31) % M;
  }
    
  console.log(answer % M);
  process.exit();
});
