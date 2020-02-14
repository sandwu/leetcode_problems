


class Solution:
    def summary(self,nums):
        res = []
        for num in nums:
            if not res or num > res[-1][1] + 1:
                res.append([])
            res[-1][1:] = num,
        return ['->'.join(map(str,r)) for r in res]