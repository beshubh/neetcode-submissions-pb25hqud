class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = l = 0
        # [10,1,5,6,7,1]
        for r in range(len(prices)):
            if prices[l] < prices[r]:
                profit = max(profit, prices[r] - prices[l])
            else:
                l = r
        return profit
