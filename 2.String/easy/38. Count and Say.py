

class Solution(object):
    """
    理解了题意即懂如何做，题意是依据上一个字符串来推导下一个字符串，第一个字符串是"1"，所以第二个就是1个1，即"11"，
    第三个就是2个1，即"21"，第四个就是1个2，1个1，即"1211"；
    解法就是遍历需要得到的答案位于第几个，然后针对每一个去求得它的值
    Runtime: 24 ms, faster than 64.32% of Python online submissions for Count and Say.
    Memory Usage: 11.8 MB, less than 5.40% of Python online submissions for Count and Say.
    """
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        for _ in range(n - 1):
            res = self.helper(res)
        return res

    def helper(self, n):
        count, i, res = 1, 0, ""
        while i < len(n) - 1:
            if n[i] == n[i + 1]:
                count += 1
            else:
                res += str(count) + n[i]
                count = 1
            i += 1
        res += str(count) + n[i]
        return res


class Solution2(object):
    """
    高阶解法，用正则来完成
    Runtime: 24 ms, faster than 64.32% of Python online submissions for Count and Say.
    Memory Usage: 12 MB, less than 5.40% of Python online submissions for Count and Say.
    """
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(group)) + digit
                        for group, digit in re.findall(r'((.)\2*)', s))
        return s

class Solution3(object):
    """
    trick解法，用itertools来完成
    Runtime: 28 ms, faster than 32.56% of Python online submissions for Count and Say.
    Memory Usage: 12 MB, less than 5.40% of Python online submissions for Count and Say
    """
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(list(group))) + digit
                        for digit, group in itertools.groupby(s))
        return s