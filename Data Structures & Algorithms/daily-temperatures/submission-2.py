class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # [30,38,30,36,35,40,28]
        # [1,4,1,2,1,0,0]
        monotonic_stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures) - 1, -1, -1):
            temperature = temperatures[i]
            numdays = 0
            while monotonic_stack and temperatures[monotonic_stack[-1]] <= temperature:
                numdays += 1
                monotonic_stack.pop()
            if monotonic_stack:
                result[i] = monotonic_stack[-1] - i
            monotonic_stack.append(i)
        return result
