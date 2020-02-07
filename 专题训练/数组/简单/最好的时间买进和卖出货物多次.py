


class Solution:
    def maxProfit(self,prices):
        #只能买一次用动态规划，买多次用贪心算法
        res = 0
        for i,v in enumerate(prices[1:],1):
            if v > prices[i-1]:
                res += v - prices[i-1]
        return res


prices = [1,2,3,4,5]
a = Solution()
a.maxProfit(prices)