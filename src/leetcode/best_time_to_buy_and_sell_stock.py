class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maximum = 0
        lowest = prices[0]
        for price in prices:
            maximum = max(max, price - lowest)
            lowest = min(lowest, price)
        return maximum
