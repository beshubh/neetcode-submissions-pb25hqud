from heapq import heappop, heappush, heapify
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        [9,10,9,-7,-4,-8,2,-6]

        q: [-7, -4, -8, 2, -6]
        heap: [9, -4, -7]

        => 10, 10, 9, 9
        """
        if k > len(nums):
            raise ValueError('invalid input')
        q = collections.deque([nums[i] for i in range(k)])
        pq = [(-nums[i], i) for i in range(k)]
        heapify(pq)
        result = [-pq[0][0]] 
        for i in range(k, len(nums)):
            dropped = q.popleft()
            if dropped == -pq[0][0]:
                heappop(pq)
            q.append(nums[i])
            heappush(pq,(-nums[i], i))
            while pq[0][1] < i - k:
                heappop(pq)
            result.append(-pq[0][0])
        return result
