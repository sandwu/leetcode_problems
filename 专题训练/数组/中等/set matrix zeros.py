

"""
Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
"""

class Solution:
    def setzeros(self,matrix):
        m,n = len(matrix),len(matrix[0])
        firstrow = not all(matrix[0])
        for row in range(1,m):
            for col in range(n):
                if matrix[row][col] == 0:
                    matrix[0][col] = matrix[row][0] = 0

        for row in range(1,m): #为什么要去掉第一行，因为第一行是作为坐标来指示
            for col in range(n-1,-1,-1):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0

        if firstrow:
            matrix[0] = [0] * n







