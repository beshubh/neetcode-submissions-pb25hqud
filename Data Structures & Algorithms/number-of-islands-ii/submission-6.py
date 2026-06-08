class DSU:

    def __init__(self)-> None:
        self.parent = {}
        self.rank = {}
        self.components = 0
    
    def add(self, node):
        self.parent[node] = node
        self.rank[node] = 0
        self.components += 1
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a, b):
        parent_a, parent_b  = self.find(a), self.find(b)
        if parent_a == parent_b:
            # already connected
            return False
        if self.rank[parent_a] < self.rank[parent_b]:
            parent_a, parent_b = parent_b, parent_a
        self.parent[parent_b] = parent_a
        self.rank[parent_a] += 1
        self.components -= 1
        return True
 
NEIGHBOURS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        dsu = DSU()
        answer = []
        land = set()
        for (r, c) in positions:
            if (r, c) in land:
                answer.append(dsu.components)
                continue
            dsu.add((r, c))
            land.add((r, c))
            for dr, dc in NEIGHBOURS:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue
                if (nr, nc) in land:
                    dsu.union((r, c), (nr, nc))
            answer.append(dsu.components)
        return answer
            
        














