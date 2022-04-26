class Solution:
    def canJump(self, nums):
        def greedy(idx, v):
            if idx == len(nums) - 1:
                return True
            if v == 0 or idx > len(nums) - 1:
                return False

            for w in range(v, 0, -1):
                next_idx = idx + w
                if next_idx < len(nums):
                    if greedy(next_idx, nums[next_idx]):
                        return True
            return False

        return greedy(0, nums[0])
