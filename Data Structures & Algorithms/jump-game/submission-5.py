class Solution:
    def canJump(self, nums: list[int]) -> bool:
        reachable = 0
        cur = 0
        for i in range(len(nums)):
            if reachable >= len(nums) - 1: return True
            elif reachable < i: return False
            reachable = max(i + nums[i], reachable)
        return False
