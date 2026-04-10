class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        prev_end = intervals[0][1]
        overlaps = 0
        for start, end in intervals[1:]:
            if start < prev_end:
                overlaps += 1
                prev_end = min(end, prev_end)
            else:
                prev_end = end
        return overlaps
