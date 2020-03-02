
"""

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

example 2:
Input: coins = [2], amount = 3
Output: -1

"""

class Solution(object): #dfs超时
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        self.res = float('inf')
        if amount == 0 :return 0
        self.dfs(0 ,coins ,0 ,amount)
        if self.res == float('inf') :return -1
        return self.res

    def dfs(self ,index ,coins ,ans ,amount):
        if amount < 0 :return 0
        if amount == 0:
            self.res = min(self.res ,ans)
            return
        for i in range(index ,len(coins)):
            self.dfs(i, coins, ans + 1, amount - coins[i])




coins = [1, 2]
amount = 2
a = Solution()
print(a.coinChange(coins, amount))