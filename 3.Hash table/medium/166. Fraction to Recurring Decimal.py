


class Solution(object):
    """
    Runtime: 36 ms, faster than 7.30% of Python online submissions for Fraction to Recurring Decimal.
    Memory Usage: 11.9 MB, less than 5.55% of Python online submissions for Fraction to Recurring Decimal.
    """
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        # divmod获取整除后的整数和余数
        n, remainder = divmod(abs(numerator), abs(denominator))
        # sign判断是否有负数
        sign = '-' if numerator*denominator < 0 else ''
        result = [sign+str(n), '.']
        stack = []
        # 循环判断余数是否开始循环
        while remainder not in stack:
            stack.append(remainder)
            n, remainder = divmod(remainder*10, abs(denominator))
            result.append(str(n))

        idx = stack.index(remainder)
        result.insert(idx+2, '(')
        result.append(')')
        return ''.join(result).replace('(0)', '').rstrip('.')