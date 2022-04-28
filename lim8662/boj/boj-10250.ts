const rl = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});
let input: string[] = [];

rl.on("line", function (line: string) {
  input.push(line);

}).on("close", function () {
  const T: number = parseInt(input.shift()!);

  for (let tc = 0; tc < T; tc++) 
    console.log(getLastRoomNo(input[tc]));
  
  process.exit();
});

function getLastRoomNo(inputRow: string): number {
  const [h, w, n] = inputRow.trim().split(" ").map((el: string) => parseInt(el));
  let roomCnt = 0;

  for (let roomNo = 1; roomNo <= w; roomNo++) 
  for (let floor = 1; floor <= h; floor++) {
    if (++roomCnt === n) 
      return (floor * 100) + roomNo;
  }
  return 0; 
}