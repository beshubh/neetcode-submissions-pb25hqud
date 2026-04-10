"""
Definition of Interval
"""


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        start = [s.start for s in intervals]
        end = [s.end for s in intervals]
        start.sort()
        end.sort()
        # start = [0, 5, 15]
        # end = [10, 20, 40]

        s, e = 0, 0 # 3, 0
        count = 0 # 2
        while s < len(intervals) and e < len(intervals):
            # meeting starts before the earliest one ends
            if start[s] < end[e]: # 15 < 10 no
                s += 1
                count += 1
            else:
                s += 1
                e += 1
        return count
