class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        best, stack = 0, []
        heights.append(0) # sentinel 0 height
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                # height of the rectangle
                h = heights[stack.pop()]
                # smaller on the left
                left_smaller = -1 if not stack else stack[-1]
                # current is the smaller on right
                width = i - left_smaller - 1
                best = max(best, h * width)
            stack.append(i)
        return best