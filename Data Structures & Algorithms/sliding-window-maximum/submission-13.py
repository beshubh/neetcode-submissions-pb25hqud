from heapq import heappop, heappush


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pq = []
        for i in range(k):
            heappush(pq, (-nums[i], i))
        result = [-pq[0][0]]
        for j in range(k, len(nums)):
            if nums[j - k] == -pq[0][0]:
                while pq and pq[0][1] <= j - k:
                    heappop(pq)
            heappush(pq, (-nums[j], j))
            result.append(-pq[0][0])
        return result


        