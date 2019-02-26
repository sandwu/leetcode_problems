
class Solution(object):
    """
    利用zip的特性，可以针对集合里的元素进行第一个、第二个依次拼接，完美达到题目要求
    Runtime: 20 ms, faster than 100.00% of Python online submissions for Rotate Image.
    Memory Usage: 10.6 MB, less than 86.93% of Python online submissions for Rotate Image.
    """
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        matrix[::] = zip(*matrix[::-1])



class Solution1(object):
    """
    先上下翻转，再以左上方到右下方斜线不动，进行翻转
    [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
    [
    [7,8,9],
    [4,5,6],
    [1,2,3]
    ]
    Runtime: 20 ms, faster than 100.00% of Python online submissions for Rotate Image.
    Memory Usage: 11 MB, less than 5.30% of Python online submissions for Rotate Image.
    """
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if matrix:
            rows = len(matrix)
            cols = len(matrix[0])
            for i in range(rows // 2):
                for j in range(cols):
                    matrix[i][j], matrix[rows - i - 1][j] = matrix[rows - i - 1][j], matrix[i][j]
            for i in range(rows):
                for j in range(i):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


class Solution2(object):
    """
    先调换4个角，再依次调换边
    Runtime: 24 ms, faster than 91.14% of Python online submissions for Rotate Image.
    Memory Usage: 10.8 MB, less than 23.67% of Python online submissions for Rotate Image.
    """
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for l in range(n // 2):
            r = n - 1 - l
            for p in range(l, r):
                q = n - 1 - p
                cache = matrix[l][p]
                matrix[l][p] = matrix[q][l]
                matrix[q][l] = matrix[r][q]
                matrix[r][q] = matrix[p][r]
                matrix[p][r] = cache
