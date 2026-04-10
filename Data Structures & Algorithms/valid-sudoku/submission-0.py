from collections import defaultdict


VALID = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '.']

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return valid_sudoku(board)


def small_board_valid(board: list[list[str]], i_start: int, j_start: int) -> bool:
    visited: set = set()

    for row in range(i_start, i_start + 3, 1):
        for col in range(j_start, j_start + 3, 1):
            # row will stay same for all col's here
            # check for duplicates in a column
            val = board[row][col]
            if val in visited:
                return False

            # check for duplicates in a row
            if val in visited:
                return False

            if not val in VALID:
                return False

            if val != '.':
                visited.add(val)

    return True


def valid_sudoku(board: list[list[str]]) -> bool:
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not small_board_valid(board, i, j):
                return False
    visited_in_columns = defaultdict(set)

    for row in range(0, 9, 1):
        visited_in_this_row = set()
        for col in range(0, 9, 1):
            val = board[row][col]
            if val in visited_in_columns[col]:
                return False
            if val in visited_in_this_row:
                return False
            if not val in VALID:
                return False
            if val != '.':
                visited_in_columns[col].add(val)
                visited_in_this_row.add(val)
    return True
