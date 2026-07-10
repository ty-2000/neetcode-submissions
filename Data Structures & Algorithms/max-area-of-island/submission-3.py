class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        def walk(i: int, j: int, size_so_far) -> None: # DFS
            # Mark the grid[i][j] to zero, and walk again to the adjacent lands
            
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                # Do walk
                grid[i][j] = 0
                size_so_far += 1
                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    size_so_far += walk(i + di, j + dj, 0)
            else:
                return 0
            return size_so_far
            
        
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cnt = max(cnt, walk(i, j, 0))
        return cnt
        