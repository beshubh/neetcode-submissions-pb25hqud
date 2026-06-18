class DSU:

    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}
        self.rank = {node: 0 for node in nodes}
    
    def find(self, n):
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]
    
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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_name_map = {}
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                email_name_map[email] = name
        
        dsu = DSU(email_name_map.keys())
        for account in accounts:
            email = account[1]
            for rest in account[2:]:
                dsu.union(email, rest)
        interim = collections.defaultdict(set)
        for account in accounts:
            for email in account[1:]:
                parent = dsu.find(email)
                interim[parent].add(email)
        result = [] 
        for key, values in interim.items():
            values = sorted(list(values))
            result.append(
               [email_name_map[key], *values] 
            )
        return result






















