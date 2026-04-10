

class DSU:

    def __init__(self, n: int):
        self.parent = [i for i in range(n + 1)]
        self.rank = [0 for _ in range(n + 1)]
    
    def find(self, x: int):
        if self.parent[x] != x:
            return self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a: int, b: int) -> bool:
        parent_a, parent_b = self.find(a), self.find(b)
        if parent_a == parent_b:
            # connected by the same parent
            return False

        if self.rank[parent_a] < self.rank[parent_b]:
            parent_a, parent_b = parent_b, parent_a
    
        self.parent[parent_b] = parent_a
        if self.rank[parent_a] == self.rank[parent_b]:
            self.rank[parent_a] += 1
        return True



class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))
        for u, v in edges:
            if not dsu.union(u, v):
                return [u, v]


        