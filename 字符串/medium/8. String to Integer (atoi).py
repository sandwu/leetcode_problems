

class Solution(object):
    """
    题目归纳为下列几种情况：
    1.输入字符串为空、或其他不合法情况，返回0；
    2.字符串开头的空格要在预处理中删掉；
    3.处理可能出现的正负号“+”，“-”，正负号只能出现一次；
    4.超出整数范围的值取整数范围的边界值。
    根据题意，可直接列出代码
    Runtime: 32 ms, faster than 96.56% of Python online submissions for String to Integer (atoi).
    Memory Usage: 12 MB, less than 5.26% of Python online submissions for String to Integer (atoi).
    """
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if len(str)==0:
            return 0
        number, flag = 0, 1
        if str[0] == '-':
            str = str[1:]
            flag = -1
        elif str[0] == '+':
            str = str[1:]
        for c in str:
            # 这里是用字符串比较，在python中是利用ASCII来比较的，所以和数字比较逻辑是一直的
            if c >= '0' and c <= '9':
                number = 10*number + ord(c) - ord('0')
            else:
                break
        number = flag * number
        # 最后判断是否位于区间范围
        number = number if number <= 2147483647 else 2147483647
        number = number if number >= -2147483648 else -2147483648
        return number


class Solution2(object):
    """
    用正则匹配简直不要太轻松
    Runtime: 28 ms, faster than 100.00% of Python online submissions for String to Integer (atoi).
    Memory Usage: 11.9 MB, less than 5.26% of Python online submissions for String to Integer (atoi).
    """
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        try:
            res = re.search('(^[\+\-]?\d+)', str).group()
            res = int(res)
            res = res if res <= 2147483647 else 2147483647
            res = res if res >= -2147483648 else -2147483648
        except:
            res = 0
        return res
