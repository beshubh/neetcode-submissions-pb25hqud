class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = {}
        nums = [1] + nums + [1]
        def dfs(l, r):
            if l > r:
                return 0
            key = (l, r)
            if key in dp:
                return dp[key]
            dp[key] = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                dp[key] = max(coins, dp[key])
            return dp[key]
        return dfs(1, len(nums) - 2)
