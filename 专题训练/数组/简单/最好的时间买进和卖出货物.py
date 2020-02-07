


class Solution:
    def maxprofit(self,prices):
        min_profit = float("inf")
        tonow_max_profit = 0
        for i in prices:
            min_profit = min(i,min_profit)
            tonow_max_profit = max(tonow_max_profit,i-min_profit)
        return tonow_max_profit