import math

class Solution:

    def get_total_hours_required(self, piles: list[int], k: int) -> int:
        hours = 0
        for b in piles:
            hours += math.ceil(b / k)
        return hours

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)
        final_k = float('inf')
        while left <= right:
            cur_k = left + ((right - left) // 2 )
            hours_reqd = self.get_total_hours_required(piles, cur_k)
            print('hours required : ', hours_reqd, ' for k: ', cur_k)
            if hours_reqd <=h:
                final_k = min(final_k, cur_k)
                right = cur_k - 1
            else:
                left = cur_k + 1
        return final_k
            
