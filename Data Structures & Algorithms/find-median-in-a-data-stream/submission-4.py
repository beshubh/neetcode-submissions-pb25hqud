import heapq

class MedianFinder:

    def __init__(self):
        self._lowerhalf = [] # contains more elements than upperhalf, is max heap, all elements are less <= median
        self._upperhalf = [] # contains less elements than lowerhalf, is min heap, all elements are >= median 
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self._lowerhalf, -num) # push everything to lower half
        # pop the maximum from lowerhalf and push to upperhalf, to maintain the variant X <= Y for all x belonging to lowerhalf, all y belonging to upperhalf
        heapq.heappush(self._upperhalf, -heapq.heappop(self._lowerhalf))

        # maintaint all lowerhalf items <= upperhalf items and |lowerhalf| ~ |upperhalf|
        if len(self._upperhalf) > len(self._lowerhalf):
            # the variant lowerhalf <= upperhalf remains true because upper half is a min heap, poping the top will gives the minimum element
            # meaining lowerhalf will contain all the elements less than or equal to the upperhalf
            heapq.heappush(self._lowerhalf, -heapq.heappop(self._upperhalf))

    def findMedian(self) -> float:
        if (len(self._lowerhalf) + len(self._upperhalf)) % 2 == 0:
            return (-self._lowerhalf[0] + self._upperhalf[0]) / 2
        return -self._lowerhalf[0]

        