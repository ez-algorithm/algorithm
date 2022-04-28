const map = new Map([
  ['2', ['a', 'b', 'c']],
  ['3', ['d', 'e', 'f']],
  ['4', ['g', 'h', 'i']],
  ['5', ['j', 'k', 'l']],
  ['6', ['m', 'n', 'o']],
  ['7', ['p', 'q', 'r','s']],
  ['8', ['t', 'u', 'v']],
  ['9', ['w', 'x', 'y', 'z']] 
]);


let answer: string[] = []; 

function letterCombinations(digits: string): string[] {
  answer.length = 0; // 정답 배열 초기화
  // 입력받은 숫자가 있으면 모든 문자 조합을 구함
  if(digits.length) comb(digits, 0, '');  
  return answer;
};

// 재귀로 조합 구현
function comb(digits: string, idx: number, str: string) {
  if (idx === digits.length) { // 문자 조합이 완성되면 정답 배열에 추가
    answer.push(str);
    return;
  }
  // 현재 숫자로 가능한 문자 배열 읽어옴
  const charArr: string[] | undefined = map.get(digits.charAt(idx));
  if (!charArr) return;
  
  for (let i = 0; i < charArr.length; i++) { 
    comb(digits, idx + 1, str + charArr[i]);    
  }

}