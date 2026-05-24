class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    cur_area = 0
                    stack = [(i, j)]
                    while stack:
                        p, q = stack.pop()
                        if 0 <= p < m and 0 <= q < n and grid[p][q]:
                            cur_area += 1
                            grid[p][q] = 0
                            stack += [(p + 1, q), (p, q + 1), (p - 1, q), (p, q - 1)]
                    max_area = max(cur_area, max_area)
        return max_area