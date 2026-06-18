class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends_set = set(deadends)
        q = collections.deque(['0000'])
        cost = 0
        visit = set()
        while q:
            cost += 1
            qlen = len(q)
            for _ in range(qlen):
                node = q.popleft()
                if node in visit:
                    continue
                if node in deadends_set:
                    continue
                visit.add(node)
                # move every one of its character forward and backwards
                for i, c in enumerate(node):
                    forword = node[:i] + str((int(c) + 1) % 10) + node[i + 1:]
                    backword = node[:i] + str((int(c) - 1) % 10) + node[i + 1:]
                    if forword == target:
                        return cost
                    if backword == target:
                        return cost
                    if forword not in deadends_set and forword  not in visit:
                        q.append(forword)
                    if backword not in deadends_set and backword not in visit:
                        q.append(backword)
        return -1
                    
