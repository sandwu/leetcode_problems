




class Solution:
    """
    题意是求给定指定的骰子d、骰子的面f、和目标数f，求多少种方式可以获得目标数
    利用dp和dfs都行，本题是用的dp，即先求每个骰子下的集合，再求所有骰子下的集合
    """
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        state = [1] + [0 for i in range(target)]
        MOD = 10 ** 9 + 7
        for i in range(d):
            for k in range(target, -1, -1):
                state[k] = 0
                for j in range(1, min(f, k) + 1):
                    state[k] += state[k - j]
                    state[k] %= MOD
        return state[-1]

a = Solution()
print(a.numRollsToTarget(2, 6, 7))