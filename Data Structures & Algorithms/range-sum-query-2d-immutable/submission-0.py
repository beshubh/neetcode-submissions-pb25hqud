class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self._index = [[0]*(COLS + 1) for _ in range(ROWS + 1)]
        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                self._index[r + 1][c + 1] = prefix + self._index[r][c + 1]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1
        ans = self._index[row2][col2] - self._index[row1 - 1][col2] - self._index[row2][col1 - 1] + self._index[row1 - 1][col1- 1]
        return ans

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)