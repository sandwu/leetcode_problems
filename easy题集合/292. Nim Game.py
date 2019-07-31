

class Solution(object):
    """
    题意是给一堆石头，两个人一次只能各取1，2，3个石头，如何根据石头的数量判断谁赢
    通过测试知道，小于3块，肯定是第一次拿的我赢；第4块就对方赢，第5，6，7我可以拿走对应的1，2，3就变成
    我赢，到第8块又是对方赢，因此不是4的倍数即可
    Runtime: 24 ms, faster than 8.30% of Python online submissions for Nim Game.
    Memory Usage: 11.7 MB, less than 65.28% of Python online submissions for Nim Game.
    """
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return bool(n % 4)