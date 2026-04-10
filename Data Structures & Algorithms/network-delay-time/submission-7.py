from typing import List
import collections
from heapq import heappop, heappush


INF = float('inf')

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))

        def dijkstra(graph: dict[int, list[int]], start_node: int):
            pq = [(0, start_node)]
            dist = collections.defaultdict(lambda : INF)
            dist[start_node] = 0
            while pq:
                w, u = heappop(pq)
                if w > dist[u]:
                    continue
                for v, nw in graph.get(u, []):
                    nd = w + nw
                    if dist[v] > nd:
                        dist[v] = nd
                        heappush(pq, (nd, v))
            return max(dist.values()) if len(dist) == n else -1
        return dijkstra(graph, k)
                    

