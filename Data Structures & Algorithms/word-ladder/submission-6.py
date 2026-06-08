import collections

class Solution:

    def diff_by_one(self, a, b):
        if len(a) != len(b):
            return False
        diff = 0
        i = 0
        while i < len(a):
            if a[i] != b[i]:
                diff += 1
            i += 1
        return diff == 1

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        graph = collections.defaultdict(set)
        if endWord not in wordList:
            return 0

        for u in wordList:
            for v in wordList:
                if self.diff_by_one(u, v):
                    graph[u].add(v)

        for word in wordList:
            if self.diff_by_one(beginWord, word):
                graph[beginWord].add(word)

        # bfs
        q = collections.deque([beginWord])
        visit = set()
        cost = 0
        print(graph)
        while q:
            qlen = len(q)
            for _ in range(qlen):
                curr = q.pop()
                if curr == endWord:
                    return cost + 1
                if curr in visit:
                    continue
                visit.add(curr)
                for nei in graph[curr]:
                    if nei in visit:
                        continue
                    q.appendleft(nei)
            
            cost += 1
        return 0

