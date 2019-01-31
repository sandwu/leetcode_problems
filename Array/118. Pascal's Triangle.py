
class MySolution:
    """
    杨辉三角，我的方法就是正常思路：杨辉三角就是给的数字是几，则列表里就含有几行，每一行的列也是和数字对应的，所以肯定是利用两个for来循环遍历；
    那在嵌套的for里构建新列表，每次在开头和结尾各插入1，中间的数字就是前一个列表的两个数字和。
    Runtime: 48 ms, faster than 98.57% of Python3 online submissions for Pascal's Triangle.
    """
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for row in range(numRows):
            inside = []
            inside.append(1)
            
            if row > 1:
                for col in range(row-1):
                    inside.append(res[row-1][col]+res[row-1][col+1])
            if row > 0:
                inside.append(1)
            
            res.append(inside)
        return res


class Solution:
    """
    官方solution，提前构造好里面的列表和列表的前后位填充1，然后二次遍历填充中间，好处是一气呵成，不用考虑if
    Runtime: 52 ms, faster than 96.18% of Python3 online submissions for Pascal's Triangle.
    """
    def generate(self, num_rows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []

        for row_num in range(num_rows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num+1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]

            triangle.append(row)

        return triangle