# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        nodes = list(range(n))
        indegree = {n: 0 for n in nodes}
        outdegree = {n: 0 for n in nodes}
        for u in nodes:
            for v in nodes:
                if u == v:
                    continue
                if knows(u, v):
                    indegree[v] += 1
                    outdegree[u] += 1
        max_knows = max(indegree.values())
        celebs = 0
        celebrity = -1
        for k in indegree.keys():
            if indegree[k] == n - 1 and outdegree[k] == 0:
                celebrity = k

        return celebrity
