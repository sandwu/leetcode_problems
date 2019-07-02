
class Solution(object):
    """
    python 自带的求幂效率还是不错的
    Runtime: 16 ms, faster than 87.02% of Python online submissions for Pow(x, n).
    Memory Usage: 11.8 MB, less than 41.74% of Python online submissions for Pow(x, n).
    """
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return x ** n


class Solution2(object):
    """
    用循环的方法，效率和python自带的无差
    math系列用的比较多的还是二进制位运算，这里的 n & 1表示当n为偶数时，和1的与运算为0，所以
    每次n为偶数时都跳过pow运算，通过x平方来求积
    Runtime: 16 ms, faster than 87.02% of Python online submissions for Pow(x, n).
    Memory Usage: 11.7 MB, less than 63.24% of Python online submissions for Pow(x, n).
    """
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow


class Solution3(object):
    """
    递归的效率最快，思路和循环的相差不大
    Runtime: 8 ms, faster than 99.55% of Python online submissions for Pow(x, n).
    Memory Usage: 11.9 MB, less than 18.72% of Python online submissions for Pow(x, n).
    """
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)