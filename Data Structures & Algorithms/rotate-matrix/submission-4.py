class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        # matrix[i][j]     -> matrix[j][n-i]
        # matrix[j][n-i]   -> matrix[n-i][n-j]
        # matrix[n-i][n-j] -> matrix[n-j][i]
        # matrix[n-j][i]   -> matrix[i][j]

        # 0 <= i, j < (n + 1) // 2

        # ooo
        # ooo
        # ooo

        # n = len(matrix) - 1
        # mid_i = (n + 1) // 2 # l = 3, n = 2 -> 1, n = 1 -> 1
        # mid_j = (n + 2) // 2 # l = 3, n = 2 -> 2, n = 1 -> 1
        # print(mid_i, mid_j)
        # for i in range(mid_i):
        #     for j in range(mid_j):
        #         matrix[i][j], matrix[j][n-i], matrix[n-i][n-j], matrix[n-j][i] \
        #          = matrix[n-j][i], matrix[i][j], matrix[j][n-i], matrix[n-i][n-j]
        # return matrix

        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l):
                matrix[l][l + i], matrix[l + i][r], matrix[r][r - i], matrix[r - i][l]\
                    = matrix[r - i][l], matrix[l][l + i], matrix[l + i][r], matrix[r][r - i]
                # (0, 0), (0, 1), (1, 1), (1, 0)
            l += 1
            r -= 1
        return 