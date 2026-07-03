class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        # array: [10, 6, 8, 5, 11, 9]
        # index: [0, 1, 2, 3, 4, 5, 6]
        # stack: [11]
        # agg:   [3, 1, 2, 1, 1, 0]
        monotonic_stack = []
        answer = [0] * len(heights)
        for i in range(len(heights) - 1, -1, -1):
            h = heights[i]
            people_h_can_see = 0
            while monotonic_stack and monotonic_stack[-1] < h:
                monotonic_stack.pop()
                people_h_can_see += 1
            if monotonic_stack:
                people_h_can_see += 1
            answer[i] = people_h_can_see
            monotonic_stack.append(h)
        return answer
