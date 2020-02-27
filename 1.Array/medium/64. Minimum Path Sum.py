

"""
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

"""

class Solution(object):
    """
    题目容易和62、63弄混了，该题的意思是在给定的双重数组里，找出从gird[0][0]到grid[-1][-1]的最短距离
    所以原理还是和unique path相差不大，即最短距离就是当前的位置+左边/上边的最短路径，依次推导便是了
    即遍历两次，每次取左边或者上边的最小值，但要考虑两种特殊情况：第一行和第一列，因为他们各自没有上边和左边，
    因此当row=0，直接取左边的值为最小值，col=0.取右边的值为最小值
    Runtime: 32 ms, faster than 94.90% of Python online submissions for Minimum Path Sum.
    Memory Usage: 11.8 MB, less than 53.62% of Python online submissions for Minimum Path Sum.
    """
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n = len(grid),len(grid[0])
        for row in range(m):
            for col in range(n):
                if row == col == 0:
                    before = 0
                elif row == 0:
                    before = grid[row][col-1]
                elif col == 0:
                    before = grid[row-1][col]
                else:
                    before = min(grid[row-1][col],grid[row][col-1])
                grid[row][col] = before + grid[row][col]
        return grid[-1][-1]