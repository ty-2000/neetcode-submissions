class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums)

        money = [0] * len(nums)

        money[0], money[1] = nums[0], max(nums[0], nums[1])
        maximum = max(money[0], money[1])
        for i in range(2, len(nums) - 1):
            money[i] = max(money[i - 2] + nums[i], money[i - 1])
            maximum = max(money[i], maximum)      
        money[1], money[2] = nums[1], max(nums[1], nums[2])
        maximum = max(maximum, money[1], money[2])
        for i in range(3, len(nums)):
            money[i] = max(money[i - 2] + nums[i], money[i - 1])
            maximum = max(money[i], maximum)
        return maximum