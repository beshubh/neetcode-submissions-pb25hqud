class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:

        monotonic_stack = []
        heights.append(0)
        answer = 0
        for i in range(len(heights)):
            h = heights[i]
            while monotonic_stack and heights[monotonic_stack[-1]] >= h:
                popped_idx = monotonic_stack.pop()
                height = heights[popped_idx]
                left = -1
                if monotonic_stack:
                    left = monotonic_stack[-1]
                width = i - left - 1
                answer = max(answer, height * width)
            monotonic_stack.append(i)
        return answer
