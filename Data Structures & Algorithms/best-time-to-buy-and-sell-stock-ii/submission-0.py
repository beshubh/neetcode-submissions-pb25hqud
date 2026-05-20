class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = prices[0]
        max_so_far = prices[0]
        profit = 0
        for i in range(len(prices)):
            price = prices[i]
            if price < min_so_far:
                # buy
                min_so_far = price
                max_so_far = price
            elif price >= max_so_far:
                # sell
                profit += price - min_so_far
                min_so_far = price
                max_so_far = price
        return profit