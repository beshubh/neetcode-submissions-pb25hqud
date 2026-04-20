from collections import Counter, deque
import heapq

"""

A -> 3
B -> 1
C -> 1

"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tsk_count = Counter(tasks)
        max_heap = [-x for x in tsk_count.values()]
        heapq.heapify(max_heap)
        q, t = deque(), 0
        while max_heap or q:
            t += 1
            if max_heap:
                cnt = -heapq.heappop(max_heap)
                if cnt - 1 > 0:
                    q.appendleft((cnt - 1, t + n))
            if q and q[-1][1] <= t:
                heapq.heappush(max_heap, -q.pop()[0])
        return t
