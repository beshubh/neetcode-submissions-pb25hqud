from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        max_heap = [-x for x in counter.values()]
        heapq.heapify(max_heap)
        q, t = deque(), 0
        while max_heap or q:
            t += 1
            if max_heap:
                task_cnt = -heapq.heappop(max_heap)
                if task_cnt - 1 > 0:
                    q.appendleft((task_cnt - 1, t + n))
            if q and q[-1][1] <= t:
                heapq.heappush(max_heap, -q.pop()[0])
        return t
