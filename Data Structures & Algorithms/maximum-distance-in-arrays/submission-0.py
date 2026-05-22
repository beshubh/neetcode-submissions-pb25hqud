from heapq import heappop, heappush


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        best = float('-inf')
        pq = []
        for i, arr in enumerate(arrays):
            heappush(pq, (arr[0], i))
        
        for i, arr in enumerate(arrays):
            mx = arr[-1]
            best_min = heappop(pq)
            if best_min[1] == i:
                best_min2 = heappop(pq)
                best = max(best, abs(mx - best_min2[0])) 
                heappush(pq, best_min)
                heappush(pq, best_min2)
            else:
                best = max(best, abs(mx - best_min[0]))
                heappush(pq, best_min)
        return best




