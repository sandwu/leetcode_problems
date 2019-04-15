class Solution:
    """
    相当于利用快排的原理，先排序然后从头选定一个数，接着从剩下的数里依次从首尾选择两个数，如果满足条件和为0，则缩小范围继续；没满足也缩小范围继续。
    Runtime: 700 ms, faster than 93.20% of Python3 online submissions for 3Sum.
    Memory Usage: 15.9 MB, less than 100.00% of Python3 online submissions for 3Sum.
    """
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            l, r = i+1, len(nums)-1
            while l < r:
                ans = nums[l] + nums[r]
                if ans == target:
                    res.append([nums[i], nums[l], nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l = l + 1
                    l += 1
                    while l<r and nums[r] == nums[r-1]:
                        r -= 1
                    r -= 1
                elif ans > target:
                    r -= 1
                else:
                    l += 1
        return res