import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = []
        for i, n in enumerate(nums[:k]):
            heapq.heappush(window, (-n, i))
        
        res = [-window[0][0]]

        for i in range(k, len(nums)):
            heapq.heappush(window, (-nums[i], i))
            while window[0][1] <= i - k:
                heapq.heappop(window)
            res.append(-window[0][0])
        return res
        