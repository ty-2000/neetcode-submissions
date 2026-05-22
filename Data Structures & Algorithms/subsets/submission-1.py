class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        def dfs(i: int, cur: list[int]):
            # If i equals to the length of nums: append the copy of current list to the result
            if i == len(nums):
                result.append(cur.copy())
                return
            dfs(i + 1, cur)
            cur.append(nums[i])
            dfs(i + 1, cur)
            cur.pop()
        dfs(0, [])
        return result