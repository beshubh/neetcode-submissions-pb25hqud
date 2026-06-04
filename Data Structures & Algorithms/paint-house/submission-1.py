class Solution:
    def minCost(self, costs: List[List[int]]) -> int:

        dp = [[None for _ in range(3)] for _ in range(len(costs))]
        INF = float('inf')
        def inner(i: int, prev_color: int | None) -> int:
            if i >= len(costs):
                return 0
            if prev_color is not None and dp[i][prev_color] is not None:
                return dp[i][prev_color]
            result = 10e9
            for color in range(3):
                if color == prev_color:
                    continue
                result = min(result, costs[i][color] + inner(i + 1, color))
            if prev_color is not None:
                dp[i][prev_color] = result
            return result
        return inner(0, None)
