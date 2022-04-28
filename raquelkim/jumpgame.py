class Solution:
    def canJump(self, nums) -> bool:
        location = 0
        for i in range(len(nums)):
            location += nums[i]
            if location == len(nums):
                return True
            elif location > len(nums):
                return False
