import collections


NEIGHBORS = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]

class Solution:
    def orangesRotting(self, grid: list[list[int]]):
        ROWS, COLS = len(grid), len(grid[0])
        time, fresh = 0, 0
        q = collections.deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.appendleft([r, c])

        while q and fresh > 0:

            qlen = len(q)
            for _ in range(qlen):
                row, col = q.pop()
                for dr, dc in NEIGHBORS:
                    r, c = row + dr, col + dc
                    if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                        continue
                    if grid[r][c] != 1:
                        continue
                    grid[r][c] = 2
                    fresh -= 1
                    q.appendleft([r, c])
            time += 1
        return time if fresh == 0 else -1
