class Solution:
    def trap(self, height: List[int]) -> int:
        l, r, = 0, len(height) - 1
        max_left = 0
        max_right = 0
        water_total = 0
        while l < r:
            lh = height[l]
            rh = height[r] 
            if lh <= rh:
                max_left = max(max_left, lh)
                water = max_left - lh
                l += 1
            else:
                max_right = max(max_right, rh)
                water = max_right - rh
                r -= 1
            water_total += water
        return water_total
            
                 
            