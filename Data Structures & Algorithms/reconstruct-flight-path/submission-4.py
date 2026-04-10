import collections

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        graph = collections.defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst) 
        
        for u in graph:
            graph[u].sort(reverse=True)
        
        start = 'JFK'
        seen = set()
        result = []
        print(graph)
        def dfs(node):
            # consume all the neighbors
            while graph[node]:
                nxt = graph[node].pop()
                dfs(nxt)
            
            # when no outgoing edge remains
            result.append(node)
        dfs(start)
        return result[::-1]
            
