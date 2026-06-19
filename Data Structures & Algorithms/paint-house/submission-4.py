class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = [[10e9 for _ in range(3)] for _ in range(len(costs) + 1)]
        for j in range(3):
            dp[len(costs)][j] = 0
        for i in range(len(costs) - 1, -1, -1):
            for j in range(3):
                for k in range(3):
                    if k == j:
                        continue
                    dp[i][j] = min(dp[i][j], costs[i][j] + dp[i + 1][k])
        return min(dp[0])
