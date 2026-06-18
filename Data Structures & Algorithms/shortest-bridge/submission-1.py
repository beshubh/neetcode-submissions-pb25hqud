

NEIGHBORS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int: 
        q = collections.deque()        
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r: int, c: int):
            if (r, c) in visit:
                return
            q.append((r, c))
            visit.add((r, c))
            for dr, dc in NEIGHBORS:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                    continue
                if (nr, nc) in visit:
                    continue
                if grid[nr][nc] == 1:
                    dfs(nr, nc)
        done = False 
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    done = True
                    dfs(r, c)
                    break
            if done:
                break
        cost = 0
        visit2 = set() 
        while q:
            qlen = len(q)
            for _ in range(qlen):
                r, c = q.popleft()
                if (r, c) in visit2:
                    continue
                visit2.add((r, c))
                for dr, dc in NEIGHBORS:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                        continue
                    if (nr, nc) in visit2:
                        continue
                    if grid[nr][nc] == 1 and (nr, nc) not in visit:
                        return cost
                    q.append((nr, nc))
            cost += 1
        return -1
