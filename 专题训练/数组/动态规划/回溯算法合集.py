

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
            if path not in self.res:
                self.res.append(path)
                return
        if target < 0:return
        for i in range(index,len(candidates)):
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

class Solution5:
    def subset2(self,nums):
        self.res = []
        nums.sort()
        self.dfs(0,nums,[])
        return self.res

    def dfs(self,index,nums,path):
        if path not in self.res:
            self.res.append(path)
        for i in range(index,len(nums)):
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