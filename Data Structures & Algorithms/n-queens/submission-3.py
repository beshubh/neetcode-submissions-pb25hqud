class Solution:

    def can_place(self, row: int, col: int, grid: list[list[int]]) -> bool:
        # we just need to check the upper left diagonal and upper right diagonal
        # upper left diagonal, (reduce row by 1 and column by 1) 
        r = row
        for c in range(col, -1, -1):
            if r >= 0 and grid[r][c] == 'Q':
                return False
            r -= 1
        
        # upper right diagonal (reduce the row, increase teh column by 1)
        c = col
        for r in range(row, -1, -1):
            if c < len(grid) and grid[r][c] == 'Q':
                return False
            c += 1
        # same column 
        for r in range(len(grid)):
            if grid[r][col] == 'Q':
                return False
        # same row
        for c in range(len(grid)):
            if grid[row][c] == 'Q':
                return False
        return True
    
    def format_output(self, grid: list[list[int]]) -> list[str]:
        return [''.join(x) for x in grid]

    def solveNQueens(self, n: int) -> List[List[str]]:
        # let's place everything row by row
        grid = [['.' for _ in range(n)] for _ in range(n)]
        result = []
        def place(row: int):
            if row == n:
                # found a valid solution
                result.append(self.format_output(grid))
                return
            # try placing at every col in this row
            for col in range(n):
                if self.can_place(row, col, grid):
                    grid[row][col] = 'Q'
                    place(row + 1)
                    grid[row][col] = '.'
                
        place(0)
        return result 



        