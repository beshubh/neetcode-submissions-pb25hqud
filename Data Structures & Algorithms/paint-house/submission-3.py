class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        cache = {}
        def inner(i: int, prev: int):
            if i >= len(costs):
                return 0
            key = (i, prev)
            if key in cache:
                return cache[key]
            result = 10e9 
            for j in range(3):
                if prev == j:
                    continue
                result = min(costs[i][j] + inner(i + 1, j), result)
            cache[key] = result
            return result

        return inner(0, -1)
