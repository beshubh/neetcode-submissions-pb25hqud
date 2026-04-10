
NEIGHBORS = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0]) 
        INF = 2147483647
        gates = []
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    gates.append([r, c])

        def bfs(r, c):
            q = collections.deque([(r, c)])
            visit = set()
            while q:
                row, col = q.pop()
                visit.add((row, col))
                for dr, dc in NEIGHBORS:
                    r, c = row + dr, col + dc
                    if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                        continue
                    if (r, c) in visit:
                        continue
                    if grid[r][c] > 0:
                        grid[r][c] = min(grid[r][c], 1 + grid[row][col])
                        q.appendleft((r, c))
        for r, c in gates:
            bfs(r, c)
