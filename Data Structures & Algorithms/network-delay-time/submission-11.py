from heapq import heappop, heappush

INF = float('inf')


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append([v, w])
    
        pq = [(0, k)]
        dist = collections.defaultdict(lambda: INF)
        dist[k] = 0
        while pq:
            d, u = heappop(pq)
            if dist[u] < d:
                continue
            for v, nw in graph[u]:
                nd = d + nw
                if dist[v] > nd:
                    dist[v] = min(dist[v], nd)
                    heappush(pq, (nd, v))
        return max(dist.values()) if len(dist) == n else -1

