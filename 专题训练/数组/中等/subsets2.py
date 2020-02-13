

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

class Solution:
    def subsets(self,nums):
        res = [[]]
        for num in nums:
            for i in range(len(res)):
                tmp = sorted(res[i]+[num])
                if tmp not in res:
                    res.append(tmp)
        return res


    def subsets2(self,nums):
        self.res = []
        nums.sort()
        self.dfs(nums,0,[])
        return self.res

    def dfs(self,nums,index,path):
        self.res.append(path)
        for i in range(index,len(nums)):
            if i>index and nums[i] == nums[i-1]:
                continue
            self.dfs(nums,i+1,path+nums[i])