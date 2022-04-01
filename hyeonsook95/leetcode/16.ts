function threeSumClosest(nums: number[], target: number): number {
    nums.sort(function (a, b) { return a - b; });
    var result = nums[0] + nums[1] + nums[2];
    for (var idx = 0; idx < nums.length; idx++) {
        var left: number = idx + 1;
        var right: number = nums.length - 1;
        while (left < right) {
            let pSum = nums[idx] + nums[left] + nums[right];
            if (Math.abs(target - pSum) < Math.abs(target - result)) {
                result = pSum;
            }
            if (result === target) {
                return result;
            }

            if (pSum > target) {
                right -= 1;
            } else {
                left += 1;
            }
        }
    }
    return result;
};