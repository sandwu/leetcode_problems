
class Solution(object):
    """
    讨论区清晰易懂解法，每步的含义都有英文注释，简单说就是把第一行和第一列作为标记位，如果第一次双重遍历有发现为0，则标记
    第一行和第一列对应的那个数为0，第二次双重遍历把该填的0填上即可。
    要注意的是填充0的话，j是从末尾开始往前填，因为如果从0开始往后填，则如果第一行第一个为0的话会把第一列全填为0，此时每行也
    因为第一行全变为0
    Runtime: 92 ms, faster than 61.68% of Python online submissions for Set Matrix Zeroes.
    Memory Usage: 11.1 MB, less than 44.39% of Python online submissions for Set Matrix Zeroes.
    """
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # First row has zero?
        m, n, firstRowHasZero = len(matrix), len(matrix[0]), not all(matrix[0])
        # Use first row/column as marker, scan the matrix
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
        # Set the zeros
        for i in range(1, m):
            for j in range(n - 1, -1, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # Set the zeros for the first row
        if firstRowHasZero:
            matrix[0] = [0] * n