from heapq import heapify, heappop, heappush


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # take a heap and queue, use heap for tasks with highest count and queue the 
        # tasks that can't be executed with timestamp for when they can bexecuted
        task_cnt = collections.Counter(tasks)
        q = deque()
        pq = [-v for v in task_cnt.values()]
        heapify(pq)
        cycles = 0
        while pq or q:
            cycles += 1
            if pq:
                cnt = -heappop(pq)
                if cnt - 1 > 0:
                    q.appendleft((cnt - 1, cycles + n))
            if q and q[-1][1] <= cycles:
                heappush(pq, -q.pop()[0])
        return cycles