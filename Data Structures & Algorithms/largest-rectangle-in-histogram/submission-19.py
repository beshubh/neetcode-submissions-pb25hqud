class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        best = 0
        # add a sentinel at the end, to make calculation easier, in case all heights are in increase order
        heights.append(0)
        stack = []
        for r in range(len(heights)):
            while stack and heights[stack[-1]] > heights[r]:
                # height at this rectangle
                h = heights[stack.pop()]
                left_smaller = 0 if not stack else stack[-1]
                if stack:
                    width = r - left_smaller - 1
                else:
                    width = r
                best = max(best, h*width)
            stack.append(r)
        return best
