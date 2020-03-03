
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

class Solution3(object): #dfs超时
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        self.res = float('inf')
        self.tmp = {}
        if amount == 0 :return 0
        self.dfs(0 ,coins ,0 ,amount)
        if self.res == float('inf') :return -1
        return self.res

    def dfs(self ,index ,coins ,ans ,amount):
        if self.tmp.get(amount):return self.tmp[amount]
        if amount < 0 :return 0
        if amount == 0:
            self.res = min(self.res ,ans)
            self.tmp[amount] = self.res
            return
        for i in range(index ,len(coins)):
            self.dfs(i, coins, ans + 1, amount - coins[i])


class Solution2(object): #dp
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        MAX = float('inf')
        dp = [0] + [MAX] * amount

        for coin in coins:
            for i in range(coin,amount+1):
                if dp[i-coin] != MAX:
                    dp[i] = min(dp[i],dp[i-coin] +1)
        return dp[-1] if dp[-1] != MAX else -1

coins = [1, 2,5]
amount = 11
a = Solution2()
print(a.coinChange(coins, amount))