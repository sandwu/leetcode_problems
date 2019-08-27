


class Solution(object):
    """
    题意是求一个列表的所有排列方式
    用DFS即可，每次递归到底即为1种，然后通过遍历该列表里总共有多少种开头，针对每种开头DFS下去即可拿到答案
    Runtime: 52 ms, faster than 36.20% of Python3 online submissions for Permutations.
    Memory Usage: 13.7 MB, less than 5.36% of Python3 online submissions for Permutations.
    """
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums ,[] ,res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)

        for i in range(len(nums)):
            self.dfs(nums[:i ] +nums[ i +1:] ,path +[nums[i]] ,res)