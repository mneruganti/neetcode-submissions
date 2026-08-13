class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        # [1, 2] -> [3, 1]
        # [3, 4] -> [4, 2]

        # [0, 0] -> [0, 1]  [0, 1] -> [1, 1]
        # [1, 0] -> [0, 0]  [1, 1] -> [1, 0]


        # [1, 2, 3]    [7, 4, 1]
        # [4, 5, 6] -> [8, 5, 2]
        # [7, 8, 9]    [9, 6, 3]

        # [0, 0] -> [0, 2]  [0,1] -> [1, 0]   [0,2] -> [2, 2]
        # [1, 0] -> [0, 1]  [1,1] -> [1, 1]   [1,2] -> [2, 1]
        # [2, 0] -> [2, 2]  [2,1] -> [2, 1]   [2,2] -> [2, 0]

        # Transpose - make rows the columns (bottom row becomes first column)
        # Formula: (col, n - 1 - row)
        # Transpose across the diagonal (matrix[r][c], matrix[c][r] = matrix[c][r],matrix[r][c])
        # reverse the matrix (matrix.reverse())

        n = len(matrix) # 2
        for r in range(n):
            for c in range(r, n):  # ← start at r, not 0
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
            matrix[r].reverse()

        