
class MySolution:
    """
    利用kadane始终维护截至目前最大值的原理，找到当前最优解和截止目前最优解，两相比较取最大值，则一直获取截止目前最大值
    效率：Runtime: 76 ms, faster than 63.45% of Python3 online submissions for Maximum Subarray.
    """
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        maxsum_tonow = maxsum_now = nums[0]
        for i in range(1,len(nums)):
            maxsum_now = max(nums[i],maxsum_now + nums[i])
            maxsum_tonow = max(maxsum_now, maxsum_tonow)
        return maxsum_tonow


class Solution:
    “”“
    讨论区找的答案，是在kadane上进行简化的解法，是真的被惊艳到了！直接在一次遍历里，判断每个数的上一个数，如果是正数就相加，不是就跳过，这样从第一个数开始
    后续的往上叠加一定是正数才会一直加。
    效率：Runtime: 68 ms, faster than 94.14% of Python3 online submissions for Maximum Subarray.
    ”“”
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)

