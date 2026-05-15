class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        best = 0
        stack = []
        heights.append(0) # sentinel
        for r in range(len(heights)):
            while stack and heights[stack[-1]] > heights[r]:
                # height of the rectangle
                h = heights[stack.pop()]
                # left smaller
                left_smaller = 0 if not stack else stack[-1]
                if stack:
                    width = r - left_smaller - 1
                else:
                    width = r
                best = max(h*width, best)
            stack.append(r) 
        return best
