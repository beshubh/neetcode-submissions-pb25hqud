
class DSU:
    def __init__(self, nodes) -> None:
        self.rank = {node: 0 for node in nodes}
        self.parent = {node: node for node in nodes}
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a, b):
        parent_a, parent_b = self.find(a), self.find(b)
        if parent_a == parent_b:
            return False
        
        if self.rank[parent_a] < self.rank[parent_b]:
            parent_a, parent_b = parent_b, parent_a
        
        self.parent[parent_b] = parent_a
        if self.rank[parent_b] == self.rank[parent_a]:
            self.rank[parent_a] += 1
        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        nodes = []
        email_map = {}
        for account in accounts:
            for f in account[1:]:
                nodes.append(f)
                email_map[f] = account[0]
        dsu = DSU(nodes) 
        for account in accounts:
            email = account[1]
            for f in account[2:]:
                dsu.union(email, f)
        print('email map', email_map)
        email_group = collections.defaultdict(list)
        for email in nodes:
            root = dsu.find(email)
            email_group[root].append(email)
        
        print('email group', email_group)
        result = []
        for k in email_group.keys():
            v = email_group[k]
            v.sort()
            v = list(set(v))
            result.append([email_map[k], *v])
        return result
            
