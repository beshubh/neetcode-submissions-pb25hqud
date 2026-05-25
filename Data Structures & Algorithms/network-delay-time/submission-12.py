from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        pq = [(0, k)]
        dist = defaultdict(lambda: float('inf'))
        graph = {u: set() for u in range(1, n + 1)}
        for u, v, t in times:
            graph[u].add((v, t))
        dist[k] = 0
        while pq:
            d, current = heappop(pq)
            if dist[current] < d:
                continue
            
            for v, t in graph.get(current, {}):
                nd = d + t
                if dist[v] > nd:
                    dist[v] = nd
                    heappush(pq, (nd, v))
        
        return max(dist.values()) if len(dist) == n else -1
