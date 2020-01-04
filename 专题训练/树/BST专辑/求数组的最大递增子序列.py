


#300

"""

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

[1,4,3,2,6,5]
"""

class Solution(object):
    """
    题意是求数组的最大递增子序列，参考博文：https://blog.csdn.net/fuxuemingzhu/article/details/79820919
    通过动态规划的思想来完成，假设要求F(n)的最大子序列，可以先求得F(n-1)的，以此类推，我们知道F(1)=1即第一个数的
    最大子序列必定是1，那接下来就比较第2个数和第一个数，如果小于第1，则第2个数最大子序列也为1；如大于，则为2。同样的第三个数
    就要比较第1和第2，如果大于，则对应的数上+1.若一直小于，则跳过！
    Runtime: 976 ms, faster than 40.42% of Python online submissions for Longest Increasing Subsequence.
    Memory Usage: 12.1 MB, less than 13.58% of Python online submissions for Longest Increasing Subsequence.
    """
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums :return 0
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(1 ,len(nums)):
            tmax = 1
            for j in range(0 ,i):
                if nums[i] > nums[j]:
                    tmax = max(tmax ,dp[j] +1)

            dp[i] = tmax
        return max(dp)
