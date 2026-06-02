
class DSU:

    def __init__(self, nodes):
        self.rank = {node: 0 for node in nodes}
        self.parent = {node: node for node in nodes}
        print(self.parent)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        row_servers = [0] * ROWS
        col_servers = [0] * COLS
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    row_servers[r] += 1
                    col_servers[c] += 1

        result = 0 
        for r in range(ROWS):
            for c in range(COLS):
                if (row_servers[r] > 1 or col_servers[c] > 1)and grid[r][c] == 1:
                    result += 1
        return result








