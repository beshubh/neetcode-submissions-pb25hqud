class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        def max_profit(i: int, buying: bool = True):
            # gives me the maximum profit if I buy or sell at i
            if i >= len(prices):
                return 0
            
            if buying:
                buy =  max_profit(i + 1, False) - prices[i]
                skip = max_profit(i + 1, buying)
                return max(buy, skip)
            else:
                sell = prices[i] + max_profit(i + 2, True)
                hold = max_profit(i + 1, buying)
                return max(sell, hold)
        return max_profit(0)
