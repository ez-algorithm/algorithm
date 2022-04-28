function isValid(s: string): boolean {
  let stack: string[] = [];
  
  for (let i: number = 0; i < s.length; i++) {
    switch (s.charAt(i)) {
      case "(":
        stack.push(")"); break;
      case "{":
        stack.push("}"); break;
      case "[":
        stack.push("]"); break;
      default: {
        if (s.charAt(i) !== stack.pop()) return false;
        break;
      }
    }
  }
  if (stack.length > 0) return false;
  return true;
};