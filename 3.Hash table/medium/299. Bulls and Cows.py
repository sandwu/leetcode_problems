


class Solution(object):
    """
    先逐一匹配看是否相等，然后算出两个列表的长度最小值，最后获取bull和cow的个数
    Runtime: 24 ms, faster than 99.74% of Python online submissions for Bulls and Cows.
    Memory Usage: 11.7 MB, less than 85.37% of Python online submissions for Bulls and Cows.
    """
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = sum(map(operator.eq, secret, guess))
        both = sum(min(secret.count(x), guess.count(x)) for x in set(guess))
        return '%dA%dB' % (bulls, both - bulls)