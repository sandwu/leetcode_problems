
class Solution(object):
    """
    题意是求的一个数的平方根，那用二分法是非常快的！
    Runtime: 32 ms, faster than 31.49% of Python online submissions for Sqrt(x).
    Memory Usage: 11.8 MB, less than 30.98% of Python online submissions for Sqrt(x).
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