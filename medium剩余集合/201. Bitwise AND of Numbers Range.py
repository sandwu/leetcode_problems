




class Solution(object):
    """
    Runtime: 40 ms, faster than 81.82% of Python online submissions for Bitwise AND of Numbers Range.
    Memory Usage: 11.8 MB, less than 50.00% of Python online submissions for Bitwise AND of Numbers Range.
    """
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return n << i