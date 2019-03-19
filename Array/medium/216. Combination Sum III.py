

class Solution(object):
    """
    dfs递归来完成
    Runtime: 20 ms, faster than 86.08% of Python online submissions for Combination Sum III.
    Memory Usage: 10.7 MB, less than 76.06% of Python online submissions for Combination Sum III.
    """
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(range(1,10),k,n,0,[],res)
        return res
    
    def dfs(self,nums,k,n,index,path,res):
        if k < 0 or n < 0:
            return 
        if k == 0 and n == 0:
            res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums,k-1,n-nums[i],i+1,path+[nums[i]],res)