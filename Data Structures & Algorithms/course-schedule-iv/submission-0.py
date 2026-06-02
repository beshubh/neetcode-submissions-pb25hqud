

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        nodes = list(range(numCourses))

        graph = collections.defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        
        def bfs(start, target):
            q = collections.deque([start])
            visit = set()
            while q:
                u = q.pop()
                if u in visit:
                    continue
                visit.add(u)
                for v in graph[u]:
                    if v == target:
                        return True
                    if v in visit:
                        continue
                    q.appendleft(v)
            return False
        answer = [] 
        for u, v in queries:
            answer.append(bfs(u,v))
        return answer



