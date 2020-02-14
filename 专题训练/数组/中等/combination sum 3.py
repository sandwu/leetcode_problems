

class Solution:
    def combination(self,k,n):
        self.res = []
        self.dfs(k, n, 0, [], range(1, 10))
        return self.res

    def dfs(self, k, n, index, path, nums):
        if k < 0 or n < 0:
            return
        if k == 0 and n == 0:
            self.res.append(path)
        for i in range(index, len(nums)):
            self.dfs(k - 1, n - nums[i], i + 1, path + [nums[i]], nums)