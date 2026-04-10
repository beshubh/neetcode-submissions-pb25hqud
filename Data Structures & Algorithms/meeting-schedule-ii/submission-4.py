"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        starts = [x.start for x in intervals]
        ends = [x.end for x in intervals]
        starts.sort()
        ends.sort()
        i = j = 0
        meetings = 0
        result = 0
        while i < len(intervals) and j < len(intervals):
            if starts[i] < ends[j]:
                i += 1
                meetings += 1
            else:
                j += 1
                meetings -= 1
            result = max(result, meetings)
        return result
