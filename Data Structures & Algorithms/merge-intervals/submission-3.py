class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        result, i, n = [], 1, len(intervals)
        # take a start and end
        s, e = intervals[0]
        while i < n:
            cur_start, cur_end = intervals[i]
            # overlap
            if cur_start <= e:
                s = min(s, cur_start)
                e = max(e, cur_end)
            else:
                result.append([s, e])
                s, e = cur_start, cur_end
            i += 1
        result.append([s, e])
        return result
