
from typing import List
import heapq



class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # DFS with a recursive function
        # Global list: min_times[] to keep the minimum time from a given k to the node so far
        # The function takes node: the node label, and the time to reach the node so far:
        # If the given time to the func is lower than the stored value, keep going. Otherwise return.
        
        # create a hash-map to search the neighbors with O(1)
        neighbors = {} # source -> (target, time)
        for t in times:
            neighbors[t[0]] = neighbors.get(t[0], [])
            neighbors[t[0]].append((t[1], t[2]))
        
        # Keep the time to reach each node: min_times[i] represents the time to take to reach i + 1 labeled node
        min_times = [float('inf')] * n
        
        def dfs(node: int, t: int) -> None:
            if t >= min_times[node - 1]: return
            
            # Update the time
            min_times[node - 1] = t
            
            # Continue the seach
            for n in neighbors.get(node, []):
                dfs(n[0], t + n[1])
        
        dfs(k, 0)
        res = max(min_times)
        
        return -1 if res == float('inf') else res
