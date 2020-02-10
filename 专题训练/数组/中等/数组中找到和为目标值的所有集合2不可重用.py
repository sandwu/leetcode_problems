


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
            if i > index and candidates[i] == candidates[i-1]:
                continue
            self.dfs(candidates, target-candidates[i],i,path+[candidates[i]])