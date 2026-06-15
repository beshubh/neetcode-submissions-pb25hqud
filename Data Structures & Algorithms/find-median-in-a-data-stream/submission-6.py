from heapq import heappop, heappush

class MedianFinder:

    def __init__(self):
        self._left = [] # max heap
        self._right = [] # min heap
        # median is max from left and min from the right 

    def addNum(self, num: int) -> None:
        heappush(self._left, -num) 
        heappush(self._right, -heappop(self._left))
        if len(self._right) > len(self._left):
            heappush(self._left, -heappop(self._right)) 

    def findMedian(self) -> float:
        if (len(self._left) + len(self._right)) % 2 == 0:
            return (-self._left[0] + self._right[0]) / 2
        return -self._left[0]
    