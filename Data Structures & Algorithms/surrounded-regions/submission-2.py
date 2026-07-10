

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        m, n = len(board), len(board[0])
        
        def dfs(r: int, c: int) -> bool:
            if 0 <= r < m and 0 <= c < n and board[r][c] == 'O':
                board[r][c] = 'T'
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    dfs(r + dr, c + dc)
        
        for r in range(m):
            if board[r][0] == 'O': dfs(r, 0)
            if board[r][n-1] == 'O': dfs(r, n - 1)
        for c in range(n):
            if board[0][c] == 'O': dfs(0, c)
            if board[m-1][c] == 'O': dfs(m-1, c)
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O': board[r][c] = 'X'
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'T': board[r][c] = 'O'
        
        