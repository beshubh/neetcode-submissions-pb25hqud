import heapq

class MedianFinder:

    def __init__(self):
        self._left = [] # left half, max heap of lower values
        self._right = [] # right half, min_heap of higher values

    def addNum(self, num: int) -> None:
        heapq.heappush(self._left, -num)
        heapq.heappush(self._right, -heapq.heappop(self._left))
        if len(self._right) > len(self._left):
            heapq.heappush(self._left, -heapq.heappop(self._right))

    def findMedian(self) -> float:
        if (len(self._left) + len(self._right)) % 2 == 0:
            return (-self._left[0] + self._right[0]) / 2
        return -self._left[0]
        