from heapq import heappop, heappush, heapify

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_cnt = collections.Counter(tasks)
        pq = [-v for v in task_cnt.values()]
        q = collections.deque()
        t = 0
        heapify(pq)
        while pq or q:
            t += 1
            if pq:
                cnt = -heappop(pq)
                if cnt - 1 > 0:
                    q.appendleft((cnt - 1, t + n))
            if q and q[-1][1] <= t:
                heappush(pq, -q.pop()[0])
        return t