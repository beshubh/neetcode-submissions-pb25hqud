import collections


class Solution:

    def diff_by_one(self, a, b):
        if len(a) != len(b):
            return False
        diff = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                diff += 1
        return diff == 1
        

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = collections.defaultdict(set)
        for u in wordList:
            for v in wordList:
                if self.diff_by_one(u, v):
                    graph[u].add(v)
        
        for word in wordList:
            if self.diff_by_one(beginWord, word):
                graph[beginWord].add(word)
        

        def bfs(start):
            q = collections.deque([start])
            dist = 0
            visit = set()
            while q:
                qlen = len(q)
                for _ in range(qlen):
                    u = q.pop()
                    if u == endWord:
                        return dist
                    if u in visit:
                        continue
                    visit.add(u)
                    for v in graph[u]:
                        if v in visit:
                            continue
                        q.appendleft(v)
                dist += 1
            return None
        
        result = bfs(beginWord)
        if result:
            return result + 1
        return 0

        