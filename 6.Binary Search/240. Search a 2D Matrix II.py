



class Solution(object):
    """
    题意是求从上到下、从左到右升序排序的矩阵里是否存在某个值
    该题也被分到了树的分类里，该解法利用到python的any，针对每一行，any匹配是否存在即可
    看到any的源码描述： Return True if bool(x) is True for any x in the iterable.
    也即是遍历每个数，用bool(x)查看是否存在
    Runtime: 156 ms, faster than 22.01% of Python online submissions for Search a 2D Matrix II.
    Memory Usage: 15.8 MB, less than 13.81% of Python online submissions for Search a 2D Matrix II.
    """
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        return any(target in row for row in matrix)


class Solution2(object):
    """
    该解法从最后一行开始遍历，如果最后一行第一个数小于该值，则往右推移一列，如果对应的数大于该值，则往上推移一列；
    这两个都是依赖于题目给的从上到下、从左到右的升序排序，所以当同一行的数小于该值，则他上一行的数也必然小于该值，
    所以可以继续往下遍历
    Runtime: 44 ms, faster than 92.26% of Python online submissions for Search a 2D Matrix II.
    Memory Usage: 15.8 MB, less than 24.21% of Python online submissions for Search a 2D Matrix II.
    """
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        y = m - 1
        x = 0
        while y >= 0 and x < n:
            if matrix[y][x] == target:
                return True
            elif matrix[y][x] < target:
                x += 1
            else:
                y -= 1
        return False
