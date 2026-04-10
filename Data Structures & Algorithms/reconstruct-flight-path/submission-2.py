import collections
from heapq import heappop, heappush


INF = float('inf')


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        SRC = 'JFK'
        for u, v in tickets:
            graph[u].append(v)
        
        for u in graph:
            graph[u].sort(reverse=True)  # this will give minimum element in O(1)
        route = []
        
        def dfs(airport: int) -> None:
            while graph[airport]:
                nxt = graph[airport].pop() # smallest value
                dfs(nxt)
            route.append(airport)
        
        dfs(SRC)
        return route[::-1]
        
