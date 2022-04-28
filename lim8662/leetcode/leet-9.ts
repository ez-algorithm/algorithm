function isPalindrome(n: number): boolean {

  if (n < 0) return false;

  const numStr: string =  n.toString()
  let left: number = 0;
  let right: number =numStr.length - 1;
  
  while (left < right) {
    if (numStr[left++] !== numStr[right--]) return false; 
  }
  
  return true;
};
