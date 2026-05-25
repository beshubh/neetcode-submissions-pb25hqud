import collections
from heapq import heappush, heappop

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf') 
        # dijsktra
        pq = [(0, src, 0)] # to get to the source i have 0 cost and used no flights
        dist = collections.defaultdict(lambda: INF)

        graph = collections.defaultdict(list)
        for u, v, p in flights:
            graph[u].append((v, p))
        
        while pq:
            cost, current, flights_used = heappop(pq)
            if dist[(current, flights_used)] < cost:
                continue

            if current == dst and flights_used <= k + 1:
                return cost

            if flights_used == k + 1:
                continue # already done too many stops

            for v, np in graph.get(current, []):
                ncost = cost + np
                if dist[(v, flights_used + 1)] > ncost:
                    dist[((v, flights_used + 1))] = ncost
                    heappush(pq, (ncost, v, flights_used + 1))
        return -1