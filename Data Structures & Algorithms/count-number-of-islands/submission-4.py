
class DSU:

    def __init__(self, nodes) -> None:
        self.parents = {node: node for node in nodes}
        self.rank = {node: 0 for node in nodes}
    
    def find(self, node):
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]
    
    def union(self, a, b):
        # connect a and b
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            # a and b are already connected
            return False
        if self.rank[pa] < self.rank[pb]:
            pa, pb = pb, pa
        self.parents[pb] = pa
        self.rank[pa] += 1
        return True

NEIGHBORS = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dsu = DSU([(r, c) for r in range(len(grid)) for c in range(len(grid[r]))])
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1':
                    for dr, dc in NEIGHBORS:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < len(grid) and 0 <= nc < len(grid[r]) and grid[nr][nc] == '1':
                            dsu.union((r, c), (nr, nc))

        groups = collections.defaultdict(list)
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1':
                    root = dsu.find((r, c))
                    groups[root].append((r, c))
        print(groups) 
        return len(groups.keys())

