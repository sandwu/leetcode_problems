
"""

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.


Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7,

"""

class Solution:
    def remduplicate(self,nums):
        i = 0
        for num in nums:
            if i < 2 or num > nums[i-2]:
                nums[i] = num
                i += 1
        return i


