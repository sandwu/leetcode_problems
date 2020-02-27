
"""
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true

"""


class Solution:
    def searchMatrix(self,matrix,target):
        if not matrix or not matrix[0]:return False
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m * n - 1
        while left <= right:
            mid = (left + right) >> 1
            mid_num = matrix[mid / n][mid % n] #行就是除以每列几个，列就是每列的余
            if mid_num == target:
                return True
            elif mid_num < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


