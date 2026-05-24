class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1: return nums[0]

        s, t = 0, 0
        for i in range(1, len(nums)):
            u = max(s, t + nums[i])
            t = s
            s = u
        maximum = s

        s, t = 0, 0
        for i in range(0, len(nums) - 1):
            u = max(s, t + nums[i])
            t = s
            s = u
        maximum = max(maximum, s)
        return maximum