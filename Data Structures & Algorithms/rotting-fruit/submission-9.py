NEIGHBORS = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        FRESH = 1
        ROTTEN = 2
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == ROTTEN:
                    q.appendleft((r, c))
                elif grid[r][c] == FRESH:
                    fresh += 1
                
        t = 0
        while q and fresh > 0:
            qlen = len(q)
            for _ in range(qlen):
                r, c = q.pop()
                for dr, dc in NEIGHBORS:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or  nr >= ROWS or nc >= COLS:
                        continue
                    if grid[nr][nc] == FRESH:
                        grid[nr][nc] = ROTTEN
                        fresh -= 1
                        q.appendleft((nr, nc))
            t += 1
        return t if fresh == 0 else -1
