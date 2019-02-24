
class Solution(object):
    """
    这道题利用了递归的思想，在函数里再次调用函数来判断target-candidates[i]的数是否在集合里，从而可以知道重复数的排列集合
    利用到递归的都相对比较难以理解，下列解法用debug或者在纸上跑一遍，会发现程序走的和预想的有出入，比如把下述代码的print注释去掉，看下结果是否如你所料？
    Runtime: 204 ms, faster than 11.86% of Python online submissions for Combination Sum.
    Memory Usage: 10.8 MB, less than 33.60% of Python online submissions for Combination Sum.
    """
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # global final_result
        final_result = []
        candidates.sort()

        def findCom(target, temp_list):
            if target in candidates:
                a = temp_list + [target]
                if sorted(a) not in final_result:
                    final_result.append(a)
            for i in [n for n in candidates if n < target]:
                # print (i, target,temp_list)
                a = temp_list + [i]
                findCom(target - i, a)

        t = []
        findCom(target, t)
        return final_result


class Solution1(object):
    """
    讨论区流行解法，用到的也是递归，而方法的效率就比上一个高多了，从命名来看是DFS，即Depth-First-Search，深度优先算法
    本质我觉得和上一个解法差不多，而且可理解性还没有上个解法好，也是从头开始遍历，然后如果target == 0，也就是找到组合，就往
    res里增加组合，没找到，就往path里增加数，直到target<0，则此次递归结束，开始下一个数的递归
    Runtime: 92 ms, faster than 47.88% of Python online submissions for Combination Sum.
    Memory Usage: 10.6 MB, less than 94.71% of Python online submissions for Combination Sum.
    """
    def combinationSum(self, candidates, target):
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
            return  
        if target == 0:
            res.append(path)
            return 
        for i in range(index, len(candidates)):
            self.dfs(candidates, target-candidates[i], i, path+[candidates[i]], res)


class Solution2(object):
    """
    回溯解法，非递归
    Runtime: 152 ms, faster than 17.24% of Python online submissions for Combination Sum.
    Memory Usage: 10.9 MB, less than 29.63% of Python online submissions for Combination Sum.
    """
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates, res, stack, lenth=sorted(set(candidates)), [], [(0, [], target)], len(candidates)
        while stack:
            i, temp, tar=stack.pop()
            while i<lenth and tar>0:
                if candidates[i]==tar:res+=temp+[candidates[i]],
                stack+=(i, temp+[candidates[i]], tar-candidates[i]),
                i+=1

        return res