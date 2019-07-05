
class Solution(object):
    """
    题意是求任意一个整数，是其他的平方数的和的最小平方数个数，这里采用动态规划来完成
    先定义1个n+1的集合，用2**32表示这个数非常大，然后开始遍历整个n+1集合，每个数则可以看成是
    两个数的和，1个是离这个数最近的平方数，另一个则是在这个数之前的数，直接找到对应之前的数的解即可。
    比如12，离他最近的是9，另一个是3，那找到3的解发现是2个，所以12的解就是1+2=3
    Runtime: 4144 ms, faster than 27.63% of Python online submissions for Perfect Squares.
    Memory Usage: 12.1 MB, less than 42.10% of Python online submissions for Perfect Squares
    """
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n== 0:
            return 0
        output = [2**32] * (n + 1)
        output[0] = 0
        output[1] = 1
        for i in range(2, n + 1):
            j = 1
            while (j * j <= i):
                output[i] = min(output[i], output[i - j * j] + 1)
                j = j + 1

        return output[n]