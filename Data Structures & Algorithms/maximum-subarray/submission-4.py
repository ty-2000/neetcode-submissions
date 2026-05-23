class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # Sliding window with Seach with greedy
        # Keep sum of nums[i] ~ nums[j] is "local maximum"
        # If sum of nums[i] ~ nums[j] < 0, we should discard the subarray for the going search
        # During the seach, keep the maximum with a global variable

        # 1, 3, -8, -2, -3, 9, 2, -3
        # i, j
        # i,     j -> -4
        #           ij
        #               ij
        #                   ij
        #                   i, j
        #                   i,     j
        #                         i,j
        #                             i,j


        j = 0
        res = -float('inf')
        cur = 0
        while j < len(nums):
            cur += nums[j]
            res = max(cur, res)
            if cur < 0:
                cur = 0
            j = j + 1
        return res