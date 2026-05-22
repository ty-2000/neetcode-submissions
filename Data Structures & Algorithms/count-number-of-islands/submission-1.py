class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m, n = len(grid), len(grid[0])
        def walk(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == '1':
                grid[i][j] = 'x'
                walk(i + 1,j)
                walk(i, j + 1)
                walk(i - 1, j)
                walk(i, j - 1)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    walk(i, j)
                    count += 1
        return count