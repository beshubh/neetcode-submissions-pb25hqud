class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        new_start, new_end = newInterval[0], newInterval[1]
        result, i, n = [], 0, len(intervals)

        # all to the left
        while i < n and intervals[i][1] < new_start:
            result.append(intervals[i])
            i += 1

        # overlapping
        while i < n and intervals[i][0] <= new_end:
            new_start = min(intervals[i][0], new_start)
            new_end = max(intervals[i][1], new_end)
            i += 1
        result.append([new_start, new_end])
        # rest
        while i < n:
            result.append(intervals[i])
            i += 1
        return result
