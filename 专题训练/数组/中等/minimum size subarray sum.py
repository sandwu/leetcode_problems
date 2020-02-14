



class Solution:
    def minimum(self,s,nums):
        l = r = 0
        csum = 0
        res = float('inf')
        while r < len(nums):
            csum += nums[r]
            while csum >= s:
                res = min(res,r-l+1)
                csum -= nums[l]
                l += 1
            r += 1
        return res if res != float('inf') else 0