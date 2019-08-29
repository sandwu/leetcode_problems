


class Solution(object):
    """
    题意是求给定一个数n，求由这个n位数组成的0101二进制共有几种，比如给2，则要组成二位数的二进制：00，01，10，11
    解法：参考讨论区https://leetcode.com/problems/gray-code/discuss/216001/Python-solution
    可以通过递归拆解，观察发现每个n的答案是由n-1的答案再加上后面新增的，这部分新增的是跟2*(n-1)成异或关系
    Consider the example n = 3. With n = 2, we have grayCode(2) = [00, 01, 11, 10] = [0, 1, 3, 2].
    For n = 3, the 4 binary numbers in grayCode(2) still show up, i.e., it will contain [000, 001, 011, 010] = [0, 1, 3, 2].
    To obtain the other 4 binary numbers, we simply flip the first binary digit to 1, i.e., [100, 101, 111, 110] = [4, 5, 7, 6].
    Finally, we append [6, 7, 5, 4] to [0, 1, 3, 2] to obtain the output for grayCode(3) = [0, 1, 3, 2, 6, 7, 5, 4].
    Note that we have to reverse the second list because 6 (110) can be obtained from 2 (010) by flipping one bit, whereas 4 (100) cannot.

    Runtime: 20 ms, faster than 65.45% of Python online submissions for Gray Code.
    Memory Usage: 11.9 MB, less than 60.00% of Python online submissions for Gray Code.
    """
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        res = self.grayCode(n-1)
        num = 2**(n-1)
        res += res[::-1]
        for i in range(num,len(res)):
            res[i] ^= num
        return res