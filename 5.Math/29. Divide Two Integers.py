

class Solution(object):
    """
    题意是求2个整数的整除，但是不准用自带的除和求余的手段！
    这里有个小技巧：用is判断两边是否都为真或假；
    通过减法+循环实现除法，利用在while里嵌套while的方式，加快减的速度，也就是通过二进制的<<左移相当于*2的方式，每次
    减去减数的倍数，直到无法相减再回到初始节点！
    Runtime: 16 ms, faster than 93.27% of Python online submissions for Divide Two Integers.
    Memory Usage: 11.7 MB, less than 60.15% of Python online submissions for Divide Two Integers.
    """
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)