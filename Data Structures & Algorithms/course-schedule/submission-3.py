class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {x: [] for x in range(numCourses)}
        for u, v in prerequisites:
            graph[v].append(u) 

        # 0: unvisited
        # 1: visiting
        # 2: visited
        visit = {u: 0 for u in graph.keys()}

        def cycle(node):
            if visit[node] == 2:
                return False
            if visit[node] == 1:
                return True
            visit[node] = 1 
            for nei in graph.get(node, []):
                if cycle(nei):
                    return True
            visit[node] = 2
            return False
        
        for node in graph.keys():
            if visit[node] == 0:
                if cycle(node):
                    return False
        return True