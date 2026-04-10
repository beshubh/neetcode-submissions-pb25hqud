
NEIGHBORS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visit = set()
        def bfs(r, c):
            q = collections.deque()
            q.append([r, c])
            while q:
                row, col = q.pop()
                visit.add((row, col))
                for dr, dc in NEIGHBORS:
                    r, c = row + dr, col + dc
                    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[r]):
                        continue
                    if (r, c) in visit or grid[r][c] == '0':
                        continue
                    q.appendleft([r, c])
        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if (r, c) not in visit and grid[r][c] == '1':
                    islands += 1
                    bfs(r,c)
        return islands

