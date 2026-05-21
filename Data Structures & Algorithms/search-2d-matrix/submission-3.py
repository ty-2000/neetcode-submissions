class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # Binary search in row-axis: i.e. to determine in which row the target exists
        # Then search in column-axis
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m - 1
        while l < r:
            # Keep the possibility that the target exists in matrix[l] ~ matrix[r]
            z = (l + r + 1) // 2 # 0, 1 => 1
            if matrix[z][0] < target:
                # target might exist in matrix[z] ~ matrix[r]
                l = z
            elif matrix[z][0] > target:
                # target might exist in matrix[l] ~ matrix[z - 1]
                r = z - 1
            else:
                return True
        
        row = l
        l, r = 0, n
        while l < r:
            # Keep the possibility that the target exists in row[l] ~ row[r - 1]
            z = (l + r) // 2 # 2,3 => 2; 3,4 => 3
            if matrix[row][z] < target:
                # target might exist in matrix[z] ~ matrix[r]
                l = z + 1
            elif matrix[row][z] > target:
                # target might exist in matrix[l] ~ matrix[z - 1]
                r = z
            else:
                return True
        return False