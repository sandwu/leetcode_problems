

#96
"""
Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

"""


class Solution(object):
    """
    题意是相对95题只需拿到拥有多少组BST即可
    用了记忆递归，即定义了map，如果存在该键值，则直接取值即可
    解法以i为根节点，比i小的数1...i-1作为左子树，比i大的数i+1...n作为右子树，左子树的排列和右子树的排列的乘积是此时的数目。
    Runtime: 20 ms, faster than 46.81% of Python online submissions for Unique Binary Search Trees.
    Memory Usage: 11.7 MB, less than 56.49% of Python online submissions for Unique Binary Search Trees.
    """
    def __init__(self):
        self.dp = dict()

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.dp:
            return self.dp[n]
        if n == 0 or n == 1:
            return 1
        ans = 0
        for i in range(1, n + 1):
            ans += self.numTrees(i - 1) * self.numTrees(n - i)
        self.dp[n] = ans
        return ans


class Solution2(object):
    """
    动态规划解法，参考博文：https://blog.csdn.net/fuxuemingzhu/article/details/79367789
    Runtime: 12 ms, faster than 90.35% of Python online submissions for Unique Binary Search Trees.
    Memory Usage: 11.8 MB, less than 47.40% of Python online submissions for Unique Binary Search Trees.
    """
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp.pop()


