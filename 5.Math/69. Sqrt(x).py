
class Solution(object):
    """
    题意是求的一个数的平方根，那用二分法是非常快的！
    Runtime: 36 ms, faster than 25.07% of Python online submissions for Sqrt(x).
    Memory Usage: 11.7 MB, less than 55.77% of Python online submissions for Sqrt(x).
    """
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l,r = 0,x
        while l<=r:
            mid = (l+r) >> 1
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            elif mid * mid > x:
                r = mid
            else:
                l = mid + 1