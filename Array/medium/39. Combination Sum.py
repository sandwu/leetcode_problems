
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


class Solution(object):
    """
    讨论区流行解法，用到的也是递归，而方法的效率就比上一个高多了
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

    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return 
        for i in range(index, len(nums)):
            self.dfs(nums, target-nums[i], i, path+[nums[i]], res)