class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int: # [1, 1]
        if len(heights) == 1:
            return heights[0]

        res = 0
        # n = 2
        for i, h in enumerate(heights):
            left, right = i, i # 0, 0
            while left > 0 and heights[left - 1] >= h: # 0 >= 0, 1 >= 1
                left -= 1

            while right  + 1 < len(heights) and heights[right + 1] >= h: # 1 < 2 and 1 <= 1
                right += 1
            # right = 2
            width = right - left  + 1  # 2 - 0 - 1 = 2 - 1 = 1
            height = h
            res = max(width * height, res) # max(0, 7 * 1) = 7
        return res
