class Solution(object):

    def maxProfit(self, prices):
        max_profit = 0
        min_buy = float("inf")

        for price in prices:
            min_buy = min(min_buy, price)
            max_profit = max(max_profit, price - min_buy)
        return max_profit


prices = [2, 4, 1]
a = Solution()
print(a.maxProfit(prices))
