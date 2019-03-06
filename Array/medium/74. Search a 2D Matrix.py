
class Solution(object):
    """
    原理很简单，普通二分法，关键要知道如何转换列表索引为矩阵索引，即num = matrix[mid/cols][mid%cols]
    Runtime: 20 ms, faster than 100.00% of Python online submissions for Search a 2D Matrix.
    Memory Usage: 11.4 MB, less than 55.04% of Python online submissions for Search a 2D Matrix.
    """
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1
        
        while low <= high:
            mid = (low + high) / 2
            num = matrix[mid / cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False

class Solution2(object):
    """
    直接用双重遍历的方式来解决，复杂度是O(m*n)，但惊讶的是时间与二分法相差不大
    Runtime: 20 ms, faster than 100.00% of Python online submissions for Search a 2D Matrix.
    Memory Usage: 11.7 MB, less than 9.30% of Python online submissions for Search a 2D Matrix.
    """
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False
        for i in range(len(matrix)):
            if target==matrix[i][-1]: return True
            elif target<matrix[i][-1]:
                for j in range(len(matrix[0])):
                    if matrix[i][j]==target: return True
                return False
        return False