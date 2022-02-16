function removeDuplicates(nums: number[]): number {
    let currentIdx = 0;
    let currentNumber = nums[0];
    for (let idx = 1; idx < nums.length; idx++) {
        if (currentNumber !== nums[idx]) {
            currentIdx += 1;

            currentNumber = nums[idx];
            nums[currentIdx] = nums[idx];

        }
    }
    return currentIdx + 1;
};