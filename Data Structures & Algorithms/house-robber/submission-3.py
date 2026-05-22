class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1: return nums[0]
        amounts = [0] * len(nums)
        amounts[0] = nums[0]
        amounts[1] = max(nums[:2])
        for i in range(2, len(nums)):
            amounts[i] = max(amounts[i - 2] + nums[i], amounts[i - 1])
        return amounts[len(nums) - 1]