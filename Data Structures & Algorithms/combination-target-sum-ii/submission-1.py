class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        # Sort the list first
        # Iterate with DFS. In each step, decide if we're going to use the element
        #  If not, skip to the next unique value
        #  If yes, add the element to the current temporary sum, and move the pointer forward
        
        # Sort
        candidates.sort()

        # Initialize
        res = []

        def dfs(i: int, sum_val: int, comb: list[int]):
            if sum_val == target:
                res.append(comb.copy())
                return
            elif sum_val > target or i == len(candidates):
                return
            
            # Dive deep into the case of using this element
            comb.append(candidates[i])
            dfs(i + 1, sum_val + candidates[i], comb)

            # Dive deep into the case of using this element
            comb.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, sum_val, comb)
        
        dfs(0, 0, [])

        return res