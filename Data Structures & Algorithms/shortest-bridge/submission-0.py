from collections import deque


NEIGHBORS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        seen = set()
        def dfs(r, c):
            global NEIGHBORS
            if (r, c) in seen:
                return
            
            seen.add((r, c))
            for dr, dc in NEIGHBORS:
                row, col = r + dr, c + dc
                if (
                    row >= 0 and row < N and col >= 0 and col < N and
                    (row, col) not in seen  and
                    grid[row][col] == 1
                ):
                    dfs(row, col)
        
        found = False
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    found = True
                    dfs(r, c)
                    break
            if found:
                break
    
        q =  deque()
        for r, c in seen:
            q.append((r, c))
        cost = 0
        seen2 = set() # [(0, 1)]
        print('queue: ', q)
        NEIGHBORS = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]

        while q: # [(1, 1)]
            qlen = len(q)
            for _ in range(qlen):
                r, c = q.pop() # 1, 1
                if (r, c) in seen2: # no
                    continue
                seen2.add((r, c)) 
                for dr, dc in NEIGHBORS:
                    row, col = r + dr, c + dc # 1, 2
                    if (
                        row >= 0 and row < N and col >= 0 and col < N and 
                        (row, col) not in seen2
                    ):
                        if grid[row][col] == 1 and (row, col) not in seen: # 
                            return cost
                        if grid[row][col] == 0: #
                            q.appendleft((row, col))
            cost += 1
        return -1
        