class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        M, N = len(matrix), len(matrix[0]) # 2, 2, 
        row_zero = False
        for r in range(M):
            for c in range(N):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0 # at this column, set first row to 0
                    if r > 0:
                        matrix[r][0] = 0 # at this row, set first column to 0
                    else:
                        row_zero = True

        # [ 
        # [0, 1],
        # [1, 1]
        # ]

        for r in range(1, M):
            for c in range(1, N):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(M):
                matrix[r][0] = 0

        if row_zero:
            for c in range(N):
                matrix[0][c] = 0        


        
 