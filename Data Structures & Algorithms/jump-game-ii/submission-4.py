class Solution:
    def jump(self, nums: list[int]) -> int:
        # Dynamic programming using a recursive function with memo
        # At the position i, minimum jump from i is the minimum values from the subproblem of i + 1 ~ i + nums[i]
        # Each step, we take a memo so that we can solve the problem with O(n * max(nums))

        memo = {} # index -> minimum jumps
        def dfs(i: int) -> int:
            if i in memo:
                return memo[i]

            # Reached to the goal
            if i >= len(nums) - 1:
                return 0
            
            # If the value is 0 before the goal, the path cannot reach goal
            # In that case, return INF
            
            minimum_jumps = float('inf')
            for j in range(nums[i], 0, -1):
                minimum_jumps = min(dfs(i + j) + 1, minimum_jumps)
            memo[i] = minimum_jumps
            return memo[i] 

        return dfs(0)