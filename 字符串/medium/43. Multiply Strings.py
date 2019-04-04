

class Solution(object):
    """
    https://blog.csdn.net/fuxuemingzhu/article/details/80681702
    参考链接做法，从末尾开始往前推算得到答案
    Runtime: 256 ms, faster than 21.94% of Python online submissions for Multiply Strings.
    Memory Usage: 12.2 MB, less than 5.23% of Python online submissions for Multiply Strings.
    """
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        ans = 0
        for i, n1 in enumerate(num2[::-1]):
            pre = 0
            curr = 0
            for j, n2 in enumerate(num1[::-1]):
                multi = (ord(n1) - ord('0')) * (ord(n2) - ord('0'))
                first, second = multi // 10, multi % 10
                curr += (second + pre) * (10 ** j)
                pre = first
            curr += pre * (10 ** len(num1))
            ans += curr * (10 ** i)
        return str(ans)
