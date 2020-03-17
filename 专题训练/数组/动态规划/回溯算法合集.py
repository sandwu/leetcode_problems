

"""
1.数组中和为目标值的所有集合1:允许重复利用一个值 (combination sum)
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
"""

class Solution:
    def combination_sum(self,candidates,target):
        self.res = []
        self.dfs(0,candidates,target,[])
        return self.res

    def dfs(self,index,nums,target,path):
        if target < 0: return
        if target == 0:
            self.res.append(path)
        for i in range(index,len(nums)):
            self.dfs(i,nums,target-nums[i],path+[nums[i]])


"""
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
数组中和为目标值的所有集合2:不允许重复利用一个值
"""

class Solution2:
    def combination_sum2(self,candidates,target):
        self.res = []
        candidates.sort()
        self.dfs(0,candidates,target,[])
        return self.res

    def dfs(self,index,candidates,target,path):
        if target == 0:
            self.res.append(path)
            return
        if target < 0:return
        for i in range(index,len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            self.dfs(i+1,candidates,target-candidates[i],path+[candidates[i]])


"""
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""
class Solution3:
    def combination_sum3(self,k,n):
        self.res = []
        self.dfs(1,k,n,[])
        return self.res

    def dfs(self,index,k,n,path):
        if k < 0 or n <0:
            return
        if n==0 and k==0:
            self.res.append(path)
            return
        for i in range(index,10):
            self.dfs(i+1,k-1,n-i,path+[i])


"""

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

class Solution4:
    def subset(self,nums):
        self.res = []
        self.dfs(0,nums,[])
        return self.res

    def dfs(self,index,nums,path):
        self.res.append(path)
        for i in range(index,len(nums)):
            self.dfs(i+1,nums,path+[nums[i]])


"""
Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

"""

class Solution5(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        nums.sort()
        self.dfs(0,nums,[])
        return self.res

    def dfs(self,index,nums,path):
        self.res.append(path)
        for i in range(index,len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            self.dfs(i+1,nums,path+[nums[i]])



"""
Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

"""


class Solution6:
    def searchword(self,board,word):
        self.res=[]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(word,board,i,j):
                    return True
        return self.res

    def dfs(self,word,board,i,j):
        if not word:return True
        if i <0 or j < 0 or i>len(board)-1 or j > len(board[0])-1 or  board[i][j] != word[0]:
            return
        tmp = board[i][j]
        board[i][j] = "#"
        res = self.dfs(word[1:],board,i+1,j) or self.dfs(word[1:],board,i-1,j) \
        or self.dfs(word[1:],board,i,j+1) or self.dfs(word[1:],board,i,j-1)
        board[i][j] = tmp
        return res




"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

"""
class Solution7:
    def unique_path(self, m, n):
        self.memo = {}
        count = self.dfs(0, 0, m - 1, n - 1)
        return count

    def dfs(self, i, j, m, n):
        if (i, j) in self.memo: return self.memo[i, j]
        if m < i or n < j: return 0
        if i == m and j == n:
            return 1
        count = self.dfs(i + 1, j, m, n) + self.dfs(i, j + 1, m, n)
        self.memo[i, j] = count
        return count



"""

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""
class Solution8(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        self.memo = {}
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        count = self.dfs(0,0,m-1,n-1,obstacleGrid)
        return count

    def dfs(self,i,j,m,n,obstacleGrid):
        if (i,j) in self.memo:return self.memo[i,j]
        if i > m or j > n:return 0
        if obstacleGrid[i][j] == 1: return 0
        if i==m and j ==n:return 1
        count = self.dfs(i+1,j,m,n,obstacleGrid) + self.dfs(i,j+1,m,n,obstacleGrid)
        self.memo[i,j] = count
        return count


"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""
class Solution9(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # if len(grid[0]) == 1:return grid[0][0]
        self.memo = {}
        m = len(grid)
        n = len(grid[0])
        res = self.dfs(0, 0, m - 1, n - 1, grid)
        return res

    def dfs(self, i, j, m, n, grid):
        if (i, j) in self.memo: return self.memo[i, j]
        if i == m and j == n: return grid[i][j]
        d = r = float('inf')
        if i < m:
            d = self.dfs(i + 1, j, m, n, grid)
        if j < n:
            r = self.dfs(i, j + 1, m, n, grid)
        res = min(d, r) + grid[i][j]
        self.memo[i, j] = res
        return res

"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
"""


class Solution10(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        self.memo = {}
        m = len(triangle)
        res = self.dfs(0, 0, m - 1, triangle)
        return res

    def dfs(self, i, j, m, triangle):
        if (i, j) in self.memo: return self.memo[i, j]
        if i == m: return triangle[i][j]
        l = self.dfs(i + 1, j, m, triangle)
        r = self.dfs(i + 1, j + 1, m, triangle)
        res = min(l, r) + triangle[i][j]
        self.memo[i, j] = res
        return res


















