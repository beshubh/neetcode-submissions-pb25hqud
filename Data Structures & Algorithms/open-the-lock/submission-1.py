from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # '0000' -> '1000', '0100', '0010', '0001'
        visit = set()
        deadends_set = set(deadends)
        q = deque(['0000'])
        cost = 0
        while q:
            qlen = len(q)
            cost += 1
            for _ in range(qlen):
                node = q.pop()
                if node in deadends:
                    return -1
                if node in visit:
                    continue
                visit.add(node)
                for i, c in enumerate(node):
                    forward = node[:i] + str((int(c) + 1) % 10) + node[i + 1:]
                    backward = node[:i] + str((int(c) - 1) % 10) + node[i + 1:]
                    if forward == target:
                        return cost
                    if backward == target:
                        return cost
                    if forward not in deadends and forward not in visit:
                        q.appendleft(forward)
                    if backward not in deadends and backward not in visit:
                        q.appendleft(backward)
        return -1