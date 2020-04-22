
"""
Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.

"""


class Solution:
    def summary(self,nums):
        res = []
        for num in nums:
            if not res or num > res[-1][1] + 1:
                res.append([])
            res[-1][1:] = num,
        return ['->'.join(map(str,r)) for r in res]


