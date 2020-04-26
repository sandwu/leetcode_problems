# 本质是自下而上、状态转移方程、

import bisect
import heapq
"""
01背包问题
cw表示当前已经装进去的物品的重量和；i表示考察到哪个物品了；
w背包重量；items表示每个物品的重量；n表示物品个数
假设背包可承受重量10，物品个数5，物品重量存储在数组a中，那可以这样调用函数：
"""


class Solution:
    def dfs_way(self, items, w):
        self.max_value = float('-inf')
        n = len(items)
        self.memo = {}
        self.dfs(0, 0, items, n, w)
        return self.max_value

    def dfs(self, index, cw, items, n, w):
        if cw > w: return
        if cw == w or index == n:
            self.max_value = max(self.max_value, cw)
            return
        if self.memo.get((index, cw)): return
        self.memo[index, cw] = True
        self.dfs(index + 1, cw, items, n, w)  # 直接不装
        for i in range(index, n):
            self.dfs(i + 1, cw + items[i], items, n, w)


items = [2, 2, 4, 6, 3]
w = 9
a = Solution()
print(a.dfs_way(items,w))

"""
斐波那契数列
"""


class Solution2:
    def fibonaci1(self, n):
        if n == 1: return 1
        if n == 2: return 2
        return self.fibonaci1(n - 1) + self.fibonaci1(n - 2)

    def fibonaci2(self, n, dict1={}):
        if n == 1: return 1
        if n == 2: return 2
        print("dict1是-->", dict1)
        if dict1.get(n): return dict1[n]
        val = self.fibonaci2(n - 1) + self.fibonaci2(n - 2)
        dict1[n] = val
        return val

    def fibonaci3(self, n):  # f(n) = f(n-1) + f(n-2)
        if n == 1: return 1
        if n == 2: return 2
        pre, post = 1, 2
        for _ in range(3, n + 1):
            res = pre + post
            pre, post = post, res
        return res

#最好的时间买进和卖出
class Solution3:
    def maxProfit(self, prices):
        min_profit = int('float')
        tonow_maxprofit = 0
        for i in prices:
            if i < min_profit:
                min_profit = i
            if i-min_profit > tonow_maxprofit:
                tonow_maxprofit = i-min_profit
        return tonow_maxprofit

#求数组的连续最大子数组
class Solution4:
    def maxSubArray(self, nums):
        if not nums:return 0
        tonow_max = now_max = 0
        for i in range(len(nums)):
            now_max = max(nums[i],nums[i] + tonow_max)
            tonow_max = max(now_max,tonow_max)
        return tonow_max

"""

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.


"""
#求数组满足值的最小子数组
class Solution5:
    def minimum(self,s,nums):
        l = r = 0
        cnum = 0
        res = float('inf')
        while r < len(nums):
            cnum += nums[r]
            while cnum >= s:
                res = min(res,r-l+1)
                cnum -= nums[l]
                l += 1
            r += 1
        return res if res != float('inf') else 0



"""
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

unique path

"""

class Solution6:
    def unique_path(self, m, n): #到每一个格子都是从左边和上边的加一步，所以只要计算到左边和上边的有多少种即可
        dp = [[1] * m for _ in range(n)]
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


"""
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

unique path2
"""
class Solution7:
    """
    直接按照62的解题思路来做
    Runtime: 24 ms, faster than 61.86% of Python online submissions for Unique Paths II.
    Memory Usage: 10.9 MB, less than 22.36% of Python online submissions for Unique Paths II.
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        else:
            return 0
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
        return dp[-1][-1]




















