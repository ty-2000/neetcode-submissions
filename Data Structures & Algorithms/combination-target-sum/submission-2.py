class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        # combinationSum(nums, target)
        # 
        #  = { combinationSum(nums[1:], target - nums[0]) + [nums[0]], combinationSum(nums[1:], target - 2 * nums[0]) + [nums[0], nums[0]],..., combinationSum(nums[1:], target - (target // nums[0]) * nums[0]) + [nums[0]] * (target // nums[0])}
        #  = ...

        def dfs(i: int, tgt: int) -> list[list[int]]:
            if tgt == 0:
                return [[]]
            elif i == len(nums):
                return []

            res = []
            n = tgt // nums[i] + 1 # 11, 3 => 4; 12, 3 => 5
            for m in range(n):
                tmps = dfs(i + 1, tgt - m * nums[i])
                for j in range(len(tmps)):
                    tmps[j] += [nums[i]] * m
                res += tmps
            return res
        res = dfs(0, target)
        return res