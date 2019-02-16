class Solution:
    """
    卡登算法，维护当前的最小值和截止目前的利润最大值，这样随着遍历就能找到截止目前的最大值
    Runtime: 40 ms, faster than 99.90% of Python3 online submissions for Best Time to Buy and Sell Stock.
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_profit = float("inf")
        tonow_max_profit = 0
        for i in prices:
            if i < min_profit:
                min_profit = i
            if i-min_profit > tonow_max_profit:
                tonow_max_profit = i - min_profit
        return tonow_max_profit


class Solution:
    """
    正常思路的优化，正常思路就是双重循环，代码做了2个优化，第1个是在第二次while的时候增加prices[i]-prices[j]>0的判断，
    可在当找到更小值时直接结束循环；第2个优化是在第一个while的if下i=j，这样虽然是双重循环，但因为i=j的骚操作，实际上也变成了
    单层循环。
    Runtime: 40 ms, faster than 99.90% of Python3 online submissions for Best Time to Buy and Sell Stock.
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = j = maxjsum = 0
        n = len(prices)
        while i < n-1:
            if prices[i] < prices[i+1]:
                j = i + 1
                while j < n and prices[j]-prices[i] > 0:
                    if prices[j] - prices[i] > 0:
                        maxjsum = max(maxjsum, prices[j]-prices[i])
                        j += 1
                i = j
            else:
                i += 1
        return maxjsum