
class Solution(object):
    """
    https://blog.csdn.net/fuxuemingzhu/article/details/82982325
    Runtime: 16 ms, faster than 82.04% of Python online submissions for House Robber II.
    Memory Usage: 11.8 MB, less than 33.33% of Python online submissions for House Robber II.
    """
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        N = len(nums)
        return max(self.rob_range(nums[0 : N - 1]), self.rob_range(nums[1 : N]))

    def rob_range(self, nums):
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        N = len(nums)
        dp = [0] * N
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, N):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]

