
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


class Solution:
    def subsets(self,nums):
        res = [[]]
        for num in nums:
            for i in range(len(res)):
                res.append(res[i]+[num])
        return res

    def sd(self,nums):
        self.res = []
        self.dfs(nums,0,[])
        return self.res

    def dfs(self,nums,index,tmp):
        self.res.append(tmp)
        for i in range(index,len(nums)):
            self.dfs(nums,i+1,tmp+[nums[i]])


nums = [1,2,3]
a = Solution()
print(a.sd(nums))