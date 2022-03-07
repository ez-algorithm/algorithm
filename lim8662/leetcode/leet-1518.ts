function numWaterBottles(numBottles: number, numExchange: number): number {

  let total = numBottles; // 마신 병의 총합
  let empty = total; // 빈 병의 수
  let full = 0; // 교환해서 받은 병의 수
  while (true) {
    full =  Math.floor(empty / numExchange); // 빈 병을 새 병으로 교환
    if (full === 0) break;
    empty = empty % numExchange; // 교환 후 남은 빈병
    
    // 교환받은 병 다 비움
    empty += full; 
    total += full;
  }

  return total;
};