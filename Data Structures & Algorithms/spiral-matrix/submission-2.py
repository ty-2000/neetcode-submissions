class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        # Layer by layer
        # x x x x  t
        # o o o o  t,b
        # o o o o  b
        # o o o o
        # l l r r

        # Key: toward ... right -> bottom -> left -> top
        res = []
        l, r, t, b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        i, j = 0, 0
        while l <= r and t <= b:


            # Right
            while j <= r:
                res.append(matrix[i][j])
                j += 1
            t += 1
            if t > b: break
            i, j = t, r

            # Towards buttom
            while i <= b:
                res.append(matrix[i][j])
                i += 1
            r -= 1
            if l > r: break
            i, j = b, r

            # Towards left
            while j >= l:
                res.append(matrix[i][j])
                j -= 1
            b -= 1
            if t > b: break
            i, j = b, l

            while i >= t:
                res.append(matrix[i][j])
                i -= 1
            l += 1
            if l > r: break
            i, j = t, l
        return res