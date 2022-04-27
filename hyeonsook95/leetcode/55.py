# https://leetcode.com/problems/jump-game/discuss/596454/Python-Simple-solution-with-thinking-process-Runtime-O(n)
class Solution:
    def canJump(self, nums):
        last_position = len(nums) - 1

        for idx in range(len(nums) - 2, -1, -1):
            if idx + nums[idx] >= last_position:
                last_position = idx
        return last_position == 0
