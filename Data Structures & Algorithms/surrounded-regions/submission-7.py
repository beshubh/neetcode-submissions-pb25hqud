

NEIGHBORS = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        def bfs(r, c):
            ROWS, COLS = len(board), len(board[r])
            q = collections.deque([[r, c]])
            board[r][c] = 'T'
            while q:
                row, col = q.pop()
                for dr, dc in NEIGHBORS:
                    r, c = row + dr, col + dc
                    if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                        continue
                    if board[r][c] == 'O':
                        print('r, c', r, c, 'is O')
                        board[r][c] = 'T'
                        q.appendleft([r, c])
        
        for r in range(len(board)):
            for c in range(len(board[r])):
                if r == 0 or c == 0 or r == len(board) - 1 or c == len(board[r]) - 1:
                    if board[r][c] == 'O':
                        print('calling bfs: ', r, c)
                        bfs(r, c)

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
        