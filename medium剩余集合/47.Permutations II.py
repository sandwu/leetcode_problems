



class Solution(object):
    """
    题意是46的变种，加上了有重复项这一前提条件
    解法：和46一样，DFS遍历，只要在dfs要加到结果集res时判断是否已存在结果集即可
    Runtime: 1196 ms, faster than 6.43% of Python online submissions for Permutations II.
    Memory Usage: 12 MB, less than 53.33% of Python online submissions for Permutations II.
    """
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums ,[] ,res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            if path not in res:
                res.append(path)

        for i in range(len(nums)):
            self.dfs(nums[:i ] +nums[ i +1:] ,path +[nums[i]] ,res)