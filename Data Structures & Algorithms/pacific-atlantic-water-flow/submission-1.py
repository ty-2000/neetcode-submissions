DS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Brute Force
        # From

        # Extend the height matrix
        # From top and left cells, search with DFS to find cells that can be reached from the ocian (water goes up)
        # Store the reachable cells

        # From buttom and right cells, search with DFS to find cells that can be reached from the ocian (water goes up)
        # Store the reachable cells

        # Cells that is marked as reachable from both ocian is the answer

        if not heights or not heights[0]: return []

        m, n = len(heights), len(heights[0])

        pacifics = [[False] * n for _ in range(m)]
        atrantics = [[False] * n for _ in range(m)]

        # Pacifics
        stack = []
        for i in range(m): stack.append((i, 0))
        for j in range(n): stack.append((0, j))
        while stack:
            r, c = stack.pop()
            pacifics[r][c] = True
            for dr, dc in DS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and heights[r][c] <= heights[nr][nc] and not pacifics[nr][nc]:
                    stack.append((nr, nc))
            
        # Atrantic
        stack = []
        for i in range(m): stack.append((i, n - 1))
        for j in range(n): stack.append((m - 1, j))
        while stack:
            r, c = stack.pop()
            atrantics[r][c] = True
            for dr, dc in DS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and heights[r][c] <= heights[nr][nc] and not atrantics[nr][nc]:
                    stack.append((nr, nc))

        res = []
        for i in range(m):
            for j in range(n):
                if pacifics[i][j] and atrantics[i][j]: res.append([i, j])
        
        return res