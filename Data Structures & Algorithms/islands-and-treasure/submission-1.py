class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # DFS
        
        # In each step, compare the current tracking distance, and marked distance at the land.
        # If the current distance is smaller, update the cell and continue the seach
        
        m, n = len(grid), len(grid[0])
        def dfs(i: int, j: int, d: int) -> None:
            # Skip case 1: out of the range
            if not(0 <= i < m) or not(0 <= j < n):
                return

            # Skip case2: water
            if grid[i][j] == -1:
                return

            # Skp case 3: water tracking distance is larger than the marked one
            if 0 < grid[i][j] <= d:
                return
            
            # Skip case 4: visit again at the treasure point
            if grid[i][j] == 0 and d > 0:
                return
            
            grid[i][j] = d
            dfs(i + 1, j, d + 1)
            dfs(i, j + 1, d + 1)
            dfs(i - 1, j, d + 1)
            dfs(i, j - 1, d + 1)

            return
        
        # Find the treasure
        i = j = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    dfs(r, c, 0)