"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        
        intervals.sort(key = lambda v: v.start)
        prev_end = intervals[0].end
        for interval in intervals[1:]:
            next_begins = interval.start
            if next_begins < prev_end:
                return False
            else:
                prev_end = interval.end
        return True