import collections


class Solution:

    def diff_by_one(self, s1, s2) -> bool:
        diff = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff += 1
        return diff == 1

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        graph = collections.defaultdict(list)
        for u in wordList:
            for v in wordList:
                if u == v:
                    continue
                if self.diff_by_one(u, v):
                    graph[u].append(v)

        def bfs(src: str) -> int:
            visited = {src}
            q = collections.deque([(src, 0)])
            while q:
                current, d = q.pop()
                if current == endWord:
                    return d
                for nei in graph.get(current, []):
                    if nei not in visited:
                        visited.add(nei)
                        q.appendleft((nei, d + 1))
            return -1

        minladder = float('inf')
        for node in graph:
            if self.diff_by_one(node, beginWord):
                shortest_distance = bfs(node)
                if shortest_distance != -1:
                    minladder = min(minladder, shortest_distance)
                    
        return minladder + 2 if minladder != float('inf') else 0

