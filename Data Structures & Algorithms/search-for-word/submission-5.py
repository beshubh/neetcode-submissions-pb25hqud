class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def exists_helper(row: int = 0, col: int = 0, word_idx: int = 0):
            if word_idx >= len(word):
                return True
            if row >= len(board) or col >= len(board[row]) or col < 0 or row < 0:
                return False
            if (row, col) not in visited and board[row][col] == word[word_idx]:
                visited.add((row, col))
                res = (
                    exists_helper(row + 1, col, word_idx + 1) or 
                    exists_helper(row - 1, col, word_idx + 1) or 
                    exists_helper(row, col + 1, word_idx + 1) or
                    exists_helper(row, col - 1, word_idx + 1)
                )
                visited.remove((row, col))
                return res

        i = 0 
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == word[0]:
                    if exists_helper(r, c, 0):
                        return True
        return False
