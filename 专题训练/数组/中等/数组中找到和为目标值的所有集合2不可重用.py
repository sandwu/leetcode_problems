"""

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""


class Solution2:
    def combinationSum(self,candidates,target):
        self.res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [])
        return self.res

    def dfs(self,candidates, target,index, path):
        if target <0:
            return
        if target ==0:
            self.res.append(path)
            return
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i-1]:
                continue
            self.dfs(candidates, target-candidates[i],i+1,path+[candidates[i]])