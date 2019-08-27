

class Solution(object):
    """
    题意和46、47差不多，求n个连续数，其中k个集合有多少种
    解法：dfs遍历
    Runtime: 664 ms, faster than 29.51% of Python online submissions for Combinations.
    Memory Usage: 13.1 MB, less than 69.23% of Python online submissions for Combinations.
    """
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(range(1,n+1), k, 0, [], res)
        return res

    def dfs(self, nums, k, index, path, res):
        #if k < 0:  #backtracking
            #return
        if k == 0:
            res.append(path)
            return # backtracking
        for i in range(index, len(nums)):
            self.dfs(nums, k-1, i+1, path+[nums[i]], res)