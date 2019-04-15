
class Solution(object):
    """
    和15题的思路差不多，利用先求得三者的和，然后进行与target最小值的判断，保持当前最小值sum1，然后逐步推进数组，直到l>=r，所以是个O(n^2)
    Runtime: 72 ms, faster than 75.37% of Python online submissions for 3Sum Closest.
    Memory Usage: 11 MB, less than 100.00% of Python online submissions for 3Sum Closest.
    """
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        sum1 = nums[0] + nums[1] + nums[2]
        for i in range(n):
            l,r = i+1, n-1
            while l < r:
                res = nums[i] + nums[l] + nums[r]
                if abs(sum1-target) > abs(res-target):
                    sum1 = res
                if res < target:
                    while l < r and nums[l]==nums[l-1]:
                        l += 1
                    l += 1
                else:
                    if res == target:
                        return res
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    r -= 1
        return sum1