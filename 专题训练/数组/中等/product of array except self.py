

"""
Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]

"""

class Solution:
    def productexpself(self,nums): #每个数都是它前面数的乘积和它后面数的乘积
        res = []
        tmp = 1
        res.append(1)
        for i in range(len(nums)-1):
            tmp *= nums[i]
            res.append(tmp)
        tmp = 1
        for i in range(len(nums)-2,-1,-1):
            tmp *= nums[i+1]
            res[i] *= tmp
        return res


nums = [1,2,3,4]
a = Solution()
print(a.productexpself(nums))