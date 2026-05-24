class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        # # Layer by layer
        # # x x x x  t
        # # o o o o  t,b
        # # o o o o  b
        # # o o o o
        # # l l r r

        # # Key: toward ... right -> bottom -> left -> top
        # res = []
        # l, r, t, b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        # i, j = 0, 0
        # while l <= r and t <= b:


        #     # Right
        #     while j <= r:
        #         res.append(matrix[i][j])
        #         j += 1
        #     t += 1
        #     if t > b: break
        #     i, j = t, r

        #     # Towards buttom
        #     while i <= b:
        #         res.append(matrix[i][j])
        #         i += 1
        #     r -= 1
        #     if l > r: break
        #     i, j = b, r

        #     # Towards left
        #     while j >= l:
        #         res.append(matrix[i][j])
        #         j -= 1
        #     b -= 1
        #     if t > b: break
        #     i, j = b, l

        #     while i >= t:
        #         res.append(matrix[i][j])
        #         i -= 1
        #     l += 1
        #     if l > r: break
        #     i, j = t, l
        # return res

        # o o o o
        # o o o o
        # o o o o
        res = []
        # (dr, dc) = (0, 1) -> (1, 0) -> (0, -1) -> (-1, 0)
        def dfs(r, c, dr, dc, rep, next_rep):
            # how many times (rep) does the pointer at (r, c) move by (dr, dc)
            # Next time, next_rep time as rep, rep - 1 as next_rep

            # append all the elements in the given direction
            if rep == 0: return
            for _ in range(rep):
                r += dr
                c += dc
                res.append(matrix[r][c])
            dfs(r, c, dc, -dr, next_rep, rep-1)
        
        dfs(0, -1, 0, 1, len(matrix[0]), len(matrix) - 1)
        return res