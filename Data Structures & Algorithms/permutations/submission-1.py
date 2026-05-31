
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Result that is going to be returned
        res = []
        remainings = set(nums) # keeps the remaining option
        
        def dfs(cur: list[int]) -> None:
            # Reach to the last
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            # Copy the remaining options temporary
            cur_remainings = list(remainings)
            for n in cur_remainings:
                remainings.remove(n)
                cur.append(n)
                dfs(cur)
                cur.pop()
                remainings.add(n)
        dfs([])
        return res