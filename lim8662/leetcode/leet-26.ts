function removeDuplicates(nums: number[]): number {
    
  let front: number = 0;
  let back: number = 1;
  
  while(back < nums.length) {
      if(nums[front] !== nums[back]) {
          front++;
          nums[front] = nums[back];
          back++
      } else back++
  
  }
  
  return front + 1;
};

