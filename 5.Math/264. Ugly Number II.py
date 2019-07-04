

class Solution(object):
    """
    题意是求能被2、3、5整除的第n个数，该解法就是从1开始，能被2、3、5整除就加入ugly的列表里，为了预防他们有
    共同的积，所以在while里再嵌套小while，如果有共同的积，则乘数+1重新相乘，最后取最小值加入列表即可。
    整个时间复杂度是O(n),也是比较简单易懂的
    Runtime: 156 ms, faster than 41.60% of Python online submissions for Ugly Number II.
    Memory Usage: 11.8 MB, less than 49.67% of Python online submissions for Ugly Number II.
    """
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1]
        i2 = i3 = i5 = 0
        while len(ugly) < n:
            while ugly[i2] * 2 <= ugly[-1]: i2 += 1
            while ugly[i3] * 3 <= ugly[-1]: i3 += 1
            while ugly[i5] * 5 <= ugly[-1]: i5 += 1
            ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
        return ugly[-1]