import collections
from heapq import heappop,heappush

class Solution:

    def diff_by_one(self, a: str, b: str) -> bool:
        if len(a) != len(b):
            return False
        diff = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                diff += 1
        return diff <= 1

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = collections.defaultdict(list)

        if endWord not in wordList: # since end word is not there in the list
            return 0
    
        for u in wordList:
            for v in wordList:
                if u == v:
                    continue
                if self.diff_by_one(u, v):
                    graph[u].append(v)
        
        for v in wordList:
            if self.diff_by_one(beginWord, v):
                graph[beginWord].append(v)

        def bfs(start: str):
            q = collections.deque([start])
            seen = set()
            cost = 0
            while q:
                qlen = len(q)
                for _ in range(qlen):
                    v = q.pop()
                    if v == endWord:
                        return cost
                    if v in seen:
                        continue
                    seen.add(v) 
                    for nv in graph[v]:
                        if nv not in seen:
                            q.appendleft(nv)
                cost += 1
            return float('inf')
        result = bfs(beginWord)
        return result + 1 if result != float('inf') else 0

