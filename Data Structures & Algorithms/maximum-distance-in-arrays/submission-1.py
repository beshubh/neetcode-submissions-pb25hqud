class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        max_val = arrays[0][-1]
        min_val = arrays[0][0]
        best = float('-inf')
        for i in range(1, len(arrays)):
            current_first = arrays[i][0]
            current_last = arrays[i][-1]
            best = max(best, abs(max_val - current_first), abs(current_last - min_val)) 
            max_val = max(max_val, current_last)
            min_val = min(min_val, current_first)
        return best
