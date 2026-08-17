import collections

class Solution:
    def diff_by_one(self, a, b: str):
        if len(a) != len(b):
            return False
        diff = 0 
        for i in range(len(a)):
            if diff > 1:
                return False
            if a[i] != b[i]:
                diff += 1
        return diff == 1

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        graph = collections.defaultdict(list) 
        for u in wordList:
            for v in wordList:
                if u == v:
                    continue
                if self.diff_by_one(u, v):
                    graph[u].append(v)
        
        for u in wordList:
            if self.diff_by_one(u, beginWord):
                graph[beginWord].append(u)
    
        def bfs():
            start = beginWord
            q = collections.deque([start])
            seen = set([start])
            length = 1
            while q:
                for _ in range(len(q)):
                    u = q.popleft()
                    if u == endWord:
                        return length
                    for v in graph[u]:
                        if v not in seen:
                            q.append(v)
                            seen.add(v)
                length += 1
            return 0
        return bfs()
        







