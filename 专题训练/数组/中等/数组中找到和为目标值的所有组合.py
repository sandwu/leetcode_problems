
"""

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
"""


class Solution:
    def combinationSum(self,candidates, target):
        self.res = []
        candidates.sort()
        self.find_com(candidates,target,[])
        return self.res

    def find_com(self,candidates,target,tmp):
        if target in candidates:
            a = tmp + [target]
            if sorted(a) not in self.res:
                self.res.append(sorted(a))
        for i in [n for n in candidates if n<target]:
            self.find_com(candidates,target-i,tmp+[i])


#上面的不推介，推介用dfs

class Solution2:
    def combinationSum(self,candidates,target):
        self.res = []
        self.dfs(candidates, target, 0, [])
        return self.res

    def dfs(self,candidates, target,index, path):
        if target <0:
            return
        if target ==0:
            self.res.append(path)
            return
        for i in range(index, len(candidates)):
            self.dfs(candidates, target-candidates[i],i,path+[candidates[i]])




