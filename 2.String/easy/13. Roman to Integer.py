
class MySolution(object):
    """
    我的想法很简单，定义个字典来匹配，然后遍历，当左边的值小于右边的值则说明加上对应的负数，反之加正数，最后
    的一个数一定是正数，当然效率也是蛮低的
    Runtime: 92 ms, faster than 34.34% of Python online submissions for Roman to Integer.
    Memory Usage: 11.7 MB, less than 5.47% of Python online submissions for Roman to Integer.
    """
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        for i in range(len(s)-1):
            if self.change(s[i]) < self.change(s[i+1]):
                sum += -self.change(s[i])
            else:
                sum += self.change(s[i])
        return sum+self.change(s[-1])
    
    def change(self,alp):
        change_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        return change_dict[alp]

class Solution(object):
    """
    思路是相同的，不过讨论区的写的更pythonic，直接定义一个I的值，然后从后往前遍历，时间复杂度也是达到了100%
    Runtime: 60 ms, faster than 100.00% of Python online submissions for Roman to Integer.
    Memory Usage: 11.9 MB, less than 5.47% of Python online submissions for Roman to Integer.
    """
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        res, p = 0, 'I'
        for c in s[::-1]:
            res, p = res - d[c] if d[c] < d[p] else res + d[c], c
        return res
