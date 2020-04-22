



#数组中和为目标值的所有集合1:允许重复利用一个值
"""
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        self.res = []
        self.dfs(0,candidates,[],target)
        return self.res

    def dfs(self,index,candidates,path,target):
        if target < 0:return
        if target == 0:
            self.res.append(path)
            return
        for i in range(index,len(candidates)):
            self.dfs(i,candidates,path+[candidates[i]],target-candidates[i])


class Solution2:
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        answer = []

        universe = [([], 0)]
        for n in candidates:
            for (ls, v) in universe:
                if v + n == target:
                    answer.append(ls + [n])
                elif v + n < target:
                    universe.append((ls + [n], v + n))

        return answer