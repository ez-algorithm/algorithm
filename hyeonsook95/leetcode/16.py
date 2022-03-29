class Solution:
    def threeSumClosest(self, nums, target):
        nums = sorted(nums)
        result = sum(nums[:3])
        for idx in range(len(nums) - 2):
            # left와 right를 양 끝 인덱스 값으로 초기화
            left, right = idx + 1, len(nums) - 1
            while left < right:
                p_sum = nums[idx] + nums[left] + nums[right]
                if abs(target - p_sum) < abs(target - result):
                    result = p_sum
                if result == target:
                    return result

                if p_sum > target:
                    right -= 1
                else:
                    left += 1
        return result
