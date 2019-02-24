
class Solution(object):
    """
    直接修改39的代码，在for下面增加一个判断，比如示例：[10,1,2,7,6,1,5]，排完序后为[1,1,2,5,6,7,10]
    通过递归直接开始找[1,1]后面的：[1,1,2,5],[1,1,2,6],[1,1,2,7],[1,1,2,10];实际可以debug跑一遍或者纸上
    运行一遍，不过递归的确浪费了不少步骤，但这种题递归是最容易想到的解法
    Runtime: 84 ms, faster than 43.76% of Python online submissions for Combination Sum II.
    Memory Usage: 10.8 MB, less than 35.21% of Python online submissions for Combination Sum II.
    """
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res
        
    def dfs(self, candidates, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return  # backtracking 
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i-1]:
                continue
            self.dfs(candidates, target-candidates[i], i+1, path+[candidates[i]], res)
        

class Solution2(object):
    """
    提供另一种非递归思路，讨论区DP solution，效率也是高的一匹
    Runtime: 36 ms, faster than 89.58% of Python online submissions for Combination Sum II.
    Memory Usage: 11 MB, less than 6.10% of Python online submissions for Combination Sum II.
    """
    def combinationSum2(self, candidates, target):
        candidates.sort()
        table = [None] + [set() for i in range(target)]
        for i in candidates:
            if i > target:
                break
            for j in range(target - i, 0, -1):
                table[i + j] |= {elt + (i,) for elt in table[j]}
            table[i].add((i,))
        return map(list, table[target])