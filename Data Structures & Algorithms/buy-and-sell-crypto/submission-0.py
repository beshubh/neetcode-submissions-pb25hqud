class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b, s = 0, 1
        max_profit = 0
        while b < len(prices) and s < len(prices):
            if prices[b] >= prices[s]:
                b = s
                s += 1
            else:
                max_profit = max(max_profit, prices[s] - prices[b])
                s += 1
        return max_profit
             