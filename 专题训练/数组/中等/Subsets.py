


class Solution:
    def subsets(self,nums):
        res = [[]]
        for num in nums:
            for i in range(len(res)):
                res.append(res[i]+[num])
        return res