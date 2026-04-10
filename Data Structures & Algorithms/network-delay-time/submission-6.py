from heapq import heappush, heappop

INF = float('inf')

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        return dijkstra(n, times, k)

def dijkstra(n: int, edges: list[tuple[int, int, int]], src: int) -> int:
    graph = {x: [] for x in range(1, n + 1)} # src -> (dst, weight)
    dist = {x: INF for x in graph}
    for u, v, w in edges:
        graph[u].append((v, w))
    dist[src] = 0 # starting dist is zero
    pq = [(0, src)]
    while pq:
        d, u = heappop(pq)
        if d > dist[u]: # stale entry, we had already updated distance of this node from the source
            continue
        for v, w in graph.get(u, []):
            nd = w + d
            if nd < dist[v]:
                dist[v] = nd
                heappush(pq, (nd, v))
    ans = max(dist.values())
    return ans if ans != INF else -1
