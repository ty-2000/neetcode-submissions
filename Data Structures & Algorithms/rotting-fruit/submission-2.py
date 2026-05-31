
from typing import List
import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS
        # Collect every (i, j) where grid[i][j] == 2 (rotten), and count the number of the fresh cell
        # Initialize a queue with all rotten points (i, j)
        # Every step, pop all element from the queue. These are reachable at the same specific time
        # For each element, add neighboors if the neighbor is fresh, and immediately update to "rotten"
        
        if not grid: return 0
        
        m, n = len(grid), len(grid[0])
        
        # Store the first rotten cells and the number of fresh fruit
        fresh_cnt = 0
        rottens = []
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    rottens.append((r, c))
                elif grid[r][c] == 1:
                    fresh_cnt += 1
        
        # Initialize que for BFS with the rotten cells
        q = deque(rottens)
        t = 0
        while q and fresh_cnt:
            t += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    ni, nj = i + di, j + dj
                    if (0 <= ni < m) and (0 <= nj < n) and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        fresh_cnt -= 1
                        q.append((ni, nj))
        
        return t if fresh_cnt == 0 else -1
        

