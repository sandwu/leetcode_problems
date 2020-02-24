

"""
Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

"""


class Solution:
    def rotate(self,matrix):
        matrix[:] = zip(**matrix[::-1])



    def rotate2(self,matrix):
        matrix[:] = matrix[::-1]
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(i): #这里要注意是i，避免被重复调换
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

"""
可以将matrix[:] = matrix[::-1]
转换为双for：
for i in range(rows)：
    for j in range(cols):
        matrix[i][j],matrix[row-i-1][j]=matrix[row-i-1][j],matrix[i][j]
"""
