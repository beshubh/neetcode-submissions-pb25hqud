class Solution:

    def can_place(self, board: list[list[str]], row: int, col: int):
        assert row >= 0 and col >= 0 
        assert row < len(board) and col < len(board)
        if board[row][col] == 'Q':
            return False
        # if we are going row by row, that we don't really need to check bottom
        # left and right diagonals

        # this row
        for c in range(len(board)):
            if board[row][c] == 'Q':
                return False
            
        # this column
        for r in range(len(board)):
            if board[r][col] == 'Q':
                return False

        # left top diagonal
        r = row
        for c in range(col, -1, -1):
            if r >= 0 and board[r][c] == 'Q':
                return False
            r -= 1

        # right top diagonal
        r = row
        for c in range(col, len(board), 1):
            if r >= 0 and board[r][c] == 'Q':
                return False
            r -= 1

        return True
    
    def format_board(self, b: list[list[str]]):
        return [''.join(r) for r in b]

    def solveNQueens(self, n: int) -> List[List[str]]: 
        result = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        def place_queens(board: list[list[str]], row: int = 0):
            # we will be going row by row and for each row we will check all the columns
            # and try place at that [row, col]

            if row == n:
                # this can only happen when we have place n queens, because we only increment row
                # after placing a queen
                result.append(self.format_board(board))
                return
            for col in range(len(board)):
                if self.can_place(board, row, col):
                    board[row][col] = 'Q'
                    place_queens(board, row + 1) # as we can't place in this same row again
                    board[row][col] = '.' # if we couldn't make a valid solution
        place_queens(board)
        return result
                




