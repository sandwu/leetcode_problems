

class Solution:
    """
    贪心算法，即一有利益就卖出，最后累计的结果即是最终结果
    因为不能当天买入和卖出，所以每买进一个，如果有收益就卖出，这样才能不断地买进卖出
    Runtime: 40 ms, faster than 99.86% of Python3 online submissions for Best Time to Buy and Sell Stock II.
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        for index,value in enumerate(prices[1:],1):
            if value > prices[index-1]:
                res += value - prices[index-1]
        return res